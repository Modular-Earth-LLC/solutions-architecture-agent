# Phase 3 Execution Plan: System Architecture & Technical Design

## Context

Phase 2 is complete (committed to main). It produced:
- `requirements.md` (792 lines): 106 functional requirements, 22 non-functional, 13 cross-cutting, 3 personas, 36 user stories, 5 test scenarios, full traceability matrix
- `workflow-design.md` (648 lines): 4 user journey maps, skill I/O contracts, KB state flow, multi-session support, error handling, SOW template, estimation model, dispatch architecture

Phase 3 transforms those requirements and workflow specifications into a concrete technical design — the blueprint that Phase 4 (cleanup), Phase 5 (skill implementation), and Phase 6 (KB schemas) will execute against.

**Why this matters**: Without a technical design, Phase 5 would need to make hundreds of micro-decisions about frontmatter fields, tool permissions, context loading, and rules structure. This phase makes those decisions once, consistently, and subjects them to human review before implementation begins.

**Open gaps from Phase 1 that Phase 3 must close**:
- Multi-session state management → codify the persistence model from workflow-design.md Section 5
- Error recovery → codify checkpoint/resume patterns from workflow-design.md Section 6
- Context budget allocation → define token budgets per tier from workflow-design.md Section 10.2

## Approach: Single Agent with Web Research

A single agent produces the technical-design.md document. Before writing, it performs web research to verify the latest:
1. Claude Code plugin documentation (plugin.json schema, skill discovery, namespacing)
2. Agent Skills open standard (SKILL.md frontmatter format, conventions)
3. Claude Code sub-agent configuration (`context: fork`, agent definition files)
4. Current Claude model IDs and capabilities (for ultrathink and model references)

This ensures the technical design reflects the actual platform as of execution date, not stale assumptions from earlier phases.

## Inputs (What the Agent Reads)

### Tier 1 — Read in Full (Critical for Design Decisions)

| File | Lines | Purpose | Key Sections |
|------|-------|---------|-------------|
| `.claude/plans/requirements.md` | 792 | Functional/non-functional requirements → skill frontmatter, rules | Section 3 (106 FR by skill), Section 4 (22 NFR), Section 5 (13 CCR) |
| `.claude/plans/workflow-design.md` | 648 | I/O contracts, dispatch, state flow → CLAUDE.md design, context tiers | Section 3 (I/O contracts), Section 4 (state flow), Section 5 (multi-session), Section 6 (error handling), Section 10 (dispatch) |
| `.claude/plans/master-plan.md` | 829 | Resolved decisions, skill definitions, target structure, plugin manifest | Resolved Decisions table (13 items), Skill Inventory, Target Plugin Structure, Appendix A (research findings) |
| `.claude/rules/guiding-principles.md` | 66 | 42 principles → rules design, skill behavior constraints | All (referenced by @import in CLAUDE.md) |
| `knowledge_base/schemas/SCHEMA_DESIGN.md` | ~2,400 | KB schema definitions → finalize or reference | All schema definitions, cross-skill data flow map, shared conventions |

### Tier 2 — Selective Reading (Reference)

| File | Purpose | What to Extract |
|------|---------|----------------|
| `.claude/plans/phase-1-results.md` | Pattern inventory → verify all 88 patterns mapped to skill frontmatter | Section: Extracted Patterns by Target Skill (patterns R1-R8, A1-A14, etc.), Gap Analysis |
| `.claude/plans/references/pre-sales-lifecycle.md` | Pre-sales process → validate proposal skill design | SOW Template Structure (12 sections), Sales Principles (14 items) |

### Tier 3 — Web Research (Dynamic)

| Research Target | Purpose | Expected Output |
|----------------|---------|----------------|
| Claude Code plugin documentation | Verify plugin.json schema, skill discovery mechanism, namespacing rules | Confirmed schema fields, any new fields since master plan research |
| Agent Skills standard (agentskills.io) | Verify SKILL.md frontmatter format, required vs optional fields | Authoritative frontmatter spec for all 9 skills |
| Claude Code sub-agents | Verify `context: fork` syntax, agent definition file format | Agent definition template for agents/ directory |
| Claude model IDs | Current model IDs for ultrathink and default model recommendations | Model ID strings for skill frontmatter |

