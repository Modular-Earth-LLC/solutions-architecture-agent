# NEXT STEPS

**Date**: 2026-03-16
**Status**: v1.0.0 released. Plugin installation tested and documented. Ready for first real engagement.

---

## Completed

### v1.0.0 — Core Plugin (Phase 1-9)
- 9 SA lifecycle skills, 2 sub-agents, 11 JSON schemas
- End-to-end validation against healthcare IBMi migration case study
- 8 test scripts (57 checks), all passing
- CI/CD on GitHub Actions

### Plugin Installation & Local Dev Environment
- Decoupled per-platform scripts: `install-deps`, `install-cli`, `install-desktop`, `run-tests`, `verify`
- `marketplace.json` for persistent CLI installation
- Multi-environment docs: CLI, Claude Desktop, VS Code
- `.venv/` in root .gitignore, hardcoded paths removed for portability

---

## Immediate Next: CVS Health Legacy System Transformation

Use the SA Agent's full capabilities to execute a real engagement — the CVS Health IBMi modernization case study for Paul's Principal Architect interview.

### How to Execute

The planning prompt is at `.claude/plans/solutions-architecture-first-assignment-planning-prompt.md`. It defines 7 phases (Phase 0-6) using the migration engagement flow.

**Step 1: Generate the master plan**

Open Claude Code with the plugin loaded and enter plan mode:

```
claude --plugin-dir .
```

Then paste or reference the planning prompt. This is a meta-planning step — it produces 7 standalone phase plans in `.claude/plans/`, not the deliverables themselves.

**Step 2: Execute phases sequentially**

Each phase plan is a self-contained prompt. Execute them one at a time, reviewing output between phases:

| Phase | Skill(s) | Output |
|-------|----------|--------|
| 0: Research & Requirements | `/requirements`, `/review` | `requirements.json` |
| 1: UX & Workflow Design | (manual — research + design doc) | UX document |
| 2: Solution Architecture | `/integration-plan`, `/architecture`, `/data-model`, `/review` | `integration_plan.json`, `architecture.json`, `data_model.json` |
| 3: Security & IAM | `/security-review`, `/review` | `security_review.json` |
| 4: Estimation & Planning | `/estimate`, `/project-plan`, `/review` | `estimate.json`, `project_plan.json` |
| 5: Deliverable Assembly | `/proposal`, `/review` | `outputs/cvs-legacy-transformation/` |
| 6: Interview Prep | (manual — study guide, Q&A, script) | `private/interview-prep/` |

**Step 3: Quality gates**

After each phase, the `/review` skill validates quality (target >= 7.5/10 across 5 dimensions). Do not proceed to the next phase until the quality gate passes.

**Step 4: Human checkpoints**

Every skill presents a checkpoint after completion. Review the output, provide feedback, iterate if needed, then proceed.

### Key Files

- Planning prompt: `.claude/plans/solutions-architecture-first-assignment-planning-prompt.md`
- Reference materials: `.claude/plans/references/` (case study PDF, SA exemplars)
- Paul's brand/career data: paths listed in the planning prompt (WSL + Windows)
- Outputs will land in: `knowledge_base/` (JSON) and `outputs/` (Markdown)
- Interview prep (private): `private/interview-prep/`

### Tips

- Run `/requirements` with the comprehensive tier for maximum coverage
- The planning prompt includes Paul's initial answers to the 5 key considerations — the agent will validate, deepen, and improve upon them
- Use web search extensively in Phase 0 (IBMi/AS/400, CVS Health tech strategy, healthcare UX)
- Phase 5 assembles everything into a single presentation-ready document
- Phase 6 is eyes-only interview prep — not shared with interviewers

---

## Post-Release Roadmap

### Near-Term (v1.1.0)
- **Second case study** — greenfield AI project (different domain from healthcare)
- **system_config.json cleanup** — decompose stale 779-line file into focused configs
- **Behavioral tests** — parameterized integration test feeding synthetic $ARGUMENTS

### Medium-Term (v1.2.0)
- **Marketplace submission** — add `categories`, engine version to plugin.json per Anthropic spec
- **Review calibration** — compare LLM-as-judge scores against human expert assessments
- **Multi-engagement management** — engagement archival workflow, namespace support
- **Proposal templates** — sample output per proposal type (discovery, implementation, internal, pitch)

### Long-Term (v2.0.0)
- **Engineering Agent** — consumes SA Agent outputs, generates implementation artifacts
- **Engagement dashboard** — readiness checks, confidence visualization
- **Fine-tuned review model** — calibrated against human SA reviewer corpus
