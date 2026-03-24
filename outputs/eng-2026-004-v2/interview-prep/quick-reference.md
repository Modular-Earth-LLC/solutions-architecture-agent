# Quick Reference -- During Q&A
## AI-Driven Prior Authorization — Autonomize AI Interview

> Keep this open during the interview for fast lookup when the panel asks questions.
> For full presentation flow, see [speaker-script.md](../speaker-script.md).

---

## Kris Nair (COO) -- Business Questions

### Q1: "What's the business case for this architecture?"

**Answer (45 sec):**

"The business case starts with cost: the CAQH Index — an annual labor cost survey of providers and health plans — shows a health plan pays $3.52 in labor per manual PA transaction. Fully electronic, that drops to about five cents. That's $3.47 saved per transaction. At a million PAs per month, that's $3.47 million in monthly savings potential from a single line item.

But the cost story isn't even the strongest argument. CMS-0057-F Phase 1 is already live -- January 2026. Non-compliance is an existential regulatory risk. And Altais proved in February 2026 that Autonomize's platform delivers 45% faster review, 54% fewer errors, and a 50% auto-determination rate.

My architecture integrates those capabilities with the right safety controls -- no auto-denial in Phase 1, human reviewers retain final authority, full audit trail for regulatory defense."

**Bridge to slide**: Slide 2 (Why This Architecture) -- the three Altais metrics are on that slide.

---

### Q2: "How fast can we see ROI?"

**Answer (50 sec):**

"Progressive delivery means value at every phase. Phase 0 is a proof-of-concept -- a working AI PA review running against real clinical data within a few weeks. That's not a demo build -- it's the actual architecture, live, with real Autonomize APIs. It proves the concept before committing to full build.

Phase 1 MVP deploys to a single line of business on a single intake channel. The first real auto-determination rate is measurable the day it goes live. Every PA that routes automatically instead of manually is immediate cost recovery -- $3.47 saved per transaction.

The key point: ROI doesn't wait for Phase 3. Each phase is designed to produce something real and measurable. And the architecture is reversible -- decision gates between phases use performance data, not optimism."

**Bridge to slide**: Slide 9 (Progressive Delivery).

---

### Q3: "How does this compare to competitors?"

**Answer (45 sec):**

"Autonomize is already in market -- three of the top five US health plans are live on the platform. Cohere Health is the closest comparable -- they process 12 million PAs per year and recently raised significant venture capital.

The Autonomize differentiator is the Genesis Platform with the Agents Marketplace -- 100+ pre-built clinical agents, each specialized. That's faster time-to-value than building custom AI from scratch. It also means new use cases -- appeals automation, clinical documentation improvement -- can be added as agents without re-architecting.

And critically: Autonomize has a dedicated Pegasus Program for health plan deployments, and they're on the Azure Marketplace. That means procurement is streamlined and the integration patterns are pre-validated."

---

### Q4: "What if the AI makes a wrong determination?"

**Answer (55 sec):**

"The architecture is designed around that exact question. In Phase 1, the AI makes two calls: auto-approve when confidence is above a configurable threshold, and route to human review when it's not. Auto-denial is not enabled in Phase 1 -- every denial requires a clinical reviewer.

The confidence threshold is a business parameter, not a technical one. If the client wants conservative AI involvement, we set a higher threshold -- more cases go to humans. If they want aggressive automation, we lower it. That's a clinical governance decision, not an architecture limitation.

When the AI is wrong -- and it will be sometimes -- the overturn rate becomes a key metric. Human corrections feed back into the eval dataset. The LLMOps pipeline monitors this continuously. Systematic errors trigger model revalidation before anything else goes to production."

**Bridge to slide**: Slide 6 (Security & Zero Trust) -- the third risk row covers auditability.

---

## Suresh Gopalakrishnan (SA) -- Integration Questions

### Q5: "How does the eligibility check work exactly?"

**Answer (55 sec):**

"The eligibility service makes a synchronous REST API call to the Payer Core System -- it's a blocking call because we need eligibility confirmed before AI review starts. The call returns member status, benefit details, whether PA is required for the requested service, and any contract-specific rules.

I've added Redis caching with a 15-minute TTL to protect the Payer Core API from repeated calls for the same member. That's a common pattern I used at AWS when we were architecting high-volume transactional systems for healthcare customers -- eligibility APIs are often the bottleneck, not the AI.

