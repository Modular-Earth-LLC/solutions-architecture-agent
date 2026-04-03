# Knowledge Base

Centralized JSON storage for the Solutions Architecture Agent. Each skill owns one file and writes only to it. Skills communicate through KB files (blackboard pattern), never directly.

## File Topology (10 files)

```
system_config.json          READ-ONLY (human-managed)
       │
       v
engagement.json             Envelope — all skills create/update
       │
       v
requirements.json           /requirements writes
       │
       ├──> architecture.json         /architecture writes
       │         │
       │         ├──> data_model.json        /data-model writes
       │         ├──> security_review.json   /security-review writes
       │         ├──> integration_plan.json  /integration-plan writes
       │         ├──> estimate.json          /estimate writes
       │         │         │
       │         │         v
       │         └──> project_plan.json      /project-plan writes

reviews.json                /review writes (dynamic $depends_on — targets any file)
```

> **Note**: `/proposal` reads from KB files but writes to `outputs/`, not a KB file.

## Ownership

| File | Owner Skill | $depends_on | Size Target |
|------|------------|-------------|-------------|
| `system_config.json` | Human (READ-ONLY) | — | Unchanged |
| `engagement.json` | Any skill (creates), all (update) | `system_config.json` | < 100 lines |
| `requirements.json` | `/requirements` | `system_config.json` | < 400 lines |
| `architecture.json` | `/architecture` | `requirements.json` | < 500 lines |
| `data_model.json` | `/data-model` | `requirements.json`, `architecture.json` | < 400 lines |
| `security_review.json` | `/security-review` | `requirements.json`, `architecture.json` | < 300 lines |
| `integration_plan.json` | `/integration-plan` | `requirements.json`, `architecture.json` | < 300 lines |
| `estimate.json` | `/estimate` | `requirements.json`, `architecture.json` | < 300 lines |
| `project_plan.json` | `/project-plan` | `requirements.json`, `architecture.json`, `estimate.json` | < 300 lines |
| `reviews.json` | `/review` | Dynamic (targets any file) | Grows over time |

## Status Lifecycle

```
not_started → draft → in_progress → complete → approved
```

- **Domain files** (requirements, architecture, etc.) use a 4-value enum: `draft | in_progress | complete | approved`
- **engagement.json lifecycle_state** uses a 5-value enum (adds `not_started`)
- **engagement.json status** has a broader 7-value enum for overall engagement state

## ID Patterns

| Entity | Pattern | Example |
|--------|---------|---------|
| Engagement | `eng-YYYY-NNN` | `eng-2026-001` |
| Success Criteria | `SC-NNN` | `SC-001` |
| Functional Requirement | `FR-NNN` | `FR-001` |
| Component | `C-NNN` | `C-001` |
| Data Flow | `DF-NNN` | `DF-001` |
| Entity | `E-NNN` | `E-001` |
| Threat | `T-NNN` | `T-001` |
| Finding | `F-NNN` | `F-001` |
| API Contract | `API-NNN` | `API-001` |
| Data Flow Mapping | `DFM-NNN` | `DFM-001` |
| Phase | `P-NNN` | `P-001` |
| Milestone | `M-NNN` | `M-001` |
| Review | `R-NNN` | `R-001` |
| Review Finding | `RF-NNN` | `RF-001` |

## Versioning

All domain files use `MAJOR.MINOR` versioning (e.g., `"1.2"`). Major increments on structural changes; minor on content updates. `engagement.json` tracks which version of each domain file is current.

## Schemas

All schemas are in `knowledge_base/schemas/` using JSON Schema Draft 2020-12. Each domain file references its schema via `$schema`.

| Schema File | Validates |
|-------------|-----------|
| `engagement.schema.json` | `engagement.json` |
| `requirements.schema.json` | `requirements.json` |
| `architecture.schema.json` | `architecture.json` |
| `data_model.schema.json` | `data_model.json` |
| `security_review.schema.json` | `security_review.json` |
| `integration_plan.schema.json` | `integration_plan.json` |
| `estimate.schema.json` | `estimate.json` |
| `project_plan.schema.json` | `project_plan.json` |
| `reviews.schema.json` | `reviews.json` |
| `system_config.schema.json` | `system_config.json` |
| `.repo-metadata.schema.json` | `.repo-metadata.json` |

## Validation

```bash
# Validate all KB files against schemas
python tests/validate_knowledge_base.py

# Validate a single file
python tests/validate_knowledge_base.py --file system_config

# Cross-file consistency checks
python tests/validate_consistency.py
```

Requires: `uv sync`

## PII Protection

KB files may contain client names, contacts, and rates. `.gitignore` covers `knowledge_base/*.json` except `system_config.json`. Never commit client data to public repositories.

## Rules

- Validate all JSON against schemas in `knowledge_base/schemas/`
- Increment version on every write (minor for content, major for structure)
- Enforce `$depends_on` — a skill must never read from KB files not listed in its dependency chain
- `system_config.json` is READ-ONLY — never modify at runtime
- Include `_metadata` block on every write: `author`, `date`, `validation_status`
- Run `python tests/validate_knowledge_base.py` after modifying any knowledge base file
