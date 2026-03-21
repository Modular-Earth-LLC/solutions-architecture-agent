# eng-2026-004: Backlog for Claude Code Plan Mode

> **Usage**: Paste this file as context when running `/plan` in Claude Code to iterate on the solution architecture. Claude Code should pick up items by priority and execute autonomously.

## Instructions for Claude Code

You are iterating on the AI-Driven Prior Authorization solution architecture (eng-2026-004). The following items are autonomous improvements you can make without human approval. Work through them in priority order. After each item, run `python tests/validate_knowledge_base.py`, commit, and push.

Reference files:
- `outputs/eng-2026-004/proposal.md` — 12-slide presentation (primary deliverable)
- `knowledge_base/architecture.json` — architecture design
- `knowledge_base/security_review.json` — STRIDE threat model
- `knowledge_base/estimate.json` — cost model
- `knowledge_base/project_plan.json` — 12-week roadmap
- `outputs/eng-2026-004/research-context.md` — all research findings

---

## P0 — Fix Before Next Review

| # | Task | What to Do | Files to Modify |
|---|------|-----------|----------------|
| 1 | **Re-run WA reviewers against current architecture.json** | Launch 6 parallel `solutions-architecture-agent:parallel-wa-reviewer` agents. Update `architecture.json` `well_architected_scores` with agent-returned scores. Replace `score_source` with `"parallel-wa-reviewer sub-agents"`. | `architecture.json` |
| 2 | **Correct SageMaker PSI claim** | KS test is natively supported. PSI requires a custom monitoring container. Update `architecture.json` observability.metrics.ai_specific to clarify. Update proposal.md slide 11 speaker notes and drift detection table to say "PSI via custom SageMaker container". | `architecture.json`, `proposal.md` |
| 3 | **Add Altais case study to proposal executive summary** | Altais Health Solutions: 10K+ physicians, 500K patients, 45% PA review time reduction, 54% error reduction, 50% auto-approval. This is the strongest verified Autonomize AI reference. Add to Slide 2 as a proof point alongside "3 of top 5 health plans". | `proposal.md` |
| 4 | **Add CAQH Index cost benchmarks to executive summary** | Manual PA: $10.97-$12.88/transaction (provider), $3.14-$3.52 (payer). Automated: ~$0.05 (payer). Source: CAQH Index 2024. Add per-transaction savings math to Slide 2. | `proposal.md` |

## P1 — Strengthen Architecture

| # | Task | What to Do | Files to Modify |
|---|------|-----------|----------------|
| 5 | **Add external audit trail anchoring** | STRIDE Tampering T-004 recommends AWS QLDB or RFC 3161 timestamping for tamper-proof external verification of DynamoDB hash chain. Add to `architecture.json` component C-011, `security_review.json` defense_in_depth layer 5, and proposal Slide 8-9. | `architecture.json`, `security_review.json`, `proposal.md` |
| 6 | **Evaluate per-LOB Kafka topics vs partitions** | STRIDE Info Disclosure T-004 recommends topic-level isolation (`pa-requests-commercial`) over partition-level. Document trade-off in `architecture.json` `alternatives_considered`. If topic-level is chosen, update C-004, data flows, and multi-tenant diagram. | `architecture.json`, `proposal.md` |
| 7 | **Add Snowflake Dynamic Data Masking** | Analytics pipeline replicates PHI before dbt masking. Add Snowflake DDM policies as first-stage transform in `architecture.json` C-014 and `security_review.json` defense_in_depth layer 4. | `architecture.json`, `security_review.json` |
| 8 | **Add FDA PCCP framework to MLOps architecture** | FDA Predetermined Change Control Plan (PCCP, Aug 2025) enables AI model updates post-clearance. Add to `architecture.json` ai_ml_components and proposal Slide 11 speaker notes as regulatory awareness. | `architecture.json`, `proposal.md` |
| 9 | **Add Wasserstein Distance to drift detection** | Evidently AI benchmark recommends WD as best compromise for large datasets. Add as third metric alongside PSI and KS in `architecture.json` and proposal Slide 11. | `architecture.json`, `proposal.md` |

## P2 — Enrich Deliverables

| # | Task | What to Do | Files to Modify |
|---|------|-----------|----------------|
| 10 | **Generate Q&A prep document** | Create `outputs/eng-2026-004/plans/qa-prep.md` with 15+ anticipated panel questions and detailed answers. Must cover: "Why Kafka?", "Why not SQS?", "Fax OCR for handwritten?", "Autonomize AI goes down?", "Prompt injection?", "Why multi-tenant?", "How does FHIR facade work?", "What if clinical accuracy < 95%?", "CMS-0057-F readiness?", "How do you handle auto-denial?" | New file: `qa-prep.md` |
| 11 | **Add state-level PA regulation awareness** | 18+ states enacted PA reforms in 2025. Indiana: 24-hour urgent (stricter than federal 72hr). Texas/Arkansas gold carding. Add brief mention to proposal Slide 8-9 speaker notes. | `proposal.md` |
| 12 | **Re-render diagrams to PNG** | Run `mmdc` with `-o .png` in addition to SVG for PowerPoint compatibility. Use `-b white` for clean backgrounds. | New files in `diagrams/` |

## P3 — Future (Post-Interview)

| # | Task | What to Do | Files to Modify |
|---|------|-----------|----------------|
| 13 | **Build the demo** | Use `outputs/eng-2026-004/plans/implementation-prompt.md` in Claude Code plan mode. 12-16 hour build target. | New project |
| 14 | **Add CCPA rights management design** | Phase 2 scope. Design deletion and opt-out workflows. Ensure Phase 1 data tagging supports future compliance. | `security_review.json` |
