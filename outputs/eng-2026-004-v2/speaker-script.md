# Speaker Script & Presentation Guide
## AI-Driven Prior Authorization | Autonomize AI Interview

> **Use alongside [presentation.md](presentation.md) during the interview.**
> For deeper technical reference, see [solution-architecture-source-of-truth.md](solution-architecture-source-of-truth.md).

---

## Opening Thesis (60 seconds -- memorize this)

"I'm Paul Prae. I've spent 15 years building AI systems in healthcare -- most recently at Arine, where our platform served 50 million members across 45 health plans, and before that as an ML Solutions Architect at AWS.

I designed this architecture to answer a specific question: how does a large US health plan integrate Autonomize AI's PA Copilot safely and effectively into its existing IT environment?

The answer is a 10-component Azure-native system that automates PA intake, clinical review, and determination -- with human oversight built in at every exception case. Based on Altais's February 2026 results: 45% faster reviews, 54% fewer errors, 50% auto-determination rate.

I'll take you through the architecture in tiers -- executive context, then technical depth, then implementation path. Stop me anywhere."

---

## Time Navigation

| Time Remaining | Action |
|---|---|
| 30+ min | Tier A (slides 1-6) at full pace, then invite questions |
| 15-20 min | Tier A only. Skip slide 4 detail if already explained verbally |
| 10-15 min | Slides 1-3 + 5 only. "Happy to go deeper on anything" |
| Under 10 min | Opening thesis only. Offer to take questions |
| Tier B (7-9) | Only if 10+ min remain after Tier A |
| Tier C (10-11) | Appendix only. Never present proactively |

**3-minute rule**: If you've been on one slide for 3 minutes without a question, stop and ask "Is this the right level of detail?"

---

## Per-Slide Notes

### Slide 1: Title & Introduction
**Core (30 sec)**: "15 years healthcare AI. Arine 50M members. AWS ML SA. Excited about PA automation."
**Don't elaborate**: Resist going deep on any single past role. 60 seconds max on intro.
**Pivot**: If asked about specific experience -- "Let me walk through the architecture -- I'll connect each decision to experience as we go."

### Slide 2: Why This Architecture
**Core (30 sec)**: "Manual PA is expensive and slow. Altais proved Autonomize cuts review time 45%, errors 54%. My architecture integrates that with safety controls."
**Expanded**: CAQH Index — $10.97 provider labor cost per manual PA, $3.52 payer side, $0.05 electronic. That's $3.47 savings per payer transaction ($3.52 − $0.05). CMS-0057-F Phase 1 live. Clinicians keep final authority.
**For Kris**: This answers "why should I care?" -- lead with business outcomes.
**Don't elaborate**: Don't dive into CAQH methodology or CMS rule details. If asked: "CAQH measures labor costs — salaries, benefits, overhead — per transaction via annual industry survey."

### Slide 3: System Context
**Core (30 sec)**: "Four actors, one AI platform in the middle. Providers submit through existing channels. Determinations flow back to payer core."
**Expanded**: Generic-first design. Integration points labeled. No new workflows for providers.
**For Suresh**: "These are the standard patterns I've seen at scale."

### Slide 4: Component Architecture
**Core (30 sec)**: "Ten components with Azure labels. AI engine is Autonomize's PA Copilot -- I'm integrating it, not rebuilding it."
**Expanded**: Azure Service Bus for async (simpler than Kafka, HIPAA-covered on Premium). Every service has AWS equivalent.
**For Ujjwal**: "Azure because Autonomize is Azure-native. My AWS background translates directly -- patterns identical, service names change."
**Don't elaborate**: Don't list all 10 components. Let the diagram speak.

### Slide 5: PA Processing Flow
**Core (30 sec)**: "Six steps, standard PA process per AMA/CAQH. Innovation in steps 4-5: AI review with confidence-based routing."
**Key point**: Confidence threshold configurable per LOB. Start conservative. Auto-denial NOT enabled Phase 1.
**For Suresh**: "Process follows CAQH CORE operating rules -- I didn't invent a new workflow."
**Don't elaborate**: No X12 278 parsing details. If asked: "Integration-build detail for discovery."

