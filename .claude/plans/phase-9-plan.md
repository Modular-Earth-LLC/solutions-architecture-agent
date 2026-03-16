# Phase 9: Marketplace Release — Execution Plan

> Created: 2026-03-15 | Prerequisites: Phase 8 complete
> Final phase — requires explicit human approval before any public action

---

## Context

Phases 5-8 created, tested, documented, and packaged the agent. Phase 9 is final QA and release.

---

## Inputs

| # | File | Purpose |
|---|------|---------|
| 1 | `.claude/plans/phase-7-results.md` | Test results, quality confirmation |
| 2 | `.claude/plans/phase-5-results.md` | Skill inventory, platform constraints |
| 3 | All `skills/*/SKILL.md` | Final skill content |
| 4 | `.claude-plugin/plugin.json` | Plugin manifest |
| 5 | `.repo-metadata.json` | Version and counts |

---

## Execution Steps

### Step 1: Final QA Checklist

- [ ] Run `python tests/validate_knowledge_base.py` — all schemas valid
- [ ] Run `python tests/validate_consistency.py` — cross-file references correct
- [ ] Verify no secrets, credentials, PII, or external filesystem references
  - `grep -rn 'C:\\dev\|\\\\wsl\|D:\\dev\|password\|secret\|api_key' skills/ agents/ CLAUDE.md hooks/ knowledge_base/`
- [ ] Verify `.gitignore` covers sensitive paths (knowledge_base/*.json except system_config)
- [ ] Verify `.repo-metadata.json` counts match actual (9 skills, 2 sub-agents)
- [ ] Verify all SKILL.md files under 500 lines, CLAUDE.md under 200 lines
- [ ] Verify no `context: fork`, no `$ARGUMENTS.0`, no `Task` tool
- [ ] Local plugin install: `claude --plugin-dir .` works
- [ ] All 9 skills invocable and produce correct frontmatter info

### Step 2: Dogfooding — Self-Review

Run `/review` targeting the agent's own architecture documentation:
- Review `ARCHITECTURE.md` for accuracy against actual implementation
- Verify skill descriptions match actual behavior
- Check KB documentation matches actual schema

### Step 3: License and Legal

- [ ] MIT LICENSE file present with correct copyright (Modular Earth LLC)
- [ ] SECURITY.md present with responsible disclosure policy
- [ ] No third-party code included without compatible license

### Step 4: Release Preparation

- [ ] Update `.repo-metadata.json` version to `1.0.0`
- [ ] Update `.claude-plugin/plugin.json` version to `1.0.0`
- [ ] Create release notes summarizing: 9 skills, 2 sub-agents, 5 engagement flows, WA compliance

### Step 5: Release (REQUIRES HUMAN APPROVAL)

**Do NOT execute without explicit human approval.**

1. Create GitHub release tag: `git tag v1.0.0`
2. Push: `git push origin main --tags`
3. Test install from GitHub: `claude /plugin install github:Modular-Earth-LLC/solutions-architecture-agent`
4. Submit to Claude Code marketplace (if available)

### Step 6: Future Agent Interface

Document what outputs this agent produces that the future AI Engineering Agent will consume:
- Write to `.claude/plans/engineering-agent-interface.md`
- Map each KB file to engineering agent consumption patterns
- Define the handoff contract

---

## Verification

- [ ] All QA checks pass
- [ ] Self-review score >= 8.0
- [ ] GitHub release tag created
- [ ] Plugin installable from GitHub URL
- [ ] Engineering agent interface documented

---

## Execution Command

```bash
claude -p "$(cat .claude/plans/phase-9-prompt.md)"
```
