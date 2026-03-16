# Phase 6: Knowledge Base Schemas and Templates — Execution Plan

> Created: 2026-03-15 | Prerequisites: Phase 5 complete (commit TBD)
> Authoritative schema source: `knowledge_base/schemas/SCHEMA_DESIGN.md`

---

## Context

Phase 5 implemented 9 skills, 2 sub-agents, CLAUDE.md, rules, and hooks. The skills reference KB files by normalized names and define exact output fields in their Section 5 (OUTPUT SPECIFICATION). Phase 6 creates the JSON schemas and templates that validate and support those outputs.

**Critical alignment**: Each skill's Section 5 defines the fields it writes. Schemas must support ALL those fields. Cross-reference against SCHEMA_DESIGN.md for full field definitions.

---

## Inputs — Read in This Order

| # | File | What to Read | Purpose |
|---|------|-------------|---------|
| 1 | `knowledge_base/schemas/SCHEMA_DESIGN.md` | Full file | Authoritative schema spec — field names, types, cross-references, shared conventions |
| 2 | `.claude/plans/technical-design.md` | Section 4 (KB Schema Specifications) | I/O contract verification, file inventory, shared conventions |
| 3 | `.claude/plans/phase-5-results.md` | Post-Phase 5 state, verification results | Current file inventory, what exists |
| 4 | `skills/*/SKILL.md` | Section 5 (OUTPUT SPECIFICATION) of each skill | Exact fields each skill writes — schemas must support all of them |
| 5 | `.claude/plans/workflow-design.md` | Section 3 (I/O contracts), Section 4 (KB state flow) | Data flow, version control, status transitions |

**Do NOT read** master-plan.md — it contains superseded KB file names (security_assessment.json, integration_map.json, estimates.json). Use normalized names from technical-design.md.

---

## Normalized KB File Names (from Phase 5)

| Skill | KB File | Old name (master-plan) |
|-------|---------|----------------------|
| /requirements | requirements.json | (same) |
| /architecture | architecture.json | (same) |
| /data-model | data_model.json | (same) |
| /security-review | security_review.json | ~~security_assessment.json~~ |
| /integration-plan | integration_plan.json | ~~integration_map.json~~ |
| /estimate | estimate.json | ~~estimates.json~~ |
| /project-plan | project_plan.json | (same) |
| /review | reviews.json | (same) |
| (all skills) | engagement.json | (same) |
| (read-only) | system_config.json | (same) |

---

## Files to Create/Update

### JSON Schema Files (11 total, in `knowledge_base/schemas/`)

| # | File | Schema For | Source |
|---|------|-----------|--------|
| 1 | `engagement.schema.json` | engagement.json | SCHEMA_DESIGN.md + workflow-design.md Section 4 |
| 2 | `requirements.schema.json` | requirements.json | SCHEMA_DESIGN.md + skills/requirements/SKILL.md Section 5 |
| 3 | `architecture.schema.json` | architecture.json | SCHEMA_DESIGN.md + skills/architecture/SKILL.md Section 5 |
| 4 | `data_model.schema.json` | data_model.json | SCHEMA_DESIGN.md + skills/data-model/SKILL.md Section 5 |
| 5 | `security_review.schema.json` | security_review.json | SCHEMA_DESIGN.md + skills/security-review/SKILL.md Section 5 |
| 6 | `integration_plan.schema.json` | integration_plan.json | SCHEMA_DESIGN.md + skills/integration-plan/SKILL.md Section 5 |
| 7 | `estimate.schema.json` | estimate.json | SCHEMA_DESIGN.md + skills/estimate/SKILL.md Section 5 |
| 8 | `project_plan.schema.json` | project_plan.json | SCHEMA_DESIGN.md + skills/project-plan/SKILL.md Section 5 |
| 9 | `reviews.schema.json` | reviews.json | SCHEMA_DESIGN.md + skills/review/SKILL.md Section 5 |
| 10 | `system_config.schema.json` | system_config.json | SCHEMA_DESIGN.md |
| 11 | `.repo-metadata.schema.json` | .repo-metadata.json | SCHEMA_DESIGN.md |

### Sample/Seed KB Files (2)

| # | File | Purpose |
|---|------|---------|
| 12 | `knowledge_base/system_config.json` | UPDATE — align with schema, add any missing fields |
| 13 | `knowledge_base/README.md` | UPDATE — document KB topology, file ownership, usage guide |

### Templates (3)

| # | File | Purpose |
|---|------|---------|
| 14 | `templates/requirements-template.md` | Template for requirements discovery output |
| 15 | `templates/architecture-template.md` | Template for architecture documentation |
| 16 | `templates/security-checklist.md` | Security review checklist template |

### Tests (2)

| # | File | Purpose |
|---|------|---------|
| 17 | `tests/validate_knowledge_base.py` | REWRITE — validate all KB files against new schemas |
| 18 | `tests/validate_consistency.py` | REWRITE — cross-file consistency checks |

---

## Key Constraints

- Every schema must include `$depends_on` array and `_metadata` block
- `_metadata` required fields: `author`, `date`, `validation_status`, `version`
- Status enum: `not_started`, `draft`, `in_progress`, `complete`, `approved`
- ID patterns: `PREFIX-NNN` (zero-padded), engagement: `eng-YYYY-NNN`
- Version format: `MAJOR.MINOR` string
- Schema IDs use: `https://github.com/Modular-Earth-LLC/solutions-architecture-agent/schemas/`
- Use `additionalProperties: true` where extensibility is needed (NFR-021)
- system_config.json is READ-ONLY — schema should document this

## Verification

- [ ] All 11 schemas validate as valid JSON Schema (draft-07 or 2020-12)
- [ ] Each schema's required fields match the corresponding skill's Section 5 output
- [ ] `$depends_on` arrays match workflow-design.md Section 3.1
- [ ] `python tests/validate_knowledge_base.py` passes with system_config.json
- [ ] KB README documents all 10 files with ownership and dependencies
- [ ] Templates align with skill output formats
- [ ] No external filesystem references

---

## Execution Command

```bash
claude -p "$(cat .claude/plans/phase-6-prompt.md)"
```
