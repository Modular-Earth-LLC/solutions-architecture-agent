# Technical Deep Dive — Per-Diagram Talking Points
## AI-Driven Prior Authorization | Autonomize AI Interview
### Paul Prae | Principal AI Engineer & Architect

> **How to use this file**: Before the interview, read the talking points aloud for each diagram. Practice the "if asked to go deeper" redirects. Know which concepts are yours to own vs. which to redirect.

---

## Diagram 1: High-Level Architecture (Slide 3) — System Context

**What it shows**: Four external actors, one AI platform in the middle. The executive view.

### Talking Points (4)

**1. "Four actors, one platform in the middle."**
Providers submit PA requests through existing channels — fax, portal, EDI. The health plan's core systems provide eligibility and clinical data. Autonomize's PA Copilot sits in the middle, processing requests and producing determinations. Regulators receive compliance reporting outputs. This is the non-technical stakeholder view — no implementation detail, all business flow.

**2. "Nothing new in the process — everything new in the execution."**
The PA business process — submit, validate, review, determine — is standardized by AMA and CAQH. This architecture doesn't reinvent the process. It automates steps 3, 4, and 5 (eligibility check, clinical data retrieval, clinical review) using AI. That framing matters for a COO audience.

**3. "Bidirectional integration with the Payer Core."**
The PA Copilot reads from the Payer Core (eligibility, benefits) and writes to it (determinations). That bidirectional relationship is the most critical integration in the system — and the one with the most unknowns until we see the actual API specification.

**4. "Compliance reporting flows to regulators as output, not as an afterthought."**
CMS-0057-F metrics are a first-class output of the system, not a reporting bolt-on. That's an architectural decision that shows regulators this isn't a last-minute compliance patch.

### If Asked to Go Deeper

**"What's the data flow for a single PA request?"** → "Let me take you to slide 5 — the PA processing flow is the detailed view of that." [Redirect to Diagram 3]

**"How does the PA Copilot actually connect to the health plan's systems?"** → "That's the integration detail on slide 7 — three specific integration points, each with the protocol and auth model." [Redirect to Diagram 4]

### Confidently Explain
- What each actor does and why they're in scope
- Why FHIR R4 is listed as a protocol label without deep implementation
- Why CMS-0057-F compliance is output, not a separate component

### Redirect Without Elaborating
- Specific EDI transaction segment details (X12 278 loops) → "EDI translation is handled at the gateway layer; the internals are translator-tool territory"
- Da Vinci IG implementation specifics → "That's a clinical informatics discovery engagement beyond the scope of this architecture"

---

## Diagram 2: System Architecture Detail (Slide 4) — Component View

**What it shows**: 10 components across 5 layers, with data flow arrows and Azure service labels.

### Talking Points (4)

**1. "Five layers, each with a clear responsibility boundary."**
Ingestion layer receives and normalizes. Integration layer connects to external systems. AI engine reviews and routes. Human review handles exception cases. Response layer closes the loop back to the Payer Core and notifies providers. Clean separation of concerns — each layer can be changed without touching others.

**2. "The AI engine is Autonomize's PA Copilot — I'm integrating it, not rebuilding it."**
This is an important framing distinction. PA Copilot and Genesis Platform are Autonomize's product. My job is to wire it correctly into the health plan's ecosystem with the right auth, data contracts, and safety controls. That's where the architectural value is — not reimplementing what Autonomize already built.

**3. "Azure Service Bus is the decoupling mechanism."**
The message queue sits between ingestion and the AI engine. Every component pushes and pulls through Service Bus — nothing calls the AI engine synchronously except what has to be synchronous. That queue is why the system is resilient to Autonomize platform outages and traffic spikes.

**4. "Every path ends at the audit and compliance store."**
Follow any data flow arrow — it terminates at immutable Blob Storage. Auto-approve, human review, pend for info — all paths write to the audit trail. That's the regulatory defense layer. CMS-0057-F and HIPAA require tamper-proof decision records; the immutable storage designation is the architectural response.

### If Asked to Go Deeper

**"How does the Document Processing pipeline handle different file types?"** → "OCR for faxes is Azure AI Document Intelligence — it extracts structured data from images. PDFs from the portal go through the same pipeline. EDI bypasses OCR entirely — it's already structured. The output in all cases is a canonical JSON PA record on Service Bus."