The critical unknown here is what API interface the Payer Core System actually exposes. TriZetto Facets, QNXT, and custom builds all have different contract structures. That's a discovery question I'd ask on day one -- what does the Payer Core API specification look like?"

**Bridge to slide**: Slide 7 (Clinical Data Integration) shows the integration layer.

---

### Q6: "What about legacy database connectors?"

**Answer (50 sec):**

"Phase 1 is FHIR R4 only -- modern EMR sources that already expose FHIR endpoints. Legacy connectors are Phase 2 work.

Why defer it? Because legacy integration is a per-system discovery effort. Every legacy database has its own schema, its own auth model, its own data quality issues. Scope that before committing to timelines, not after.

At Booz Allen and in my AWS practice, legacy clinical system integration was consistently the longest-tail work -- not because it's architecturally hard, but because it requires clinical informaticists to map source data to the target schema, and that's domain expert work that can't be engineered around.

The Phase 2 approach: clinical informaticists scope each legacy source, we build per-system adapters behind a unified aggregation layer. The AI engine never sees the legacy system -- it always gets normalized FHIR-compatible format."

---

### Q7: "What about fax OCR for handwritten notes?"

**Answer (45 sec):**

"Azure AI Document Intelligence handles printed and typed fax content well. Handwritten clinical notes are genuinely hard -- the OCR accuracy drops and it varies by handwriting quality.

The architecture handles this with a confidence threshold: low-confidence OCR extractions are flagged and routed to manual review, same queue as low-confidence AI determinations. A reviewer sees the original fax image alongside the OCR extraction, corrects it, and the corrected version is the record of truth.

At Arine, we processed clinical documents at scale -- the pattern of 'extract, flag low-confidence, human-in-the-loop for exceptions' is the only one that works reliably when input quality is variable. Start the fax rollout with typed forms, validate OCR accuracy, then phase in handwritten after you've tuned the confidence thresholds."

---

### Q8: "What if clinical accuracy drops over time -- AI drift?"

**Answer (55 sec):**

"This is LLMOps, not traditional MLOps, which changes the monitoring approach. We're not monitoring model weights -- we're monitoring output quality against known standards.

The three signals are: overturn rate -- the percentage of AI recommendations that human reviewers override; confidence distribution shift -- if the AI starts being less certain on cases it used to handle easily; and eval regression -- automated test cases against a golden dataset of known-correct PA determinations.

When any signal exceeds thresholds, the pipeline triggers: no model changes to production, re-validation against the golden test set, staged rollout if improved.

The practical driver of 'drift' here isn't model degradation -- it's coverage criteria changes. Clinical guidelines update quarterly. If the coverage criteria the AI was trained against are stale, accuracy drops. That's a knowledge base update problem, not a model problem."

**Bridge to slide**: Slide 8 (AI Model Monitoring & Feedback).

---

### Q9: "How does the FHIR facade work for legacy sources?"

**Answer (45 sec):**

"The aggregation service is an adapter layer -- it reads from legacy data sources using whatever interface each system exposes and normalizes the output to a FHIR R4-compatible JSON structure before the AI engine sees it.

This is not full FHIR conformance -- I'm deliberately not claiming that. Full FHIR implementation, including Da Vinci IG compliance, is a deep clinical informatics engagement that requires EHR vendor coordination and clinical data governance. That's discovery-phase work.

What I've designed is a well-understood adapter pattern: standardize at the boundary before the AI processes it. The AI always gets clean, normalized clinical context regardless of what the source system looks like. Ujjwal can speak to whether this needs to be a full FHIR server or just the transformation layer -- that's a design decision that follows from the data governance requirements."

---

### Q10: "What about X12 278 EDI intake -- how does that work?"

**Answer (50 sec):**

"X12 278 is the standard PA request transaction in EDI. The ingestion gateway accepts it as one of three intake channels alongside fax and web portal.

EDI intake gets normalized to the canonical PA record format at the gateway -- the same internal format that fax and portal submissions produce. Downstream components don't know or care which channel the request came from.

I'll be direct about my EDI depth: I understand the role X12 278 plays in the PA workflow and the normalization pattern, but the specific segment-level transaction details -- ISA/GS loops, 2000B loops, specific field mappings -- are something I'd work through with an EDI integration specialist. In real practice, you use an EDI translator (Edifecs, Optum ClearingHouse) rather than building raw X12 parsing yourself."

