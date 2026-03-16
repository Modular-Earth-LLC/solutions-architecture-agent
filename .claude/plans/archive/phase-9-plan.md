# Phase 9: QA Automation & Release Readiness — Execution Plan

> Created: 2026-03-15 | Updated: 2026-03-16 (Phase 7 learnings incorporated)
> Prerequisites: Phase 8 complete
> Final phase — requires explicit human approval before any public action

---

## Context

Phases 5-8 created, tested, documented, and packaged the agent. Phase 9 is automated QA, a second case study for genericity validation, and release.

### Phase 7 Learnings That Shape This Phase

1. **Manual validation worked but should be automated** — Phase 7 ran validate_knowledge_base.py and validate_consistency.py manually after each skill; automate into a single `/qa` command
2. **Review score thresholds are proven** — >= 7.5 PASS, 5.0-7.4 CONDITIONAL, < 5.0 FAIL; codify in test infrastructure
3. **A second case study is needed** — Phase 7 used healthcare IBMi modernization (migration flow); Phase 9 should test greenfield AI project (different flow, different domain)
4. **$depends_on DAG validation caught a real issue** — keep and extend this check
5. **Schema validation is solid** — 11/11 PASS first time for most files; the validation infrastructure works
6. **Sub-agent runtime testing** — should be covered in Phase 8; if not, must be in Phase 9
7. **Proposal quality needs human review** — 972-line SOW is high quality but the `/review` skill doesn't currently review proposals (only KB files)

---

## Inputs

| # | File | Purpose |
|---|------|---------|
| 1 | `.claude/plans/phase-7-results.md` | Test results, quality confirmation |
| 2 | `.claude/plans/phase-8-plan.md` | What Phase 8 accomplished |
| 3 | All `skills/*/SKILL.md` | Final skill content |
| 4 | `.claude-plugin/plugin.json` | Plugin manifest |
| 5 | `.repo-metadata.json` | Version and counts |

---

## Part A: Test Infrastructure

### A1: New Test Scripts
| File | Purpose |
|------|---------|
| `tests/test_plugin_structure.py` | Verify plugin packaging: plugin.json valid, all skills have SKILL.md, frontmatter correct, allowed-tools valid, no external filesystem refs |
| `tests/test_engagement_flow.py` | E2E lifecycle: verify engagement.json lifecycle_state transitions, prerequisite checks, flow ordering |
| `tests/test_skill_schemas.py` | Verify each SKILL.md Section 5 field list matches its schema required/properties |

### A2: /qa Skill
Create `skills/qa/SKILL.md` that runs all validation:
1. `python tests/validate_knowledge_base.py`
2. `python tests/validate_consistency.py`
3. `python tests/test_plugin_structure.py`
4. `python tests/test_engagement_flow.py`
5. `python tests/test_skill_schemas.py`
6. Report aggregate results

---

## Part B: Second Case Study — Greenfield AI Project

### B1: Case Study Selection
Use a greenfield AI/ML project (e.g., enterprise knowledge management with RAG, or customer support AI assistant) to test the greenfield engagement flow:
`/requirements` → `/architecture` → `/data-model` → `/security-review` → `/estimate` → `/project-plan` → `/proposal` → `/review`

### B2: Validation
Same validation as Phase 7 Part B:
- All KB files pass schema validation
- All consistency checks pass
- All review scores >= 7.5
- AI-specific schema fields exercised (tech_stack.llm, vector_schemas, ai_ml_components, ai_security_controls)

### B3: Genericity Confirmation
Compare case study 1 (healthcare IBMi) and case study 2 (AI greenfield) to confirm:
- No case-study-specific code in skills or schemas
- Both engagement flows work correctly
- Schema flexibility is sufficient without being too loose

---

## Part C: Final QA Checklist

- [ ] Run `python tests/validate_knowledge_base.py` — all schemas valid
- [ ] Run `python tests/validate_consistency.py` — cross-file references correct
- [ ] Run all new test scripts — PASS
- [ ] Verify no secrets, credentials, PII, or external filesystem references
- [ ] Verify `.gitignore` covers sensitive paths
- [ ] Verify `.repo-metadata.json` counts match actual
- [ ] Verify all SKILL.md files under 500 lines, CLAUDE.md under 200 lines
- [ ] Verify no `context: fork`, no `$ARGUMENTS.0`, no `Task` tool
- [ ] Local plugin install: `claude --plugin-dir .` works
- [ ] All 9 skills invocable and produce correct output

---

## Part D: Self-Review (Dogfooding)

Run `/review` targeting the agent's own documentation:
- Review `ARCHITECTURE.md` for accuracy against actual implementation
- Verify skill descriptions match actual behavior
- Check KB documentation matches actual schema

---

## Part E: License and Legal

- [ ] MIT LICENSE file present with correct copyright (Modular Earth LLC)
- [ ] SECURITY.md present with responsible disclosure policy
- [ ] No third-party code included without compatible license

---

## Part F: Release Preparation

- [ ] Update `.repo-metadata.json` version to `1.0.0`
- [ ] Update `.claude-plugin/plugin.json` version to `1.0.0`
- [ ] Create release notes summarizing: 9 skills, 2 sub-agents, 5 engagement flows, WA compliance, 2 case studies validated

---

## Part G: Release (REQUIRES HUMAN APPROVAL)

**Do NOT execute without explicit human approval.**

1. Create GitHub release tag: `git tag v1.0.0`
2. Push: `git push origin main --tags`
3. Test install from GitHub: `claude plugin install github:Modular-Earth-LLC/solutions-architecture-agent`
4. Submit to Claude Code marketplace (if available)

---

## Part H: Future Agent Interface

Document what outputs this agent produces that the future AI Engineering Agent will consume:
- Write to `.claude/plans/engineering-agent-interface.md`
- Map each KB file to engineering agent consumption patterns
- Define the handoff contract

---

## Verification

- [ ] All QA checks pass (automated)
- [ ] Second case study validates genericity
- [ ] Self-review score >= 8.0
- [ ] GitHub release tag created
- [ ] Plugin installable from GitHub URL
- [ ] Engineering agent interface documented

---

## Execution Command

```bash
claude -p "$(cat .claude/plans/phase-9-plan.md)"
```