**"What's in the canonical PA record format?"** → "Member ID, requested service/procedure code, provider NPI, submission timestamp, intake channel, extracted clinical summary fields. Exact schema is a design-phase artifact with clinical informatics input — I haven't defined it to that field level here."

**"Why Azure Container Apps over AKS?"** → "Container Apps is managed Kubernetes — I get autoscaling and container orchestration without managing control plane infrastructure. AKS is the right choice if you need deep Kubernetes customization. At PA volumes of 1-3M/month, Container Apps handles it without the operational overhead of a self-managed cluster. AKS is a Phase 3 consideration if we need node-pool customization."

### Confidently Explain
- What each component does and which Azure service powers it
- Why the message queue decouples the AI engine from the ingestion layer
- How the confidence-based router connects to the human review dashboard
- Why both FHIR R4 and legacy DB connectors feed into the same aggregation layer

### Redirect Without Elaborating
- Specific SageMaker vs. Azure ML comparison → "SageMaker is AWS's ML training and deployment service; this architecture uses Azure AI Foundry Agent Service for the agent runtime, not a custom model training pipeline"
- Specific dbt/Snowflake data warehouse patterns → "Data warehouse integration isn't in scope for this architecture — the data flows are transactional, not analytical"

---

## Diagram 3: PA Processing Flow (Slide 5) — Business Process Sequence

**What it shows**: The 6-step PA lifecycle from provider submission to determination, with the three routing outcomes.

### Talking Points (3)

**1. "This is the AMA/CAQH standard PA process — we're not inventing steps, we're automating them."**
Receive, validate eligibility, retrieve clinical data, review, determine, respond. These steps exist today. The innovation is in the speed and consistency of steps 4 and 5. When Kris asks "what does this do," this diagram is the answer — PA requests go in, determinations come out faster and more consistently.

**2. "Three determination outcomes, configured by clinical governance — not hardcoded."**
Auto-approve fires when confidence is above the threshold. Human review fires when confidence is below. Pend fires when data is insufficient. The threshold is a parameter, not a constant. A conservative health plan sets a higher threshold — more cases go to humans. An aggressive one sets lower. The architecture supports the business decision without constraining it.

**3. "Auto-denial is explicitly not on this diagram."**
That's intentional. Phase 1 has no auto-denial path. If the AI is confident it should be denied, it still goes to a human reviewer. That's a safety and regulatory position — not a technical limitation. The panel will notice the absence. Own it before they ask.

### If Asked to Go Deeper

**"What happens to the PA request that gets pended?"** → "The system notifies the provider via their preferred channel — fax, portal response, or EDI 278 acknowledgment — with a specific request for the additional clinical information needed. It's queued for reprocessing when the provider responds. CMS-0057-F mandates the response timing, so the pend state has a clock attached."

**"What's the eligibility check actually checking?"** → "Member ID validity, coverage active status, whether the requested service requires PA under the member's benefit plan, and contract-specific rules. That last one — contract rules — is the complexity layer. Different contracts have different PA requirements for the same CPT code. That's why the Payer Core System is the authoritative source."

**"What about urgent PA requests — different flow?"** → "The flow is the same steps, different SLA clock. CMS-0057-F requires 24-hour turnaround for urgent vs. 72 hours for standard. The system tags urgency at ingestion and the confidence threshold for auto-routing can be adjusted for urgent cases — faster determination is worth accepting slightly lower confidence on an urgent PA."

### Confidently Explain
- Each step in the flow and what happens at each
- Why auto-denial is absent from Phase 1
- How the confidence threshold creates the three routing outcomes
- The regulatory SLA context (24h urgent, 72h standard)

### Redirect Without Elaborating
- Specific InterQual vs. MCG coverage criteria differences → "Coverage criteria are the health plan's clinical guidelines — the AI matches evidence against whichever guidelines the client uses. Selection is a clinical governance decision."
- KS test / PSI drift statistics → "Drift detection here is output-quality monitoring — overturn rates and eval regression — not traditional model statistics. The LLMOps diagram covers that."

---

## Diagram 4: Clinical Data Integration (Slide 7) — Integration Detail

**What it shows**: Two-source clinical data architecture — FHIR R4 for modern EMRs, legacy DB connectors for older systems.

### Talking Points (3)

**1. "Two worlds, one aggregation layer."**
Modern EMRs — Epic, Oracle Health, Cerner — expose FHIR R4 endpoints natively. Older systems — legacy claims databases, older clinical systems — don't. The aggregation service handles both, normalizing to FHIR-compatible format before the AI engine sees it. The AI always gets clean, consistent clinical context regardless of source.

