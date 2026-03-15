# Solutions Architecture Agent - GitHub Copilot Instructions

This repository is a solutions architecture framework being refactored from a multi-agent prompt system into a single specialized agent with skills.

Read first:
- `CLAUDE.md`
- `.claude/rules/guiding-principles.md`
- `.claude/rules/refactoring-direction.md`

## Mission

Help contributors ship practical architecture assets faster while preserving:
- Human-centered design principles
- Security and privacy constraints
- Simplicity (KISS) and incremental reversible changes

## Repository Priorities

1. Move toward "1 agent + skills" architecture, not more agents.
2. Keep `.repo-metadata.json` as the single source of truth for counts/version metadata.
3. Treat `knowledge_base/system_config.json` as read-only.
4. Preserve quality gates (Well-Architected and TRM expectations).
5. Keep sensitive data out of version control.

## Preferred Copilot Behavior

When suggesting edits, favor:
- Minimal, targeted diffs over broad rewrites
- Markdown and JSON structure consistency with nearby files
- Clear validation steps and deterministic commands
- Backward compatibility with existing repository layout

When proposing architecture or process changes:
- Prefer adding reusable skills in `.claude/skills/`
- Avoid introducing new agent prompts unless explicitly requested
- Explain tradeoffs and risks briefly

## File-Specific Guidance

### Prompt files

Applies to:
- `supervisor_agent.system.prompt.md`
- `ai_agents/**/*.md`

Rules:
- Preserve section headers and structure
- Keep cross-references between prompts consistent
- Do not remove validation and quality sections
- Keep prompts self-contained and runnable

### Knowledge base files

Applies to:
- `knowledge_base/**/*.json`
- `knowledge_base/**/*.schema.json`

Rules:
- Never modify `knowledge_base/system_config.json`
- Validate knowledge base JSON after changes:
	- `python tests/validate_knowledge_base.py`

### Security-sensitive paths

Applies to:
- `private/**/*`
- `**/.env*`
- `**/*credential*`
- `**/*secret*`

Rules:
- Never output or commit secrets, tokens, credentials, or PII
- Keep sensitive artifacts in `private/` only

## High-Value Commands

- `python tests/validate_knowledge_base.py`
- `python tests/validate_consistency.py`
- `python tests/validate_urls.py`

Run relevant validation after changing prompts, docs, or knowledge-base assets.

## What "Good" Looks Like

- Instructions are concise, specific, and testable
- Changes are easy to review and revert
- Generated guidance aligns with `CLAUDE.md` and `.claude/rules/`
- Outputs improve developer flow without creating lock-in or dark patterns
