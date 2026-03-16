# AI Solutions Architecture Agent

[![QA Validation](https://github.com/Modular-Earth-LLC/solutions-architecture-agent/actions/workflows/validate-knowledge-base.yml/badge.svg)](https://github.com/Modular-Earth-LLC/solutions-architecture-agent/actions/workflows/validate-knowledge-base.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Turn a project idea into a complete, Well-Architected solution design — requirements, architecture, security review, cost estimate, project plan, and client-ready proposal — in a single Claude Code session.**

A Claude Code plugin covering the **solutions architecture lifecycle**: requirements discovery, system design, data modeling, security review, integration planning, estimation, project planning, and proposal assembly. Designs solutions — does NOT implement or deploy.

**Who this is for**: Solutions Architects, Consultants, Enterprise Architects, Technical Pre-Sales, and Engineering Managers who need consistent, high-quality deliverables.

**Version**: 1.0.0 | **Owner**: [Modular Earth LLC](https://github.com/Modular-Earth-LLC) | **Validated**: 9-skill end-to-end against a HIPAA-compliant healthcare IBMi migration (500+ users). [See example outputs](examples/healthcare-ibmi-migration/) | [Changelog](CHANGELOG.md)

---

## Quick Start

```bash
# Clone
git clone https://github.com/Modular-Earth-LLC/solutions-architecture-agent.git
cd solutions-architecture-agent

# Install Python test dependencies
python -m venv .venv && .venv/Scripts/activate  # Windows
# source .venv/bin/activate                     # Linux/macOS
pip install -r requirements.txt

# Load plugin (development — reads live from this directory)
claude --plugin-dir .

# Or install persistently (see docs/local-setup.md)
# claude plugin marketplace add .
# claude plugin install solutions-architecture-agent@solutions-architecture-agent

# Run your first skill
# Type: /requirements
# Or: "I need to design a system for [your project]"
```

Claude loads `CLAUDE.md` and `.claude/rules/` automatically. Skills appear as `solutions-architecture-agent:<skill-name>`.

---

## Skills

| Skill | Command | Purpose | KB Output |
|-------|---------|---------|-----------|
| Requirements Discovery | `/requirements` | Progressive discovery (quick/standard/comprehensive), AI suitability | `requirements.json` |
| Solution Architecture | `/architecture` | System design, tech stack, diagrams, WA scoring | `architecture.json` |
| Estimation | `/estimate` | LOE, cost, team composition, confidence scoring | `estimate.json` |
| Technical Project Plan | `/project-plan` | Phased roadmap, sprints, milestones, dependencies | `project_plan.json` |
| Proposal Assembly | `/proposal` | SOW assembly from KB (4 proposal types) | `outputs/` |
| Data Modeling | `/data-model` | ER, vector, graph, ontology, governance | `data_model.json` |
| Security & Privacy Review | `/security-review` | STRIDE, compliance, defense-in-depth, AI security | `security_review.json` |
| Integration Planning | `/integration-plan` | APIs, migration, legacy bridging, data flows | `integration_plan.json` |
| Deliverable Review | `/review` | LLM-as-judge, 3 iterations, 5 dimensions | `reviews.json` |

---

## Engagement Flows

| Flow | Sequence | When |
|------|----------|------|
| **Greenfield** | req → arch → dm → sr → est → ppl → pro → rv | Complete 0-to-1 engagement |
| **Migration** | req → ip → arch → dm → sr → est → ppl → pro → rv | Migration/modernization |
| **Streamlined** | req → arch → est → pro | Small projects, time-constrained |
| **Assessment** | req → arch → [sr] → pro | Discovery-only, pre-commitment |
| **Quick Qualify** | req (quick tier) | Pipeline qualification |

Natural language also works — describe your project and the agent classifies intent and routes to the right skill.

---

## Knowledge Base

Skills communicate through a shared **knowledge base** (`knowledge_base/`) using the blackboard pattern:

- **JSON files** — each skill owns one, writes only to it (see `.repo-metadata.json` for counts)
- **JSON schemas** — validate structure at `knowledge_base/schemas/`
- **`$depends_on`** — each file declares upstream dependencies
- **`engagement.json`** — tracks lifecycle state across all domain files
- **`system_config.json`** — read-only reference data (Well-Architected definitions, technical references)

Validate anytime: `python tests/validate_knowledge_base.py`

---

## Repository Structure

```
solutions-architecture-agent/
├── .claude-plugin/plugin.json     # Plugin manifest
├── CLAUDE.md                      # Agent identity + dispatch rules
├── skills/                        # SA lifecycle skills (see .repo-metadata.json for list)
│   ├── requirements/SKILL.md
│   ├── architecture/SKILL.md
│   ├── estimate/SKILL.md
│   ├── project-plan/SKILL.md
│   ├── proposal/SKILL.md
│   ├── data-model/SKILL.md
│   ├── security-review/SKILL.md
│   ├── integration-plan/SKILL.md
│   └── review/SKILL.md
├── agents/                        # Sub-agents for parallel execution
│   ├── parallel-wa-reviewer.md
│   └── stride-analyzer.md
├── knowledge_base/                # Shared state (blackboard pattern)
│   ├── schemas/                   # JSON Schema (Draft 2020-12)
│   ├── system_config.json         # Read-only reference
│   └── engagement.json            # Lifecycle state tracker
├── hooks/hooks.json               # Pre-commit validation hooks
├── scripts/                       # Setup & verification (per-platform, decoupled)
├── templates/                     # Output templates
├── tests/                         # Validation scripts (8 scripts, 57 checks)
├── docs/                          # User documentation
├── examples/                      # Sample engagement outputs (explore these first)
├── .claude/rules/                 # Guiding principles, KB rules, security
├── .repo-metadata.json            # Single source of truth (version, counts)
└── outputs/                       # Generated deliverables (gitignored)
```

---

## Documentation

- **[ARCHITECTURE.md](ARCHITECTURE.md)** — System design with Mermaid diagrams
- **[CONTRIBUTING.md](CONTRIBUTING.md)** — How to add skills, PR process
- **[docs/getting-started.md](docs/getting-started.md)** — First project walkthrough
- **[docs/local-setup.md](docs/local-setup.md)** — Multi-environment setup (CLI, Desktop, VS Code)
- **[docs/workflow_guide.md](docs/workflow_guide.md)** — Engagement lifecycle details
- **[docs/executive_overview.md](docs/executive_overview.md)** — Business value and ROI
- **[docs/human-ai-collaboration.md](docs/human-ai-collaboration.md)** — Human-in-the-loop design

---

## Who Should Use This

- **Solutions Architects** — Systematic Well-Architected designs, consistent deliverables
- **Consultants** — Professional proposals in hours, accurate estimates
- **Enterprise Architects** — Standardized assessment frameworks across engagements
- **Technical Pre-Sales** — Rapid qualification and scoping
- **Engineering Managers** — Evidence-based project planning and estimation

---

## Quality Standards

- **Well-Architected compliance** — AWS 6 pillars + GenAI Lens, Azure WAF, GCP WAF on every architecture
- **Technology-agnostic** — recommends best-fit via web search, never defaults to specific vendors
- **Confidence scoring** — COMPLETE/PARTIAL/INCOMPLETE (requirements), HIGH/MEDIUM/LOW (estimates), 0-10 (WA pillars)
- **Human checkpoints** — after every skill: summarize, list deliverables, suggest next skill
- **Scope boundary** — designs solutions only; implementation is out of scope (future Engineering Agent)

---

## Status

**v1.0.0** — Validated end-to-end in Phase 7 against a healthcare IBMi modernization case study (migration flow, HIPAA compliance, 500+ users).

- 11/11 schema validations PASS
- 5/5 consistency checks PASS
- 4 deliverable reviews >= 7.5/10

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add new skills, sub-agents, and submit PRs.

## License

MIT License — see [LICENSE](LICENSE).
