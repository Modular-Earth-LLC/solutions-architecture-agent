# Testing Framework

Automated validation for the AI Solutions Architecture Agent plugin.

---

## Validation Scripts

### Knowledge Base Validation

```bash
python tests/validate_knowledge_base.py
```

Validates all KB JSON files against their schemas in `knowledge_base/schemas/`:

- JSON syntax correctness
- Schema compliance (structure, types, required fields)
- Envelope fields (`$schema`, `$depends_on`, `engagement_id`, `version`, `status`)
- Enum value validity

**Files validated**: `.repo-metadata.json`, `system_config.json`, `engagement.json`, and all 8 domain KB files (when present).

**Expected output** (clean state): `2 PASS, 0 FAIL, 9 SKIP` (only `.repo-metadata` and `system_config` exist without an active engagement).

### Consistency Validation

```bash
python tests/validate_consistency.py
```

Checks cross-file consistency:

1. **Metadata sync** — skill/sub-agent counts in `.repo-metadata.json` match actual `skills/` and `agents/` directories
2. **Schema completeness** — every KB file has a corresponding schema
3. **`$depends_on` chains** — DAG integrity, no missing dependencies
4. **Engagement ID consistency** — all KB files share the same `engagement_id`
5. **ID uniqueness** — no duplicate IDs across KB files

**Expected output** (clean state): `5 PASS, 0 FAIL`

---

## Running Tests

### Before Committing

```bash
# Always run both
python tests/validate_knowledge_base.py
python tests/validate_consistency.py
```

### After Skill Changes

1. Run both validation scripts
2. Install plugin: `claude --plugin-dir .`
3. Invoke the changed skill and verify output validates
4. Check `engagement.json` was updated correctly

### Pre-Release

1. Run both validation scripts — 0 FAIL
2. Verify plugin loads: `claude --plugin-dir .`
3. Test at least 2 skills end-to-end
4. Check all documentation links resolve

---

## Test Environment

### Setup

```bash
pip install jsonschema
```

Run all tests from the project root directory.

### Troubleshooting

| Error | Fix |
|-------|-----|
| `jsonschema library not installed` | `pip install jsonschema` |
| `Path not found` | Run from project root |
| Schema validation fails | Check JSON syntax, review error message for specific field |

---

## CI/CD

**GitHub Actions workflow**: `.github/workflows/validate-knowledge-base.yml`

Currently manual-trigger only. To enable on push/PR:
1. Edit the workflow file
2. Uncomment the `on: push/pull_request` triggers
3. Commit and push

---

## Adding New Tests

1. Create `tests/test_<feature>.py`
2. Use clear naming and include a docstring
3. Add to GitHub Actions workflow if appropriate
4. Document in this README

See [CONTRIBUTING.md](../CONTRIBUTING.md) for the full testing guide.
