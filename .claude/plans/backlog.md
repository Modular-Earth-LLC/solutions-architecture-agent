# Backlog

Prioritized work items for the SA Agent. Each item has enough context for a coding assistant to pick up and implement.

---

## P0 — High Impact, Do Next

### B-001: `/plan-engagement` skill
**Source**: CVS audit — the single highest-leverage addition.
**Problem**: Writing 8 phase plans for CVS required a 4000-word meta-prompt and produced 130KB of files that needed auditing.
**Scope**: New skill that takes engagement type + client context, reads the canonical flow from CLAUDE.md, and generates a master plan + N phase plans with structured YAML frontmatter, pre-populated skill invocations, engagement.json management, KB validation, quality gates.
**KB output**: `engagement.json` (creates with initial lifecycle state)
**Files**: `skills/plan-engagement/SKILL.md`, `knowledge_base/schemas/phase_plan.schema.json`

### B-002: `/research` skill — Structured web research with citations
**Source**: CVS audit — Phase 0 required 9 research clusters with 36+ WebSearch queries.
**Problem**: Every engagement starts with domain research. No standardized way to do it.
**Scope**: New skill. Input: research topic clusters. Executes WebSearch in parallel clusters, synthesizes findings with source citations and confidence ratings, flags contradictions and thin areas, produces structured findings with bibliography.
**KB output**: None — produces `outputs/{engagement}/research-findings.md`
**Files**: `skills/research/SKILL.md`

### B-003: Post-skill checklist in all SKILL.md files
**Source**: CVS audit Issue 1 — engagement.json lifecycle not operationalized.
**Problem**: Skills are expected to update engagement.json but have no enforcement or reminder.
**Scope**: Add `## Post-Execution Checklist` after Section 6 in all 7 KB-producing skills: (1) update engagement.json lifecycle_state, (2) run `python tests/validate_knowledge_base.py --file {output}`, (3) present human checkpoint.
**Files**: All `skills/*/SKILL.md`

### B-004: Review dimension constants in system_config.json
**Source**: CVS audit Issue 6 — plans said "5 dimensions" without naming them.
**Problem**: Review dimensions are scattered across SKILL.md, plans, CLAUDE.md.
**Scope**: Add `review_dimensions` to system_config.json with core dimensions list and default threshold. Update CLAUDE.md and review/SKILL.md to reference it.
**Files**: `knowledge_base/system_config.json`, `CLAUDE.md`, `skills/review/SKILL.md`

### B-005: system_config.json cleanup
**Source**: DESIGN_RATIONALE.md backlog item 6.
**Problem**: `self_improvement_framework` and `validation_framework` sections reference defunct multi-agent architecture (`optimization_agent`, `prompt_engineering_agent`). 779 lines total.
**Scope**: Decompose into focused configs or trim dead sections. Requires schema update + re-validation.
**Files**: `knowledge_base/system_config.json`, `knowledge_base/schemas/system_config.schema.json`

---

## P1 — Medium Impact

### B-006: `/ux-design` skill
**Source**: CVS audit — Phase 1 had no skill invocation, was pure manual writing.
**Scope**: New skill for user personas, workflow analysis, journey maps, accessibility strategy. Uses guiding-principles.md (principles 1-8). Fits between `/requirements` and `/architecture` in Migration/Greenfield flows.
**KB output**: `ux_design.json`
**Files**: `skills/ux-design/SKILL.md`, `knowledge_base/schemas/ux_design.schema.json`

### B-007: Domain knowledge packs
**Source**: CVS audit — every engagement starts with same domain research overhead.
**Scope**: Pre-built `knowledge_base/domains/{industry}.json` packs. Priority: healthcare (HIPAA, PBM), financial (PCI DSS, SOX), legacy modernization (IBMi patterns, middleware vendors).
**Files**: `knowledge_base/domains/*.json`

### B-008: Regulatory compliance checklists
**Source**: CVS audit — Phase 3 required mapping HIPAA/HITECH/PCI DSS to controls.
**Scope**: `knowledge_base/compliance/{regulation}.json` with sections, technical safeguard mappings, cloud service mappings. Priority: HIPAA, SOC 2, PCI DSS, GDPR, CCPA.
**Files**: `knowledge_base/compliance/*.json`

