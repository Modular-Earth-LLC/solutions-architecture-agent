# Phase 8: Documentation, Packaging & Plugin Testing — Execution Plan

> Created: 2026-03-15 | Updated: 2026-03-16 (Phase 7 learnings incorporated)
> Prerequisites: Phase 7 complete (all exit criteria met — see phase-7-results.md)
> Plugin spec: phase-5-context.md (Claude Code plugin docs, March 2026)

---

## Context

Phases 5-7 created the functional agent (9 skills, 11 schemas, 2 validation scripts, 2 sub-agents) and validated it end-to-end against a healthcare IBMi modernization case study. Phase 8 writes documentation, tests plugin installation, verifies sub-agent runtime behavior, and cleans up development artifacts.

### Phase 7 Learnings That Shape This Phase

1. **All 9 skills produce schema-valid output** — documentation can confidently describe the skill outputs
2. **Sub-agents (parallel-wa-reviewer, stride-analyzer) need runtime testing** — output format validated via schema, but Agent tool invocation not yet tested
3. **Plugin not yet tested as installed plugin** — skills executed manually in Phase 7; `claude --plugin-dir .` validation critical
4. **Envelope fields note (A1) is essential** — CONTRIBUTING.md must document this for skill authors
5. **Schema-to-SKILL.md alignment** was the most common issue class — document the rules
6. **Integration_plan can run before architecture** in migration flow — engagement lifecycle documentation must reflect this
7. **KB files can be large** (security_review ~300 lines) — selective section loading pattern should be documented
8. **Proposal output is substantial** (972 lines, 12 sections) — quality is high

---

## Inputs

| # | File | Purpose |
|---|------|---------|
| 1 | `.claude/plans/phase-7-results.md` | Test results, quality scores, issue table, optimization analysis |
| 2 | `.claude/plans/phase-6-results.md` | Deferred doc issues (tests/README.md, architecture template) |
| 3 | `.claude/plans/phase-5-results.md` | Skill inventory, file structure |
| 4 | `.claude/plans/phase-5-context.md` | Claude Code plugin spec, sub-agent spec |
| 5 | `.claude/plans/technical-design.md` Section 8 | Architecture diagrams (Mermaid) |
| 6 | `.claude-plugin/plugin.json` | Current plugin manifest |
| 7 | `CLAUDE.md` | Current agent identity |
| 8 | `.repo-metadata.json` | Version and counts |

---

## Part A: Plugin Installation & Runtime Testing

### A1: Local Plugin Install
- Run `claude --plugin-dir .` and verify plugin loads
- Verify all 9 skills discoverable via `solutions-architecture-agent:` prefix
- Test `/reload-plugins` to confirm hot reload works

### A2: Sub-Agent Runtime Testing
- Invoke `parallel-wa-reviewer` via Agent tool with a test architecture payload
- Verify it runs 6 times (one per WA pillar) and returns structured pillar scores
- Invoke `stride-analyzer` via Agent tool with a test architecture payload
- Verify it runs 6 times (one per STRIDE category) and returns structured threat entries

### A3: Skill Invocation Smoke Test
- Invoke at least 2 skills via plugin prefix (e.g., `solutions-architecture-agent:requirements`)
- Verify they load SKILL.md correctly and follow the workflow
- No need for full engagement flow — Phase 7 already validated end-to-end

---

## Part B: Documentation Overhaul (5 files)

### B1: README.md — REWRITE
- What it does, quick start, 9-skill reference table, engagement types, target users
- Scope boundary: designs and plans, NOT implements
- Installation: `claude --plugin-dir .` (local), GitHub URL (remote)
- Under 200 lines
- MIT license badge

### B2: ARCHITECTURE.md — REWRITE
- Plugin structure, skill dispatch flow, KB data flow DAG
- Context tiers, sub-agent orchestration
- Mermaid diagrams from technical-design.md Section 8
- Engagement lifecycle flows (greenfield, migration, streamlined, assessment, quick qualify)
- Document that integration_plan can run before architecture in migration flow

### B3: CONTRIBUTING.md — REWRITE
- How to create a new skill (10th skill guide)
- Skill frontmatter reference (name, description, argument-hint, allowed-tools)
- Section 5 rules: envelope fields, schema alignment, field name matching
- Testing: validate_knowledge_base.py, validate_consistency.py
- PR process

### B4: docs/getting-started.md — REWRITE
- Step-by-step: install plugin, run greenfield flow, run migration flow
- Copy-paste-run walkthrough
- Expected outputs per skill

### B5: docs/README.md — UPDATE
- Index of all documentation files

---

## Part C: Plans Cleanup

### C1: Archive Development Plans
Move completed phase plans to `.claude/plans/archive/`:
- master-plan.md, master-planning-prompt.md
- phase-1-results.md
- phase-3-plan.md, phase-3-prompt.md
- phase-4-prompt.md
- phase-5-context.md
- requirements.md
- workflow-design.md

### C2: Keep Active Files
Keep in `.claude/plans/`:
- NEXT_STEPS.md (updated roadmap)
- phase-5-results.md (skill inventory — still relevant)
- phase-6-plan.md, phase-6-results.md (schema details — still relevant)
- phase-7-plan.md, phase-7-results.md (test results — still relevant)
- phase-8-plan.md (this file)
- phase-9-plan.md
- technical-design.md (architecture diagrams)
- solutions-architecture-first-assignment-planning-prompt.md (interview prep)

### C3: Keep Reference Files
All files in `.claude/plans/references/` stay (interview materials, SA exemplars, research).

### C4: Fix Phase 6 Deferred Doc Issues
- Fix `tests/README.md` references to old file names (user_requirements.json → requirements.json, etc.)
- Add IaC section to architecture-template.md (low priority, from Phase 6)

---

## Part D: GitHub Configuration

### D1: .github/copilot-instructions.md — UPDATE
Align with CLAUDE.md identity and skill list.

### D2: .github/pull_request_template.md — UPDATE
PR template for skill contributions.

### D3: .github/ISSUE_TEMPLATE/*.md — UPDATE
Issue templates: bug report, feature request, skill request.

### D4: .github/CODEOWNERS — UPDATE
@paulpham157 owns all.

---

## Part E: Plugin Manifest & Metadata

### E1: Verify .claude-plugin/plugin.json
- All fields correct
- Version matches .repo-metadata.json
- Skills list matches actual skills/ directory

### E2: Verify .repo-metadata.json
- Counts correct (9 skills, 2 sub-agents, 11 schemas)
- Version consistent across files

---

## Verification

- [ ] `claude --plugin-dir .` loads plugin successfully
- [ ] All 9 skills discoverable via `solutions-architecture-agent:` prefix
- [ ] Sub-agents (parallel-wa-reviewer, stride-analyzer) execute correctly
- [ ] README under 200 lines
- [ ] No external filesystem references in any documentation
- [ ] All Mermaid diagrams render correctly
- [ ] .repo-metadata.json version matches plugin.json version
- [ ] MIT license present and correct
- [ ] Phase 6 deferred doc issues fixed
- [ ] Development plans archived
- [ ] `python tests/validate_knowledge_base.py` — 2 PASS, 0 FAIL, 9 SKIP (clean state)
- [ ] `python tests/validate_consistency.py` — 5 PASS, 0 FAIL

---

## Execution Command

```bash
claude -p "$(cat .claude/plans/phase-8-plan.md)"
```
