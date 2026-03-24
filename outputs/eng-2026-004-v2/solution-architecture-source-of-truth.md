# Solution Architecture — Source of Truth
## AI-Driven Prior Authorization | Autonomize AI
### March 2026

> **This document is the master reference for all other deliverables.** The slide deck, speaker notes, email draft, and interview prep are all views of this document. When in doubt, this document is correct.

---

## 1. System Description

A large US-based health plan integrates **Autonomize AI's PA Copilot** into its existing IT environment to automate the intake, clinical review, and determination of prior authorization (PA) requests. The solution uses **AI-driven clinical review** with configurable confidence thresholds and mandatory human oversight, deployed on **Microsoft Azure** to align with Autonomize AI's platform and cloud strategy.

### What the system does:
1. **Receives** PA requests from providers via fax, web portal, and X12 278 EDI
2. **Processes** unstructured documents (OCR, extraction) into structured PA records
3. **Validates** member eligibility and PA requirements against the payer core system
4. **Retrieves** clinical data from FHIR R4 endpoints and legacy databases
5. **Reviews** clinical evidence against coverage criteria using AI (Autonomize PA Copilot + Claude)
6. **Routes** determinations based on AI confidence: auto-approve (high), human review (low), pend for info (insufficient)
7. **Records** every decision with full audit trail for HIPAA and CMS-0057-F compliance

### What the system does NOT do:
- Replace clinical reviewers — AI augments human judgment
- Auto-deny PA requests (Phase 1) — all denials require human clinical review
- Implement FHIR Da Vinci Implementation Guide internals — FHIR R4 is the interoperability label
- Replace the Payer Core System — integrates alongside it

---

## 2. Technology Decision Table

