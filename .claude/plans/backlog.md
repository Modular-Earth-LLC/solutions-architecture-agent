# SA Agent — Product Backlog

> Improvements to the Solutions Architecture Agent itself, informed by real engagement experience.
> Items are prioritized by impact on engagement quality and agent reliability.
> Updated: 2026-03-24 | Last engagement: eng-2026-004-v2 (Autonomize AI)

---

## P0 — High Impact, Learned from eng-2026-004

| # | Area | Improvement | Context |
|---|------|-------------|---------|
| 1 | **Engagement lifecycle** | Add `complete` and `archived` status transitions with cleanup actions | eng-2026-004 left `engagement.json` as `in_progress` after all skills finished. No built-in way to close an engagement, archive plans, or restore `.gitignore` defaults. Had to do manual cleanup. |
| 2 | **Iterative versioning** | Support v1→v2 iteration within a single engagement directory | eng-2026-004 required a separate `eng-2026-004-v2/` directory because there was no versioning within outputs/. Should support `outputs/eng-2026-004/v1/`, `v2/` etc., or KB-level version branches. The v1 backlog (14 items) directly informed v2 priorities — that feedback loop worked but was manual. |
| 3 | **Output export/packaging** | Add a `/package` or `/export` skill that copies deliverables to a target repo with path transforms | Migrating 35 files from `outputs/eng-2026-004-v2/` to `autonomize-healthcare-ai-demo/docs/` required a custom 7-phase ETL plan with 15+ path rewrites. This should be a repeatable skill. |
| 4 | **Autonomous execution protocol** | Formalize the overnight autonomous run pattern as a canonical flow | The eng-2026-004-v2 execution protocol (`eng-2026-004-v2-sa-iteration.md`) worked well: 9 phases, parallel agents, human checkpoints, session context saves. But it was hand-written. Should be a template or flow type. |
| 5 | **Session context persistence** | Standardize the session-context.md pattern as a first-class feature | `eng-2026-004-session-context.md` captured engagement state for resumption across sessions. This pattern worked but wasn't formalized — each engagement reinvents it. |

## P1 — Architecture & Quality

| # | Area | Improvement | Context |
|---|------|-------------|---------|
| 6 | **Git hygiene automation** | Add pre-engagement and post-engagement git workflows | Post-engagement: restore `.gitignore`, archive plans, untrack engagement artifacts. Pre-engagement: validate clean state, create engagement directory, initialize KB files. Currently manual. |
| 7 | **Output directory structure** | Define a standard `outputs/<engagement>/` structure that all skills write to | eng-2026-004-v2 had a good final structure (presentation, diagrams, interview-prep, inputs, plans, slide-generation-prompts) but it emerged organically. The `/proposal` skill should produce a structured output directory, not a flat pile of files. |
| 8 | **Diagram rendering pipeline** | Integrate mmdc rendering into the architecture skill | Mermaid → SVG → PNG rendering required manual steps. The `/architecture` skill should produce `.mmd` sources and the agent should render them automatically using mmdc if available. The mermaid-diagrams.md rules are good but enforcement isn't automated. |
| 9 | **Cross-reference integrity** | Validate internal links across output files | When files are renamed or reorganized (e.g., `solution-architecture-source-of-truth.md` → `solution-architecture.md`), internal markdown links break silently. Need a link checker that runs post-generation. |
| 10 | **Review skill iteration** | `/review` should track which specific items were fixed between iterations | v1 scored 8.8/10, v2 scored 9.1/10. The improvement was real but the review skill doesn't diff against prior reviews to show what improved. |

## P2 — Engagement Support

| # | Area | Improvement | Context |
|---|------|-------------|---------|
| 11 | **Interview prep generation** | Add interview prep as a deliverable type in `/proposal` | eng-2026-004-v2 produced study-guide, pre-show-checklist, quick-reference, speaker-script — all manually scoped. These are high-value for interview assignments and should be a `--type interview` proposal variant. |
| 12 | **Presentation-first flow** | Add a canonical flow optimized for slide deck delivery | The Autonomize engagement's primary deliverable was a presentation, not a document. The current flows are document-centric. A presentation flow would: requirements → architecture → diagrams → presentation → speaker notes → interview prep. |
| 13 | **Research context as first-class KB** | Make `research-context.md` a KB file with schema and versioning | Research findings (50+ verified sources for eng-2026-004-v2) were critical to deliverable quality but lived outside the KB. Should be `knowledge_base/research.json` with citation validation. |
| 14 | **Engagement templates** | Pre-built engagement configs for common scenarios | "Interview take-home", "discovery engagement", "migration assessment" etc. Each would pre-set depth, deliverables, and flow. eng-2026-004 was an interview take-home — that pattern is reusable. |

## P3 — Future Enhancements

| # | Area | Improvement | Context |
|---|------|-------------|---------|
| 15 | **Multi-repo awareness** | Skills should understand when deliverables are consumed by other repos | eng-2026-004-v2 outputs were consumed by autonomize-healthcare-ai-demo. The SA agent had no awareness of the downstream repo's structure or needs. |
| 16 | **Deliverable diff tracking** | Show what changed between engagement versions | v1→v2 involved re-running 7 of 9 skills. No easy way to see what substantively changed in the architecture between versions beyond git diff. |
| 17 | **KB archive management** | Automated archival of KB files to `knowledge_base/archive/<engagement>/` | Currently manual. eng-2026-003 KB files were manually moved to archive. Should happen automatically on engagement close. |
| 18 | **Engagement metrics** | Track engagement statistics (time, iterations, scores, file counts) | eng-2026-004: 2 iterations, 9.1/10 final score, 35 deliverable files, ~20 commits. This data would help calibrate estimates and improve the agent. |

---

## Completed (eng-2026-004-v2)

Items from the engagement-specific backlog (`outputs/eng-2026-004/plans/backlog.md`) that were resolved in v2:

- [x] P0-1: Re-run WA reviewers — 6 parallel agents, scores updated
- [x] P0-2: Correct SageMaker PSI claim — removed, architecture is now Azure-native
- [x] P0-3: Add Altais case study — included in presentation Slide 2
- [x] P0-4: Add CAQH Index benchmarks — $3.52 payer, $515M savings, verified
- [x] P2-10: Generate Q&A prep — 18 questions in quick-reference.md
- [x] P2-12: Re-render diagrams to PNG — 6 diagrams × 3 formats
- [x] P3-13: Build the demo — autonomize-healthcare-ai-demo repo created
