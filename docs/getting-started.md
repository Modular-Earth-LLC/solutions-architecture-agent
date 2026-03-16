# Getting Started

Get productive in 15 minutes.

---

## Prerequisites

- **Claude Code CLI** — [install guide](https://docs.anthropic.com/en/docs/claude-code/overview)
- **Git** — to clone the repository
- **Python 3.10+** — for validation scripts (`pip install jsonschema`)

---

## Install the Plugin

```bash
# 1. Clone
git clone https://github.com/Modular-Earth-LLC/solutions-architecture-agent.git
cd solutions-architecture-agent

# 2. Install as Claude Code plugin
claude mcp add-from-claude-plugin .

# Or load directly for development
claude --plugin-dir .
```

Claude automatically loads `CLAUDE.md` and `.claude/rules/` configuration. Skills appear as `solutions-architecture-agent:<skill-name>`.

---

## Run Your First Skill

**Option A — Slash command:**
```
/requirements
```

**Option B — Natural language:**
```
I need to design a healthcare data platform that modernizes our legacy systems.
```

The agent classifies your intent and routes to the appropriate skill. After each skill completes, it presents a **human checkpoint**: summary, deliverables, and suggested next skill.

---

## Understanding the System

**Single agent with 9 skills.** Each skill handles one phase of the SA lifecycle:

1. `/requirements` — Discover what the client needs
2. `/architecture` — Design the system
3. `/data-model` — Model the data layer
4. `/security-review` — STRIDE threat modeling + compliance
5. `/integration-plan` — APIs, migration, legacy bridging
6. `/estimate` — LOE, cost, team composition
7. `/project-plan` — Phased roadmap with sprints
8. `/proposal` — Assemble SOW from all upstream deliverables
9. `/review` — LLM-as-judge quality review

Skills communicate through JSON files in `knowledge_base/` — each skill reads from upstream files and writes to its own file.

---

## Engagement Flows

Choose the flow that matches your engagement type:

| Flow | Skills | When |
|------|--------|------|
| **Greenfield** | req → arch → dm → sr → est → ppl → pro → rv | New system from scratch |
| **Migration** | req → ip → arch → dm → sr → est → ppl → pro → rv | Legacy modernization |
| **Streamlined** | req → arch → est → pro | Small/time-constrained |
| **Assessment** | req → arch → [sr] → pro | Discovery-only |
| **Quick Qualify** | req (quick tier) | Pipeline qualification |

You don't need to run every skill — the agent checks prerequisites and tells you what's missing.

---

## Validation

Run validation scripts to check KB file integrity:

```bash
# Schema validation
python tests/validate_knowledge_base.py

# Metadata consistency, $depends_on chains, ID uniqueness
python tests/validate_consistency.py
```

---

## Security & Sensitive Data

- Use the `private/` directory for any sensitive files (gitignored)
- See `private/README.md` for security guidelines
- Never commit API keys, credentials, or PII to version control
- Verify with `git status` before committing

---

## Next Steps

- **[workflow_guide.md](workflow_guide.md)** — Detailed engagement flow walkthrough
- **[human-ai-collaboration.md](human-ai-collaboration.md)** — What the agent does vs. what you do
- **[../ARCHITECTURE.md](../ARCHITECTURE.md)** — System design with Mermaid diagrams
- **[../CONTRIBUTING.md](../CONTRIBUTING.md)** — How to add new skills
