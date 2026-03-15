# Solutions Architecture Agent

A specialized AI agent for the **solutions architecture lifecycle**: ideation, requirements, architecture design, team composition, cost estimation, and deployment planning.

**Owner**: Modular Earth LLC (@paulpham157)
**Dual deployment**: Claude Code CLI (local, primary) + Anthropic Cloud Platform (SaaS, future)

## Repository Layout

```
solutions-architecture-agent/
├── CLAUDE.md                         # This file (always loaded)
├── .claude/                          # Claude Code configuration
│   ├── settings.json                 # Project permissions and hooks
│   ├── rules/                        # Scoped instructions (loaded contextually)
│   ├── skills/                       # Slash-command skills (loaded on invocation)
│   ├── agents/                       # Subagent definitions
│   ├── plans/references/             # Planning reference materials
│   └── hooks/                        # Automation scripts
├── supervisor_agent.system.prompt.md # Legacy supervisor (source for refactoring)
├── ai_agents/                        # Legacy agent prompts (source for skill migration)
├── knowledge_base/                   # JSON state + schemas (on-demand reference)
├── user_prompts/                     # Task-specific prompts (source for skill templates)
├── docs/                             # User documentation
├── templates/                        # Output templates
├── tests/                            # Validation scripts
├── outputs/                          # Generated outputs (git-ignored content)
├── private/                          # Sensitive data (git-ignored content)
└── .repo-metadata.json               # Single source of truth for version/counts
```

## Key Rules

- **`.repo-metadata.json`** is the single source of truth — never hard-code version or counts elsewhere
- **`system_config.json`** is READ-ONLY — reference it but never modify it
- **Agent prompts** (`.system.prompt.md`) are being migrated to skills — see @.claude/plans/references/agent-to-skill-mapping.md
- New capabilities go into `.claude/skills/`, not new agent prompts
- Validate JSON against schemas: `python tests/validate_knowledge_base.py`

## Refactoring Direction

This repo is being consolidated from 23 agents into **1 agent + N skills**. See @.claude/rules/refactoring-direction.md for details and @.claude/plans/references/target-architecture.md for the target state.

## Tech Stack

Python 3.12+ | Streamlit | Anthropic Claude | AWS Bedrock | MCP | LangChain | JSON Schema

## GitHub Integration

Use the `gh` CLI (GitHub CLI) for all GitHub operations — issues, PRs, releases, repo management. Do not use the GitHub MCP plugin. The `gh` CLI is already authenticated and permitted in project settings.

## Quality Standards

- AWS Well-Architected compliance (6 pillars + GenAI Lens)
- TRM validation for generated outputs
- Code: coverage >= 80%, type hints >= 90%, no secrets in version control
