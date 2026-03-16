# Testing Framework

Automated validation for the AI Solutions Architecture Agent plugin.

---

## Validation Scripts (5 Total)

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

### Plugin Structure Validation

```bash
python tests/test_plugin_structure.py
```

Validates plugin packaging:

- `plugin.json` exists, valid JSON, required fields, version matches `.repo-metadata.json`
- Every `skills/*/SKILL.md` has YAML frontmatter (`name`, `description`, `allowed-tools`)
- Agent files have required frontmatter (`name`, `description`, `tools`, `model`, `maxTurns`)
- Required directories exist
- No forbidden patterns (`context: fork`, `$ARGUMENTS.0` dot syntax, `Task` in allowed-tools)
- No SKILL.md exceeds 500 lines
- `.repo-metadata.json` `skill_names`/`sub_agent_names` match filesystem

**Expected output**: `7 PASS, 0 FAIL`

### Engagement Flow Validation

```bash
python tests/test_engagement_flow.py
```

Validates engagement lifecycle logic:

- Canonical flow DAG validity (5 flows, predecessors appear earlier)
- `engagement.schema.json` lifecycle_state covers all domain KB files
- Status enum consistency between schema and SKILL.md references
- ARCHITECTURE.md KB ownership table matches authoritative DEPENDS_ON_DAG
- Skills with `$depends_on` have prerequisite-checking language

**Expected output**: `5 PASS, 0 FAIL`

### Skill Independence Validation

```bash
python tests/test_skill_independence.py
```

Validates each skill can run independently (marketplace requirement):

- No SKILL.md references another SKILL.md by path
- Every STOP directive also provides an alternative path (`$ARGUMENTS`)
- Each SKILL.md contains its own role, workflow, and output sections
- No SKILL.md hardcodes repo name or local filesystem paths
- `allowed-tools` is a specific list, not "all"
- Each SKILL.md documents `$ARGUMENTS` for standalone invocation

**Expected output**: `6 PASS, 0 FAIL`

---

## Running Tests

### Before Committing

```bash
python tests/validate_knowledge_base.py
python tests/validate_consistency.py
python tests/test_plugin_structure.py
python tests/test_engagement_flow.py
python tests/test_skill_independence.py
```

### After Skill Changes

See [CONTRIBUTING.md § Manual Skill Testing](../CONTRIBUTING.md#manual-skill-testing) for the complete testing workflow after modifying skills.

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

GitHub Actions runs all 5 validation scripts on PRs. See `.github/workflows/validate-knowledge-base.yml` and [CONTRIBUTING.md § CI/CD](../CONTRIBUTING.md#cicd).

---

## Adding New Tests

1. Create `tests/test_<feature>.py` following existing output conventions (PASS/FAIL summary, `sys.exit(1)` on failure)
2. Add to `.github/workflows/validate-knowledge-base.yml` as a named step
3. Document in this README

See [CONTRIBUTING.md](../CONTRIBUTING.md) for the full contributing guide.
