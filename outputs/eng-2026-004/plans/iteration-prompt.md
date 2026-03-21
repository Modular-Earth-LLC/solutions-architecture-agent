# Iteration Prompt Template: eng-2026-004

> **Usage**: Fill in the sections below, then paste the entire file as a prompt to Claude Code. The SA agent will apply your feedback and produce an updated version of all affected deliverables.

---

## Prompt

You are iterating on the AI-Driven Prior Authorization solution architecture (eng-2026-004) for my Autonomize AI interview. I've reviewed the current deliverables and have feedback.

**Context files** (read these first):
- `outputs/eng-2026-004/proposal.md` — current 12-slide presentation
- `outputs/eng-2026-004/plans/backlog.md` — autonomous improvement backlog
- `outputs/eng-2026-004/research-context.md` — research findings
- `knowledge_base/architecture.json` — architecture design
- `knowledge_base/security_review.json` — security review
- `knowledge_base/estimate.json` — cost model
- `knowledge_base/project_plan.json` — 12-week roadmap

**Instructions**:
1. Apply all feedback below to the affected deliverables
2. Run `python tests/validate_knowledge_base.py` after each KB file change
3. Re-render any changed Mermaid diagrams with `mmdc`
4. Git commit and push after each logical change
5. After all changes, re-run `/review --depth COMPREHENSIVE` to verify quality
6. Pick up any backlog items from `outputs/eng-2026-004/plans/backlog.md` that align with the feedback direction

---

## Section 1: What I Liked (Keep These)

<!--
List things that are working well. This prevents the AI from changing things
that don't need changing. Be specific — cite slide numbers, component IDs,
or section names.

Examples:
- "The system context diagram (Slide 3-4) layout is clean — keep it"
- "The multi-tenant justification (Slide 12) is convincing"
- "Speaker notes for security (Slides 8-9) hit the right depth"
-->

-
-
-

## Section 2: What Needs to Change (Specific Feedback)

<!--
For each change, use this format:

**Target**: [slide number, file name, or component ID]
**Current**: [what it says/does now]
**Problem**: [why it's wrong or could be better]
**Direction**: [what you want instead — be as specific as possible]

Examples:
- Target: Slide 2, executive summary
  Current: Mentions "3 of top 5 health plans"
  Problem: Vendor-sourced claim, can't verify
  Direction: Lead with Altais case study instead (verified, named customer)

- Target: architecture.json, C-005 FHIR Facade
  Current: Assumes SMART on FHIR for all endpoints
  Problem: Autonomize AI told me they use a different auth model
  Direction: Change to [whatever they told you]
-->

**Change 1:**
- Target:
- Current:
- Problem:
- Direction:

**Change 2:**
- Target:
- Current:
- Problem:
- Direction:

**Change 3:**
- Target:
- Current:
- Problem:
- Direction:

## Section 3: New Information from Interview Prep / Research

<!--
Add anything you learned that should be incorporated. This might come from:
- Conversations with Autonomize AI contacts
- Reading their documentation more carefully
- Your own domain expertise corrections
- New requirements or constraints discovered

Format:
**Topic**: [what you learned]
**Source**: [where this came from]
**Impact**: [which deliverables need updating]
-->

**New info 1:**
- Topic:
- Source:
- Impact:

**New info 2:**
- Topic:
- Source:
- Impact:

## Section 4: Technical Direction Pivots

<!--
Use this for architectural decisions you want to change. The AI will update
all downstream deliverables (architecture → security → estimate → plan → proposal).

Examples:
- "Switch from Kafka to SQS — simpler, and we don't need replay"
- "Change from multi-tenant to multi-instance for regulatory reasons"
- "Add Azure as secondary cloud — Autonomize AI prefers Azure"
- "Remove fax ingestion from Phase 1 — portal-only for MVP"
-->

-
-

## Section 5: Presentation Adjustments

<!--
Specific changes to the slide content, speaker notes, or structure.

Examples:
- "Slide 1: Change title to match Autonomize AI's preferred terminology"
- "Slide 11: Add a sentence about FDA PCCP in the speaker notes"
- "Shorten speaker notes for Slides 5-6 — I'm running long in practice"
- "Add a slide for Q&A topics between Slide 12 and the appendix"
-->

-
-

## Section 6: Backlog Items to Prioritize

<!--
Reference items from backlog.md by number. The AI will execute these
in addition to your feedback above.

Example: "Do backlog items 1, 3, 5, and 10"
-->

Do backlog items:

---

## Pre-filled Suggestions from Claude Code

Based on the review (8.8/10 PASS) and research agent findings, I recommend addressing these in the next iteration:

### Suggested Changes
1. **Add Altais case study to Slide 2** (backlog #3) — strongest verified proof point. Autonomize AI's Altais partnership is independently published by Altais with specific metrics (45% review time reduction).
2. **Correct SageMaker PSI claim** (backlog #2) — minor but important technical accuracy. KS test native, PSI via custom container. Mention Wasserstein Distance as the emerging best practice per Evidently AI benchmark.
3. **Add CAQH Index per-transaction costs** (backlog #4) — $10.97 manual vs $0.05 automated per PA transaction strengthens the ROI math in executive summary.
4. **Generate Q&A prep** (backlog #10) — essential for a 1-hour panel. 15+ questions covering Kafka choice, OCR accuracy, platform outage, prompt injection, multi-tenant justification.
5. **Add FDA PCCP to MLOps slide** (backlog #8) — shows awareness of the regulatory ML lifecycle beyond just monitoring. Demonstrates principal-level thinking.

### Suggested Pivots to Consider
- If Autonomize AI tells you they're Azure-native: consider a hybrid deployment diagram showing Azure ↔ AWS PrivateLink bridge
- If they push back on 12-week timeline: have a ready fallback to portal-only MVP in 8 weeks with fax/EDI in Phase 2
- If they want to discuss auto-denial: explain the Phase 1 exclusion as a deliberate risk mitigation, with Phase 2 activation after clinical validation and legal review

### Technical Confidence Gaps to Probe in Interview
- Ask about Genesis Platform inter-agent authentication (our STRIDE analysis flagged this as a black box)
- Ask about their drift detection approach (does PA Copilot have built-in monitoring, or do we need to build it?)
- Ask about deployment model: SaaS multi-tenant, dedicated tenant in your cloud, or on-prem agent?
