# Refactoring Direction

This repo is being refactored from a 23-agent multi-agent system into a **single AI Solutions Architecture Agent with 9 skills**, packaged as a Claude Code plugin.

## Target Architecture

1. **Single agent** — CLAUDE.md defines identity, skills handle domain workflows
2. **9 skills** at plugin root (`skills/`), following the Agent Skills open standard
3. **Plugin structure** — `.claude-plugin/plugin.json` manifest, skills/, agents/, hooks/ at root
4. **Knowledge base** — 10 specialized JSON files with engagement-centered topology
5. **Templates** — output document templates referenced by skills
6. **Dynamic references** — skills use WebSearch/WebFetch for latest technology knowledge

## Scope Boundary

This agent designs solutions. It does NOT implement, deploy, or write production code. A future AI Engineering Agent handles that.

## What NOT to Do

- Do not expand the legacy multi-agent architecture
- Do not create technology-specific skills (no `/build-streamlit`, `/aws-infra`)
- Do not put skills in `.claude/skills/` — they go in `skills/` (plugin root)
- Do not embed static vendor knowledge — use WebSearch for dynamic references
- Do not reference external filesystems or private repos
