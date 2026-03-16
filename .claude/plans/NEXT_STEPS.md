# NEXT STEPS

**Date**: 2026-03-16
**Status**: v1.0.0 released. Plugin installed and validated. Ready for first real engagement.

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
- Archive exclusions added to CLAUDE.md, .vscode/settings.json, and copilot-instructions.md

---

## Immediate Next: CVS Health Legacy System Transformation

Use the SA Agent's full capabilities to execute a real engagement — the CVS Health IBMi modernization case study for Paul's Principal Architect interview at CVS Health.

### How to Execute

The planning prompt is at `.claude/plans/solutions-architecture-first-assignment-planning-prompt.md`. It defines 8 phases (Phase 0-7) using the migration engagement flow with ultrathink and mandatory web research.

**Step 1: Generate the master plan**

Load the plugin and reference the planning prompt:

```
claude --plugin-dir .
```

This is a meta-planning step — it produces 8 standalone phase plans in `.claude/plans/cvs-engagement/`, not the deliverables themselves. The agent will ask clarifying questions first.

**Step 2: Execute phases sequentially**

Each phase plan is a self-contained prompt with ultrathink and WebSearch directives. Execute one at a time, reviewing output between phases:

| Phase | Skill(s) | Output |
|-------|----------|--------|
| 0: Research & Requirements | `/requirements` (comprehensive), `/review` | `requirements.json` + research doc |
| 1: UX & Workflow Design | WebSearch + design doc | UX document with personas, journeys |
| 2: Solution Architecture | `/integration-plan`, `/architecture`, `/data-model`, `/review` | 3 KB JSON files + Mermaid diagrams |
| 3: Security & IAM | `/security-review`, `/review` | `security_review.json` + IAM strategy |
| 4: Estimation & Planning | `/estimate`, `/project-plan`, `/review` | `estimate.json` + `project_plan.json` |
| 5: Deliverable Assembly | `/proposal`, `/review` | `outputs/cvs-legacy-transformation/` |
| 6: Interview Prep | Study guide, Q&A (25+/topic), script | `private/interview-prep/` |
| 7: AI Methodology & Citation | Portfolio docs, LLM citations | Methodology section + portfolio summary |

**Step 3: Quality gates**

After each phase, `/review` validates quality (target >= 7.5/10 across 5 dimensions). Do not proceed until the gate passes.

**Step 4: Human checkpoints**

Every skill presents a checkpoint. Review, provide feedback, iterate, then proceed. Paul sets direction; the agent executes.

### Key Files

- Planning prompt: `.claude/plans/solutions-architecture-first-assignment-planning-prompt.md`
- Phase plans output to: `.claude/plans/cvs-engagement/`
- Reference materials: `.claude/plans/references/` (case study, job descriptions, SA exemplars)
- Paul's brand/career data: paths listed in the planning prompt (WSL + Windows)
- KB outputs: `knowledge_base/` (JSON)
- Final deliverable: `outputs/cvs-legacy-transformation/solution-architecture-document.md`
- Interview prep (private): `private/interview-prep/`

### Key Design Decisions in the Prompt

- **Ultrathink on every phase** — extended reasoning for maximum quality
- **Mandatory WebSearch** — no factual claims from training data alone
- **Honesty calibration** — Paul's exact experience mapped; IBMi (1/5), GCP gap, IAM-as-design gap all declared transparently
- **Dual competency** — must prove Paul can lead as both SA and data science thought leader
- **Phase 7 (new)** — LLM citations, portfolio documentation, "How I Built the AI Agent" narrative
- **GitHub Flavored Markdown** — Mermaid diagrams render natively, future Word export via pandoc
- **Archive exclusion** — `.claude/plans/archive/` blocked from all indexing to prevent context poisoning

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
