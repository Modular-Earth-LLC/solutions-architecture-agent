# Contributing to the Solutions Architecture Agent

Thank you for your interest in contributing. This guide focuses on the most common contribution: **adding a new skill**.

---

## Prerequisites

- **Claude Code CLI** — primary development and testing tool
- **Git** — version control
- **Python 3.10+** — for running validation scripts (`pip install jsonschema`)
- Familiarity with the [ARCHITECTURE.md](ARCHITECTURE.md) design

---

## How to Add a New Skill

This is the step-by-step guide for adding a 10th (or Nth) skill to the plugin.

### Step 1: Create the SKILL.md

Create `skills/<skill-name>/SKILL.md`. Every SKILL.md follows this structure:

```markdown
---
name: <skill-name>
description: One-line description shown in skill discovery
---

# Section 1: Agent Identity
- Role, domain expertise, behavioral constraints

# Section 2: Workflow
- Step-by-step execution procedure
- When to use WebSearch vs training knowledge
- Human checkpoint instructions

# Section 3: Quality Criteria
- Minimum quality bar for outputs
- Review dimensions and thresholds

# Section 4: Context Loading
- `$depends_on`: list of upstream KB files this skill reads
- Which KB files to load and which sections to use

# Section 5: Output Rules
- JSON structure specification
- Field-by-field output format
- MUST include envelope fields paragraph (see below)

# Section 6: Error Handling
- What to do when upstream data is missing
- How to handle ambiguous requirements
```

### Step 2: Envelope Fields (Required)

Every SKILL.md Section 5 (Output Rules) **must** include a paragraph specifying these envelope fields that wrap every KB output:

```
Every output file MUST include these envelope fields:
- "$schema": relative path to the schema file
- "$depends_on": array of upstream KB file names this output depends on
- "engagement_id": from engagement.json (e.g., "eng-2026-001")
- "version": MAJOR.MINOR version string
- "created_at" / "updated_at": ISO 8601 timestamps
- "status": one of "draft", "in_progress", "complete", "approved"
```

Without these envelope fields, `validate_knowledge_base.py` and `validate_consistency.py` will fail.

### Step 3: Create the JSON Schema

Create `knowledge_base/schemas/<skill_name>.schema.json`:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "<skill_name>.schema.json",
  "title": "<Skill Name> Output",
  "type": "object",
  "required": ["$schema", "$depends_on", "engagement_id", "version", "status"],
  "properties": {
    "$schema": { "type": "string" },
    "$depends_on": { "type": "array", "items": { "type": "string" } },
    "engagement_id": { "type": "string", "pattern": "^eng-" },
    "version": { "type": "string" },
    "status": { "type": "string", "enum": ["draft", "in_progress", "complete", "approved"] }
  }
}
```

**Schema alignment rule**: Every field name in the SKILL.md Section 5 output specification must exactly match a property in the schema. Mismatches between SKILL.md and schema are the most common issue class found during testing.

Refer to `knowledge_base/schemas/SCHEMA_DESIGN.md` for the full design guide and conventions.

### Step 4: Register in CLAUDE.md

Add your skill to the skill table in `CLAUDE.md`:

```markdown
| Your Skill Name | `/your-skill` | Brief purpose | `your_skill.json` |
```

If the skill participates in engagement flows, add it to the canonical flows table.

### Step 5: Update Agent Identity

If the skill invokes sub-agents, create `agents/<sub-agent-name>.md` following the pattern in `agents/parallel-wa-reviewer.md`.

### Step 6: Update Metadata

In `.repo-metadata.json`:
- Increment `architecture.skills` count
- Add skill name to `architecture.skill_names` array
- Increment `knowledge_base.schemas` if you added a schema
- Update `knowledge_base.files` if you added a KB file

### Step 7: Validate

```bash
# Schema validation — your new schema should appear
python tests/validate_knowledge_base.py

# Consistency — skill count, schema count, $depends_on chains
python tests/validate_consistency.py
```

Both must pass with 0 FAIL before submitting a PR.

---

## How to Add a Sub-Agent

Sub-agents are for **parallel execution only** — scoring or analysis that benefits from running multiple instances concurrently via the Agent tool.

1. Create `agents/<sub-agent-name>.md` with a focused prompt
2. Add the agent name to `.repo-metadata.json` → `architecture.sub_agent_names`
3. Increment `architecture.sub_agents` count
4. Reference the sub-agent from the parent SKILL.md workflow section

Sub-agents receive a focused prompt + relevant KB context and return structured JSON. They do not maintain state or invoke other skills.

---

## Knowledge Base Rules

- Each skill **owns exactly one** KB file and writes only to it
- `system_config.json` is **read-only** — never modify it
- `engagement.json` is the **lifecycle tracker** — skills update their domain's status there
- Files declare dependencies via `$depends_on` — used for prerequisite validation
- All KB files must validate against their schema in `knowledge_base/schemas/`
- Version KB files with MAJOR.MINOR — increment MINOR for additive changes, MAJOR for breaking changes

---

## Schema Alignment Rules

These rules prevent the most common issue class found during Phase 7 testing:

1. **Field names must match exactly** between SKILL.md Section 5 and the JSON schema `properties`
2. **Required fields in schema** must appear in SKILL.md output specification
3. **Enum values in schema** must match the exact values listed in SKILL.md
4. **Nested object structures** in SKILL.md must mirror the schema's `properties` hierarchy
5. **Array item schemas** must match the structure described in SKILL.md

When in doubt, write the schema first, then write the SKILL.md output rules to match it.

---

## Testing

### Automated Validation

```bash
# Validate all KB files against schemas
python tests/validate_knowledge_base.py

# Check metadata consistency, $depends_on chains, ID uniqueness
python tests/validate_consistency.py
```

### Manual Skill Testing

1. Install plugin: `claude --plugin-dir .`
2. Invoke your skill via slash command or natural language
3. Verify the output file validates: `python tests/validate_knowledge_base.py --file <your_file>`
4. Check `engagement.json` was updated with correct lifecycle_state

### What to Test

- Skill produces valid JSON matching its schema
- Envelope fields are present and correct
- `$depends_on` chain is accurate
- Upstream prerequisite checking works (try invoking without prerequisites)
- Human checkpoint fires at end of skill execution

---

## Pull Request Process

### Branch Strategy

```bash
git checkout main && git pull
git checkout -b feature/<skill-name>
# ... make changes ...
git push -u origin feature/<skill-name>
```

### PR Checklist

- [ ] SKILL.md follows the 6-section structure
- [ ] Schema created and validates
- [ ] Envelope fields paragraph in Section 5
- [ ] CLAUDE.md skill table updated
- [ ] `.repo-metadata.json` counts updated
- [ ] `python tests/validate_knowledge_base.py` — 0 FAIL
- [ ] `python tests/validate_consistency.py` — 0 FAIL
- [ ] No secrets or credentials committed
- [ ] Documentation updated if adding to engagement flows

### Conventional Commits

```bash
feat(skills): add <skill-name> skill for <purpose>
fix(knowledge-base): correct <file> schema validation
docs(contributing): update skill creation guide
```

---

## Code of Conduct

We are committed to providing a welcoming and inclusive environment for all contributors. Be respectful, constructive, and focused on what is best for the project. See the full [Contributor Covenant](https://www.contributor-covenant.org/) for details.

---

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
