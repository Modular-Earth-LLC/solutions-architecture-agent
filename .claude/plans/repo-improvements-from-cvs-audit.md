# Repo Improvements: Lessons from the CVS Engagement Planning Audit

**Source**: Audit of `.claude/plans/cvs-engagement/` phase plans (March 2026)
**Goal**: Make future phased, human-in-the-loop engagements smoother — less manual prompting, better automation, tighter integration between plans, skills, lifecycle, and validation.

---

## Issues Found During the Audit

### Issue 1: engagement.json Lifecycle is Documented but Not Operationalized

**What happened**: None of the 8 phase plans mentioned `engagement.json` creation or updates until the audit added them manually. The CLAUDE.md dispatch rules say "check engagement.json lifecycle_state for required upstream KB files" but no skill or plan actually does this automatically.

**Root cause**: engagement.json management is described in CLAUDE.md prose but has no operational hook. Skills are *expected* to update it but have no enforcement, reminder, or template for doing so. When writing plans, the planner (human or AI) has to remember to include these steps — and both forgot.

**Impact**: Without engagement.json tracking, there's no way to know which phases are complete, which KB files have been reviewed, or whether prerequisites are met. Each session starts blind.

### Issue 2: KB Validation Exists but Is Never Referenced in Workflows

**What happened**: `python tests/validate_knowledge_base.py` exists and is thorough (validates all KB files against Draft 2020-12 JSON Schemas). But no plan mentioned running it after producing KB artifacts. CI runs it on PRs, but during the interactive engagement workflow (where most KB writing happens), it's invisible.

**Root cause**: The validation script is framed as a CI/testing tool, not as an inline workflow step. The skill SKILL.md files don't mention it. The CLAUDE.md knowledge-base rules mention "validate with `python tests/validate_knowledge_base.py`" but this is buried in a rules file, not surfaced at the point of action.

### Issue 3: Plans Don't Reference Sub-Agents

**What happened**: The repo has two sub-agents (`parallel-wa-reviewer`, `stride-analyzer`) that the `/architecture` and `/security-review` skills can use. The phase plans didn't mention them, so a future session executing those phases wouldn't know to leverage them.

**Root cause**: Sub-agents are defined in `agents/` and referenced in skill SKILL.md files, but there's no surface-level documentation that says "when you invoke `/architecture`, it can parallelize WA scoring via sub-agents." The connection between skills and sub-agents is implicit.

### Issue 4: The `/proposal` Skill Was Overlooked

**What happened**: The canonical Migration flow includes `/proposal` as a step. The assembly phase (Phase 6) does exactly what `/proposal` does — assembles KB data into a deliverable — but didn't reference the skill at all. The audit added a "consider `/proposal`" section.

**Root cause**: The engagement was treated as a custom format (Solution Architecture Document for a job interview), so the planner skipped `/proposal` assuming it only produces SOWs. But `/proposal` supports 4 types (discovery, implementation, internal, pitch deck) and could have been useful as scaffolding.

### Issue 5: Phase Plans Are Not Machine-Readable

**What happened**: Each phase plan is a Markdown file optimized for human reading. When phases need to reference each other (dependencies, outputs, context handoffs), they do so in prose. When the audit renumbered phases, every cross-reference had to be found and updated manually across 9 files.

**Root cause**: No structured metadata (YAML frontmatter, JSON sidecar, or index file) links plans together. Dependencies are expressed as sentences like "Phase 4 needs architecture.json" rather than structured data.

### Issue 6: Review Dimensions Were Unnamed

**What happened**: Plans said ">= 7.5/10 across all 5 dimensions" without naming them. A session executing the plan wouldn't know which dimensions to score without reading the review schema.

**Root cause**: The review schema defines 5 core dimensions (completeness, technical soundness, well-architected, clarity, feasibility) plus optional ones (security). But CLAUDE.md's skill table just says "5 dimensions" without listing them. This ambiguity propagated into the plans.

### Issue 7: Canonical Flow Reference Was Missing

**What happened**: The master plan didn't cite which canonical engagement flow (Greenfield, Migration, Streamlined, Assessment, Quick Qualify) the engagement follows. This matters because the canonical flow determines skill ordering and whether steps are required or optional.

