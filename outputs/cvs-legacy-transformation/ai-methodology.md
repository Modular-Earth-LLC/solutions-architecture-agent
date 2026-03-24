# AI-Assisted Methodology

> How this solution architecture was produced — and what it demonstrates about AI-augmented practice

## Human-AI Collaboration Model

This solution architecture document was produced through a structured human-AI collaboration where I directed the engagement and an AI assistant executed research, drafting, and structured analysis under my continuous review.

**My role (human architect)**:
- Defined the engagement scope, phasing, and quality gates
- Made every architecture decision (three-option structure, GCP recommendation, strangler fig pattern, tiered inference)
- Authored the experience honesty map — a transparent self-assessment of where I lead with depth vs. where I rely on research
- Reviewed every artifact at phase gates, directing pivots when outputs didn't meet the standard (e.g., replacing strawman architecture options with three genuinely viable alternatives)
- Owned the narrative voice, ensuring deliverables reflect how I actually think and communicate

**AI role (research and drafting assistant)**:
- Executed web research across 54 sources in Phase 0 alone, organized into 9 thematic clusters
- Generated structured JSON artifacts (requirements, architecture, data model, security review, estimates, project plans) conforming to predefined schemas
- Ran parallel analysis (e.g., 6 STRIDE threat categories analyzed simultaneously, 6 Well-Architected pillars scored in parallel)
- Produced draft prose for review, which I then refined for voice and accuracy
- Performed quality reviews using LLM-as-judge methodology (7 reviews, average 8.2/10, all PASS)

**The model is directive, not generative.** I don't ask AI to "design an architecture." I define the constraints, make the decisions, and use AI to execute research and drafting at a pace that would be impossible solo. The architecture reflects my judgment; the AI amplified my capacity to gather evidence and produce structured artifacts.

## What AI Did Well

**Research synthesis at scale.** Phase 0 produced 54 cited sources across IBM i modernization, GCP services, healthcare compliance, change management, and PBM domain knowledge — organized into 9 research clusters with cross-references. This depth of research, validated against primary sources, would take days of solo work. AI completed it in hours.

**Structured artifact generation.** The engagement produced 8 knowledge base files, each conforming to JSON schemas with cross-references (`$depends_on` declarations). The architecture file alone contains 3 complete option analyses, 12 component specifications, 5 Mermaid diagrams, and Well-Architected scoring across 6 pillars. Schema validation catches structural errors automatically.

**Parallel analysis.** STRIDE threat modeling across 6 categories (30 threats identified, 23 critical, 7 high) and Well-Architected assessment across 6 pillars ran as parallel workstreams. The security review mapped 21 compliance controls across 6 regulatory frameworks (HIPAA, HITECH, PCI-DSS 4.0, DEA 21 CFR 1311, SOC 2, NIST SP 800-207) with specific section citations.

**Quantitative estimation.** Three-point cost estimation (PERT methodology) with 30 team roles, infrastructure cost modeling across 17 GCP services, and TCO projections — all benchmarked against the Kyndryl 2025 survey of 500 IBM i modernization projects. The AI maintained consistency across 73,840 estimated hours without arithmetic drift.

## What Required Human Judgment

**Architecture decisions.** When the initial plan proposed three options (screen transformation, strangler fig, full rewrite), I recognized these included a strawman. I directed the pivot to three genuinely viable cloud-native options (GCP-Native, AWS-Native, Modern Cloud) — each backed by cited vendor reference architectures. AI cannot assess whether an option is genuinely competitive or merely fills a template slot.

**Experience mapping.** The honesty map required honest self-assessment across 8 competency areas. AI can help structure the assessment, but only I know that my IBMi experience is 2/5 (entirely researched) while my GenAI/ML leadership is 4.5/5 (15+ ML projects across 3 healthcare AI roles). This transparency shaped every section's framing.

**Scope pivots.** When research revealed that GCP Dual Run supports z/OS but not IBM i, I directed the fallback strategy (custom shadow traffic via Apigee request mirroring + BigQuery comparison). When the Healthcare NLP API deprecation timeline (May 2026) surfaced, I ensured the GenAI pipeline design used Gemini/MedGemma from the start. These judgment calls require understanding of what matters to the client.

**Voice and tone.** Every section needed to sound like me — collaborative ("I recommend"), empirical (evidence-cited), warm but professional. AI drafts tend toward formal and generic. I adjusted framing throughout: "In my AWS architecture practice, I solved [problem] using [service]. The GCP equivalent is [service]" rather than "the recommended service is [service]."

**Quality gate decisions.** Seven formal reviews scored 7.5-8.4/10 across 5 dimensions (completeness, technical soundness, well-architected alignment, clarity, feasibility). I determined which findings to address immediately vs. defer, and which review feedback to override based on engagement context.

## Quality Assurance Process

The engagement used a multi-gate quality process:

