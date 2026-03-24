# Assumptions & Discovery Questions
## AI-Driven Prior Authorization | Autonomize AI Interview
### Paul Prae | Principal AI Engineer & Architect

> **How to use this file**: Every assumption in the architecture is a question you couldn't answer without a real client engagement. Knowing these questions — and being able to articulate why they matter — demonstrates the thoroughness of a Principal Architect. These are not gaps. They are the right questions to ask.

---

## How to Frame This in the Interview

When Kris, Suresh, or Ujjwal asks "what don't you know?" or "what would you need to validate?" — this is your moment to demonstrate senior-level thinking.

**Opening frame**: "Every architecture starts with assumptions. A good SA makes them explicit, states which design decisions they support, and knows which questions to ask first. Here are mine."

---

## Ask Early — These Impact the Overall Architecture

*If the answers here are materially different from the assumptions, the architecture changes shape.*

---

### A-1: PA Volume and Channel Distribution

**Assumption**: Top-5 US health plan scale — approximately 1 to 3 million PA requests per month, with fax as the dominant channel.

**Design decision it supports**: Service Bus Premium tier sizing; Document Processing pipeline as a core component; OCR capacity planning; Redis cache TTL calibration.

**Discovery question**: "What is the actual monthly PA volume, and what percentage arrives via fax, web portal, and X12 278 EDI? Is volume seasonal or event-driven?"

**Why it matters**: If 90% of volume is already via portal (structured input), the Document Processing pipeline is far simpler — no OCR, no handwriting challenges. If volume is 10M/month, Service Bus and Container Apps sizing changes significantly. If volume is 100K/month, we may over-engineer the async architecture.

---

### A-2: Payer Core System Interface

**Assumption**: The Payer Core System exposes a synchronous REST API for eligibility lookups and determination writes.

**Design decision it supports**: Synchronous eligibility check as a blocking step in the PA flow; real-time determination write-back; Redis caching to reduce API load.

**Discovery question**: "What is the Payer Core System? (TriZetto Facets, QNXT, Amisys, custom?) What does its API interface look like — REST, SOAP, batch file, database connector? What are the rate limits and SLA guarantees?"

**Why it matters**: If the Payer Core API is SOAP, integration is harder but not impossible. If it's batch-only (no real-time), the eligibility step can't be synchronous — the architecture needs a pre-fetched eligibility cache or a redesigned flow. If the SLA is 5 seconds per call, the cache TTL design changes entirely.

---

### A-3: FHIR R4 Adoption Percentage

**Assumption**: A mix of FHIR R4-capable EMRs and legacy systems — roughly 50/50 in Phase 1 scope.

**Design decision it supports**: Clinical Data Aggregation service with both FHIR R4 connectors and legacy DB adapters; Phase 1 FHIR-only, Phase 2 legacy connector build.

**Discovery question**: "Which EMR systems are deployed across the health plan's provider network? What percentage of those systems have live FHIR R4 endpoints? What are the legacy systems — HL7 v2, flat files, direct DB access?"

**Why it matters**: If 90% of clinical sources are FHIR R4-capable today, Phase 1 scope is much richer than assumed — more clinical data available immediately, higher AI accuracy. If 90% are legacy, Phase 1 is very limited clinical context, and the AI's accuracy depends heavily on what's available from the FHIR minority.

---

### A-4: Autonomize Platform Components Available

**Assumption**: PA Copilot, Genesis Platform, and AI Studio are available to deploy for this engagement.

**Design decision it supports**: The entire AI engine is Autonomize's product, not custom-built. Clinical Review Dashboard is AI Studio. Multi-tenant LOB config uses Genesis capabilities.

**Discovery question**: "What Autonomize platform components are currently licensed or available under the engagement? Is this a net-new deployment or integration into an existing Autonomize deployment? What's the relationship with the Pegasus Program?"

**Why it matters**: If only a subset of Genesis Platform is licensed, the architecture needs custom components for what's missing. If there's an existing Autonomize deployment at the health plan, integration patterns change — we're plugging into something, not standing it up fresh.

---

### A-5: Cloud Commitment and Multi-Cloud Constraints

**Assumption**: Azure is the correct cloud platform with no conflicting commitments or regulatory restrictions.

**Design decision it supports**: All service choices are Azure-native; no hybrid or multi-cloud routing.

**Discovery question**: "Does the health plan have existing cloud commitments — Enterprise Agreement discounts, Reserved Instance pools, compliance certifications in a specific cloud? Are there regulatory restrictions on cloud deployment for this data classification?"

