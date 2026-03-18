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

All requirements are implemented in the current 9-skill + 2-sub-agent architecture. Requirements traceability derived from progressive discovery workshop sessions (March 2026).

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

**Priya — Enterprise Solutions Architect**: Senior SA at a consulting firm (10-200 person team). Runs complex multi-stakeholder engagements for mid-market to enterprise clients. Uses the **Greenfield** or **Migration** flow at STANDARD/COMPREHENSIVE depth. Needs exemplar-quality deliverables that pass principal engineer review. Spans healthcare (HIPAA), fintech (SOC2/GLBA), and general enterprise.

**Marcus — Independent Consultant**: Solo SA consultant working with startups and SMBs. Wears multiple hats (sales, SA, delivery). Uses the **Streamlined** or **Rapid Assessment** flow at QUICK/STANDARD depth. Needs professional deliverables quickly (hours, not days). Clients often lack technical vocabulary. Works across diverse industries.

**Aisha — Startup Technical Founder**: Technical co-founder (ML engineer background) making architecture decisions for the first time as a business owner. Uses the **Direct Delivery** or **Assessment** flow at QUICK depth. Needs guidance alongside output — plain-language explanations of architectural concepts. Budget-sensitive, building greenfield exclusively.

See CLAUDE.md Canonical Flows table for full flow definitions and sequences.

---

## Decision 7: Depth Tiers (v1.1)

**Problem**: The CVS IBMi case study exposed that a ~10-page interview assignment took 13 hours across 8 phases, producing 5,919 lines of KB JSON that had to be manually condensed to 284 lines. All 9 skills produced maximum-depth output regardless of context.

**Decision**: Add three depth tiers (QUICK/STANDARD/COMPREHENSIVE) to all skills. QUICK mode skips KB file production entirely, writes output directly to the final deliverable, and invokes zero sub-agents.

**Research basis**:
- Constrained output improves quality [arXiv:2407.19825]: shorter output scored higher accuracy (36%→41%).
- Word budgets per section [arXiv:2508.13805, pending verification]: 95% length compliance vs <30% with vague instructions. Verify ID against current arXiv listings.
- Task-complexity routing [IBM Research/NeurIPS 2025, manuscript in submission]: route by complexity — 92% accuracy, 37% cost savings. Replace with published reference when available.

**Use case**: QUICK tier enables 10-30 minute turnaround for interview assignments and prospect qualification — use cases that would otherwise require 2-4 hours of SA preparation time. For Marcus (Independent Consultant) and Aisha (Technical Founder), the QUICK tier is the primary mode, not a fallback.

**Impact**: Eliminates 12-18 parallel sub-agent invocations and 5,000+ lines of KB JSON for QUICK engagements. Target: under 1 hour for equivalent quality to the 13-hour CVS engagement.

## Decision 8: Deliverable-First Mode (v1.1)

**Problem**: Skills optimized for their own KB output, not the final document. The agent treated every task as a full consulting engagement, even when the user needed a single document.

**Decision**: Add deliverable-first dispatch that works backward from the desired output. When a user specifies a target deliverable (format, length, audience), the agent routes to Direct Delivery or Custom Document flow, sets QUICK depth, and uses skeleton-of-thought generation (outline first, expand after approval).

**Research basis**:
- Skeleton-of-thought (ICLR 2024): generate outline first, expand after approval — 2x speed, equal quality
- Progressive disclosure (Anthropic): load only metadata at discovery, task-specific context on demand

**Key insight**: Deliverable-first mode addresses a key failure mode in generalist LLMs: they optimize for completeness over constraints. Without an explicit output anchor, the agent produces exhaustive KB artifacts instead of audience-appropriate documents. By anchoring on format, page count, and audience first, scope is bounded before any analysis begins — producing scoped, usable deliverables rather than maximally complete but unusable ones.

**Impact**: Three new canonical flows (Direct Delivery, Rapid Assessment, Custom Document) for fast turnaround without sacrificing quality.

---

## Decision 9: Blackboard Pattern for Skill Communication (v1.0)

**Problem**: Skills need to share state across a multi-step engagement. Options: direct skill-to-skill calls, conversation history, shared memory, or a structured knowledge store.

