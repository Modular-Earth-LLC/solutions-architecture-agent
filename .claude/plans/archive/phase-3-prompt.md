<role>
You are a Distinguished AI Architect designing a Claude Code plugin for solutions architecture.
</role>

<instructions>
Phase 3: System Architecture & Technical Design.

Read the detailed execution plan FIRST: .claude/plans/phase-3-plan.md — it specifies exactly what each section of the output must contain, with verification criteria and cross-reference checks.

Then read all Tier 1 inputs:
- .claude/plans/master-plan.md (resolved decisions, skill definitions, target structure)
- .claude/plans/requirements.md (106 FR + 22 NFR + 13 CCR, 3 personas, 36 user stories)
- .claude/plans/workflow-design.md (I/O contracts, state flow, dispatch architecture, error handling)
- .claude/rules/guiding-principles.md (42 principles)
- knowledge_base/schemas/SCHEMA_DESIGN.md (KB schema definitions, cross-skill data flow map)

Selectively read:
- .claude/plans/phase-1-results.md (88 patterns by skill, gap analysis — Sections: Extracted Patterns, Gap Analysis)
- .claude/plans/references/pre-sales-lifecycle.md (SOW template, sales principles)

Perform web research to verify latest:
1. Claude Code plugin documentation (plugin.json schema, skill discovery, namespacing)
2. Agent Skills standard (SKILL.md frontmatter format, required vs optional fields)
3. Claude Code sub-agent configuration (context: fork, agent definition file format)
4. Current Claude model IDs for ultrathink references

Produce .claude/plans/technical-design.md containing these 10 sections (see phase-3-plan.md for detailed specs per section):

1. Plugin Directory Layout — Complete file tree with phase annotations
2. CLAUDE.md Design — Full draft under 200 lines
3. Skill Inventory — Complete SKILL.md frontmatter for all 9 skills with tool lists, KB reads/writes, source patterns, and key requirements
4. KB Schema Specifications — Confirm or modify SCHEMA_DESIGN.md, list all schema files
5. Rules Design — Spec for each .claude/rules/ file (unscoped and path-scoped)
6. Sub-Agent Strategy — Agent definitions for agents/ directory
7. Context Budget Allocation — Per-skill token estimates by tier
8. Architecture Diagrams — At least 4 Mermaid diagrams (plugin structure, skill dispatch, KB data flow, context loading)
9. Plugin Manifest — Final plugin.json verified against latest docs
10. Phase 1 Gap Closure Report — Status of all 13 gaps (CLOSED or DEFERRED)
</instructions>

<constraints>
- CLAUDE.md under 200 lines. Unscoped rules under 100 lines total.
- Skills at plugin root (skills/), not .claude/skills/.
- Plugin manifest at .claude-plugin/plugin.json per Anthropic's schema.
- All skills technology-agnostic with WebSearch/WebFetch for dynamic references.
- Include "ultrathink" in skills requiring deep reasoning (architecture, data-model, security-review, review).
- No external filesystem references.
- Web research citations required — do not guess at current plugin/skill format.
- Every design decision must trace to a requirement (FR-XXX-NNN) or resolved decision from master-plan.md.
</constraints>

<verification>
After producing technical-design.md, verify:
- [ ] All 9 skills have complete frontmatter
- [ ] CLAUDE.md draft ≤ 200 lines
- [ ] Every FR from requirements.md maps to a skill frontmatter
- [ ] Every I/O contract from workflow-design.md matches skill KB reads/writes
- [ ] At least 4 valid Mermaid diagrams
- [ ] All 13 Phase 1 gaps addressed
- [ ] No external filesystem paths
- [ ] Plugin manifest JSON is valid
- [ ] All unscoped rules ≤ 100 lines total
</verification>

<git>
git add .claude/plans/technical-design.md
git commit -m "Phase 3: Technical design and plugin architecture complete"
</git>

<human_checkpoint>
Present: plugin structure visualization, skill frontmatter table (9 rows with tools and KB access), CLAUDE.md line count, key design decisions, Mermaid diagram previews, gap closure status. Wait for human review.
</human_checkpoint>