**2. "FHIR R4 is the interoperability label, not a deep implementation commitment."**
I use FHIR R4 as the standard because it's the CMS-mandated baseline and modern EMRs speak it natively. What I haven't done is design a full FHIR server with Da Vinci Implementation Guide conformance — that's a clinical informatics project, not a solutions architecture diagram. Suresh will know this distinction. Own it directly.

**3. "PHI tokenization happens at this boundary."**
Before any clinical data crosses into the AI engine, PHI is tokenized. Patient name, date of birth, SSN, and other direct identifiers are replaced with tokens. The AI sees clinical facts — diagnosis codes, procedure history, lab values, medication history — without patient identity. The de-identified clinical context is sufficient for coverage matching.

### If Asked to Go Deeper

**"What specific FHIR resources does the AI receive?"** → "Patient (demographics needed for context, tokenized), Encounter (recent care history), Observation (labs, vitals), DiagnosticReport (radiology, pathology), Condition (diagnosis list), MedicationRequest (current medications). Those six resources give the AI the clinical narrative it needs for coverage matching. Additional resources — CarePlan, Procedure history — are Phase 2 additions."

**"How does SMART on FHIR auth work in this architecture?"** → "SMART on FHIR is the OAuth 2.0 profile for healthcare API authorization. The aggregation service authenticates to each FHIR endpoint using a service account with read-only scope. Entra ID manages the credentials and enforces conditional access. The service account has minimum necessary access — it can read clinical resources for the specific member in the PA request, nothing broader."

**"What if a FHIR endpoint is down during PA processing?"** → "The aggregation service has a retry with exponential backoff. If the FHIR endpoint doesn't respond within the SLA window, the PA is pended — routed to human review with a flag that clinical data was unavailable. We don't auto-determine without clinical data. The audit log captures the unavailability event."

### Confidently Explain
- Why two source types exist and how the aggregation layer unifies them
- What FHIR R4 means as an interoperability standard (not implementation detail)
- Why PHI tokenization happens at this boundary, not earlier or later
- Which FHIR resources are in scope

### Redirect Without Elaborating
- FHIR Da Vinci Implementation Guide specifics → "Da Vinci IG is the clinical informatics layer — profiles, extensions, must-support elements. That's discovery-phase work with the EMR vendors and clinical informatics team."
- Specific legacy system schemas (TriZetto Facets field names, etc.) → "Per-system field mapping is a per-source discovery activity — that's what the Phase 2 legacy connector work scopes."

---

## Diagram 5: LLMOps Pipeline (Slide 8) — AI Model Monitoring

**What it shows**: The four-step feedback loop for monitoring and maintaining AI output quality over time.

### Talking Points (3)

**1. "This is LLMOps, not MLOps — the monitoring approach is fundamentally different."**
Traditional ML drift monitoring watches for input distribution shift and model performance decay. We're not retraining models — Autonomize's PA Copilot is a hosted AI service. LLMOps monitors output quality: are the determinations correct? Are the reasoning chains valid? Are human reviewers overturning AI recommendations at an acceptable rate? The signal is behavioral, not statistical.

**2. "Human reviewer corrections are the most valuable signal in the system."**
When a reviewer overturns an AI recommendation — approves a case it would have denied, or vice versa — that correction is captured. It feeds into the eval dataset. Over time, a library of human-validated cases becomes the benchmark against which new model versions are tested. The feedback loop converts clinical expertise into a continuously improving quality measure.

**3. "Guardrails are always active — they don't turn off during blue-green deployment."**
Input filtering, output validation, and citation requirements are enforced regardless of what model version is running. They're infrastructure, not application logic. During a blue-green rollout of a new model version, both environments run with identical guardrails. That's the safety layer that makes confident deployment possible.

### If Asked to Go Deeper

**"What's in the golden test case dataset?"** → "Clinical PA scenarios with known-correct determinations — a mix of clear approvals, clear denials, and edge cases. Each test case includes the clinical context, the PA request, and the expected determination with reasoning. The dataset is built from historically validated cases, de-identified. Size matters — we want enough cases per procedure type and LOB to be statistically meaningful. Starting size is a clinical governance decision."

**"How do you decide when to trigger model revalidation?"** → "Three triggers: overturn rate exceeds the baseline by more than X% over a rolling window; confidence distribution shifts detectably; or eval pass rate drops below the acceptance threshold. The specific thresholds are business parameters set by clinical governance. Engineering sets the monitoring infrastructure; clinical sets the alarm levels."

