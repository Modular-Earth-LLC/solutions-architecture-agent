# Implementation Planning Prompt: AI-Driven Prior Authorization Demo

## Instructions for Claude Code Plan Mode

Paste this prompt into Claude Code in plan mode (`/plan`) to produce an executable implementation plan for a **minimal demo** of the AI-Driven Prior Authorization system.

---

## Context

You are building a **demo-scope prototype** of an AI-driven Prior Authorization system. This is NOT the full enterprise architecture — it's a focused demonstration that proves the core PA automation concept end-to-end.

**Full architecture reference**: See `outputs/eng-2026-004/proposal.md` for the complete enterprise design. This demo implements a narrow vertical slice.

## Demo Scope (Tightly Bounded)

### What This Demo Does
A single PA request flows through: **Portal submission → Eligibility check → Clinical data retrieval → AI determination → Response delivery**

### What This Demo Does NOT Do
- No fax ingestion or OCR (use portal-only)
- No X12 278 EDI processing
- No legacy database connectors (FHIR-only)
- No multi-LOB configuration (single LOB)
- No MLOps pipeline or drift detection
- No production security hardening
- No multi-AZ deployment

### Demo Architecture (Minimal)

```
Provider Portal (FastAPI) → Kafka (local) → PA Processing Service →
  ├── Eligibility Check (mock Facets API)
  ├── Clinical Data (mock FHIR R4 endpoint)
  ├── Guidelines Match (mock InterQual API)
  └── AI Determination (Amazon Bedrock Claude) →
      Kafka → Response Service → API response
```

## Technology Stack (Demo)

| Layer | Demo Technology | Production Equivalent |
|-------|----------------|----------------------|
| **API** | FastAPI (Python 3.12) | Amazon API Gateway |
| **Event Bus** | Apache Kafka (Docker Compose) | Amazon MSK |
| **AI** | Amazon Bedrock (Claude) | Autonomize AI PA Copilot |
| **Database** | PostgreSQL (Docker) | Amazon RDS |
| **Audit** | PostgreSQL table (append-only) | DynamoDB |
| **Clinical Data** | Mock FHIR R4 server (FastAPI) | AWS HealthLake + EMR endpoints |
| **Eligibility** | Mock Facets API (FastAPI) | TriZetto Facets |
| **Guidelines** | Mock InterQual API (FastAPI) | InterQual/MCG APIs |

## Implementation Plan Structure

Produce a plan with these phases:

### Phase 1: Project Setup (2-4 hours)
- Python project with `pyproject.toml`
- Docker Compose: Kafka (Confluent), PostgreSQL, Zookeeper
- FastAPI application skeleton with health check endpoint
- Kafka producer/consumer utilities
- Database schema: `pa_requests`, `pa_determinations`, `audit_trail`

### Phase 2: Mock Services (2-3 hours)
- **Mock Facets API**: `/eligibility/{member_id}` — returns mock eligibility response
- **Mock FHIR Server**: `/fhir/Patient/{id}`, `/fhir/Condition`, `/fhir/Observation` — returns mock FHIR R4 Bundles
- **Mock InterQual API**: `/guidelines/match` — returns mock guideline match result with citations
- All mocks return realistic healthcare data (ICD-10 codes, CPT codes, FHIR resources)

### Phase 3: Ingestion Pipeline (2-3 hours)
- POST `/pa/submit` endpoint accepting PA request JSON
- Schema validation (member ID, provider NPI, diagnosis codes, procedure codes)
- Kafka producer publishes to `pa-requests` topic
- Request stored in PostgreSQL with status tracking

### Phase 4: PA Processing Service (3-4 hours)
- Kafka consumer on `pa-requests` topic
- Step 1: Call mock Facets API for eligibility verification
- Step 2: Call mock FHIR server for clinical evidence
- Step 3: Call mock InterQual API for guidelines match
- Step 4: Call Amazon Bedrock (Claude) with prompt:
  ```
  You are a clinical prior authorization reviewer. Given:
  - Eligibility: {eligibility_result}
  - Clinical Evidence: {fhir_bundle}
  - Guidelines Match: {guidelines_result}

  Determine: Should this PA request be APPROVED or PENDED FOR REVIEW?
  Provide: determination, confidence (0-1), clinical_rationale, guideline_citations
  Respond in JSON format.
  ```
