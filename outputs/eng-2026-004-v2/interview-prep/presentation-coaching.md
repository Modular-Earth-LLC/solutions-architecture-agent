# Presentation Coaching — Time Management & Pivot Guides
## AI-Driven Prior Authorization | Autonomize AI Interview
### Paul Prae | Principal AI Engineer & Architect

> **Read this the morning of the interview.** The goal is not to deliver a perfect rehearsed presentation. The goal is to have a sharp, confident conversation where you control the narrative.

---

## The Mindset Going In

This is not a lecture. It is a technical conversation where you happen to have prepared materials. The panel is evaluating whether they want to work with you, not just whether you can present slides. Let the slides serve the conversation — don't serve the slides.

**You are the expert in the room on this architecture.** You built it. You know every trade-off. Kris doesn't know the Altais metrics as well as you do. Suresh doesn't know this specific system's integration points as well as you do. Ujjwal hasn't seen this trade-off table. Lead with confidence.

---

## Priority Tier Navigation Map

```
TIME REMAINING → ACTION
───────────────────────────────────────────────────────
30+ min remaining   →  Tier A (slides 1-6) at full pace
                       15 min target, then invite questions
                       If conversation takes over — let it

15-20 min remaining →  Tier A only
                       Skip slide 4 component detail if
                       already explained verbally
                       Go straight to Slide 6 (Security)

10-15 min remaining →  Slides 1-3 + 5 only
                       Context, business case, flow
                       "I'll skip the component detail —
                       happy to go deeper on anything"

Under 10 min        →  Opening thesis only (memorized)
                       Offer to take questions
                       "I have the full deck if you want
                        to drill into any area"

Tier B (slides 7-9) →  Present only if explicitly asked
                       OR if 10+ min remain after Tier A
                       AND the conversation is going deep

Tier C (10-11)      →  Appendix / on-demand only
                       Never present proactively
                       "I have a trade-off table in the
                        appendix — want to walk through it?"
```

---

## 60-Second Opening Thesis — Memorize This

*Deliver this at the start, before advancing past the title slide. Slow down. Make eye contact. Don't rush.*

---

"I'm Paul Prae. I've spent 15 years building AI systems in healthcare — most recently at Arine, where our platform served 50 million members across 45 health plans, and before that as an ML Solutions Architect at AWS.

I designed this architecture to answer a specific question: how does a large US health plan integrate Autonomize AI's PA Copilot safely and effectively into its existing IT environment?

The answer is a 10-component Azure-native system that automates PA intake, clinical review, and determination — with human oversight built in at every exception case. Based on Altais's February 2026 results: 45% faster reviews, 54% fewer errors, 50% auto-determination rate.

I'll take you through the architecture in tiers — executive context, then technical depth, then implementation path. Stop me anywhere."

---

*That last sentence — "Stop me anywhere" — is the most important. It signals conversational format and invites the panel to redirect you.*

---

## 30-Second Closing Summary — Land This No Matter What

*Use this if you're running out of time, if the conversation has been deep and fractured, or as a deliberate closing move.*

---

"Let me land on the core of what I've designed: a system where Autonomize's PA Copilot integrates safely into the health plan's ecosystem — reliable intake from fax, portal, and EDI; AI-driven clinical review with human oversight for exceptions; full audit trail for regulatory defense. Phase 0 proves the concept immediately. Phase 1 puts it in production on a single LOB. Progressive delivery from there. I'm excited about this problem space and I'd love to dig into how Autonomize is solving it in production."

---

## Conversation Pivot Phrases

Use these when you need to redirect, bridge, or recover control.

### When you want to anchor on the slide:
- "Let me point you to slide [N] — I've captured that trade-off there."
- "That's the integration detail on slide 7 — want me to walk through it?"
- "I have a table for that in the appendix — gives you the full comparison."

### When you want to buy time or think:
- "Great question — let me think about which piece of that is most relevant to your context."
- "There are two ways to look at that — from an architecture standpoint, and from an operational standpoint. Which is more useful?"
- "I want to make sure I answer the right part of that — are you asking about [A] or [B]?"

### When you're redirecting from a gap:
- "That's exactly the kind of detail I'd want to discover in a real engagement. Here's what I'd ask and why it matters..."
- "I've designed around an assumption there — [state assumption]. If the real answer is different, [explain how architecture adjusts]."
- "My depth there is [honest level]. Here's how I'd handle it in practice: [pattern description]."

### When you want to bring it back to business value:
- "The technical answer is [X], but the business reason for it is [Y] — which matters more to you?"
- "That design choice comes back to the Kris question — ROI and risk. Here's the trade-off..."
- "The Altais result is the evidence that this approach works. The architecture I've built delivers the same pattern."

### When you want to invite the panel to drive:
- "I could go deeper on any of these components — what's most relevant to your current challenges?"
- "Where would you like to spend time? I'm equally comfortable going deep on integration details or stepping back to business case."
- "Is there a specific piece you'd push back on? I'd rather address skepticism directly."

---

## "Don't Elaborate" Topic List

These topics should get a brief, honest answer and move on. Elaborating creates exposure for topics where your depth is bounded.

