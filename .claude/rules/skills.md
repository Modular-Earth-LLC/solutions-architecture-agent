---
paths:
  - "skills/**"
---

# Skill Editing Rules

- Follow the Agent Skills standard: each skill is a `SKILL.md` file with YAML frontmatter in `skills/<name>/SKILL.md`
- No static vendor knowledge — use WebSearch/WebFetch for dynamic technology references at runtime
- Include `ultrathink` directive in the body (not frontmatter) for deep reasoning skills (/architecture, /data-model, /security-review, /review)
- Keep each SKILL.md under 500 lines; move reference tables or supplemental material to separate files in the skill directory, referenced via `${CLAUDE_SKILL_DIR}`
- Tool grants follow least privilege — only tools listed in `allowed-tools` are available without permission prompts
- Use `Agent` in `allowed-tools` for skills that invoke sub-agents
- Use bracket syntax `$ARGUMENTS[0]` for argument access
- `${CLAUDE_SKILL_DIR}` is available for referencing files in the skill's own directory
- No skill uses `context: fork` — all skills run inline within the main agent context (Decision 1: sequential reasoning)