**"What if a new model version is worse — what's the rollback?"** → "Blue-green deployment means the previous version is still running. Traffic shift is incremental — 10%, then 25%, then 100%. If metrics degrade at any shift point, we shift traffic back to the previous version. Container Apps makes this a configuration change, not a redeployment. Rollback time is under a minute."

### Confidently Explain
- Why this is LLMOps vs. MLOps and why the distinction matters
- How the overturn rate signal works
- What the feedback loop produces (eval dataset updates)
- Why guardrails are infrastructure, not application code

### Redirect Without Elaborating
- Kolmogorov-Smirnov test / PSI (Population Stability Index) specifics → "Those are traditional ML drift statistics — for tabular model monitoring. We're in LLMOps territory here; the quality signal is behavioral, not distributional. I'd rely on an ML engineer to spec out the statistical monitoring layer if the client wants it."
- Specific Azure ML model registry details → "Azure AI Foundry manages model versioning for the hosted models. The LLMOps pipeline integrates with those version APIs — the specifics are implementation-level detail."

---

## Diagram 6: Security & Zero Trust (Slide 6) — Risk and Mitigation Table

**What it shows**: Three top security risks with architectural mitigations. The table format rather than a flow diagram.

### Talking Points (4)

**1. "I led with AI-specific risks, not generic cloud security."**
PHI exposure through the AI pipeline and prompt injection are novel attack surfaces in healthcare AI — they didn't exist five years ago. A generic security review of a cloud app would miss them. Leading with AI-specific risks signals that this is security-informed AI architecture, not AI bolted onto a standard cloud app.

**2. "PHI tokenization is the key AI safety control."**
The AI engine never sees patient identity. It sees clinical facts — diagnosis codes, procedure history, medication list. PHI tokens map back to patient identity only in the audit layer, which operates outside the AI engine's context window. Even if the AI is compromised or an adversarial clinical document attempts extraction, there's no PHI to exfiltrate.

**3. "The audit trail is the regulatory defense artifact."**
Every determination record contains: model version, input document hash, clinical context hash, reasoning chain, evidence citations, confidence score, and the reviewer identity if applicable. Immutable 7-year retention. That's what you need to defend a PA determination before a state regulator or in an ERISA appeal.

**4. "Human review for all denials is a safety principle, not a Phase 1 limitation."**
Phase 2 may add auto-denial with additional safeguards — dual-review, clinical oversight committee sign-off on threshold settings. But the principle that auto-denial requires stronger governance than auto-approval is permanent. The asymmetry exists because denying access to care has higher stakes than approving it.

### If Asked to Go Deeper

**"What about HIPAA BAA coverage for Azure services?"** → "All Azure services in this architecture are covered by Microsoft's HIPAA BAA — Service Bus Premium tier specifically requires the Premium SKU for BAA coverage. Standard tier is not BAA-eligible. That's a line item in the architecture decision table and a procurement checkpoint."

**"How does Entra ID RBAC work for clinical reviewers?"** → "Clinical reviewers are assigned role-based access to the Autonomize AI Studio dashboard — they can see cases assigned to their queue, confirm or override recommendations, and add notes. They cannot see cases outside their assigned LOB or queue. Service accounts for system integrations are separate identities with minimum necessary permissions — read-only where read-only is sufficient."

**"What about SOC 2 / HITRUST for the deployment?"** → "Azure Health Data Services and the core services are HITRUST-certified. Autonomize AI has HIPAA BAA and is designed for healthcare deployment. The application layer — the code we write — needs to go through a HITRUST assessment. That's a project activity, not an architecture question, but it's scoped in Phase 3."

### Confidently Explain
- The three-risk table and why each mitigation addresses the specific risk
- PHI tokenization concept and why it's the right AI safety control
- Why the audit trail design (what it captures and why) matters for regulatory defense
- Zero Trust principles applied to healthcare AI

### Redirect Without Elaborating
- Specific NIST control IDs → "I design to NIST CSF principles — identify, protect, detect, respond, recover. Mapping to specific control IDs (like SC-28 or AC-17) is compliance documentation work that follows the architecture. I'd work with a compliance team to do that mapping."
- Specific HITRUST CSF control inheritance → "HITRUST inheritance is a compliance assessment activity — Azure's certification covers the infrastructure layer; the application layer assessment is scoped as a project deliverable, not an architecture artifact."
