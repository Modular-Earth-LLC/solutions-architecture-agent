# Phase 7: Integration Testing — Execution Plan

> Created: 2026-03-15 | Prerequisites: Phase 6 complete
> Test scenarios from: requirements.md Section 7, master-plan.md Phase 7

---

## Context

Phase 5 implemented 9 skills with defined I/O contracts. Phase 6 will have created JSON schemas and templates. Phase 7 validates end-to-end that skills work as designed — invoking skills in sequence, verifying KB read/write contracts, testing prerequisite validation, and scoring output quality.

---

## Inputs

| # | File | Purpose |
|---|------|---------|
| 1 | `.claude/plans/phase-5-results.md` | Skill inventory, verification results |
| 2 | `.claude/plans/requirements.md` Section 7 | User stories and test scenarios |
| 3 | `.claude/plans/workflow-design.md` | Canonical flows and error handling |
| 4 | `skills/*/SKILL.md` | All 9 skills (invoke and test) |
| 5 | `knowledge_base/schemas/*.schema.json` | Validation schemas (Phase 6 output) |

---

## Test Scenarios (5)

### Scenario 1: Healthcare Platform (Full Greenfield)
**Flow**: req → arch → dm → sr → est → ppl → pro → rv
**Persona**: Priya (enterprise)
**Context**: Clinical data platform startup, HIPAA compliance, RAG-powered support agent
**Compare against**: Hyperbloom/AGADA architecture and project plan exemplars
**Tests**: All 9 skills, full lifecycle

### Scenario 2: Cloud Migration Assessment
**Flow**: req → ip → arch → dm → sr → est → ppl → pro → rv
**Persona**: Priya (enterprise)
**Context**: Legacy on-prem to cloud migration, multiple integrations, parallel run
**Tests**: Integration-plan before architecture (migration flow), migration-specific content in all skills

### Scenario 3: GenAI Agent Platform (Streamlined)
**Flow**: req → arch → est → pro
**Persona**: Marcus (independent)
**Context**: AI agent platform for customer service, startup client, budget-conscious
**Compare against**: Revelex/Hyperbloom proposal exemplar
**Tests**: Streamlined flow, T-shirt estimation, discovery proposal

### Scenario 4: Discovery-Only Assessment
**Flow**: req → arch → [sr] → pro
**Persona**: Marcus (independent)
**Context**: Pre-commitment assessment, $5K-$25K range
**Tests**: Optional skill skip, discovery proposal format

### Scenario 5: Quick Pipeline Qualification
**Flow**: req (quick tier only)
**Persona**: Aisha (founder)
**Context**: Multiple prospects needing quick BANT qualification
**Tests**: Quick tier selection, AI suitability scoring, partial requirements

---

## Validation Checks Per Skill

For each skill invocation:
1. Prerequisites validated correctly (block/warn/proceed)
2. KB files read match declared `$depends_on`
3. Output JSON validates against schema
4. `engagement.json` lifecycle_state updated correctly
5. Version incremented
6. Human checkpoint presented with correct next-step recommendation

## Quality Scoring

Run `/review` on key deliverables:
- Target: overall score >= 7.5 on all reviewed deliverables
- Score dimensions: Completeness, Technical Soundness, WA Alignment, Clarity, Feasibility
- 3 iterations per review (early stop at 9.0+)

## Error Handling Tests

- Invoke /architecture without requirements.json → expect STOP message
- Invoke /estimate with draft architecture → expect WARN message
- Invoke /proposal without all required files → expect guidance on missing skills
- Provide implementation request → expect scope boundary response

---

## Deliverables

- `.claude/plans/phase-7-results.md` — Test results matrix, quality scores, issues found and fixed
- Any skill fixes applied during testing

## Verification

- [ ] All 9 skills tested at least once
- [ ] All 5 canonical flows tested
- [ ] All 3 personas represented
- [ ] Error handling verified (missing prerequisites, scope violations)
- [ ] /review scores >= 7.5 on all reviewed deliverables
- [ ] Sub-agents (parallel-wa-reviewer, stride-analyzer) tested via /architecture and /security-review
- [ ] No external filesystem references in any output

---

## Execution Command

```bash
claude -p "$(cat .claude/plans/phase-7-prompt.md)"
```
