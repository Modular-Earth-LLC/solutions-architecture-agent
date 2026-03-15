# Refactoring Direction

This repo is being refactored from a 23-agent multi-agent system into a **single specialized agent with skills**.

When making changes, move toward this target architecture:

1. **Single system prompt** — consolidate supervisor + domain agents into one solutions architecture agent
2. **Skills** — each current agent prompt maps to a skill in `.claude/skills/`
3. **Reference files** — knowledge base files become on-demand references, not always-loaded context
4. **User prompts** — become skill invocation templates or slash commands

Target platforms:
- **Claude Code CLI** (local, primary) — system prompt + skills
- **Anthropic Cloud Platform** (SaaS, future) — API-accessible agent service

Do not expand the multi-agent architecture. New capabilities should be added as skills, not new agents.