| Generic Component | Azure Service | AWS Equivalent | Justification | Verified URL |
|---|---|---|---|---|
| Cloud Platform | Microsoft Azure | Amazon Web Services | Autonomize Azure Marketplace, Pegasus Program | [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/284109.autonomize-prior-auth-copilot) |
| LLM Provider | Claude via Azure AI Foundry | Claude via Amazon Bedrock | Only cloud with Claude + GPT; healthcare connectors | [MS Learn](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-claude) |
| Agent Platform | Autonomize Genesis Platform | N/A (proprietary) | Assignment specifies Autonomize AI integration | [Autonomize](https://autonomize.ai/) |
| Agent Service | Azure AI Foundry Agent Service | Amazon Bedrock Agents | MCP support, Python SDK, free preview until Apr 2026 | [Azure Agent Service](https://azure.microsoft.com/en-us/products/ai-foundry/agent-service) |
| Message Queue | Azure Service Bus (Premium) | Amazon SQS / SNS | HIPAA BAA on Premium, sufficient for PA volume. Kafka as future scale. | [MS Learn](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview) |
| Container Compute | Azure Container Apps | Amazon ECS / EKS | Managed Kubernetes, auto-scale, serverless option | [MS Learn](https://learn.microsoft.com/en-us/azure/container-apps/) |
| Relational Database | Azure Database for PostgreSQL | Amazon RDS for PostgreSQL | PA records, audit logs, workflow state | [Azure PostgreSQL](https://azure.microsoft.com/en-us/products/postgresql/) |
| Vector Search | Azure AI Search | Amazon OpenSearch | Hybrid vector + keyword; clinical knowledge bases | [MS Learn](https://learn.microsoft.com/en-us/azure/search/vector-search-overview) |
| Object Storage | Azure Blob Storage | Amazon S3 | Fax images, clinical docs, immutable audit logs | [Azure Blob](https://azure.microsoft.com/en-us/products/storage/blobs/) |
| Healthcare Data | Azure Health Data Services | AWS HealthLake | FHIR R4, DICOM, HIPAA/HITRUST certified | [MS Learn](https://learn.microsoft.com/en-us/azure/healthcare-apis/healthcare-apis-overview) |
| Document AI | Azure AI Document Intelligence | Amazon Textract | OCR, form extraction, clinical document processing | [MS Learn](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/) |
| Identity | Microsoft Entra ID | AWS IAM + Cognito | RBAC, SMART on FHIR, conditional access | [MS Learn](https://learn.microsoft.com/en-us/azure/healthcare-apis/fhir/smart-on-fhir) |
| Monitoring | Azure Monitor + App Insights | Amazon CloudWatch + X-Ray | OpenTelemetry, distributed tracing, HIPAA-compliant logs | [MS Learn](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview) |
| Cache | Azure Cache for Redis | Amazon ElastiCache | Eligibility lookup cache, rate limiting | [Azure Redis](https://azure.microsoft.com/en-us/products/cache/) |
| API Gateway | Azure API Management | Amazon API Gateway | Rate limiting, WAF, developer portal | [Azure APIM](https://azure.microsoft.com/en-us/products/api-management/) |

---

## 3. Architecture Components (10)

| ID | Component | Technology | Purpose |
|---|---|---|---|
| C-001 | PA Request Ingestion Gateway | Azure API Mgmt + Functions | Receives all PA channels, normalizes to canonical format |
| C-002 | Document Processing Pipeline | Azure AI Document Intelligence | OCR for faxes, extracts structured data from unstructured docs |
| C-003 | Member Eligibility Service | Payer Core REST API | Validates eligibility, retrieves benefits and PA requirements |
| C-004 | Clinical Data Aggregation | Azure Health Data Services | Retrieves clinical records from FHIR R4 + legacy sources |
| C-005 | Autonomize PA Copilot | Genesis Platform + Claude | AI clinical review — coverage matching, determination, reasoning |
| C-006 | Determination Router | Azure Functions + Rules | Confidence-based routing: auto-approve, human review, pend |
| C-007 | Clinical Review Dashboard | Autonomize AI Studio | Human reviewer UI — confirm/override AI with feedback capture |
| C-008 | Determination Response | Azure Functions | Writes determination to Payer Core, notifies provider |
| C-009 | LLMOps Pipeline | Azure Monitor + Evals | Performance monitoring, drift detection, feedback loop |
| C-010 | Audit & Compliance | Immutable Blob Storage | Tamper-proof decision audit trail, CMS-0057-F reporting |

---

## 4. PA Business Process (Standard Flow)

The system follows the standard PA business process as defined by AMA, CAQH, and CMS — technology innovation is in the execution, not the process.

1. **Provider submits PA request** (fax, portal, or X12 278 EDI)
2. **Intake and normalization** — document processing converts to structured record
3. **Eligibility verification** — confirm member is covered, service requires PA
4. **Clinical data retrieval** — gather relevant clinical records from FHIR and legacy sources
5. **AI clinical review** — match clinical evidence against coverage criteria, assess medical necessity
6. **Confidence-based routing**:
   - High confidence approval → auto-approve
   - Low confidence → human clinical reviewer queue
   - Insufficient data → pend and request more information from provider
7. **Human review** (when routed) — reviewer sees AI recommendation + evidence, confirms or overrides
8. **Determination response** — write to Payer Core, notify provider
9. **Audit logging** — every step recorded with reasoning for compliance

**Authoritative sources**:
- [AMA Prior Authorization Overview](https://www.ama-assn.org/practice-management/prior-authorization)
- [CAQH CORE PA Operating Rules](https://www.caqh.org/core/prior-authorization-referrals-operating-rules)
- [CMS-0057-F Fact Sheet](https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-prior-authorization-final-rule-cms-0057-f)

---

## 5. Three Deep Integration Points

### Integration 1: Member Eligibility API
- **Direction**: Bidirectional (read eligibility, write determination)
- **Protocol**: REST API to Payer Core System
- **Auth**: Service account with least privilege, mutual TLS
- **Data**: Member ID → eligibility status, benefit details, PA requirement flag, contract rules
- **Latency**: <2 seconds (synchronous, blocking)
- **Caching**: Azure Cache for Redis (TTL: 15 minutes) to reduce Payer Core load

### Integration 2: PA Request Ingestion (One Format Focus: Fax)
- **Direction**: Inbound
- **Protocol**: Fax gateway (SFTP) → Azure Blob Storage → Document Processing Pipeline
- **Processing**: Azure AI Document Intelligence (OCR) → structured extraction → canonical PA record
- **Security**: TLS in transit, encrypted at rest, PHI handling per HIPAA
- **Challenge**: Handwritten clinical notes — OCR accuracy varies; low-confidence extractions flagged for manual review
- **Output**: Normalized JSON PA record on Azure Service Bus for downstream processing

### Integration 3: Clinical Data for AI Processing
- **Direction**: Read-only from clinical sources
- **Sources**: FHIR R4 endpoints (modern EMRs) + Legacy DB connectors (older systems)
- **Protocol**: FHIR R4 REST API (OAuth 2.0) for modern; database connector (service account + VNet) for legacy
- **Standardization**: All clinical data normalized to FHIR R4-compatible format before AI processing
- **Security boundary**: PHI tokenized before passing to LLM; only necessary clinical context included
- **FHIR Resources used**: Patient, Encounter, Observation, DiagnosticReport, Condition

---

## 6. Assumptions Table

| # | Assumption | Design Decision It Supports | Discovery Question |
|---|---|---|---|
| A-1 | Client is top-5 US health plan scale | Architecture designed for 1-3M PA/month | What is actual monthly PA volume by channel? |
| A-2 | Fax is dominant PA intake channel | Document processing pipeline is a core component | What % of PA requests arrive via fax vs. portal vs. EDI? |
| A-3 | Mix of FHIR R4 and legacy clinical data sources | Clinical Data Aggregation service with dual connectors | Which EMR systems are deployed? What % are FHIR R4 capable? |
| A-4 | Payer Core System exposes REST API for eligibility | Synchronous eligibility check in PA flow | What is the Payer Core API interface? Is it real-time capable? |
| A-5 | Autonomize PA Copilot is the designated AI engine | Architecture integrates around PA Copilot, not custom-built | What Autonomize platform components are available to us? |
| A-6 | CMS-0057-F compliance is a regulatory driver | FHIR R4 API foundation, compliance reporting component | What is the client's current CMS-0057-F readiness status? |
| A-7 | Auto-denial requires additional safeguards | Phase 1 is auto-approve only; denials require human review | What is the regulatory/legal position on auto-denial? |
| A-8 | Azure is the deployment platform | All services selected from Azure ecosystem | Are there any existing cloud commitments or restrictions? |
| A-9 | Clinical guidelines change quarterly | LLMOps pipeline includes continuous eval and retraining triggers | How frequently do coverage criteria change? Who maintains them? |
| A-10 | 20 LOBs with different admin rules | Config-driven LOB isolation within shared platform | Which LOBs are in scope? What are the key rule differences? |

---

## 7. Open Questions for Real Discovery

These are questions a thorough SA would ask before committing to implementation. Framing them shows the panel that Paul understands what requires real client engagement.

### Ask Early (impacts architecture):
1. What is the actual monthly PA volume and channel distribution?
2. Which Payer Core System is deployed (TriZetto Facets, QNXT, custom)?
3. What Autonomize platform components are currently licensed/available?
4. What is the current FHIR R4 adoption percentage across clinical data sources?
5. Are there existing cloud commitments or multi-cloud requirements?

### Ask During Design (impacts integration):
6. What is the Payer Core System API interface specification?
7. Which clinical guidelines are used (InterQual, MCG, custom)?
8. What is the current auto-approval rate without AI?
9. What confidence threshold is acceptable for auto-determination?
10. How are PA denials currently reviewed and appealed?

### Ask Before Go-Live (impacts operations):
11. What is the clinical reviewer team size and workflow?
12. What are the state-specific PA requirements beyond CMS-0057-F?
13. What is the regulatory/legal position on AI-assisted auto-denial?
14. How should the system behave during Autonomize platform outages?
15. What SLAs does the Payer Core System API guarantee?

---

## 8. Key Metrics (Cited Sources Only)

| Metric | Value | Source |
|---|---|---|
| Manual PA cost (provider) | $10.97 per transaction | [2024 CAQH Index](https://www.caqh.org/hubfs/Index/2024%20Index%20Report/CAQH_IndexReport_2024_FINAL.pdf) |
| Manual PA cost (payer) | $3.52 per transaction | Same |
| Automated PA cost | ~$0.05 per transaction | Same |
| Review time reduction (Altais) | 45% | [BusinessWire Feb 2026](https://www.businesswire.com/news/home/20260224376992/en/Altais-Cuts-Prior-Authorization-Review-Time-by-45-and-Reduces-Manual-Errors-by-54-with-Autonomize-AI) |
| Error reduction (Altais) | 54% | Same |
| Auto-approval rate (Altais) | 50% | Same |
| Physician PA burden | 12-13 hours/week | [AMA 2024 Survey](https://www.ama-assn.org/system/files/prior-authorization-survey.pdf) |
| PA requests per physician/week | 39 | Same |
| PA causes care delays | 93% of physicians | Same |
| CMS-0057-F Phase 1 | Live Jan 1, 2026 | [CMS Fact Sheet](https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-prior-authorization-final-rule-cms-0057-f) |
| CMS-0057-F Phase 2 | Jan 1, 2027 | Same |

---

## 9. Version History

| Version | Date | Description |
|---|---|---|
| 2.0 | 2026-03-23 | Azure-native architecture, single orchestrator pattern, assignment-aligned scope |
