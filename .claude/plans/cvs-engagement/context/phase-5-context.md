# Phase 5 Context Summary — AI Methodology and Portfolio Documentation

> **Completed**: 2026-03-16
> **Status**: complete

## Key Findings

- **METR RCT (July 2025, arXiv:2507.09089)**: 16 experienced devs, 246 real tasks — AI users were 19% slower. Follow-up (Feb 2026): devs refused to work without AI, collapsing the control group. Strengthens the directive model — AI works when humans direct, not when they blindly accept.
- **BCG x Harvard (2025, Organization Science)**: 758 BCG consultants — 12.2% more tasks, 25.1% faster, >40% higher quality within AI's capability frontier. Outside frontier: 19% less likely correct. "Centaur" (divide by capability) > "Cyborg" (fully integrated). This engagement follows Centaur model.
- **Faros AI (2025, 10K+ devs, 1,255 teams)**: 21% more tasks completed, 98% more PRs merged — but 9% more bugs, 154% larger PRs, 91% longer reviews. No correlation to company-level velocity. The "AI Productivity Paradox" — individual gains neutralized by downstream bottlenecks.
- **McKinsey State of AI (Nov 2025)**: 88% adoption, but only 39% report EBIT impact. <5% of EBIT attributable to AI. High performers 3x more likely to scale AI agents.
- **LLM citation standards still emerging**: IEEE requires Acknowledgments disclosure; ACM prohibits AI authorship; ISO/IEC 42001 requires transparency documentation; NIST AI RMF requires model provenance. No Big 4/MBB firm uses standardized in-document AI citation. This framework goes further with per-section attribution.
- **The engagement itself is the strongest AI methodology evidence**: 7 reviews averaging 8.2/10, 54 sources in Phase 0, 30 STRIDE threats, $11.7M three-point estimate — all produced through directive human-AI collaboration with measurable quality outcomes.
- **LLM citation standards are still emerging**: No single industry standard exists for AI attribution in professional deliverables. The citation framework produced (4-tier attribution: human-authored, human-directed, human-decided, human-directed/AI-generated) provides a practical model.

## Artifacts Produced

| File | Description |
|------|-------------|
| `outputs/cvs-legacy-transformation/ai-methodology.md` | AI-assisted methodology section: collaboration model, what AI did well vs. what required human judgment, quality assurance process, CVS relevance, productivity evidence base |
| `outputs/cvs-legacy-transformation/llm-citations.md` | LLM citation framework: tools used, per-section human vs. AI attribution table, disclosure statement, document footer language |
| `outputs/cvs-legacy-transformation/portfolio-narrative.md` | Portfolio narrative: guiding principles in action, dual competency demonstration (architect + GenAI leader), key differentiators, experience evidence map with career-data.json verification |

## Decisions Made

- **Directive, not generative model**: Framed the human-AI collaboration as "I define constraints, make decisions, AI executes research and drafting" — not "AI designs, human reviews." This framing is both accurate to how the engagement worked and positions Paul as a leader of AI workflows, not a consumer of AI output.
- **4-tier attribution model**: Human-authored (minimal AI), Human-directed/AI-drafted, Human-decided/AI-researched, Human-directed/AI-generated. Each section of the final document maps to one tier. No section is "AI-generated without human review."
- **METR nuance as a strength**: Rather than hiding the METR finding (19% slower), incorporated it as evidence that Paul understands AI productivity research deeply enough to design around its limitations. The directive model explicitly avoids the "METR trap."
- **Experience evidence map**: Every claim in the portfolio narrative maps to a verifiable source (career-data.json or honesty-map.md). Included a table with 15 claims, each with evidence and source citation. Explicitly notes zero GCP and zero IBMi hands-on experience.
- **Guiding principles as narrative thread**: Selected 6 of 42 guiding principles to demonstrate in the portfolio narrative, each with concrete examples from the engagement. This connects Paul's philosophy to his practice.

## Surprises and Pivots

- **METR finding required rewrite**: Initial draft characterized METR as showing "measurable gains." The actual finding (19% slower for experienced developers) required a nuanced rewrite that turned a potential negative into a sophisticated understanding of AI limitations — which strengthens the methodology argument.
- **No new research needed for productivity section**: Phase 4 already researched McKinsey, BCG, METR, and Faros AI during the estimate revision. The AI methodology section drew directly from that prior work, as the plan anticipated.

## Assumptions

### Confirmed
- The engagement data (7 reviews, 54 sources, 30 threats, etc.) is sufficient evidence for the methodology section — no new research gaps identified

### New
- A-5-001: CVS hiring panel will view AI-assisted methodology as a strength (demonstrates GenAI leadership), not a weakness (suggests the work isn't "original")
- A-5-002: The 4-tier attribution model is sufficiently transparent for enterprise professional standards

## Insights for Future Phases

- **Phase 6 (Assembly)**: Three Phase 5 documents are ready for embedding: ai-methodology.md → Section 9, llm-citations.md → Appendix D, portfolio-narrative.md → Appendix E. The ai-methodology section should be concise in the main document (1-2 pages) with full detail in the appendix. The portfolio narrative's experience evidence map can serve as the "About the Author" section.
- **Phase 6 (Assembly)**: The METR nuance (19% slower finding) should appear in the methodology section — it demonstrates sophisticated understanding of AI productivity, not just cheerleading. Frame: "I designed my AI workflow around this evidence."
- **Phase 6 (Assembly)**: The dual competency thread is strongest in the portfolio narrative's "Integration Point" section — the three "why" questions (tiered inference, VPC-SC isolation, HITL) each demonstrate architect + AI leader thinking simultaneously. Consider surfacing this in the executive summary.
- **Phase 7 (Interview Prep)**: AI methodology is a likely interview topic. Prepare Paul to discuss: directive vs. generative model, METR findings and their implications, quality assurance process (7 reviews, 8.2/10 avg), and the specific human judgments that shaped the architecture (option pivot, Dual Run fallback, Healthcare NLP deprecation response).
- **Phase 7 (Interview Prep)**: The experience evidence map provides pre-verified talking points — every claim has a source. Paul can confidently cite any row in the table during interviews.
- **Phase 7 (Interview Prep)**: Prepare for the curveball: "Did AI write this document?" Answer: "I used AI as a research and drafting assistant, documented the methodology transparently, and I'm prepared to discuss every technical decision in depth. The methodology section shows exactly what AI did and what I did."

## Paul's Feedback

- [Pending — Paul has not yet reviewed Phase 5 outputs]
