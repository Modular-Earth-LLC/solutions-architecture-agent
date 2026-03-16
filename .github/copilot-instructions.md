# Solutions Architecture Agent — GitHub Copilot Instructions

A Claude Code plugin with 9 SA lifecycle skills and 2 sub-agents.

Read first:
- `CLAUDE.md`
- `.claude/rules/guiding-principles.md`

## Architecture

Single agent with skills (not multi-agent). See `ARCHITECTURE.md` for full design.

- 9 skills in `skills/*/SKILL.md`
- 2 sub-agents in `agents/*.md`
- Knowledge base in `knowledge_base/` (blackboard pattern)
- Schemas in `knowledge_base/schemas/`

## Repository Priorities

1. Keep the "1 agent + skills" architecture — don't add more agents.
2. `.repo-metadata.json` is the single source of truth for counts/version metadata.
3. `knowledge_base/system_config.json` is read-only.
4. Preserve Well-Architected quality gates.
5. Keep sensitive data out of version control (`private/` is gitignored).

## Preferred Copilot Behavior

When suggesting edits:
- Minimal, targeted diffs over broad rewrites
- Markdown and JSON consistency with nearby files
- Clear validation steps and deterministic commands

When proposing changes:
- Prefer adding skills in `skills/` following the pattern in CONTRIBUTING.md
- Avoid introducing new agent prompts unless explicitly requested
- Explain tradeoffs briefly

## File-Specific Guidance

### Skill files (`skills/*/SKILL.md`)
- Follow the 6-section structure (Identity, Workflow, Quality, Context, Output, Error Handling)
- Include envelope fields paragraph in Section 5
- Ensure schema alignment (field names match exactly)

### Knowledge base (`knowledge_base/**/*.json`)
- Never modify `system_config.json`
- Validate after changes: `python tests/validate_knowledge_base.py`

### Security-sensitive paths (`private/**`, `**/.env*`, `**/*credential*`)
- Never output or commit secrets, tokens, credentials, or PII

## Validation Commands

```bash
python tests/validate_knowledge_base.py
python tests/validate_consistency.py
```

Run after changing skills, schemas, or knowledge base files.