## Output: `.claude/plans/technical-design.md` (target: 900-1,400 lines)

### Section 1: Plugin Directory Layout (~60 lines)

**Content**: Complete file tree showing every file that will exist after Phases 4-6. This is the authoritative layout — Phase 4 creates the structure, Phase 5 populates skills, Phase 6 populates KB.

**Must include**:
- `.claude-plugin/plugin.json` location and purpose
- `skills/` with all 9 subdirectories and SKILL.md files
- `agents/` with sub-agent definition files
- `hooks/hooks.json` (if any hooks needed)
- `knowledge_base/` with all 10 JSON files + `schemas/` with 11 schema files
- `templates/` with output templates per skill
- `.claude/rules/` with all rule files (unscoped and path-scoped)
- `.claude/plans/` preserved as planning artifacts
- Root files: CLAUDE.md, README.md, ARCHITECTURE.md, CONTRIBUTING.md, LICENSE, .repo-metadata.json
- Annotation per file: which phase creates it, which phase populates it

**Verification**: Every file in the tree must map to a phase. No orphan files.

### Section 2: CLAUDE.md Design (~120 lines)

**Content**: Complete draft of the CLAUDE.md file (under 200 lines), ready for Phase 5 to write verbatim or with minimal adjustment.

**Must include**:
- Agent identity block: name, role, scope boundary (designs, doesn't implement)
- Skill reference table: all 9 skills with invocation command and 1-line description
- @import reference to guiding-principles.md
- Engagement lifecycle overview (from workflow-design.md Section 4)
- Dispatch logic summary (from workflow-design.md Section 10.1)
- KB rules: files the agent reads/writes, single source of truth (.repo-metadata.json)
- Scope boundary table (This Agent Does / Engineering Agent Does)
- Quality standards: Well-Architected compliance, exemplar-level, technology-agnostic
- Plugin compatibility note

**Constraints**: Under 200 lines. Uses @import, not inline copies. References skills/ not .claude/skills/.

**Verification**: Line count ≤ 200. No external filesystem paths. Skill names match plugin namespacing.

### Section 3: Skill Inventory with SKILL.md Frontmatter (~250 lines)

**Content**: For each of 9 skills, the complete SKILL.md frontmatter block plus a specification of what the skill body must contain. Phase 5 uses this as the blueprint for implementation.

**Per skill, specify**:
```yaml
---
name: skill-name
description: "One-line description for skill discovery"
# All other frontmatter fields per Agent Skills standard
---
```

Plus a specification table:
| Field | Value |
|-------|-------|
| Invocation | /skill-name |
| Tools Allowed | [list of tools: Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch, Agent (if sub-agents), ultrathink flag] |
| KB Reads | [list of JSON files from workflow-design.md Section 3.1] |
| KB Writes | [target JSON file] |
| Upstream Prerequisites | [which KB files must exist/be complete] |
| Engagement Types | [greenfield, migration, assessment, all] |
| Source Patterns | [pattern IDs from phase-1-results.md: R1-R8, A1-A14, etc.] |
| Key Requirements | [FR-XXX-NNN IDs from requirements.md] |
| Body Sections | [outline of what the skill body covers — methodology, output format, quality criteria] |

**Skills to specify** (all 9):
1. `/requirements` — 3 tiers, AI suitability, progressive questioning (R1-R8, FR-REQ-001-015)
2. `/architecture` — multi-step design, diagrams, WA scoring, ultrathink (A1-A14, FR-ARC-001-018)
3. `/estimate` — LOE, cost, team, confidence scoring (E1-E5, FR-EST-001-008)
4. `/project-plan` — phased delivery, sprints, gates, dependencies (PP1-PP3, FR-PPL-001-009)
5. `/proposal` — assembly from KB, 4 proposal types, SOW template (P1-P4, FR-PRO-001-008)
6. `/data-model` — ER, vector, graph, ontology, governance, ultrathink (DM1-DM7, FR-DM-001-011)
7. `/security-review` — STRIDE, defense-in-depth, compliance, AI security, ultrathink (SR1-SR9, FR-SR-001-012)
8. `/integration-plan` — APIs, migration, legacy bridging, CI/CD (IP1-IP8, FR-IP-001-013)
9. `/review` — LLM-as-judge 3 iterations, 5 dimensions, dual-persona, ultrathink (RV1-RV10, FR-RV-001-012)

**Verification**: All 9 skills have frontmatter. Every FR maps to exactly one skill. Tool lists are consistent with requirements (WebSearch in all skills per CCR-012).

### Section 4: KB Schema Specifications (~150 lines)

**Content**: Final determination on KB schemas. Since SCHEMA_DESIGN.md already has comprehensive schemas (~2,400 lines), this section should:

1. **Confirm or modify** each of the 10 schemas, noting any changes from SCHEMA_DESIGN.md
2. **List all 11 schema files** needed in `knowledge_base/schemas/` with status (NEW, REWRITE, KEEP)
3. **Resolve open questions** from SCHEMA_DESIGN.md (backward compatibility, migration path)
4. **Cross-reference** with skill I/O contracts in workflow-design.md Section 3 to ensure consistency
5. **Document shared conventions** (ID patterns, version strings, status enum, $depends_on)

**Key decision**: Whether to modify SCHEMA_DESIGN.md schemas or accept them as-is. If accepting, state "SCHEMA_DESIGN.md is the authoritative schema specification; Phase 6 implements it directly."

**Verification**: All 10 data files and 11 schema files listed. Schemas match I/O contracts from workflow-design.md. Status enum is consistent across all files.

### Section 5: Rules Design (~80 lines)

**Content**: Specification for each `.claude/rules/` file.

**Files to specify**:

| File | Scope | Purpose | Line Target |
|------|-------|---------|-------------|
| `guiding-principles.md` | Unscoped | 42 principles (already exists, keep as-is) | 66 (no change) |
| `skills.md` | Path-scoped: `skills/**` | Rules for editing skills: Agent Skills standard compliance, tool restrictions, no static vendor knowledge, ultrathink usage | ~30 |
| `knowledge-base.md` | Path-scoped: `knowledge_base/**` | Rules for KB operations: schema validation, version incrementing, $depends_on enforcement, never modify system_config.json | ~30 |
| `security.md` | Path-scoped: `private/**` | Rules for sensitive data: no PII in public files, no credentials, sanitization requirements | ~20 |
| `refactoring-direction.md` | Unscoped | Current file — DELETE in Phase 4 (no longer needed after technical design is complete) | 0 (deletion) |

**Constraint**: Total unscoped rules under 100 lines (guiding-principles.md = 66, so ~34 lines available for any other unscoped rules).

**Verification**: Total unscoped lines ≤ 100. Path-scoped rules use correct glob patterns. No redundancy with CLAUDE.md.

### Section 6: Sub-Agent Strategy (~80 lines)

**Content**: When and how to use sub-agents (`context: fork`), and agent definition files for `agents/`.

**Decision framework** (from Google/MIT research and workflow-design.md Section 10.3):
- **Use sub-agents for**: Independent parallel tasks (WA pillar reviews, STRIDE categories, multi-scenario estimation)
- **Do NOT use for**: Sequential reasoning (single agent outperforms by 39-70%)

**Agent definitions to specify**:
| Agent | File | Purpose | Used By |
|-------|------|---------|---------|
| `parallel-wa-reviewer` | `agents/parallel-wa-reviewer.md` | Reviews one WA pillar independently | /architecture, /review |
| `stride-analyzer` | `agents/stride-analyzer.md` | Analyzes one STRIDE category | /security-review |

For each agent: frontmatter (name, description, tools), invocation context, input/output contract.

**Verification**: Each agent has a definition file. No sequential reasoning delegated to sub-agents. Agent tool lists are minimal (least-privilege).

### Section 7: Context Budget Allocation (~80 lines)

**Content**: Token budget allocation per context tier, with specific estimates.

**Tiers** (from workflow-design.md Section 10.2):

| Tier | Content | Est. Tokens | When Loaded |
|------|---------|-------------|-------------|
| Hot | CLAUDE.md + active rule files + target SKILL.md | ~3,000-4,000 | Every invocation |
| Warm | Upstream KB files ($depends_on) + engagement.json | ~2,000-5,000 per file | On skill invocation |
| Cold | Reference documents, templates, SCHEMA_DESIGN.md | As needed | Skill requests specific data |

**Per-skill budget estimates**: For each of 9 skills, estimate total context at invocation:
- Hot tier (constant) + Warm tier (varies by skill's $depends_on count) = estimated total

**Budget constraints**:
- CLAUDE.md ≤ 200 lines (~1,500 tokens)
- Each SKILL.md should target 200-400 lines (~1,500-3,000 tokens)
- Each KB JSON file targets 100-500 lines (~800-4,000 tokens)
- Guiding principles: 66 lines (~500 tokens)

**Verification**: No skill's total invocation context exceeds reasonable budget (~20K tokens for context loading). Skills with more dependencies (e.g., /proposal reads ALL) have strategies for selective section loading.

### Section 8: Architecture Diagrams (~100 lines)

**Content**: Mermaid diagrams that serve as the visual specification for the plugin. At least 4 diagrams:

1. **Plugin Structure** — Visual file tree showing the plugin organization (directories, key files, relationships)
2. **Skill Dispatch Flow** — User message → CLAUDE.md dispatch → prerequisite validation → skill invocation → KB write → engagement.json update → human checkpoint
3. **KB Data Flow** — Refined version of workflow-design.md Section 4.3 diagram, showing $depends_on relationships between all 10 KB files
4. **Context Loading Sequence** — Sequence diagram showing what gets loaded when: Hot tier → Warm tier ($depends_on resolution) → Skill execution → Cold tier (on-demand)

**Optional** (if adding value):
5. **Engagement Lifecycle** — State machine from workflow-design.md Section 4.1 (may be sufficient as-is)
6. **Sub-Agent Orchestration** — Fork/join pattern for parallel reviews

**Verification**: Each diagram renders valid Mermaid. Diagrams are consistent with Sections 1-7. File names in diagrams match Section 1 layout.

### Section 9: Plugin Manifest Specification (~30 lines)

**Content**: Final `plugin.json` with all fields, verified against latest Anthropic documentation.

**Base from master-plan.md**:
```json
{
  "name": "solutions-architecture-agent",
  "version": "1.0.0",
  "description": "...",
  "author": { "name": "Modular Earth LLC", "url": "..." },
  "homepage": "...",
  "repository": "...",
  "license": "MIT",
  "keywords": [...]
}
```

**Verify via web research**: Are there new optional fields (e.g., custom paths for skills/agents/hooks, minimum Claude version, tool permissions)?

**Verification**: JSON is valid. All required fields present per latest Anthropic schema. Repository URL uses correct GitHub org.

### Section 10: Phase 1 Gap Closure Report (~40 lines)

**Content**: Status update on all 13 gaps from phase-1-results.md Gap Analysis table. For each gap, state: CLOSED (with evidence) or DEFERRED (to which phase).

| Gap | Status | Resolution |
|-----|--------|-----------|
| Multi-session state management | CLOSED | workflow-design.md Section 5 + this document Section 7 |
| Error recovery | CLOSED | workflow-design.md Section 6 + this document Section 5 (rules) |
| Neurosymbolic AI architecture | DEFERRED to Phase 5 | /data-model skill uses WebSearch at invocation |
| Strangler fig pattern | DEFERRED to Phase 5 | /integration-plan skill uses WebSearch |
| ... | ... | ... |

**Verification**: All 13 gaps accounted for. No gap left without a resolution or deferral.

## Execution Steps

1. **Read all Tier 1 inputs** (~4,735 lines of markdown + ~2,400 lines of SCHEMA_DESIGN.md)
2. **Perform web research**: Claude Code plugin docs, Agent Skills standard, sub-agent format, current model IDs
3. **Produce Section 1** (Plugin Directory Layout) — establishes the structural foundation
4. **Produce Section 3** (Skill Frontmatter) — the most complex section; depends on requirements.md FRs, workflow-design.md I/O contracts, and web research for frontmatter format
5. **Produce Section 2** (CLAUDE.md Design) — depends on Section 3 skill inventory for reference table
6. **Produce Section 4** (KB Schema) — confirm or modify SCHEMA_DESIGN.md, cross-reference with Section 3 I/O contracts
7. **Produce Sections 5-7** (Rules, Sub-Agents, Context Budget) — derived from Sections 1-4
8. **Produce Section 8** (Mermaid Diagrams) — visualize Sections 1-7
9. **Produce Section 9** (Plugin Manifest) — finalize from web research
10. **Produce Section 10** (Gap Closure) — verify all Phase 1 gaps addressed
11. **Cross-reference verification**: every requirement in requirements.md maps to a design element; every I/O contract in workflow-design.md is reflected in skill frontmatter and KB schemas
12. **Git commit**: `git add .claude/plans/technical-design.md && git commit`
13. **Human checkpoint**: present plugin structure, skill frontmatter table, key design decisions, architecture diagrams

## Verification Criteria

### technical-design.md

- [ ] Plugin directory layout lists every file with creating phase annotated
- [ ] CLAUDE.md draft is ≤ 200 lines and includes: identity, 9-skill reference, @import principles, dispatch logic, scope boundary
- [ ] All 9 skills have complete SKILL.md frontmatter verified against latest Agent Skills standard
- [ ] Each skill frontmatter references its source patterns (R1-R8, A1-A14, etc.) and key requirements (FR-XXX-NNN)
- [ ] KB schema section is consistent with SCHEMA_DESIGN.md and workflow-design.md I/O contracts
- [ ] Rules design has ≤ 100 lines total for unscoped rules
- [ ] Sub-agent strategy includes agent definition files with frontmatter
- [ ] Context budget estimates are per-skill with token counts
- [ ] At least 4 Mermaid diagrams that render correctly
- [ ] Plugin manifest JSON is valid and verified against latest Anthropic docs
- [ ] All 13 Phase 1 gaps have CLOSED or DEFERRED status
- [ ] No external filesystem references (C:\dev\, \\wsl.localhost\, D:\dev\)
- [ ] Web research citations included (plugin docs URL, Agent Skills URL)

### Cross-Reference Checks

- [ ] Every FR-XXX-NNN in requirements.md Section 3 maps to a skill frontmatter in Section 3
- [ ] Every skill I/O contract in workflow-design.md Section 3.1 matches skill frontmatter KB Reads/Writes
- [ ] Every KB file in Section 4 appears in Section 1 directory layout
- [ ] Every sub-agent in Section 6 appears in Section 1 directory layout under agents/
- [ ] Every rule file in Section 5 appears in Section 1 directory layout under .claude/rules/
- [ ] Context budget in Section 7 is consistent with CLAUDE.md line count in Section 2

## Risks

| Risk | Mitigation |
|------|-----------|
| Agent Skills standard has changed since master plan research (Dec 2025) | Web research step verifies current spec before writing frontmatter |
| Claude Code plugin schema has new fields | Web research step checks latest docs; design includes only verified fields |
| SCHEMA_DESIGN.md needs modifications | Phase 3 decides: accept as-is or modify. If modifying, document changes explicitly |
| Over-specification (design too rigid for Phase 5 to implement) | Each section notes "Phase 5 may adjust" where flexibility is needed |
| Under-specification (design leaves too many decisions to Phase 5) | Verification criteria require concrete values, not placeholders |
| Context overflow from reading all inputs | Total inputs ~7,000 lines markdown; well within 1M context budget |

## Downstream Consumers

| Phase | What It Reads from technical-design.md | Section(s) |
|-------|---------------------------------------|-----------|
| Phase 4 (Cleanup) | Plugin directory layout, plugin manifest | Sections 1, 9 |
| Phase 5 (Skills) | CLAUDE.md draft, skill frontmatter, rules design, sub-agent definitions | Sections 2, 3, 5, 6 |
| Phase 6 (KB & Templates) | KB schema specifications, context budget | Sections 4, 7 |
| Phase 7 (Validation) | All sections (verify implementation matches design) | All |
| Phase 8 (Documentation) | Architecture diagrams, plugin manifest | Sections 8, 9 |

## Document Permanence Note

The planning documents produced in Phases 1-3 (phase-1-results.md, requirements.md, workflow-design.md, technical-design.md) are permanent project artifacts, not throwaway scaffolding. During Phase 8 (Documentation), they should be:
- Preserved in `.claude/plans/` as the design history
- Referenced from ARCHITECTURE.md as the authoritative design documents
- Key diagrams and tables promoted into user-facing documentation where appropriate

## Execution Command

After human approval of this plan, reset context and execute:

```bash
claude -p "$(cat .claude/plans/phase-3-prompt.md)"
```

The phase-3-prompt.md file must exist before execution. It should reference this plan for detailed section specifications.