---

## Ujjwal Rajbhandari (VP Eng) -- Architecture Questions

### Q11: "Why Azure over GCP -- you have AWS certs, Autonomize is Azure-native, but why not GCP?"

**Answer (50 sec):**

"Three reasons, in priority order: platform alignment, model availability, and pattern transferability.

Platform alignment: Autonomize is in the Azure Marketplace with an active Pegasus Program for health plan deployments. That means faster procurement, pre-validated integration patterns, and joint engineering support. That's not a technical argument -- it's an enterprise deployment reality.

Model availability: Azure AI Foundry is the only cloud where Claude and GPT-4 models are available in the same environment. For an AI-driven PA architecture, having both models available without cross-cloud latency matters.

Pattern transferability: Every AWS pattern I know -- SQS maps to Service Bus, CloudWatch maps to Azure Monitor, Textract maps to Document Intelligence. My five AWS certifications mean I understand the architectural principles deeply. The cloud-specific APIs are the easy part to learn. And GCP is a legitimate alternative -- if the client had an existing Google relationship, this diagram would be essentially the same with GCP labels."

---

### Q12: "Multi-tenant vs multi-instance for 20 LOBs -- how do you make that call?"

**Answer (55 sec):**

"Start multi-tenant with per-LOB configuration -- that's the recommendation on slide 10. It's lower cost, lower operational complexity, and Autonomize's Genesis Platform already supports multi-tenant LOB isolation via configuration.

The only reason to move to separate instances is regulatory isolation. If a specific LOB is subject to different state regulations, or a specific contract requires data not commingled with other LOB data -- those are cases for separate instances. That's a compliance question, not a technical preference.

The architectural safeguard in multi-tenant: every PA record is tagged with LOB identifier from the moment it enters the ingestion gateway. All queries, all audit logs, all reporting are LOB-scoped. Data isolation is enforced at the application and database level, not just at the instance level. That gives you the cost benefits of multi-tenant with auditable per-LOB boundaries."

**Bridge to slide**: Slide 10 (Scaling to 20 LOBs) -- the trade-off table is there.

---

### Q13: "How do you handle prompt injection in clinical documents?"

**Answer (50 sec):**

"Clinical documents are user-supplied input that flows into an LLM -- that's exactly the attack surface for prompt injection. Three layers of defense:

First, document sanitization. Before the OCR output or portal text reaches the AI engine, it's stripped of content that could contain instructions -- HTML, script-like patterns, anything that looks like an LLM control sequence.

Second, system prompt isolation. The AI engine's coverage criteria and instructions are loaded in the system context, not as user-role messages. The clinical document goes in as user-role content. This isn't injection-proof on its own, but it reduces the attack surface.

Third, and most important: output validation. Every determination must include specific evidence citations from the clinical record. An injected instruction can't produce evidence-backed reasoning -- if the output lacks clinical citations, it's flagged as invalid and routed to human review. That's the architectural control that actually defends against a real injection attack."

**Bridge to slide**: Slide 6 (Security & Zero Trust) -- row 2 of the risk table.

---

### Q14: "What's your deployment model -- how do you do zero-downtime updates?"

**Answer (45 sec):**

"Azure Container Apps with blue-green deployment. The AI engine is one of the components on this model -- when a new model version is approved through LLMOps, it deploys to the green environment, traffic shifts 10% initially, metrics confirm parity, then we shift 100%.

Azure Service Bus provides the async buffer that makes this work cleanly. During a deployment, new PA requests queue. Once the new version is live and validated, it processes from the queue. No PA request is dropped, no half-processed records.

The Payer Core integration is the constraint -- that's a synchronous blocking call to an external system we don't control. We wrap it with circuit breaker pattern so if the Payer Core API degrades, requests queue rather than fail. That's the pattern I'd insist on in a production health plan environment."

---

### Q15: "How does monitoring work -- what does your LLMOps dashboard actually show?"

**Answer (55 sec):**

"Two monitoring planes: infrastructure and AI-specific.

Infrastructure: Azure Monitor with OpenTelemetry distributed tracing across all components. Every PA request gets a correlation ID that flows through the entire lifecycle -- ingestion to audit log. App Insights gives us latency percentiles, error rates, queue depth. Standard observability stack, same as I'd build on AWS CloudWatch and X-Ray.