**Decision**: Blackboard pattern — skills communicate exclusively through JSON files in `knowledge_base/`. No direct skill-to-skill calls. Each skill owns exactly one KB file and writes only to it.

**Alternatives considered**:
- Direct skill-to-skill calls: Creates coupling — if `/architecture` calls `/requirements` directly, neither can be tested or run independently. Breaks the plugin marketplace distribution model.
- Conversation history: Not persistent across sessions. Cannot be validated by schema. Not diff-able for human review. Violates the "auditable" quality standard.
- Shared in-memory state: Race conditions in parallel sub-agent execution. Not portable across sessions or agents.

**Rationale**: The blackboard pattern supports three critical properties:
1. **Independent skill testing**: Each skill can be unit-tested with a synthetic KB file as input. No orchestration required.
2. **Replay and resume**: Any skill can be re-run mid-engagement without re-running upstream skills. The KB file is the checkpoint.
3. **Human auditability**: Every intermediate state is a JSON file with a schema, a version, and a status field. Humans can review, edit, and approve KB files before the next skill runs.

**`$depends_on` declaration**: Each KB file declares its upstream dependencies. Prerequisite validation is automatic — if `architecture.json` lists `$depends_on: ["requirements.json"]`, the dispatch layer checks `requirements.json` status before invoking `/architecture`.

---

## Known Limitations

**LLM-as-judge circularity**: The `/review` skill uses the same LLM that generated deliverables to evaluate them. This is a known limitation in AI evaluation — the model may be blind to its own systematic biases. Mitigations: (1) the 3-iteration review protocol with adversarial "Tester" persona reduces single-pass blindness, (2) structured scoring rubrics (5 dimensions, 0-10) constrain subjective drift, (3) human review is mandatory before any client-facing deliverable (Guiding Principle 42). Future work: calibrate LLM review scores against human expert assessments to measure correlation and identify systematic gaps.

**Structural tests only**: The automated test suite validates file structure, schema compliance, DAG integrity, and metadata consistency — it does not invoke skills at runtime or validate behavioral output. Runtime validation was performed manually during Phase 7 (healthcare case study) and Phase 9 (sub-agent testing). Future work: parameterized integration tests with synthetic inputs.

**Benchmark research quality**: Model and technology benchmark research depends on WebSearch tool availability. Offline or restricted environments (enterprise proxies, air-gapped systems) cannot perform live benchmarking. Mitigation: pre-load benchmark data in `inputs/` before running `/architecture`. The benchmark fallback guidance in `/architecture` SKILL.md covers this case.

**QUICK depth skips prerequisite checks**: QUICK depth deliberately skips all upstream KB validation. This is a speed-over-auditability trade-off by design — for interview assignments, prospect qualification, and rapid turnaround scenarios, requiring KB files would eliminate the use case entirely. Consequence: QUICK output cannot be upgraded to STANDARD output without re-running upstream skills. Use QUICK only for non-client-facing deliverables or initial qualification.

---

## Product Backlog

Intentional scope deferrals for future versions — disciplined scope management, not unresolved design issues:

1. **Discovery tier thresholds**: Quick tier duration — 15 min (from Phase 1 patterns) vs 30 min (from plan). Should we standardize to Quick (15-30 min), Standard (45-60 min), Comprehensive (90 min)?

2. **Test scenario fidelity**: Test scenarios are derived from real engagements but use synthetic inputs. Should we create standardized synthetic inputs, or attempt to anonymize real engagement data?

3. **Proposal type coverage**: 4 proposal types defined (discovery, implementation, internal, pitch). Are additional types needed (e.g., renewal, expansion, assessment-only)?

4. **Sprint methodology rigidity**: The consulting delivery model mandates 2-week sprints. Should `/project-plan` support alternative sprint durations (1-week, 3-week) for different client contexts?

5. **Estimation currency**: Currently hardcoded to USD. Should `/estimate` support multi-currency output?

6. **system_config.json cleanup**: The `self_improvement_framework` and `validation_framework` sections reference defunct multi-agent architecture (`optimization_agent`, `prompt_engineering_agent`). These sections are harmless but confusing. Clean up when the READ-ONLY constraint on `system_config.json` is revisited (requires schema update and re-validation).
