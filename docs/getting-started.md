# Getting Started

Get productive in 15 minutes.

---

## Prerequisites

- **Claude Code CLI** — [install guide](https://docs.anthropic.com/en/docs/claude-code/overview)
- **Git** — to clone the repository
- **Python 3.10+** and **[uv](https://docs.astral.sh/uv/)** — for validation scripts (`uv sync`)

---

## Install the Plugin

```bash
# 1. Clone
git clone https://github.com/Modular-Earth-LLC/solutions-architecture-agent.git
cd solutions-architecture-agent

# 2. Install Python test dependencies
uv sync

# 3. Load as Claude Code plugin
claude --plugin-dir .

# Or install persistently (see docs/local-setup.md)
# claude plugin marketplace add .
# claude plugin install solutions-architecture-agent@solutions-architecture-agent
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

The agent classifies your intent and routes to the appropriate skill. It asks structured questions, you answer, and it produces validated JSON output in `knowledge_base/`. After each skill completes, it presents a **human checkpoint**: summary, deliverables, and suggested next skill.

Want to see what a full engagement produces? Read the [sample proposal](../examples/healthcare-ibmi-migration/proposal.md) or explore the [complete example outputs](../examples/healthcare-ibmi-migration/).

---

## Understanding the System

**Single agent with skills.** Each skill handles one phase of the SA lifecycle:

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
| **Direct Delivery** | single skill (QUICK) | Single-document tasks, interview prep |
| **Rapid Assessment** | req (QUICK) → arch (QUICK) → pro (QUICK) | Same-day turnaround |
| **Custom Document** | selective skills (QUICK) → proposal --type custom | User-specified format and sections |

You don't need to run every skill — the agent checks prerequisites and tells you what's missing.

---

## Depth Tiers

| Tier | When to Use | KB Files? | Sub-Agents? | Typical Output |
|------|------------|-----------|-------------|----------------|
| QUICK | Time-constrained, interview prep, same-day | No | No | 1-4 page doc |
| STANDARD | Client engagements, complete SA work | Yes | Conditional | Full KB + output |
| COMPREHENSIVE | High-stakes, enterprise procurement | Yes | Yes | Full KB + review |

Use `--depth QUICK` flag to set tier explicitly. Otherwise, the agent determines tier from your answers during scope negotiation.

---

## Validation

Run the validation scripts to check file integrity. See [tests/README.md](../tests/README.md) for details and expected output.

```bash
python tests/validate_knowledge_base.py
python tests/validate_consistency.py
python tests/test_plugin_structure.py
python tests/test_engagement_flow.py
python tests/test_skill_independence.py
```

---

## Security & Sensitive Data

- Use the `private/` directory for any sensitive files (gitignored)
- See `private/README.md` for security guidelines
- Never commit API keys, credentials, or PII to version control
- Verify with `git status` before committing

---

## Next Steps

- **[local-setup.md](local-setup.md)** — Multi-environment setup (CLI, Desktop, VS Code)
- **[workflow_guide.md](workflow_guide.md)** — Detailed engagement flow walkthrough
- **[human-ai-collaboration.md](human-ai-collaboration.md)** — What the agent does vs. what you do
- **[../ARCHITECTURE.md](../ARCHITECTURE.md)** — System design with Mermaid diagrams
- **[../CONTRIBUTING.md](../CONTRIBUTING.md)** — How to add new skills
