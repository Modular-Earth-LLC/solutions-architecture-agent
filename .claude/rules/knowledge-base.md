---
paths:
  - "knowledge_base/**"
---

# Knowledge Base Rules

- Validate all JSON against schemas in `knowledge_base/schemas/`
- Increment version on every write: minor for content updates, major for structural changes (MAJOR.MINOR format)
- Enforce `$depends_on` — a skill must never read from KB files not listed in its dependency chain
- `system_config.json` is READ-ONLY — never modify at runtime
- Each skill owns exactly one KB file and writes only to it:
  - /requirements → requirements.json
  - /architecture → architecture.json
  - /data-model → data_model.json
  - /security-review → security_review.json
  - /integration-plan → integration_plan.json
  - /estimate → estimate.json
  - /project-plan → project_plan.json
  - /review → reviews.json
  - All skills → engagement.json (create/update lifecycle_state)
- Include `_metadata` block on every write: author, date, validation_status
- Status transitions follow: `not_started → draft → in_progress → complete → approved`
- ID patterns: `PREFIX-NNN` (zero-padded). Engagement IDs: `eng-YYYY-NNN`
- Version strings: `MAJOR.MINOR` (e.g., `"1.2"`)
- PII protection: `.gitignore` covers `knowledge_base/*.json` except `system_config.json` — KB files may contain client names, contacts, and rates
- Run `python tests/validate_knowledge_base.py` after modifying any knowledge base file
