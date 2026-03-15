---
paths:
  - "ai_agents/**/*.md"
  - "supervisor_agent.system.prompt.md"
---

# Agent Prompt Editing Rules

When editing agent system prompts:

- Preserve existing section structure and headers — agents reference each other's sections by name
- Keep cross-references between agents consistent (e.g., "delegate to Architecture Agent")
- Do not remove quality gates (TRM validation, Well-Architected checks)
- Update `.repo-metadata.json` if adding or removing agents
- Each agent prompt should be self-contained — it must work as a standalone system prompt
- Test prompts in Claude Code CLI or Cursor IDE before committing