| Phase | Review ID | Score | Verdict | Key Finding |
|-------|-----------|-------|---------|-------------|
| 0 — Requirements | R-001 | 8.3/10 | PASS | RTO/RPO not specified in NFRs (addressed in Phase 2) |
| 2 — Integration Plan | R-002 | 8.3/10 | PASS | Solid integration architecture; Mermaid diagrams accurate |
| 2 — Architecture | R-003 | 8.1/10 | PASS | Three options genuinely viable; WA scoring consistent |
| 2 — Data Model | R-004 | 8.2/10 | PASS | PBM domain ontology well-structured |
| 3 — Security Review | R-005 | 8.2/10 | PASS | STRIDE coverage comprehensive; 8 open findings transparent |
| 4 — Estimate | R-006 | 8.2/10 | PASS | Three-point methodology sound; ROI calculation flagged for clarity |
| 4 — Project Plan | R-007 | 8.4/10 | PASS | Decision gates well-defined; critical path realistic |

**Average: 8.2/10 | All PASS (threshold: 7.5/10) | 0 blockers across 7 reviews**

Each review scored across 5 dimensions and identified specific findings. No review was skipped or overridden. Open findings (like the 8 security gaps requiring implementation before go-live) are documented transparently rather than hidden.

## Why This Matters for CVS

This engagement demonstrates the collaboration model I would bring to the Principal Architect role:

1. **Architect + GenAI team leader.** The GenAI pipeline I designed for this solution (tiered inference with Gemini and MedGemma, confidence-based routing, human-in-the-loop for all PA decisions, OWASP LLM Top 10 alignment) reflects the same AI systems I would lead the GenAI data science team to build. I don't just architect around AI — I understand how to build, evaluate, and govern it.

2. **AI-augmented velocity without quality loss.** This solution architecture — covering 5 key considerations, 3 architecture options, 30 STRIDE threats, $11.7M three-point estimate, and 78-week project plan — was produced with research rigor that 7 formal quality reviews validated. AI amplified my throughput; it didn't replace my judgment.

3. **Responsible AI in practice.** I used AI transparently, with clear human-AI attribution, quality gates at every phase, and honest labeling of what is direct experience vs. research-backed knowledge. This is the standard I would bring to CVS's GenAI initiatives — responsible AI isn't a policy document, it's a practice.

4. **Research-informed decisions.** The AI productivity research that informed this engagement's methodology — including McKinsey's findings on AI-augmented knowledge work, BCG's studies on AI-assisted consulting, and Faros AI's engineering metrics — is the same evidence base I draw from when advising on AI adoption strategy. I practice what I recommend.

## The AI Productivity Evidence Base

This engagement's AI-first approach is grounded in the same research that would inform CVS's AI adoption strategy:

- **BCG x Harvard Business School (2025, *Organization Science*)**: In a study of 758 BCG consultants across 18 realistic tasks, those using AI completed 12.2% more tasks, 25.1% faster, with >40% higher quality — *within AI's capability frontier*. Outside the frontier, consultants using AI were 19% less likely to produce correct solutions. The study identified two usage patterns: "Centaurs" (humans and AI dividing tasks by capability) and "Cyborgs" (fully integrated). This engagement follows the Centaur model — I handle architecture decisions and judgment calls; AI handles research synthesis and structured generation.

- **METR Randomized Controlled Trial (July 2025, arXiv:2507.09089)**: 16 experienced open-source developers across 246 real tasks on their own repositories. Result: AI-assisted developers took **19% longer** to complete tasks — despite predicting a 24% speedup beforehand. The key insight: experienced developers in mature codebases lose time debugging AI hallucinations. In a follow-up (February 2026), METR couldn't maintain a control group because developers **refused to work without AI** — itself a data point on tool dependency. This engagement's directive model avoids the METR trap: I define constraints and review all output rather than accepting AI suggestions uncritically.

- **Faros AI (2025, 10,000+ developers, 1,255 teams)**: Teams with high AI adoption completed 21% more tasks and merged 98% more PRs — but with a 9% increase in bugs per developer, 154% increase in average PR size, and 91% increase in review time. No significant correlation between AI adoption and company-level delivery velocity. The "AI Productivity Paradox": individual output gains are neutralized by downstream bottlenecks. This engagement avoids the paradox by using AI for research and drafting (where gains are real) while keeping architecture decisions and quality review human-owned (where gains are illusory).

- **McKinsey "State of AI" (November 2025)**: 88% of companies use AI regularly in at least one function. But only 39% report EBIT impact at the enterprise level, and less than 5% of total EBIT is attributable to AI in most cases. AI high performers are 3x more likely to be scaling AI agents across business functions. The gap between adoption and impact is a leadership problem, not a technology problem — which is why the GenAI team leader role matters.

The pattern across all four studies is consistent: **AI amplifies human expertise on structured, well-scoped tasks** (research synthesis, drafting, schema generation) **but can actively slow down work when used uncritically** on judgment-heavy tasks (architecture decisions, experience assessment, quality evaluation). This engagement's directive model — human decides, AI executes — is designed around that evidence. It's the same informed AI adoption posture I would bring to CVS's GenAI initiatives.
