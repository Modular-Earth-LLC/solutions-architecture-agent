# Phase 0 Context Summary — Research & Requirements Foundation

> **Engagement**: eng-2026-001 | CVS Health Legacy System Transformation
> **Completed**: 2026-03-16
> **Author**: Solutions Architecture Agent

## Artifacts Produced

| Artifact | Path | Status | Validation |
|----------|------|--------|-----------|
| Research findings (9 clusters, 54 sources) | `outputs/cvs-legacy-transformation/research-findings.md` | COMPLETE | IBMi audit passed; zero unsourced claims |
| Engagement tracker | `knowledge_base/engagement.json` | COMPLETE | Schema validated |
| Requirements (comprehensive tier) | `knowledge_base/requirements.json` | COMPLETE | Schema validated; reviewed 8.3/10 PASS |
| Quality review | `knowledge_base/reviews.json` | COMPLETE | Schema validated |
| Experience honesty map | `outputs/cvs-legacy-transformation/honesty-map.md` | FINAL | 8 areas, evidence-typed |

## Key Discoveries

### CVS Health Strategic Context (Critical for All Phases)
1. **Google Cloud Partnership** (March 5, 2026): Strategic partnership launching Health100 subsidiary with agentic AI using Gemini, BigQuery, Cloud Healthcare API
2. **$20B Investment**: 10-year technology modernization commitment focused on interoperability
3. **Leadership**: Tilak Mandadi (Chief Experience & Technology Officer, ex-Disney/AmEx), Ali Keshavarz (Chief Data & AI Officer)
4. **Current Stack**: GCP (new initiatives), Azure (myPBM), AWS (some); Java, Python, React, Angular, Spring Boot, Kafka, Kubernetes
5. **myPBM**: Cloud-based PBM client management portal on Azure; 130+ APIs
6. **RPA Impact**: Claims processing time reduced 40% via automation within Caremark

### IBMi Modernization Strategy (Shapes Phase 2 Architecture)
- **Recommended Pattern**: Sidecar/strangler fig — modern React frontend + IBM i backend via API layer (IWS + Apigee)
- **Big-Bang Risk**: 70% failure rate for full rewrites; industry consensus favors incremental
- **API Options**: IBM IWS (native, no middleware), Eradani Connect, MDRest4i, Profound.js
- **Dual Run**: GCP-unique capability for parallel production validation
- **Vendor Landscape**: Rocket Software, Profound Logic, Fresche (X-Modernize AI), LANSA, Replay

### IAM Architecture (Shapes Phase 3 Security)
- **Framework**: Zero trust (NIST SP 800-207) + SMART on FHIR + hybrid RBAC/ABAC
- **GCP Service**: Cloud Identity Platform (HIPAA-capable with BAA)
- **Authentication**: OAuth 2.0 + OIDC + MFA + enterprise SSO federation
- **Key Insight**: SMART on FHIR is the healthcare-specific authorization standard for FHIR data

### GCP Service Mapping (Shapes All Technical Phases)
- 18-service AWS→GCP translation table produced in research findings
- Key mappings: S3→Cloud Storage, Redshift→BigQuery, SageMaker→Vertex AI, ECS→Cloud Run/GKE, SNS/SQS→Pub/Sub
- GCP-unique: Dual Run, Apigee (enterprise API mgmt), Cloud Healthcare API

### PBM Domain Knowledge (Shapes Phase 2)
- Claims adjudication: NCPDP B1 transactions, real-time at POS, sub-second latency
- 99%+ electronic adjudication rate
- Workflow: eligibility → DUR → UM → pricing → adjudication → response
- 70% of PBM market on legacy systems

### Change Management (Shapes Phase 4 Planning)
- Prosci ADKAR + Kotter 8-step as dual framework
- 85% of digital transformation failures are people/process, not technology
- Green screen → GUI reduces onboarding from 6-8 weeks to <10 days
- 40% error reduction with modernized interface

## Requirements Summary

- **13 functional requirements** (8 must-have, 5 should-have)
- **8 success criteria** with baselines, targets, measurements
- **9 stakeholders** across decision-makers, contributors, end-users
- **AI suitability**: 8/10 (strong fit)
- **Review score**: 8.3/10 (PASS, 0 blockers)
- **Key open finding**: RF-001 — RTO/RPO not specified in NFRs (deferred to /architecture)

## Assumptions (A-0-001 through A-0-010)

See `outputs/cvs-legacy-transformation/research-findings.md` Appendix B for full register.

Most critical:
- **A-0-001**: Legacy PBM systems run on IBMi (from case study language)
- **A-0-005**: GCP is primary cloud platform (from Google Cloud partnership)
- **A-0-010**: Sub-second claims adjudication latency is non-negotiable

## Honesty Map Summary

| Area | Rating | Strategy |
|------|--------|----------|
| **GenAI/ML Leadership** | 4.5/5 | Lead with depth — strongest differentiator |
| **HCD Design** | 4/5 | Lead with Cognitive Science degree + healthcare UX projects |
| **Healthcare Domain** | 4/5 | Deep healthcare experience; PBM-specific is researched |
| **Change Management** | 3.5/5 | Frame coaching + training through ADKAR/Kotter |
| **Technology Stack** | 3/5 | AWS expertise + GCP translation table |
| **IAM Strategy** | 2.5/5 | AWS IAM + NIST/SMART on FHIR frameworks |
| **IBMi/AS400** | 2/5 | Research-backed patterns; transparent about no hands-on |
| **GCP** | 2/5 | Never claim GCP experience; present through AWS lens |

## Instructions for Future Phases

1. **Re-read from disk**: Always read `outputs/cvs-legacy-transformation/research-findings.md` and `knowledge_base/requirements.json` from disk rather than relying on context memory
2. **GCP-first**: All architecture decisions should use GCP services given the March 2026 partnership
3. **IBMi citations**: Every IBMi technical claim must have a source URL
4. **Dual competency**: Weave GenAI DS team leadership throughout, not as a separate section
5. **Assumptions**: All new assumptions use A-N-NNN format where N = phase number
