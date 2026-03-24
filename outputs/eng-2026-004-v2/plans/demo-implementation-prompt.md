# Demo Implementation Prompt
## eng-2026-004: AI-Driven Prior Authorization Demo
### For Paul to execute on March 24, 2026 morning

> **Instructions for Claude Code**: Use this document as a plan-mode prompt. Execute iteratively — each iteration produces a working, demonstrable artifact. Commit and push after each iteration.

---

## Context

**Who**: Paul Prae, Principal AI Engineer & Architect candidate at Autonomize AI
**What**: Build a working demo of AI-driven PA review to present during an interview to accompany the presentation of an enterprise-grade solution architecture you can see here `C:\dev\solutions-architecture-agent\outputs\eng-2026-004-v2\proposal.md`
**When**: One workday (March 24 morning). Presentation is afternoon.
**Why**: Proves the architecture from the slide deck is implementable, demonstrates Paul's AI engineering skills, shows how Autonomize could leverage Claude for PA automation
**Audience**: Kris Nair (COO/CTO), Suresh Gopalakrishnan (SA, ex-Elevance Health), Ujjwal Rajbhandari (VP Eng, ex-Google Cloud/Dell)

## Foundation

**Start here**: Anthropic's open-source PA review skill
- Repository: [github.com/anthropics/healthcare](https://github.com/anthropics/healthcare)
- Install: `/plugin install prior-auth-review@healthcare`
- Capabilities: NPI validation, ICD-10 lookup, CMS Coverage DB, medical necessity summarization
- This skill does the heavy lifting — Paul builds the integration layer around it

## Architecture

```
Mock Clinical Data → PA Review Tool → Claude (Anthropic SDK) → Determination + Reasoning
```

---

## MVP (Must-Ship, First 3-4 Hours)

**Goal**: CLI tool that accepts a PA case and returns an AI-generated determination with clinical reasoning.

### Step 1: Project Setup
```bash
mkdir pa-review-demo && cd pa-review-demo
python -m venv .venv && source .venv/bin/activate
pip install anthropic fastapi uvicorn
```

### Step 2: Create Mock PA Cases
Create `mock_data/` with 3-5 realistic PA cases:
1. **Clear approval**: Knee MRI for acute injury with documented clinical findings
2. **Clear denial**: Cosmetic procedure not covered under plan
3. **Requires review**: Complex case with partial clinical evidence — confidence below threshold
4. **Missing information**: Incomplete clinical documentation — pend for more info

Each case as JSON:
```json
{
  "patient_id": "MOCK-001",
  "member_id": "M-12345678",
  "provider_npi": "1234567890",
  "diagnosis_code": "M17.11",
  "procedure_code": "27447",
  "clinical_notes": "Patient presents with...",
  "plan_type": "Commercial PPO"
}
```

### Step 3: Build Core Review Tool
Create `pa_review.py`:
- Accept PA case as input (JSON file or dict)
- Use Anthropic SDK with Claude healthcare connectors
- Prompt Claude to: (1) validate NPI, (2) check ICD-10 code, (3) lookup CMS coverage criteria, (4) assess medical necessity, (5) generate determination with reasoning
- Return structured output: determination (approve/deny/pend), confidence score (0-1), reasoning narrative, evidence citations

### Step 4: Build CLI Interface
Create `cli.py`:
- `python cli.py review --case mock_data/case_001.json`
- Pretty-print determination with color-coded confidence
- Show reasoning and evidence in readable format

### Step 5: Test All Mock Cases
Run each mock case, verify:
- Approval case gets approved with high confidence
- Denial case gets denied with clinical rationale
- Complex case gets medium confidence (routes to human review)
- Missing info case gets pended with specific data requests

**Commit and push after MVP works.**

---

## Iteration 1 (Next 2 Hours): FastAPI Wrapper

**Goal**: REST API that accepts PA cases and returns determinations.

### Step 6: Create API
Create `api.py` with FastAPI:
```python
POST /api/v1/pa-review
  Body: PA case JSON
  Response: determination, confidence, reasoning, evidence

GET /api/v1/pa-review/{case_id}
  Response: stored determination result

GET /api/v1/health
  Response: service status
```

### Step 7: Add Request Logging
- Log every request/response with timestamp
- Store determination history in SQLite (simple, no external DB needed)
- Track: case_id, determination, confidence, processing_time_ms

### Step 8: Test via curl/Postman
```bash
curl -X POST http://localhost:8000/api/v1/pa-review \
  -H "Content-Type: application/json" \
  -d @mock_data/case_001.json
```

**Commit and push after API works.**

---

## Iteration 2 (Next 1-2 Hours): Simple Web UI

**Goal**: Browser-accessible interface for the demo.

### Step 9: Build Simple Frontend
Options (pick one based on time):
- **Option A — Streamlit** (fastest): `pip install streamlit` → single-file app
- **Option B — HTML/JS** (more polished): Static page served by FastAPI

UI should show:
1. Text area or file upload for PA case
2. "Review" button
3. Results panel: determination badge (Approved/Denied/Pend), confidence meter, reasoning text, evidence list
4. History of reviewed cases

### Step 10: Polish for Demo
- Add Autonomize-relevant framing (title: "PA Review — Powered by Claude")
- Include mock data selector (dropdown of pre-built cases)
- Make confidence threshold configurable (slider)
- Show "would route to human review" for low-confidence cases

**Commit and push after UI works.**

---

## Stretch Goal: Azure Deployment

**Only if time permits. Local demo is perfectly acceptable.**

### Step 11: Deploy to Azure App Service
```bash
# Create requirements.txt
pip freeze > requirements.txt

# Azure CLI deployment
az webapp up --name pa-review-demo --resource-group rg-pa-demo --runtime "PYTHON:3.12"
```

Or use Azure Container Apps:
```bash
# Build container
docker build -t pa-review-demo .
# Push to Azure Container Registry and deploy
```

**Set environment variables**:
```
ANTHROPIC_API_KEY=<your-key>
```

---

## Demo Walkthrough Script

> Use this script during the presentation to walk the panel through the demo.

**Opening** (30 seconds):
"To validate the architecture I'm proposing, I built a working proof-of-concept. This demonstrates the core AI-driven PA review flow — the same pattern that would power the production Autonomize PA Copilot integration."

**Show Case 1 — Clear Approval** (60 seconds):
"Here's a straightforward case — knee MRI for documented injury. The AI reviews the clinical evidence, checks coverage criteria, and returns an approval with high confidence. Note the reasoning — it cites specific clinical findings and coverage criteria."

**Show Case 2 — Complex Case** (60 seconds):
"Now a more complex case where the evidence is partial. Notice the confidence score drops — this is where our architecture routes to a human clinical reviewer. The AI pre-digests the case and presents its recommendation, but the final call is human."

**Show Case 3 — Missing Information** (30 seconds):
"Here the clinical documentation is incomplete. Rather than force a determination, the system identifies exactly what's missing and pends the case for additional information."

**Bridge to Architecture** (30 seconds):
"This demo uses Claude's healthcare connectors for NPI validation, ICD-10 lookup, and CMS coverage criteria. In production, this same pattern integrates with the Autonomize PA Copilot and the health plan's actual clinical data sources — that's what my architecture describes."

---

## Technical Notes

- **Azure-only hosting** — no Vercel, no Heroku, no competing platforms (Phase 0 decision DM-4)
- **Mock data first** — do not try to connect to real healthcare APIs (Phase 0 decision DM-3)
- **Python + Anthropic SDK** — no LangChain, no unnecessary frameworks (Phase 0 research finding)
- **Claude healthcare connectors** — these work within Claude's interface; for API use, implement tool-use pattern with Anthropic SDK
- **Mention SA Agent**: "I built this using my Solutions Architecture Agent — a Claude Code plugin I developed — to iteratively design and validate the architecture. The demo is the first phase of the implementation roadmap."