**Root cause**: The canonical flows are defined in CLAUDE.md but aren't referenced in the planning workflow. There's no step that says "when creating an engagement plan, first identify which canonical flow applies."

### Issue 8: Phase Numbering Drifted from Execution Order

**What happened**: Phases were numbered 0-7 but executed in order 0→1→2→3→4→7→5→6. This created confusion because "Phase 5" (Assembly) depended on "Phase 7" (AI Methodology), but Phase 7 hadn't been produced yet. The audit renumbered to make execution order match phase numbers.

**Root cause**: The original planning prompt specified content-logical groupings (design phases together, execution phases together) rather than dependency-ordered numbering. No constraint enforced that phase numbers match execution order.

---

## Recommended Solutions

### Solution 1: Engagement Plan Template with Structured Frontmatter

Create a plan template that every phase plan must follow. Add YAML frontmatter with machine-readable metadata:

```yaml
---
phase: 0
title: Research and Requirements
engagement_id: eng-2026-001
engagement_type: modernization
canonical_flow: migration
skills:
  - requirements
  - review
produces:
  - knowledge_base/requirements.json
  - knowledge_base/engagement.json
  - outputs/cvs-legacy-transformation/research-findings.md
  - outputs/cvs-legacy-transformation/honesty-map.md
depends_on: []  # phase numbers
quality_gate:
  min_score: 7.5
  dimensions: [completeness, technical_soundness, well_architected, clarity, feasibility]
  review_targets: [requirements.json]
engagement_json:
  creates: true  # or updates: [requirements]
kb_validation: true
---
```

**Benefits**:
- Plans become queryable: "which phases produce KB files?" "what are Phase 3's dependencies?"
- Renumbering only changes the `phase` field + `depends_on` arrays, not prose
- Automated tooling can verify dependency ordering, completeness, and consistency
- A future "plan validator" test can check all plans in a directory

**Implementation**: Create `knowledge_base/schemas/phase_plan.schema.json`, add to CI validation.

### Solution 2: Post-Skill Automation Checklist in SKILL.md Files

Add a `## Post-Execution` section (Section 6.5) to every SKILL.md that produces KB output:

```markdown
## Post-Execution Checklist
After this skill completes:
1. Update `knowledge_base/engagement.json` → set `lifecycle_state.{domain}.status` to `complete`
2. Run `python tests/validate_knowledge_base.py --file {output_file}`
3. Present human checkpoint (Section 6)
```

**Benefits**:
- engagement.json updates become part of the skill definition, not something the planner has to remember
- KB validation is surfaced at the point of action, not buried in CI
- Consistent across all skills

**Implementation**: Add to all 7 KB-producing skills (requirements, architecture, data-model, security-review, integration-plan, estimate, project-plan). The review skill updates reviews.json differently — adapt accordingly.

### Solution 3: Engagement Lifecycle Automation Skill or Hook

Create a lightweight automation that runs after any skill completes:

**Option A: Claude Code hook** (in `hooks/hooks.json`):
```json
{
  "PostToolUse": [{
    "matcher": "Skill",
    "hooks": [{
      "type": "command",
      "command": "python scripts/post_skill_hook.py"
    }]
  }]
}
```

The script would:
1. Detect which KB files changed (via git diff)
2. Update engagement.json lifecycle_state for changed files
3. Run KB validation on changed files
4. Print a summary of what was updated

**Option B: A `/lifecycle` skill** that the agent invokes after each phase:
- Reads all KB files and their `_metadata.validation_status`
- Updates engagement.json to match actual state
- Reports missing prerequisites for the next canonical flow step
- Suggests the next skill to invoke