**Why it matters**: If there's a major AWS spend commitment and no Azure EA, the cost model changes. If a state regulator requires on-premises for certain data, the architecture needs a hybrid layer. This isn't a blocker — it's a deployment constraint that changes the service map.

---

## Ask During Design — These Impact Integration Specifics

*These questions shape the technical design of specific components. Get answers before finalizing integration specifications.*

---

### A-6: Clinical Guidelines Source

**Assumption**: The health plan uses a standard clinical guideline system (InterQual or MCG) that the AI engine can be configured against.

**Design decision it supports**: AI engine coverage criteria configuration; eval dataset construction; human reviewer workflow design.

**Discovery question**: "Which clinical guidelines does the health plan use for PA determinations — InterQual, MCG, custom payer criteria, or a mix by LOB? How frequently are they updated, and what is the change management process?"

**Why it matters**: Autonomize's PA Copilot needs to be configured against the actual guidelines used. If the health plan uses custom payer-specific criteria, that's a more complex configuration and knowledge base build than standard InterQual. Quarterly updates mean the LLMOps pipeline needs a guidelines change management workflow.

---

### A-7: Acceptable Confidence Threshold

**Assumption**: The health plan's clinical governance team will define an acceptable confidence threshold for auto-determination.

**Design decision it supports**: Determination Router configuration; expected auto-determination rate; clinical reviewer queue sizing.

**Discovery question**: "What is the current manual auto-approval rate — PA requests that reviewers approve immediately without extended review? That's the baseline target for AI auto-determination. What confidence level would clinical governance require before auto-determination goes live?"

**Why it matters**: If clinical governance wants 95% confidence before auto-determination, the auto-approval rate will be conservative — maybe 20-30%. If they accept 80% confidence, auto-determination rate could reach Altais levels (50%). This is a clinical safety decision that determines how much reviewer time is actually saved.

---

### A-8: Fax Gateway Infrastructure

**Assumption**: The health plan has an existing fax gateway that can be integrated via SFTP file drop to Azure Blob Storage.

**Design decision it supports**: Fax ingestion path — SFTP → Blob → Document Processing — is the correct pattern.

**Discovery question**: "How is fax currently handled — physical fax machines, virtual fax service (eFax, RightFax), or a clearinghouse? What format do fax files land in — TIFF, PDF? Is there an existing fax API or is it SFTP file drop?"

**Why it matters**: If there's a virtual fax service with an API (eFax has one), the integration is push-based and real-time. If it's SFTP file drop, we need a polling job and there's inherent latency. If fax is handled by a clearinghouse that already does some digitization, the OCR requirement might be partially met.

---

### A-9: PA Denial Appeal Workflow

**Assumption**: The existing denial appeal workflow is out of scope for Phase 1 — the system produces determinations, humans handle appeals.

**Design decision it supports**: No appeals automation in Phase 1 scope. Audit trail is the appeals support mechanism.

**Discovery question**: "What is the current PA denial appeal process? How many appeals are filed per month? Do clinicians manually pull the PA record to support appeals, or is there a workflow system? Is appeal automation on the roadmap?"

**Why it matters**: If appeals are a major administrative burden, there's a Phase 2 opportunity to surface the AI's reasoning chain and evidence citations in the appeals workflow. That could be a significant value-add that changes the Phase 2 scope — and it's an Autonomize capability worth asking about.

---

### A-10: LOB Rule Complexity

**Assumption**: 20 LOBs with different administrative rules, manageable with per-LOB configuration rather than separate deployments.

**Design decision it supports**: Multi-tenant architecture with per-LOB config is sufficient; separate instances only where regulatory isolation is required.

**Discovery question**: "What are the 20 lines of business? What are the key rule differences between them — commercial vs. Medicare Advantage vs. Medicaid vs. Exchange? Are there LOBs with contractual data isolation requirements?"

**Why it matters**: If commercial and Medicare Advantage share most coverage criteria, per-LOB config handles the differences easily. If Medicaid requires state-specific rules that differ significantly from commercial, the configuration model gets complex. If any LOB has contractual data isolation requirements (separate tenant, no data commingling), multi-instance is required for that LOB.

---

## Ask Before Go-Live — These Impact Operations

*These questions don't change the architecture but they must be answered before a production launch.*

---

### A-11: Clinical Reviewer Team Size and Workflow

**Assumption**: The health plan has an existing clinical reviewer team that will be onboarded to the Autonomize AI Studio dashboard.

