# Phase 2 Context Summary — Solution Architecture and Technical Design

> **Completed**: 2026-03-16
> **Status**: complete

## Key Findings

- **Three genuinely viable architecture options** (GCP-Native, AWS-Native, Modern Cloud) — all use API-First Strangler Fig pattern. Eliminates strawman options in favor of three modern approaches each with cited vendor reference architectures. GCP recommended due to CVS Health100 partnership alignment.
- **Neither AWS DMS nor Google Datastream supports Db2 for i (AS/400)** — CDC requires third-party tooling (Precisely Connect or Striim) on all three cloud platforms. Precisely reads native IBM i journals without triggers or table scans.
- **Healthcare NLP API deprecating May 2026** — GenAI pipeline must use Gemini/MedGemma-based extraction from the start. MedGemma 1.5 (4B params, 128K context, 89.6% EHRQA accuracy) available on Vertex AI.
- **IWS 3.0 released Oct 2025** — Jakarta EE foundation, 20% performance improvement, OpenAPI UI built-in. YAJL recommended for high-throughput JSON handling on hot paths (claims adjudication).
- **Vercel HIPAA BAA available on Pro plan ($350/mo)** since Sept 2025 — makes Modern Cloud option viable for enterprise healthcare. Supabase has SOC 2 Type II + HIPAA BAA on Team plan ($599/mo).
- **Vercel AI SDK 6 provides model-agnostic access to 24+ official providers + 50+ community providers** — swap AI providers via configuration, zero lock-in on most volatile layer (Paul's Paloist architecture principle).
- **GCP Dual Run for online transactions is in preview** (batch is GA) — fallback plan: custom shadow traffic via Apigee request mirroring + BigQuery comparison.
- **WCAG 2.2 AA deadline May 2026** — CVS already has Compass design system + open-source accessibility toolkit (Testaro/Testilo, Inclusive Design annotation kits). New UI must be WCAG 2.2 AA from day one.
- **React Server Components reduce client bundle 40-60%**, keep PHI server-side for HIPAA compliance, achieve LCP 1.28s with streaming SSR.
- **Module Federation enables screen-by-screen micro-frontend migration** — each pharmacy workflow deployed as independent remote, independently deployable with 150KB JS budget per route.
- **AWS HealthLake provides FHIR R4 with built-in NLP + zero-ETL SQL** — strongest healthcare data platform, but doesn't align with CVS's GCP partnership.
- **13 PBM data entities modeled** covering members, plans, claims, pharmacies, providers, drugs, formulary, PA, users, audit log, AI recommendations, migration status, CDC sync.

## Artifacts Produced

| File | Description |
|------|-------------|
| `knowledge_base/integration_plan.json` | 12 integration points, 10 API contracts, strangler fig migration strategy, CDC, CI/CD |
| `knowledge_base/architecture.json` | 3 architecture options (GCP/AWS/Modern Cloud), 12 components, 5 Mermaid diagrams, WA scores, GenAI pipeline |
| `knowledge_base/data_model.json` | 13 entities, vector schema, PBM ontology, validation rules, data governance, migration notes |
| `knowledge_base/reviews.json` | 3 reviews (R-002, R-003, R-004) — all PASS ≥8.1/10 |
| `knowledge_base/engagement.json` | Updated lifecycle_state for integration_plan, architecture, data_model |

## Decisions Made

- **Three options structure**: GCP-Native (recommended, CVS partnership), AWS-Native (Paul's deep expertise), Modern Cloud (Paul's production practice — Paloist/paulprae.com inspired). No strawman options.
- **GCP recommended as primary** due to Health100 partnership, but AWS and Modern Cloud presented as genuinely viable alternatives.
- **Strangler fig pattern across all options** — member eligibility first (lowest risk), then claims adjudication, then formulary/PA with GenAI, then remaining workflows.
- **CDC via Precisely Connect** (not Debezium, which has maturity limitations for IBM i) — journal-based, no triggers or table scans.
- **Cloud Run + GKE Autopilot hybrid** (GCP option) — Cloud Run for stateless APIs, GKE Autopilot for Dual Run and orchestration.
- **Tiered AI inference** — Gemini for complex PA cases, MedGemma 1.5 for routine (Paul's three-tier AI pipeline principle from Paloist).
- **Supabase PostgreSQL with RLS** (Modern Cloud option) — database-level tenant isolation, Paul's production pattern.

## Surprises and Pivots

- **Major pivot**: User requested replacing the original three options (Screen Transformation / Strangler Fig / Full Rewrite) with three cloud-native options (GCP / AWS / Modern Cloud). This eliminated strawman options and created a stronger interview presentation.
- **Vercel HIPAA BAA maturity**: Vercel's HIPAA BAA on Pro plan (since Sept 2025) was more mature than expected. Makes Modern Cloud option genuinely viable, not just theoretical.
- **AWS HealthLake strength**: HealthLake's built-in NLP + zero-ETL SQL is technically superior to Cloud Healthcare API for analytics workflows. This was surprising — noted in AWS option as a strength.
- **IWS performance concern**: Community consensus that IWS was designed for ease, not peak throughput. This is a genuine risk for CVS's claims volume — YAJL/CGIDEV2 alternatives recommended for hot paths.

## Assumptions

### Confirmed
- A-0-005 (GCP primary): Confirmed by Health100 partnership and multiple job postings
- A-0-006 (Strangler fig preferred): Validated across all three options
- A-0-007 (React frontend): Confirmed by CVS job postings

### New
- A-2-001: IWS 3.0 is available on CVS's IBMi OS version (requires IBM i 7.4+ with specific PTF levels)
- A-2-002: CVS has or can provision Partner Interconnect connectivity via existing carrier (AT&T/Verizon)
- A-2-003: Precisely Connect licensing is available to CVS or CVS is willing to procure it
- A-2-004: GCP Dual Run for online transactions will reach GA before Phase 2 claims migration (fallback: custom shadow traffic)
- A-2-005: CVS's Compass design system can be extended with healthcare-specific components (medication display, patient search)
- A-2-006: Clinical pharmacists will accept AI-generated PA recommendations with confidence ≥0.8 threshold for standard review queue
- A-2-007: Vercel AI SDK 6 model-agnostic pattern is applicable to CVS's multi-model strategy (Gemini + MedGemma + potential fine-tuned models)

## Insights for Future Phases

- **Phase 3 (Security & IAM)**: Architecture uses Cloud Identity Platform, SMART on FHIR scopes, hybrid RBAC/ABAC. STRIDE threat modeling should focus on: IBMi→GCP API surface (IWS + Partner Interconnect), CDC pipeline data integrity, GenAI pipeline output validation (HITL, confidence thresholds), cross-cloud auth (GCP ↔ Azure myPBM). VPC Service Controls perimeter defined for all HIPAA-regulated services. 23 PHI/PII fields inventoried in data model.
- **Phase 4 (Estimation)**: Key cost drivers by option: Option A (Apigee Enterprise ~$100K/yr, Partner Interconnect ~$600-1,500/mo, Vertex AI inference), Option B (API Gateway pay-per-request, Direct Connect, Bedrock/SageMaker), Option C (Vercel Pro+HIPAA $370/mo, Supabase Team+HIPAA ~$950/mo). CDC tooling (Precisely/Striim) licensing needed across all options. Team composition: need RPG/CL developers for IWS API layer, React + TypeScript developers, ML engineers for GenAI pipeline, platform engineers for multi-cloud. Three-option comparison table needed.
- **Phase 5 (Methodology)**: GenAI pipeline architecture demonstrates dual competency (architect + GenAI DS team leader). Tiered inference pattern (Gemini for complex, MedGemma for routine) mirrors Paul's Paloist three-tier pipeline. Vercel AI SDK 6 model-agnostic approach mirrors paulprae.com architecture. Evaluation framework (correctness, safety, groundedness, consistency) maps directly to GenAI DS JD responsibilities.
- **Phase 6 (Assembly)**: 5 Mermaid diagrams ready for embedding. Three-option analysis section maps directly to interview expectation #4 ("explore and present multiple options"). Architecture sections self-contained for interview topic assignment. GenAI pipeline diagram shows HITL flow — visual proof of human-centered AI approach.
- **Phase 7 (Interview Prep)**: Three options map to Paul's experience: GCP (researched, translate from AWS), AWS (3 years as Enterprise SA — deepest expertise), Modern Cloud (Paloist + paulprae.com — production systems Paul built). For architecture interview: prepare to defend GCP recommendation given Paul's AWS background — frame as "I architect for the client's platform, not my preferred platform." For GenAI pipeline questions: reference Arine autonomous pharmacist agent as directly analogous.

## Paul's Feedback

- Pivoted from tactical/recommended/strategic options to GCP/AWS/Modern Cloud options — all modern, all viable, no strawmen
- Directed that Option C draw from Paul's actual production architectures (Paloist, paulprae.com)
- Required cited vendor reference architectures for each option
- Required rigorous validation against March 2026 cloud architecture patterns
