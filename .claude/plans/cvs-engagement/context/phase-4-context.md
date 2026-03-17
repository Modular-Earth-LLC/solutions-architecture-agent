# Phase 4 Context Summary — Estimation, Team Composition, and Project Plan

> **Completed**: 2026-03-16
> **Status**: complete

## Key Findings

- **$11.7M P50 estimate** (P10: $8.5M, P90: $16.5M) for 18-month engagement — 63% above Kyndryl $7.2M IBMi modernization average, justified by GenAI pipeline + multi-cloud + HIPAA complexity
- **30 peak FTE across 19 roles** including 4 RPG/CL ILE developers ($130/hr with scarcity premium), 3 ML/AI engineers, dedicated change management lead + OCM specialist
- **73,840 total hours** across 4 phases: Foundation (14%), Pilot (21%), Expansion (42%), Completion (23%)
- **Complexity: 9/10 (Very High)** — scored on 10-point checklist; only "evolving requirements" scored 0 because requirements are comprehensive and complete
- **GCP infrastructure: $22,803/month** across 17 services — Cloud Armor Enterprise ($3K/mo) and Apigee X Enterprise (~$8.3K/mo amortized) are the largest line items
- **Three-party tooling: $7,500/month** — Precisely Connect CDC ($5K/mo est.), DEA CSP ($2K/mo est.), Document AI ($500/mo)
- **TCO 3-year: $17.05M** — Year 1 (build): $11.75M, Year 2 (ops): $2.85M, Year 3 (ops): $2.45M
- **ROI: ~$6.5M annual savings** from training reduction (6-8 weeks → <10 days), 40% error reduction, PA automation (days → minutes), reduced RPG/CL dependency
- **39 sprints across 78 weeks** with 4 decision gates at phase boundaries — each with specific, measurable go/no-go criteria
- **Critical path**: Partner Interconnect → IWS API → eligibility migration → claims Dual Run → GenAI pipeline → compliance audits → go-live
- **Change management (ADKAR) embedded in every phase**: Awareness → Desire → Knowledge+Ability → Reinforcement, with 15% of program budget (Gartner recommendation)
- **10 risks identified** with mitigations, owners, triggers, and contingencies — RPG/CL sourcing (R-002) rated critical

## Artifacts Produced

| File | Description |
|------|-------------|
| `knowledge_base/estimate.json` | Three-point estimate with team composition, LOE breakdown, cost model, TCO, ROI, 7 optimization strategies, 14 assumptions |
| `knowledge_base/project_plan.json` | 4-phase roadmap with 39 sprints, 4 decision gates, 10 risks, 12 milestones, critical path, migration-specific section |
| `knowledge_base/reviews.json` | R-006 (estimate, 8.2/10 PASS) and R-007 (project plan, 8.4/10 PASS) |
| `knowledge_base/engagement.json` | Updated: estimate and project_plan status=complete v1.0, review_summary total=7 |

## Decisions Made

- **Three-point methodology (PERT)**: Weighted average across P10/P50/P90 provides defensible range for enterprise budget conversations
- **All-contractor team model**: Assumption A-EST-002 — all engineering staff are contractors; CVS provides clinical SMEs only. Simplifies cost model and reflects typical consulting engagement structure.
- **20% contingency buffer**: Applied to very_high complexity (9/10). Explicitly does NOT cover scope changes — GenAI expansion beyond PA requires re-estimation.
- **Pass 2 accuracy (±50%)**: Appropriate for plan-level estimate with architecture defined but no sprint backlog. Pass 3 (±15%) after sprint planning.
- **$130/hr RPG/CL rate with scarcity premium**: Based on IT Jungle 2024 and Arc.dev benchmarks plus 20-30% scarcity premium for 60-90 day sourcing lead time.
- **Phase 3 is 42% of total effort**: Claims adjudication + formulary + PA + GenAI + security hardening concentrated in months 7-12 at 35 FTE peak. This is the make-or-break phase.
- **4 decision gates, not 3**: Added DG-004 (Go-Live Approval) requiring CTO + Legal sign-off for green screen decommissioning.

## Surprises and Pivots

- **Apigee X pricing opacity**: Enterprise pricing not publicly listed — $100K/yr is a floor estimate from community data. Actual cost could be significantly higher. This is the largest infrastructure cost uncertainty.
- **ROI calculation complexity**: Simple payback period (~24 months) is straightforward, but 3-year ROI depends heavily on methodology (NPV vs simple, total investment vs initial investment). Stated 42% doesn't cleanly derive — flagged in R-006 for clarification.
- **Cloud Healthcare API promotional pricing**: Standard FHIR operations currently free — creates budget uncertainty post-promotion. Budgeted conservatively at $250/mo.
- **Change management is 15% budget, not 10%**: Gartner recommends 15% for change-averse enterprise environments. The 10% Prosci benchmark is an industry minimum. At CVS pharmacy scale (1,000+ users transitioning from green screen), 15% is the floor.

## Assumptions

### New
- A-EST-001 through A-EST-014 documented in estimate.json (see assumptions array)
- Key new: all engineering are contractors (A-EST-002), RPG/CL 60-90 day lead time (A-EST-003), Apigee ~$100K/yr floor (A-EST-005), Precisely ~$5K/mo (A-EST-006)

### Confirmed
- A-0-005 (GCP primary): Confirmed through pricing research — all GCP services HIPAA-eligible with BAA
- A-0-006 (Strangler fig): Confirmed by Kyndryl survey showing 288-362% ROI for incremental modernization vs 70% big-bang failure rate

## Insights for Future Phases

- **Phase 5 (AI Methodology)**: GenAI pipeline costs are well-defined: Gemini 2.5 Pro at $1.25/$10 per 1M tokens, MedGemma self-hosted on Vertex AI for cost-optimized fallback. The tiered inference strategy (40-60% cost savings for routine PA cases) should be highlighted as a key GenAI architecture decision. Include evaluation framework costs (BigQuery for metrics storage, Vertex AI Gen AI Evaluation Service). Team composition shows dedicated ML Lead + 2 ML Engineers + MLOps — this maps directly to the GenAI DS team Paul would manage.
- **Phase 5 (AI Methodology)**: Google published a reference architecture for "Automate utilization-review using generative AI" on Vertex AI — directly validates the PA automation use case and GCP toolchain selection.
- **Phase 6 (Assembly)**: Estimate summary section should include the three-point range ($8.5M-$16.5M) and the Kyndryl benchmark comparison. Project plan section should highlight the 4 decision gates with measurable criteria — these demonstrate pragmatic enterprise delivery. Change management budget at 15% with Prosci 7x multiplier citation is a strong differentiator showing business awareness.
- **Phase 6 (Assembly)**: Feature parity checklist (16 items) from project_plan.json is a concrete artifact the interviewer can evaluate.
- **Phase 7 (Interview Prep)**: For the "how would you estimate this project?" question: lead with three-point methodology, complexity assessment (9/10), and Kyndryl benchmark. For "how would you manage risk over 18 months?": lead with 4 decision gates, each with specific go/no-go criteria and measurable thresholds (≥99.9% parallel validation, P95 ≤500ms, escape hatch <20%). For "what does the team look like?": RPG/CL scarcity story (avg age ~70, 69% of shops cite as #1 concern) demonstrates domain awareness.

## Paul's Feedback

- [Pending — Paul has not yet reviewed Phase 4 outputs]