AI-specific -- the LLMOps plane: overturn rate by LOB and procedure type, confidence distribution, auto-determination rate, eval pass rate against golden test cases, time-to-determination. These metrics live in a separate dashboard because they have different audiences -- clinical governance reviews overturn rate, engineering reviews latency.

The key insight is that AI drift in this system is rarely a technical failure -- it's a clinical knowledge base problem. The LLMOps dashboard is the early warning system that tells you when coverage criteria changes are making the AI wrong before you find out from claims disputes."

**Bridge to slide**: Slide 8 (AI Model Monitoring & Feedback).

---

## General Skepticism

### Q16: "What if the Autonomize platform goes down?"

**Answer (40 sec):**

"The queue-based architecture is specifically designed for this scenario. PA requests arrive at the ingestion gateway and go onto Azure Service Bus. The AI engine -- the Autonomize PA Copilot -- processes from the queue asynchronously.

If Autonomize goes down, requests queue. The Payer Core System continues operating. Clinical reviewers continue working on already-queued cases in the dashboard. When Autonomize is restored, the queue drains in order.

For regulatory compliance, CMS-0057-F requires a 72-hour response window for standard PAs and 24 hours for urgent. A short Autonomize outage doesn't violate that window if the queue processes on restoration. A prolonged outage triggers the business continuity plan -- that's a clinical operations decision, not an architecture decision."

---

### Q17: "I'm worried about vendor lock-in -- what if we need to swap out components?"

**Answer (45 sec):**

"The architecture is intentionally generic-first. Every component is labeled by function before it's labeled by vendor. The AI engine is 'PA Copilot / Genesis Platform' -- if Autonomize were replaced by a different AI platform, the integration surface is the Service Bus message format and the REST API contract. That's a well-defined boundary.

The Azure services -- Service Bus, Container Apps, Health Data Services -- have AWS equivalents for every one of them. I've built the same patterns on both clouds. The Azure-specific APIs are the thin layer; the architectural patterns are cloud-agnostic.

For Autonomize specifically: the Genesis Platform exposes standard REST APIs and MCP protocol, which is an emerging standard. That's better than a proprietary SDK integration -- it means portability is possible even within the AI engine layer."

---

### Q18: "What don't you know? Where are your gaps on this?"

**Answer (60 sec):**

"Excellent question -- this is exactly what a thorough SA should be honest about.

What I'd want to discover before committing to implementation:

One -- the actual Payer Core API specification. Everything in the integration layer is designed around an assumed REST interface. If it's a SOAP service, batch-only, or has rate limits we don't know about, that changes the design.

Two -- the FHIR R4 adoption percentage across their clinical data sources. If 80% of their EMR systems are legacy-only, Phase 1 scope changes significantly.

Three -- the exact LOB rule complexity. If the 20 LOBs have truly independent coverage criteria with no overlap, the AI engine configuration model becomes more complex.

Four -- the state regulatory position on AI-assisted determination in each LOB's geography.

Five -- what Autonomize platform components are already licensed versus what requires new procurement.

These aren't gaps in my architecture -- they're the questions that require a real discovery engagement before anyone should commit to implementation timelines. Surfacing them now is the job of a principal architect."

---

## Quick Pivots

| If Asked About... | Say This |
|---|---|
| FHIR Da Vinci | "Discovery-phase activity with clinical informaticists" |
| EDI X12 details | "Integration-build detail -- translator-tool territory" |
| KS test / PSI | "LLMOps is eval-driven, not distribution-driven" |
| Autonomize internals | "No public API docs -- discovery question for onboarding" |
| TOGAF | "I focus on iterative architecture -- design, validate, iterate" |
| Snowflake/dbt | "Not in scope -- PA processing is transactional" |
| NIST control IDs | "I design to principles; control ID mapping follows the architecture" |
| SageMaker | "AWS ML training -- this uses Azure AI Foundry Agent Service" |
| InterQual vs MCG | "Clinical governance decision -- the AI matches whatever the client uses" |
| TriZetto Facets API | "Discovery question -- designed around assumed REST interface" |
| HITRUST CSF controls | "HITRUST inheritance is a compliance assessment activity -- scoped as a Phase 3 project deliverable" |
