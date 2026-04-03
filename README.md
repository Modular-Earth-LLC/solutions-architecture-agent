# AI Solutions Architecture Agent

[![QA Validation](https://github.com/Modular-Earth-LLC/solutions-architecture-agent/actions/workflows/validate-knowledge-base.yml/badge.svg)](https://github.com/Modular-Earth-LLC/solutions-architecture-agent/actions/workflows/validate-knowledge-base.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://python.org) [![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-orange)](https://docs.anthropic.com/en/docs/claude-code)

> A production-grade Claude Code plugin that covers the complete pre-sales SA lifecycle — requirements through proposal — in a single conversation. Built by a principal SA for principal SAs. Not a chatbot wrapper: a structured, reviewable, expert system.

**Turn a project idea into a complete, Well-Architected solution design — requirements, architecture, security review, cost estimate, project plan, and client-ready proposal — in a single Claude Code session.**

**Version**: 1.1.0 | **Owner**: [Modular Earth LLC](https://github.com/Modular-Earth-LLC) | **Validated**: 9-skill end-to-end against a HIPAA-compliant healthcare IBMi migration (500+ users). [See example outputs](examples/healthcare-ibmi-migration/) | [Changelog](CHANGELOG.md)

---

## Why This Exists

Traditional SA work is slow, inconsistent, and hard to review. A single engagement produces requirements documents, architecture diagrams, security reviews, cost estimates, and proposals — each assembled manually, each varying by the individual SA. The output is hard to diff, hard to audit, and hard to reproduce.

This agent makes SA work **reproducible, auditable, and peer-reviewable**. Every output is a structured KB artifact with a JSON schema, a version number, and a declared dependency chain — not a free-form conversation. Each skill runs in isolation, produces a single file it owns, and never writes to a file it doesn't own. Human review is mandatory at every checkpoint.

---

## Quick Start

```bash
# Clone
git clone https://github.com/Modular-Earth-LLC/solutions-architecture-agent.git
cd solutions-architecture-agent

# Install Python test dependencies
uv sync

# Load plugin (development — reads live from this directory)
claude --plugin-dir .

# Run your first skill
# Type: /requirements
# Or: "I need to design a system for [your project]"
```

Claude loads `CLAUDE.md` and `.claude/rules/` automatically. Skills appear as `solutions-architecture-agent:<skill-name>`.

---

## Skills

| Skill | Command | What It Produces |
|-------|---------|-----------------|
| Requirements Discovery | `/requirements` | Progressive discovery workshop output — AI suitability score, classified pain points, 7-category requirements list, BANT qualification |
| Solution Architecture | `/architecture` | Tech stack selection with cited benchmarks, component design, 3 Mermaid diagrams, AWS/Azure/GCP Well-Architected scores per pillar |
| Data Modeling | `/data-model` | ER schema, vector DB collection design (embedding model, chunking strategy, reranking), graph schema, governance policy |
| Security & Privacy Review | `/security-review` | STRIDE threat model (6 parallel sub-agents), defense-in-depth architecture, compliance posture per framework, AI threat mapping |
| Integration Planning | `/integration-plan` | API contract definitions, migration strategy (strangler fig/parallel run), data flow mappings, legacy bridging patterns |
| Estimation | `/estimate` | 3-point LOE estimates, team composition, infrastructure cost model, confidence scoring (HIGH/MEDIUM/LOW) |
| Technical Project Plan | `/project-plan` | Phased roadmap, 2-week sprint plans, risk register, dependency graph, Fist-of-Five decision gates |
| Proposal Assembly | `/proposal` | SOW (12 sections), discovery proposal, internal pitch deck, or custom-format document — assembled from KB |
| Deliverable Review | `/review` | LLM-as-judge 3-iteration review, 5-dimension scoring (0-10 per dimension), Well-Architected pillar scores for architecture reviews |

---

## Design Philosophy

This agent was designed around three non-obvious architectural decisions. See [DESIGN_RATIONALE.md](DESIGN_RATIONALE.md) for the full reasoning.

**Single agent with skills, not multi-agent orchestration.** Research shows multi-agent pipelines degrade sequential reasoning by 39-70% (arXiv:2512.08296). One agent with structured skills eliminates inter-agent handoff failures and maintains full conversation context across the engagement.

**Blackboard pattern for skill communication.** Skills communicate exclusively through JSON files in `knowledge_base/`. No direct skill-to-skill calls. This supports independent skill testing, replay/resume capability, and human auditability of every intermediate state.

**LLM-as-judge review with three iterations.** The `/review` skill uses adversarial dual-persona (Builder + Tester) with 3 iteration passes — each catching gaps the prior pass missed. Scored against 5 dimensions with early-stop at 9.0+ to avoid over-scoring.

---

## Engagement Flows

| Flow | Sequence | Depth | When |
|------|----------|-------|------|
| **Greenfield** | req → arch → dm → sr → est → ppl → pro → rv | STANDARD | Complete 0-to-1 engagement |
| **Migration** | req → ip → arch → dm → sr → est → ppl → pro → rv | STANDARD | Migration/modernization |
| **Streamlined** | req → arch → est → pro | STANDARD | Small projects, time-constrained |
| **Assessment** | req → arch → [sr] → pro | STANDARD | Discovery-only, pre-commitment |
| **Quick Qualify** | req | QUICK | Pipeline qualification |
| **Direct Delivery** | scope negotiation → single skill → output | QUICK | Single-document, interview prep |
| **Rapid Assessment** | req → arch → pro | QUICK | Same-day turnaround (`--depth QUICK`) |
| **Custom Document** | selective skills → proposal --type custom | QUICK | User-specified format and sections |

### Depth Tiers

Every skill supports three depth tiers:

| Tier | Behavior | KB Files | Sub-Agents | Typical Output |
|------|----------|----------|------------|----------------|
| **QUICK** | Minimal output, no KB writes | None | None | 1-4 page doc |
| **STANDARD** | Full workflow (default) | Yes | Conditional | Full KB + output |
| **COMPREHENSIVE** | Extended analysis, multi-cloud | Yes | Yes | Full KB + review |

Use `--depth QUICK` to skip scope negotiation and go straight to output.

---

## Knowledge Base

Skills communicate through a shared **knowledge base** using the blackboard pattern — no direct skill-to-skill communication.

```json
{
  "$schema": "../schemas/architecture.schema.json",
  "$depends_on": ["requirements.json"],
  "engagement_id": "eng-2026-001",
  "version": "1.0",
  "status": "complete",
  "executive_summary": {
    "recommended_approach": "Event-driven microservices on AWS ECS Fargate",
    "confidence": "high",
    "go_no_go": "go"
  },
  "well_architected_scores": {
    "operational_excellence": { "score": 8, "max": 10 },
    "security": { "score": 9, "max": 10 }
  }
}
```

- Each skill owns exactly one KB file and writes only to it
- `$depends_on` declares upstream dependencies — prerequisite validation is automatic
- `engagement.json` tracks lifecycle state across all domain files
- `system_config.json` is read-only reference data (Well-Architected definitions)

Validate anytime: `python tests/validate_knowledge_base.py`

---

## Repository Structure

```
solutions-architecture-agent/
├── .claude-plugin/plugin.json     # Plugin manifest
├── CLAUDE.md                      # Agent identity + dispatch rules
├── skills/                        # SA lifecycle skills (each: <name>/SKILL.md)
│   ├── requirements/SKILL.md
│   ├── architecture/SKILL.md
│   └── ... (9 skills total)
├── agents/                        # Sub-agents for parallel execution
│   ├── parallel-wa-reviewer.md    # 6-pillar WA scoring
│   └── stride-analyzer.md        # 6-category STRIDE threat analysis
├── knowledge_base/                # Shared state (blackboard pattern)
│   ├── schemas/                   # JSON Schema (Draft 2020-12) — 11 schemas
│   ├── system_config.json         # Read-only reference
│   └── engagement.json            # Lifecycle state tracker
├── hooks/hooks.json               # Pre-commit validation hooks
├── templates/                     # Output templates (11 files)
├── tests/                         # Validation scripts (10 scripts, 57+ checks)
├── docs/                          # User documentation
├── examples/                      # Sample engagement outputs
├── .claude/rules/                 # Guiding principles, KB rules, security
├── .repo-metadata.json            # Single source of truth (version, counts)
└── outputs/                       # Generated deliverables (gitignored)
```

---

## Quality Standards

- **Well-Architected compliance** — AWS 6 pillars + GenAI Lens, Azure WAF, GCP WAF. Scored 0-10 per pillar via 6 parallel sub-agent invocations.
- **Technology-agnostic** — No vendor lock-in: recommends best-fit stack via live WebSearch benchmarking. No hardcoded preferences.
- **Evidence-based recommendations** — "Superior quality" claims require a cited benchmark. Model selection requires documented rationale.
- **Confidence scoring** — COMPLETE/PARTIAL/INCOMPLETE (requirements), HIGH/MEDIUM/LOW (estimates), 0-10 per WA pillar (architecture).
- **Human checkpoints** — MANDATORY STOP after every skill. Never auto-invokes the next skill.
- **Scope boundary** — Designs solutions only. Implementation is explicitly out of scope (future Engineering Agent).
- **Validated quality** — Four deliverable reviews scored ≥ 7.5/10 against the healthcare IBMi migration example (`examples/healthcare-ibmi-migration/`) using LLM-as-judge methodology.

---

## Documentation

- **[ARCHITECTURE.md](ARCHITECTURE.md)** — System design, plugin structure, sub-agent orchestration
- **[DESIGN_RATIONALE.md](DESIGN_RATIONALE.md)** — Research citations, design decisions, known trade-offs
- **[CONTRIBUTING.md](CONTRIBUTING.md)** — How to add skills, PR process, manual testing guide
- **[docs/getting-started.md](docs/getting-started.md)** — First project walkthrough
- **[docs/local-setup.md](docs/local-setup.md)** — Multi-environment setup (CLI, Desktop, VS Code)
- **[docs/workflow_guide.md](docs/workflow_guide.md)** — Engagement lifecycle and canonical flows
- **[docs/executive_overview.md](docs/executive_overview.md)** — Business value and ROI
- **[docs/human-ai-collaboration.md](docs/human-ai-collaboration.md)** — Human-in-the-loop design

---

## For Contributors

**Target contributor profile**: Senior AI/cloud SA, principal engineer, solutions consultant, or AI researcher with domain knowledge in enterprise architecture or pre-sales consulting.

This repository is AI-first: primary contributors are AI coding assistants (Claude Code, GitHub Copilot). All conventions are explicit, machine-parseable, and verified by automated tests.

To add a new skill, see [CONTRIBUTING.md § How to Add a New Skill](CONTRIBUTING.md#how-to-add-a-new-skill). The process is: create SKILL.md → create schema → register in CLAUDE.md → update `.repo-metadata.json` → validate all 10 test scripts.

---

## Exporting to Word/DOCX

The agent produces Markdown output. Convert to Word with [pandoc](https://pandoc.org/) + the [Mermaid CLI](https://github.com/mermaid-js/mermaid-cli):

```bash
# Pre-render Mermaid diagrams to PNG
mmdc -i diagram.mmd -o diagram.png -t neutral -b transparent
# Convert Markdown to DOCX
pandoc output.md -o output.docx --reference-doc=template.docx
```

---

## License

MIT License — see [LICENSE](LICENSE).
