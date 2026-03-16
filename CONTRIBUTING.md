# Contributing

This is the single source of truth for contributing to the Solutions Architecture Agent. Both human engineers and AI coding assistants (Claude Code, GitHub Copilot) should follow these conventions.

---

## Prerequisites

- **Claude Code CLI** — [install guide](https://docs.anthropic.com/en/docs/claude-code/overview)
- **Git** — version control
- **Python 3.10+** — for validation scripts (`pip install jsonschema`)
- Familiarity with the [ARCHITECTURE.md](ARCHITECTURE.md) design

---

## Project Structure

```
solutions-architecture-agent/
├── .claude-plugin/plugin.json    # Plugin manifest (name, version, description)
├── skills/                       # SA lifecycle skills (each: <name>/SKILL.md)
├── agents/                       # Sub-agents for parallel execution
├── hooks/hooks.json              # Pre-commit validation hooks
├── knowledge_base/               # Blackboard KB (JSON files + schemas)
│   ├── schemas/                  # JSON Schema Draft 2020-12 definitions
│   └── system_config.json        # READ-ONLY reference configuration
├── tests/                        # Validation scripts (stdlib + jsonschema)
├── docs/                         # User documentation
├── .claude/rules/                # Governing rules (loaded automatically)
├── CLAUDE.md                     # Agent identity and dispatch rules (<100 lines)
├── ARCHITECTURE.md               # System design with Mermaid diagrams
├── DESIGN_RATIONALE.md           # Historical context and research citations
├── .repo-metadata.json           # Single source of truth for version/counts
└── .github/workflows/            # CI/CD (runs on PR, manual dispatch)
```

**Key files**:
- `.repo-metadata.json` — version, skill/agent counts, skill names. All other files reference this instead of hardcoding.
- `CLAUDE.md` — loaded first by Claude Code. Defines agent identity, skill table, engagement flows, dispatch rules.
- `.claude/rules/` — scoped rules automatically loaded. `guiding-principles.md` contains 42 technology principles governing all output.

---

## Development Conventions

### AI-First Development

The primary contributors to this repo are AI coding assistants. All conventions are:
- **Explicit** — no implicit assumptions; everything is declared in files
- **Programmatic** — machine-parseable structures (JSON schemas, YAML frontmatter)
- **Verifiable** — 8 automated test scripts validate structure and consistency
- **No commented-out code** — either active or deleted; never disabled-by-comment

### Single Source of Truth

| Data | Source | Rule |
|------|--------|------|
| Version, counts | `.repo-metadata.json` | Never hardcode in docs or skills |
| Agent behavior | `CLAUDE.md` + `.claude/rules/` | Loaded automatically by Claude Code |
| Skill behavior | `skills/*/SKILL.md` | Self-contained; no cross-skill imports |
| KB structure | `knowledge_base/schemas/` | Draft 2020-12 JSON Schema |
| Contributing guide | This file (`CONTRIBUTING.md`) | Other docs reference, not repeat |

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(skills): add <skill-name> skill for <purpose>
fix(knowledge-base): correct <file> schema validation
docs(contributing): update skill creation guide
test(qa): add plugin structure validation
```

---

## How to Add a New Skill

### Step 1: Create the SKILL.md

Create `skills/<skill-name>/SKILL.md` with YAML frontmatter and 6 sections:

```markdown
---
name: <skill-name>
description: "One-line description shown in skill discovery"
argument-hint: "[what arguments this skill accepts]"
allowed-tools: Read, Write, Edit, Glob, Grep, WebSearch, WebFetch
---

## 1. ROLE & CONTEXT
Role, domain expertise, behavioral constraints

## 2. PREREQUISITES
Upstream KB files to check. Use advisory language:
"If missing → suggest running /upstream-skill first, OR accept context directly via $ARGUMENTS"

## 3. CONTEXT LOADING
Which KB files and sections to read

## 4. WORKFLOW
Step-by-step execution procedure

## 5. OUTPUT RULES
JSON structure specification with envelope fields (see Step 2)

## 6. HUMAN CHECKPOINT
Summary, deliverables, next skill suggestion
```

For a complete canonical example, see [skills/requirements/SKILL.md](skills/requirements/SKILL.md).

**Rules**:
- Keep under 500 lines (enforced by `test_plugin_structure.py`); move reference tables to `${CLAUDE_SKILL_DIR}/` files
- No cross-skill imports at runtime — each skill is self-contained
- Use `ultrathink` directive (in body, not frontmatter) only for deep reasoning skills
- Use bracket syntax `$ARGUMENTS[0]` (not dot syntax `$ARGUMENTS.0`)
- Prerequisites must be advisory, not blocking — always offer `$ARGUMENTS` as alternative
- `allowed-tools` follows least privilege — only tools the skill needs

### Step 2: Envelope Fields (Required)

Every SKILL.md Section 5 **must** specify these envelope fields:

```
Every output file MUST include these envelope fields:
- "$schema": relative path to the schema file
- "$depends_on": array of upstream KB file names
- "engagement_id": from engagement.json (e.g., "eng-2026-001")
- "version": MAJOR.MINOR version string
- "status": one of "draft", "in_progress", "complete", "approved"
```

Without these, `validate_knowledge_base.py` and `validate_consistency.py` will fail.

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

Refer to `knowledge_base/schemas/SCHEMA_DESIGN.md` for the full design guide.

### Step 4: Register the Skill

Update these files (all required):

1. `CLAUDE.md` — add to skill table; add to engagement flows if applicable
2. `README.md` — add to the skills table
3. `.repo-metadata.json` — update:
   - Increment `architecture.skills`
   - Add to `architecture.skill_names`
   - Increment `knowledge_base.schemas`
   - Update `knowledge_base.files`

### Step 5: Validate

```bash
python tests/validate_knowledge_base.py    # Your schema should appear
python tests/validate_consistency.py       # Skill count, $depends_on chains
python tests/test_plugin_structure.py      # Frontmatter, naming, forbidden patterns
python tests/test_engagement_flow.py       # DAG validity if added to flows
python tests/test_skill_independence.py    # Advisory prereqs, $ARGUMENTS, no cross-imports
```

All must pass with 0 FAIL.

### Schema Alignment Rules

The most common issue class found during testing. Prevent it by following these rules:

1. **Field names must match exactly** between SKILL.md Section 5 and the JSON schema `properties`
2. **Required fields in schema** must appear in SKILL.md output specification
3. **Enum values in schema** must match the exact values listed in SKILL.md
4. **Nested object structures** in SKILL.md must mirror the schema's `properties` hierarchy
5. **Array item schemas** must match the structure described in SKILL.md

When in doubt, write the schema first, then write the SKILL.md output rules to match it.

---

## How to Add a Sub-Agent

Sub-agents are for **parallel execution only** — e.g., scoring 6 WA pillars or analyzing 6 STRIDE categories concurrently.

1. Create `agents/<sub-agent-name>.md` with YAML frontmatter:
   ```yaml
   ---
   name: <sub-agent-name>
   description: "One-line description"
   tools: Read, Glob, Grep, WebSearch, WebFetch
   model: sonnet
   maxTurns: 5
   ---
   ```
2. Update `.repo-metadata.json`: add to `sub_agent_names`, increment `sub_agents`
3. Reference the sub-agent from the parent SKILL.md workflow section

Sub-agents receive a focused prompt + relevant KB context and return structured output. They do not maintain state or invoke other skills.

---

## Knowledge Base Rules

- Each skill **owns exactly one** KB file and writes only to it
- `system_config.json` is **read-only** — never modify it
- `engagement.json` is the **lifecycle tracker** — skills update their domain's status
- Files declare dependencies via `$depends_on` — used for prerequisite validation
- All KB files validate against their schema in `knowledge_base/schemas/`
- Version with MAJOR.MINOR — increment MINOR for additive, MAJOR for breaking changes
- `knowledge_base/*.json` (except `system_config.json`) are gitignored — they contain engagement data

---

## Testing

### Automated Validation

All test scripts, runnable from the project root:

```bash
# Core validation (7 scripts — run before every commit)
python tests/validate_knowledge_base.py    # Schema compliance (Draft 2020-12)
python tests/validate_consistency.py       # Metadata sync, DAG integrity, ID uniqueness
python tests/test_plugin_structure.py      # Plugin packaging, frontmatter, section anchors
python tests/test_engagement_flow.py       # Canonical flow DAG, lifecycle coverage
python tests/test_skill_independence.py    # Advisory prereqs, standalone invocation
python tests/validate_well_architected.py  # Multi-cloud WA pillar coverage
python tests/test_end_to_end_example.py    # Example engagement schema + integration

# Optional (requires `pip install requests`)
python tests/validate_urls.py              # External link health check
```

See [tests/README.md](tests/README.md) for expected output, troubleshooting, and test environment setup.

### Manual Skill Testing

1. Install plugin: `claude --plugin-dir .`
2. Invoke your skill via slash command
3. Verify output validates: `python tests/validate_knowledge_base.py --file <name>`
4. Check `engagement.json` was updated with correct lifecycle_state

### CI/CD

GitHub Actions runs all test scripts on PRs touching skills, schemas, agents, plugin config, or tests. See `.github/workflows/validate-knowledge-base.yml`. Trigger manually via `workflow_dispatch`.

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

- [ ] SKILL.md follows the 6-section structure with advisory prerequisites
- [ ] Schema created and validates (Draft 2020-12)
- [ ] Envelope fields paragraph in Section 5
- [ ] CLAUDE.md skill table updated
- [ ] `.repo-metadata.json` counts updated
- [ ] All test scripts pass with 0 FAIL
- [ ] No secrets, credentials, or PII committed
- [ ] Documentation updated if adding to engagement flows

---

## Code of Conduct

We are committed to providing a welcoming and inclusive environment. Be respectful, constructive, and focused on what is best for the project. See our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