| Topic | Brief Redirect | Reasoning |
|---|---|---|
| FHIR Da Vinci IG internals | "Da Vinci IG implementation is clinical informatics discovery work — beyond this architecture's scope" | You know FHIR as a label, not the IG spec |
| Specific NIST control IDs | "I design to NIST CSF principles; control ID mapping is compliance documentation that follows the architecture" | You don't have NIST IDs memorized |
| SageMaker specifics | "SageMaker is AWS's ML training service — this architecture uses Azure AI Foundry Agent Service for the agent runtime" | AWS-only knowledge; redirect to what's in scope |
| EDI X12 segment-level details | "EDI translation is handled by the gateway — ISA/GS loop specifics are translator-tool territory" | Acknowledge the pattern, not the field-level detail |
| KS test / PSI statistics | "LLMOps monitoring here is behavioral — overturn rates and eval regression — not distributional statistics" | Honest depth boundary; redirect to what you know |
| Snowflake / dbt patterns | "Data warehouse integration isn't in scope — PA processing is transactional, not analytical" | This architecture doesn't use those tools |
| Specific InterQual/MCG criteria differences | "Coverage criteria selection is a clinical governance decision — the AI matches against whatever the client uses" | Not your domain |
| Specific TriZetto Facets API fields | "Payer Core API specifics are a discovery question — I've designed around an assumed REST interface" | Assumption, not knowledge |

---

## Time Awareness Tips

### The 3-Minute Rule
If you have been on one slide for more than 3 minutes without a question, you are presenting a lecture, not having a conversation. Stop. Ask: "Is this the right level of detail, or should I move on?"

### The Silence Signal
If the panel is quiet, it does not mean they are engaged. It may mean they are waiting for you to finish so they can ask their real question. Pause and invite: "Any questions on this before I move on?"

### Tier Navigation in Real Time
Watch the clock actively:
- If you finish Tier A in 10 minutes instead of 15, that's excellent — more time for Q&A.
- If you're still on slide 3 at the 15-minute mark, skip slides 4 and 5, go directly to slide 6, and say "I'm going to move to security given our time — I can come back to the component detail if useful."

### The Best Outcome
The best interview outcome is the panel spending 20 of 30 minutes asking you questions rather than watching you present. That means the presentation resonated. Don't be attached to covering all the slides.

---

## Handling "I Don't Know"

This phrase, used correctly, is a strength signal at Principal Architect level. Use the full version:

**Template**: "That's a great discovery question — here's what I'd want to find out and why it matters for the architecture: [brief, specific statement]. In practice, I'd [describe how you'd investigate]. That answer changes [specific design decision]."

**Examples:**

*"Do you know the Payer Core API spec?"*
"I don't — that's the first thing I'd validate in a real engagement. If it's REST, the synchronous eligibility check works as designed. If it's SOAP or batch-only, I'd redesign the eligibility step to use a pre-fetched cache. I've built both patterns — the architecture supports either."

*"What's the standard HITRUST control set for this?"*
"I design to the HITRUST framework principles — access control, encryption, audit logging, business continuity — but I don't have the specific CSF control numbers memorized. I'd work with a compliance team to do that mapping as a project deliverable. The architecture covers the required controls; the documentation is the artifact we'd produce together."

*"How would you implement the X12 278 parser?"*
"I'd use a commercial EDI translator — Edifecs, Optum Clearing House, or a similar service — rather than building raw X12 parsing. The architecture shows EDI as an intake channel; the translation to canonical format is a commodity integration, not custom engineering. My depth on X12 segment specifics is limited, but the integration pattern is well-understood."

---

## The Autonomize-Specific Questions to Prepare For

These are questions only Autonomize insiders would ask. Have brief frames ready.

**"How does the Genesis Platform handle multi-tenancy?"**
"My understanding from Autonomize's documentation is that Genesis supports per-customer and per-LOB configuration isolation. The specific implementation — whether it's schema-per-tenant or row-level — is something I'd want to confirm with your platform team in discovery. The architecture is designed to use whatever isolation model Genesis provides."

**"What's your experience with the Agents Marketplace?"**
"I've reviewed the Agents Marketplace documentation — it's the right model for adding new AI capabilities (appeals, clinical documentation improvement) without re-architecting. I haven't deployed agents from the Marketplace in production. The integration pattern — agent as a skill invoked from the PA Copilot — is clear from the documentation."

**"How does PA Copilot handle coverage criteria updates?"**
"That's one of my discovery questions — how does Genesis manage coverage criteria versioning, and what's the update workflow? My LLMOps pipeline design assumes there's a knowledge base update process, but the specifics depend on how PA Copilot stores and versions criteria. I'd want to walk through that with your platform team in week one."

---

## Final Reminders

**Before walking in:**
- Reread the 60-second opening thesis. Say it out loud once.
- Know slides 1-6 cold. Slides 7-9 at talking-point level. Slides 10-11 by title only.
- Have the assumptions file mentally available — you know the five early-stage discovery questions.

**During the presentation:**
- Slow down when you're confident. Speed is nervous energy.
- "Stop me anywhere" signals confidence and conversational mode.
- Every question is a chance to show depth — welcome them.

**If it goes sideways:**
- The closing summary works from anywhere in the conversation. Use it to land.
- An honest "I don't know, here's how I'd find out" beats a wrong confident answer every time.
- Your 15 years in healthcare AI and your understanding of the PA problem space are real. The slides are just scaffolding.