### Slide 6: Security & Zero Trust
**Core (30 sec)**: "Three risks, three architectural mitigations. AI-specific controls first -- that's the novel attack surface."
**Risk 1**: PHI tokenization -- LLM sees clinical facts without patient identity.
**Risk 2**: Prompt injection defense -- output validation requires evidence citations. Injected content can't produce evidence-backed determination.
**Risk 3**: Tamper-proof audit trail -- model version, input hash, reasoning, evidence, confidence. 7-year retention.
**For Ujjwal**: "This is zero trust for AI -- verify every input, validate every output, log everything."

### Slide 7: Clinical Data Integration
**Core (30 sec)**: "Two worlds -- FHIR R4 and legacy. Aggregation service presents unified context. FHIR at label level."
**Don't elaborate**: No Da Vinci IG, no SMART on FHIR scopes, no FHIR resource schemas. If asked: "Discovery-phase activity with clinical informaticists."

### Slide 8: LLMOps Pipeline
**Core (30 sec)**: "LLMOps not MLOps. Monitoring LLM output quality -- evals, guardrails, human feedback."
**Key distinction**: Drift = coverage criteria changed, not model weights shifted. Overturn rate is the key metric.
**For Ujjwal**: "Traditional ML drift metrics (KS, PSI) apply if we add a triage classifier. LLM monitoring is eval-driven."

### Slide 9: Implementation Roadmap
**Core (30 sec)**: "Four phases, each producing something real. AI features front-loaded."
**Don't elaborate**: No specific week numbers or team sizes. If asked: "Depends on discovery findings and team composition."

### Slide 10: Scaling to 20 LOBs
**Core (30 sec)**: "Multi-tenant with per-LOB config as starting point. Separate instances only for regulatory isolation."
**Key framing**: Trade-off discussion, not prescriptive answer. Discovery questions determine the right approach.

### Slide 11: Discussion Starters
**Core**: "These are questions I'd ask in real discovery. Love to explore any of these with you."

---

## Conversation Pivot Phrases

**Anchor on slide**: "Let me point you to slide [N] -- I've captured that there."
**Buy time**: "Great question -- are you asking about [A] or [B]?"
**Redirect from gap**: "That's exactly what I'd discover in a real engagement. Here's what I'd ask and why it matters..."
**Back to business value**: "The Altais result is the evidence. My architecture delivers the same pattern."
**Invite the panel**: "Where would you like to spend time? I'm comfortable going deep on integration or stepping back to business case."

---

## Closing Summary (30 seconds -- land this no matter what)

"Let me land on the core: a system where Autonomize's PA Copilot integrates safely into the health plan's ecosystem -- reliable intake from fax, portal, and EDI; AI-driven clinical review with human oversight for exceptions; full audit trail for regulatory defense. Phase 0 proves the concept immediately. Phase 1 puts it in production. Progressive delivery from there. I'm excited about this problem space and I'd love to dig into how Autonomize is solving it in production."

---

## "Don't Elaborate" Topics

| Topic | Brief Redirect |
|---|---|
| FHIR Da Vinci IG | "Clinical informatics discovery work -- beyond this architecture's scope" |
| NIST control IDs | "I design to principles; control ID mapping follows the architecture" |
| SageMaker | "AWS ML training -- this uses Azure AI Foundry Agent Service" |
| EDI X12 segments | "Handled by gateway -- translator-tool territory" |
| KS test / PSI | "LLMOps is behavioral -- overturn rates and eval regression" |
| Snowflake / dbt | "Not in scope -- PA processing is transactional, not analytical" |
| InterQual vs MCG | "Clinical governance decision -- the AI matches whatever the client uses" |
| TriZetto Facets API | "Discovery question -- designed around assumed REST interface" |

---

## Handling "I Don't Know"

**Template**: "That's a great discovery question -- here's what I'd want to find out and why it matters for the architecture."

**Example**: "Do you know the Payer Core API spec?" -- "I don't -- that's the first thing I'd validate. If REST, the synchronous eligibility check works as designed. If SOAP or batch-only, I'd redesign to use a pre-fetched cache. I've built both patterns."