**Discovery question**: "How large is the current PA clinical reviewer team? Are reviewers generalists or specialists by LOB or clinical area? What is the current PA review workflow — queue management, escalation paths, peer review? Are reviewers employed or contracted?"

**Why it matters**: The Clinical Review Dashboard needs to match the existing workflow, not replace it. If reviewers specialize by clinical area, the routing logic should route to the right reviewer. If there's a peer review requirement for certain denial categories, the dashboard needs a second-reviewer capability.

---

### A-12: State-Specific PA Requirements

**Assumption**: CMS-0057-F federal requirements are the primary compliance driver.

**Discovery question**: "In which states does the health plan operate? What are the state-specific PA requirements that go beyond federal baseline — some states have stricter PA timeframe requirements, specific denial reason codes, or gold-carding provisions. Has the compliance team completed a state-by-state mapping?"

**Why it matters**: CMS-0057-F is the federal floor. Several states (California AB 352, Texas HB 3459, New York) have additional requirements on PA timeframes, denial reasons, and AI-use disclosure. If the health plan operates in these states, the compliance reporting component needs to capture and report state-specific metrics.

---

### A-13: Legal Position on AI-Assisted Determination

**Assumption**: Legal has reviewed and approved AI-assisted auto-approval. Auto-denial requires additional legal review before Phase 2.

**Discovery question**: "Has the health plan's legal team reviewed the use of AI in PA determination? What documentation is required for regulatory defense of an AI-assisted determination? Has the plan obtained legal opinion on CMS-0057-F AI disclosure requirements?"

**Why it matters**: In February 2024, a federal judge ruled against UnitedHealth for using AI (NaviHealth) to deny claims without adequate oversight. The legal landscape for AI-assisted healthcare decisions is active. The health plan's legal team needs to be part of the clinical governance design for Phase 2 auto-denial.

---

### A-14: Payer Core SLA During PA Processing

**Assumption**: The Payer Core API can support the synchronous eligibility call within the PA processing latency budget (target: under 5 seconds).

**Discovery question**: "What SLA does the Payer Core System API guarantee for eligibility lookups? What is the current P95 and P99 latency? Are there maintenance windows or known peak-load degradation periods?"

**Why it matters**: If the Payer Core API SLA is 2 seconds P95 but 15 seconds P99, the Redis cache design becomes more important — we need to pre-warm eligibility for high-volume members. If there are daily maintenance windows, the PA processing flow needs a graceful degradation path for those windows.

---

### A-15: Business Continuity and Regulatory Defense During Outage

**Assumption**: During Autonomize platform outages, PA requests queue and process on restoration within CMS-0057-F SLA windows.

**Discovery question**: "What is the health plan's current business continuity plan for PA processing? During system outages, how are CMS-0057-F timeframe commitments maintained? What is the escalation path if Autonomize has an extended outage during high-volume periods?"

**Why it matters**: CMS-0057-F has hard timeframe requirements — 72 hours standard, 24 hours urgent. If Autonomize has a 4-hour outage during a high-volume period, can the queue drain fast enough on restoration to meet SLAs for requests that arrived near the deadline? This is a clinical operations design question as much as a technical one.

---

## Summary: Assumption Dependency Map

```
Architecture Shape          → A-1 (volume), A-3 (FHIR %)
Integration Specifications  → A-2 (Payer Core API), A-8 (fax gateway)
AI Engine Configuration     → A-4 (Autonomize components), A-6 (guidelines), A-7 (threshold)
Deployment Platform         → A-5 (cloud commitment)
Multi-tenant vs Multi-inst  → A-10 (LOB complexity)
Phase 1 Scope               → A-3 (FHIR %), A-9 (appeals)
Compliance Reporting        → A-12 (state requirements), A-13 (legal position)
Operational Procedures      → A-11 (reviewer workflow), A-14 (Payer Core SLA), A-15 (BCP)
```

---

## Using These in the Interview

**When Suresh asks a deep integration question you can't fully answer**:
"That's exactly the question I'd ask during discovery. I've designed around [assumption], but the actual answer determines [specific design decision]. Here's what I'd want to find out and why it matters."

**When Ujjwal asks about a design trade-off**:
"The architecture is designed around [assumption]. If the discovery finding is different — for example, [alternative] — the design pivots to [alternative approach]. I've documented both paths."

**When Kris asks about risk**:
"The top assumptions that could change the architecture are [A-1, A-2, A-4]. The first thing I'd do in a real engagement is validate those three. Everything else is integration detail that adjusts without reshaping the architecture."