### B-009: Cloud provider comparison matrix
**Source**: CVS audit — mapping AWS to GCP was a recurring need.
**Scope**: `knowledge_base/cloud_comparison.json` with service-by-service AWS/GCP/Azure mapping, differentiators, pricing model differences.
**Files**: `knowledge_base/cloud_comparison.json`

### B-010: Marketplace submission
**Source**: NEXT_STEPS.md v1.2.0 roadmap.
**Scope**: Add `categories`, engine version to plugin.json per Anthropic spec. Test installation via marketplace flow.
**Files**: `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`

### B-011: Second case study — greenfield AI project
**Source**: NEXT_STEPS.md v1.1.0 roadmap.
**Scope**: Validate agent against a greenfield engagement in a different domain (not healthcare). Exercises the greenfield canonical flow.

### B-012: Behavioral integration tests
**Source**: NEXT_STEPS.md v1.1.0 roadmap + DESIGN_RATIONALE.md limitation.
**Scope**: Parameterized tests feeding synthetic `$ARGUMENTS` to skills. Currently only structural tests exist.
**Files**: `tests/test_behavioral.py`

### B-013: Review calibration
**Source**: NEXT_STEPS.md v1.2.0 roadmap + DESIGN_RATIONALE.md limitation.
**Problem**: `/review` uses the same LLM that generated deliverables (LLM-as-judge circularity).
**Scope**: Compare LLM review scores against human expert assessments to measure correlation and identify systematic gaps.

---

## P2 — Lower Priority

### B-014: `/change-management` skill
**Source**: CVS audit — was embedded in `/project-plan` but deserves its own skill.
**Scope**: Stakeholder analysis, communication plans, training programs, adoption KPIs, resistance mitigation. After `/project-plan`, before `/proposal`.
**Files**: `skills/change-management/SKILL.md`, `knowledge_base/schemas/change_management.schema.json`

### B-015: Lifecycle automation hook
**Source**: CVS audit Solution 3.
**Scope**: Post-skill hook that detects KB file changes, updates engagement.json, runs KB validation. Eliminates "forgot to update engagement.json."
**Files**: `hooks/hooks.json`, `scripts/post_skill_hook.py`

### B-016: Context handoff automation
**Source**: CVS audit Solution 5.
**Scope**: `scripts/phase_handoff.py` — generates context summaries from KB metadata + git diff, writes `context/phase-N-context.md`, identifies which future plans need updates.
**Files**: `scripts/phase_handoff.py`

### B-017: Phase plan structured frontmatter
**Source**: CVS audit Solution 1.
**Scope**: YAML frontmatter template for phase plans with machine-readable metadata (phase number, skills, produces, depends_on, quality_gate). Phase plan schema + CI validation.
**Files**: `knowledge_base/schemas/phase_plan.schema.json`, `tests/validate_phase_plans.py`

### B-018: Multi-engagement management
**Source**: NEXT_STEPS.md v1.2.0.
**Scope**: Engagement archival workflow, namespace support for multiple concurrent engagements.

### B-019: Skill-to-sub-agent mapping in .repo-metadata.json
**Source**: CVS audit Solution 6.
**Scope**: Add `skill_sub_agents` mapping so plan generators know which sub-agents are available.
**Files**: `.repo-metadata.json`

---

## P3 — Future / Long-Term

### B-020: Engineering Agent
**Source**: NEXT_STEPS.md v2.0.0.
**Scope**: Consumes SA Agent outputs, generates implementation artifacts (code, IaC, CI/CD). Out of scope for current agent.

### B-021: Engagement dashboard
**Source**: NEXT_STEPS.md v2.0.0.
**Scope**: Readiness checks, confidence visualization across engagement phases.

### B-022: Fine-tuned review model
**Source**: NEXT_STEPS.md v2.0.0.
**Scope**: Calibrated against human SA reviewer corpus for more accurate scoring.
