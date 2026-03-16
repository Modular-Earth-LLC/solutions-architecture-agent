# Design Rationale

Historical context and design decisions behind the AI Solutions Architecture Agent. Extracted from the Phase 1-2 requirements analysis (March 2026) to preserve unique content not captured in CLAUDE.md or ARCHITECTURE.md.

---

## Research Citations

Architectural decisions are grounded in the following research:

| Topic | Finding | Source |
|-------|---------|--------|
| Single-agent vs multi-agent | 180 experiments: multi-agent degrades sequential reasoning 39-70%. Single-agent achieves 67.7 successful tasks per 1K tokens vs 21.5 for centralized multi-agent. Threshold: if single agent solves >45% correctly, multi-agent rarely helps. | [Google/MIT arXiv:2512.08296](https://arxiv.org/abs/2512.08296) |
| Agent Skills standard | Released December 18, 2025. 32 platforms adopted as of March 2026. | [agentskills.io](https://agentskills.io), [Anthropic engineering blog](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) |
| AWS Well-Architected | 6 pillars + 3 AI lenses (Responsible AI, ML, GenAI — all updated at re:Invent 2025). GenAI Lens includes agentic AI patterns. | [AWS docs](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/agentic-ai.html) |
| Azure Well-Architected | 5 pillars + dedicated AI workload section with maturity models. | [Microsoft Learn](https://learn.microsoft.com/en-us/azure/well-architected/ai/) |
| GCP Well-Architected | 5 pillars + AI/ML cross-pillar perspective. | [Google Cloud docs](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) |
| Competitive landscape | No widely adopted tool covers the full SA lifecycle (ideation through project plan). Market is fragmented across diagramming, IaC generation, compliance, and coding tools. | Phase 1 analysis |

---

## Requirements Traceability Summary

The agent was designed against **141 traceable requirements** extracted from 88 source patterns found in real SA deliverables:

| Category | Count | Scope |
|----------|-------|-------|
| Functional (FR) | 106 | 9 skills: REQ(15), ARC(18), EST(8), PPL(9), PRO(8), DM(11), SR(12), IP(13), RV(12) |
| Non-Functional (NFR) | 22 | Context efficiency, portability, quality, usability, security, extensibility |
| Cross-Cutting (CCR) | 13 | KB blackboard, dispatch, lifecycle flows, human checkpoints, tech-agnostic, WA compliance |

**Pattern coverage**: 88/88 source patterns traced to requirements (100%).

All requirements are implemented in the current 9-skill + 2-sub-agent architecture. See `archive/requirements.md` for the full traceability matrix (Section 9).

---

## Pre-Sales Lifecycle Mapping

The 21-step consulting pre-sales lifecycle maps to agent skills:

| Phase | Steps | Owner | Agent Skills |
|-------|-------|-------|-------------|
| Lead Generation | 1. Identify leads | Human (Sales) | -- |
| Lead Qualification | 2-3. Prospect research, BANT | Human + Agent | `/requirements` |
| Discovery | 4-7. Interviews, objectives, requirements, market analysis | Human (SA) + Agent | `/requirements`, `/data-model` |
| Solution Design | 8-12. Architecture, data model, security, integration, review | Human (SA) + Agent | `/architecture`, `/data-model`, `/security-review`, `/integration-plan`, `/review` |
| Estimation | 13-14. T-shirt sizing, detailed estimation | Human (SA) + Agent | `/estimate` |
| Project Planning | 15-16. Roadmap, sprint/release planning | Human (SA) + Agent | `/project-plan` |
| Proposal Assembly | 17-18. SOW drafting, pricing | Human (SA) + Agent | `/proposal`, `/estimate` |
| Negotiation | 19. SOW review | Human (Owner + Client) | `/proposal` |
| Execution | 20. SOW signing | Human only | -- |
| Kickoff | 21. Sprint planning | Human (Team) + Agent | `/project-plan`, `/requirements` |

---

## Sales Principles Governing Agent Behavior

14 principles from consulting sales methodology, embedded in skill behaviors:

| # | Principle | How It Manifests |
|---|-----------|-----------------|
| 1 | Treat clients like business partners | Frame all outputs as partnership artifacts; collaborative tone |
| 2 | Sell solutions, not hours | Tie every recommendation to business value and ROI |
| 3 | Practice active listening | `/requirements` must capture and reflect back before recommending |
| 4 | Find and build emotional connections | Acknowledge human impact in architecture decisions |
| 5 | We do not waste anyone's time | Every output delivers tangible value; no filler or boilerplate |
| 6 | Follow the data; leave nothing to guesswork | Evidence-based estimation; cite sources and benchmarks |
| 7 | Eliminate surprises | Surface risks, assumptions, unknowns early and explicitly |
| 8 | Highlight losses rather than gains | Lead with what client risks losing by not acting |
| 9 | Add long-term considerations | Address sustainability and TCO, not just MVP |
| 10 | Messages are highly personalized | All outputs tailored to specific client context |
| 11 | Shoot for the stars | Reflect full solution value; don't undersell |
| 12 | Avoid enshittification | Recommend open, non-lock-in architectures |
| 13 | Human always in the loop | Human review mandatory before client-facing deliverables |
| 14 | Sales is a team sport; handoff smoothly | Maintain state across full pre-sales lifecycle via KB persistence |

---

## Personas

Three personas drive skill design and user story coverage:

**Priya — Enterprise Solutions Architect**: Senior SA at a consulting firm (10-200 person team). Runs complex multi-stakeholder engagements for mid-market to enterprise clients. Uses the full lifecycle flow. Needs exemplar-quality deliverables that pass principal engineer review. Spans healthcare (HIPAA), fintech (SOC2/GLBA), and general enterprise.

**Marcus — Independent Consultant**: Solo SA consultant working with startups and SMBs. Wears multiple hats (sales, SA, delivery). Uses the streamlined flow. Needs professional deliverables quickly (hours, not days). Clients often lack technical vocabulary. Works across diverse industries.

**Aisha — Startup Technical Founder**: Technical co-founder (ML engineer background) making architecture decisions for the first time as a business owner. Uses focused flows. Needs guidance alongside output — plain-language explanations of architectural concepts. Budget-sensitive, building greenfield exclusively.

---

## Known Limitations

**LLM-as-judge circularity**: The `/review` skill uses the same LLM that generated deliverables to evaluate them. This is a known limitation in AI evaluation — the model may be blind to its own systematic biases. Mitigations: (1) the 3-iteration review protocol with adversarial "Tester" persona reduces single-pass blindness, (2) structured scoring rubrics (5 dimensions, 0-10) constrain subjective drift, (3) human review is mandatory before any client-facing deliverable (Guiding Principle 42). Future work: calibrate LLM review scores against human expert assessments to measure correlation and identify systematic gaps.

**Structural tests only**: The automated test suite validates file structure, schema compliance, DAG integrity, and metadata consistency — it does not invoke skills at runtime or validate behavioral output. Runtime validation was performed manually during Phase 7 (healthcare case study) and Phase 9 (sub-agent testing). Future work: parameterized integration tests with synthetic inputs.

---

## Open Questions

Unresolved product evolution questions from the original requirements analysis:

1. **Discovery tier thresholds**: Quick tier duration — 15 min (from Phase 1 patterns) vs 30 min (from plan). Should we standardize to Quick (15-30 min), Standard (45-60 min), Comprehensive (90 min)?

2. **Test scenario fidelity**: Test scenarios are derived from real engagements but use synthetic inputs. Should we create standardized synthetic inputs, or attempt to anonymize real engagement data?

3. **Proposal type coverage**: 4 proposal types defined (discovery, implementation, internal, pitch). Are additional types needed (e.g., renewal, expansion, assessment-only)?

4. **Sprint methodology rigidity**: The consulting delivery model mandates 2-week sprints. Should `/project-plan` support alternative sprint durations (1-week, 3-week) for different client contexts?

5. **Estimation currency**: Currently hardcoded to USD. Should `/estimate` support multi-currency output?