**Benefits**:
- Eliminates the "forgot to update engagement.json" problem
- Makes lifecycle state always accurate
- Reduces plan complexity (phases don't need to include boilerplate engagement.json steps)

### Solution 4: Plan Generation from Canonical Flow

Create a `/plan-engagement` skill (or enhance the dispatch logic in CLAUDE.md) that, given an engagement type and context, generates the phase plan structure automatically:

**Input**: engagement type (greenfield/migration/modernization/assessment), client context, key requirements
**Output**: A set of phase plan files with:
- Correct skill ordering from the canonical flow
- Pre-populated dependencies
- Pre-populated engagement.json management steps
- Pre-populated KB validation steps
- Pre-populated quality gates with named dimensions
- Context handoff templates
- Human checkpoint templates

**Benefits**:
- Eliminates 80% of the manual plan-writing work
- Ensures every plan includes lifecycle management, validation, and quality gates by construction
- Makes the canonical flows executable, not just documented
- Reduces the "meta-planning" prompting overhead from ~4000 words to ~200 words

**Implementation path**:
1. Start with a plan template generator (Python script in `scripts/`)
2. Later, promote to a full skill (`/plan-engagement`) with its own SKILL.md
3. Eventually, make it the default entry point: user describes the engagement, agent generates the plan, user reviews and approves, then execution begins

### Solution 5: Context Handoff Automation

The current context handoff pattern (write a summary, update future plans, commit) is labor-intensive and error-prone. Automate it:

**Create `scripts/phase_handoff.py`**:
```
Usage: python scripts/phase_handoff.py --phase N --engagement-dir .claude/plans/cvs-engagement/

1. Reads all KB files and generates a context summary from:
   - KB file metadata (versions, statuses, review scores)
   - Git diff since last phase commit
   - engagement.json current state
2. Writes context/phase-N-context.md with structured template
3. Scans remaining phase plan files for references to outputs from this phase
4. Reports which future plans need manual updates (can't auto-update prose)
5. Commits context + plan updates
```

**Benefits**:
- Context summaries are consistent and complete (no forgotten sections)
- Future plan update needs are identified automatically
- Git commits are standardized
- Reduces the context handoff from ~15 minutes of manual work to ~2 minutes of review

### Solution 6: Skill-to-Sub-Agent Mapping in .repo-metadata.json

Add a `skill_sub_agents` mapping to `.repo-metadata.json`:

```json
"skill_sub_agents": {
  "architecture": ["parallel-wa-reviewer"],
  "security-review": ["stride-analyzer"]
}
```

**Benefits**:
- Plan generators (Solution 4) can automatically note which sub-agents are available
- Documentation stays in one place (single source of truth)
- Testable: CI can verify sub-agents referenced in skills actually exist

### Solution 7: Review Dimension Constants

Define the 5 review dimensions as a constant in `system_config.json` or `reviews.schema.json`, and reference them by name everywhere:

```json
"review_dimensions": {
  "core": ["completeness", "technical_soundness", "well_architected", "clarity", "feasibility"],
  "optional": ["security"],
  "default_threshold": 7.5
}
```

Then CLAUDE.md, SKILL.md files, and plan templates can reference `system_config.json → review_dimensions` instead of repeating the list.

**Benefits**:
- Single source of truth for dimension names and thresholds
- No more "5 dimensions" without naming them
- If dimensions change, they change in one place

### Solution 8: Phase Numbering Constraint

Add a validation rule (in `scripts/` or `tests/`) that checks:
- Phase files are numbered sequentially (0, 1, 2, ...)
- Phase N's `depends_on` only references phases < N
- No gaps in numbering

This prevents the drift where phases are numbered by content grouping rather than execution order.

**Implementation**: Add to `tests/` as `validate_phase_plans.py`. Run as part of CI when `.claude/plans/` files change.

---

## Priority Matrix

| Solution | Impact | Effort | Priority |
|----------|--------|--------|----------|
| **1. Plan Template with Frontmatter** | High — prevents most audit findings | Medium | **P0** |
| **2. Post-Skill Checklist in SKILL.md** | High — eliminates forgotten lifecycle steps | Low | **P0** |
| **7. Review Dimension Constants** | Medium — eliminates ambiguity | Low | **P0** |
| **3. Lifecycle Automation (Hook/Skill)** | High — eliminates manual engagement.json management | Medium | **P1** |
| **4. Plan Generation from Canonical Flow** | Very High — eliminates most planning overhead | High | **P1** |
| **6. Skill-to-Sub-Agent Mapping** | Low — documentation improvement | Low | **P2** |
| **5. Context Handoff Automation** | Medium — reduces manual work per phase | Medium | **P2** |
| **8. Phase Numbering Constraint** | Low — prevents edge case | Low | **P2** |

---

## What This Means for the Next Engagement

If Solutions 1-3 and 7 are implemented before the next multi-phase engagement:

**Before (current state)**:
1. Write a 4000-word meta-planning prompt specifying every detail
2. Generate 9 plan files (~130 KB total)
3. Audit for missing engagement.json, KB validation, review dimensions, sub-agents, canonical flow
4. Manually renumber phases when execution order doesn't match
5. During execution: manually update engagement.json, manually run KB validation, manually write context summaries
6. Between sessions: hope the context files are complete enough to reconstruct state

**After (with improvements)**:
1. Invoke `/plan-engagement` with engagement type + context (~200 words)
2. Agent generates phase plans with frontmatter, lifecycle steps, validation, and quality gates pre-included
3. Audit is automated (CI validates plan structure, dependencies, dimension naming)
4. Phase numbering is constrained to execution order
5. During execution: post-skill hooks auto-update engagement.json and run validation
6. Between sessions: engagement.json is always current; context summaries are auto-generated from KB state

---

## Task: Documentation Refactoring

The repo's documentation is scattered across multiple locations with overlapping scope, stale content, and no clear hierarchy. This task should be completed before the next major engagement.

### Current State

| File | Location | Content |
|------|----------|---------|
| `target-architecture.md` | `docs/` (just moved from references) | Plugin deployment model, context budget strategy, file structure — written during refactoring, may not reflect current state |
| `anthropic-cloud-deployment.md` | `docs/` (just moved from references) | Cloud packaging: API, Agent SDK, Claude Projects — forward-looking, needs validation against current Anthropic platform |
| `current-claude-code-setup.md` | `docs/` (just moved from references) | Paul's dev environment snapshot: 18 plugins, 5 MCP servers — point-in-time, likely stale |
| `reference-materials-index.md` | `.claude/plans/references/` | Catalogs Hyperbloom/AVAHI/Florence/AGADA exemplars — references old refactoring phase numbers (Phases 2, 5, 7, 8) |
| `.repo-metadata.json` | repo root | Claims `ARCHITECTURE.md`, `CONTRIBUTING.md`, and `docs/` exist — `ARCHITECTURE.md` and `CONTRIBUTING.md` are not on disk |
| `sa-best-practices-research-2026.md` | `.claude/plans/references/` | SA frameworks research — good content, unclear if it should live in references or docs |

### Problems

1. **`.repo-metadata.json` references files that don't exist on disk**: `ARCHITECTURE.md`, `CONTRIBUTING.md` are listed but not present. Either they were never materialized, or they were removed.
2. **`target-architecture.md` may be stale**: Written during the multi-agent-to-single-agent refactoring. The plugin structure it describes may not match the current state.
3. **`current-claude-code-setup.md` is a point-in-time snapshot**: Plugin list, MCP servers, and integration points change frequently. Needs a freshness strategy or should be auto-generated.
4. **`reference-materials-index.md` uses old phase numbers**: References "Phase 2", "Phase 5", "Phase 7", "Phase 8" from the old 9-phase refactoring, not the current repo state or CVS engagement.
5. **No `docs/` directory existed**: Documentation was scattered between `.claude/plans/references/` (engagement materials), `.claude/rules/` (behavioral rules), and root-level files.
6. **No clear documentation hierarchy**: A reader can't tell where to find architecture decisions vs. operational guides vs. engagement reference materials.

### Recommended Actions

1. **Audit `.repo-metadata.json`**: Either create `ARCHITECTURE.md` and `CONTRIBUTING.md`, or remove the references. Single source of truth should be accurate.
2. **Update `target-architecture.md`**: Verify against the actual repo structure. Update or mark sections that are aspirational vs. implemented.
3. **Update `current-claude-code-setup.md`**: Refresh with current plugins and MCP servers, or add a "last verified" date and note that it needs periodic refresh.
4. **Update `reference-materials-index.md`**: Remove old refactoring phase numbers. Reframe around the skill names (`/requirements`, `/architecture`, etc.) rather than phase numbers.
5. **Establish `docs/` directory structure**:
   ```
   docs/
   ├── target-architecture.md        ← How the plugin is structured and deployed
   ├── anthropic-cloud-deployment.md  ← Cloud deployment roadmap
   ├── current-claude-code-setup.md   ← Development environment reference
   └── (future: getting-started.md, engagement-guide.md)
   ```
6. **Consider moving `sa-best-practices-research-2026.md`** to `docs/` since it's general SA knowledge, not engagement-specific reference material.