- Step 5: If confidence >= 0.85 → auto-approve. Otherwise → pend for review.
- Publish determination to `pa-determinations` Kafka topic
- Write audit trail record

### Phase 5: Response and Dashboard (2-3 hours)
- Kafka consumer on `pa-determinations` topic
- GET `/pa/status/{request_id}` — returns current PA status
- GET `/pa/dashboard` — returns summary metrics (total, approved, pended, avg confidence)
- Simple HTML dashboard page showing real-time PA processing metrics

### Phase 6: End-to-End Test (1-2 hours)
- Submit 10 sample PA requests with varying clinical scenarios
- Verify: eligibility check, clinical data retrieval, AI determination, audit trail
- Demonstrate: auto-approval for clear cases, pend-for-review for ambiguous cases
- Print dashboard metrics

## Key Files to Create

```
pa-demo/
├── docker-compose.yml          # Kafka, PostgreSQL, Zookeeper
├── pyproject.toml              # Python dependencies
├── src/
│   ├── main.py                 # FastAPI app (ingestion + status API)
│   ├── config.py               # Environment configuration
│   ├── models.py               # Pydantic models (PA request, determination)
│   ├── database.py             # PostgreSQL connection + schema
│   ├── kafka_utils.py          # Kafka producer/consumer helpers
│   ├── pa_processor.py         # Core PA processing pipeline
│   ├── bedrock_client.py       # Amazon Bedrock Claude integration
│   ├── mock_services/
│   │   ├── facets.py           # Mock Facets eligibility API
│   │   ├── fhir_server.py      # Mock FHIR R4 server
│   │   └── interqual.py        # Mock InterQual guidelines API
│   └── dashboard.py            # Simple metrics dashboard
├── tests/
│   └── test_e2e.py             # End-to-end demo test
└── README.md                   # Demo setup instructions
```

## Dependencies

```
fastapi>=0.115.0
uvicorn>=0.32.0
confluent-kafka>=2.6.0
psycopg2-binary>=2.9.0
boto3>=1.35.0
anthropic>=0.40.0
pydantic>=2.9.0
httpx>=0.28.0
```

## Amazon Bedrock Configuration

- **Model**: `anthropic.claude-sonnet-4-6-20260320` (or latest available)
- **Region**: `us-east-1`
- **Auth**: AWS credentials (default profile or environment variables)
- **Max tokens**: 1024 per determination
- **Temperature**: 0.1 (deterministic clinical decisions)

## Sample PA Request (for testing)

```json
{
  "member_id": "MBR-2026-001",
  "provider_npi": "1234567890",
  "diagnosis_codes": ["M54.5"],
  "procedure_codes": ["97110"],
  "service_description": "Physical therapy evaluation and treatment for low back pain",
  "clinical_notes": "Patient presents with chronic low back pain, duration 6 months. Conservative treatment (NSAIDs, home exercise) has not provided adequate relief. Requesting 12 sessions of physical therapy.",
  "urgency": "standard",
  "lob": "commercial"
}
```

## Verification Criteria

The demo is successful when:
1. PA request submitted via API and appears in PostgreSQL
2. Kafka message published and consumed
3. Eligibility check returns positive result
4. FHIR clinical data retrieved and included in AI context
5. Guidelines match returned with InterQual citation
6. Amazon Bedrock produces determination with confidence score and rationale
7. Auto-approved requests (confidence >= 0.85) marked as approved
8. Low-confidence requests marked as pended for review
9. Complete audit trail record created for every determination
10. Dashboard shows processing metrics

## Constraints

- **Build time**: Target 12-16 hours total
- **No cloud deployment**: Docker Compose only (local development)
- **No real PHI**: All test data is synthetic
- **No production security**: No TLS, no auth, no encryption (demo only)
- **Single developer**: Designed for one person to build and demo

---

*This prompt was generated from the full solution architecture (eng-2026-004). See `outputs/eng-2026-004/proposal.md` for the complete enterprise design.*
