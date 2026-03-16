# NEXT STEPS — Phases 7-9 Roadmap

**Date**: 2026-03-15
**Status**: Phase 6 complete. Phase 7 plan in progress.

## Phase 7: Integration Testing & Optimization

**Goal**: Validate the SA agent end-to-end against the Legacy System Transformation case study (IBMi/AS/400 green screen modernization), fix every bug/gap discovered, and use findings to improve the agent for all use cases.

### What Happens
1. Run the full greenfield engagement flow against Use Case 1: `/requirements` -> `/architecture` -> `/data-model` -> `/security-review` -> `/integration-plan` -> `/estimate` -> `/project-plan` -> `/proposal` -> `/review`
2. Validate every KB output against schemas (`validate_knowledge_base.py`)
3. Validate cross-file consistency (`validate_consistency.py`)
4. Run `/review` on each deliverable — target >= 7.5 on all 5 dimensions
5. Fix every bug, schema gap, and skill deficiency discovered
6. Re-run until all deliverables pass quality bar
7. Test error paths: missing prerequisites, draft files, scope violations
8. Record all issues and fixes in `phase-7-results.md`

### Key Considerations
- The legacy modernization case exercises every skill (legacy integration, IAM, HCD, tech stack, change management)
- Fixes should improve the agent generically, not over-fit to one domain (technology-agnostic principle)
- All deferred issues from Phase 6 review (listed in `phase-6-results.md`) must be addressed
- SKILL.md Section 5 output reconciliation with schema field names happens here

## Phase 8: Documentation, Packaging & Plans Cleanup

**Goal**: Make the plugin crystal clear for users, marketplace-ready, and clean up all development artifacts.

### What Happens
1. **Deep research** on Claude Code plugin packaging (plugin vs .claude/ separation of concerns)
2. **Documentation overhaul**: Rewrite README.md, ARCHITECTURE.md, CONTRIBUTING.md, docs/getting-started.md
3. **Redundancy reduction**: Eliminate repetition across all documentation, clear separation of concerns with references to source of truth
4. **Plans cleanup**: Extract useful info from `.claude/plans/` into core docs, archive/delete old plans, keep interview-related files
5. **Plugin packaging**: Verify `.claude-plugin/plugin.json`, test local install, test GitHub install
6. **Documentation quality**: Elegant, minimalistic, AI-first, GitHub best practices
7. **Iterative QA**: Fix all issues before moving to Phase 9

### Files to Keep in `.claude/plans/references/`
- `solution-architect-case-study-and-interview.md` (active interview prep)
- `solution-architect-case-study-and-interview.pdf` (source document)
- `solutions-architecture-first-assignment-planning-prompt.md` (active interview prep)

## Phase 9: QA Automation & Release Readiness

**Goal**: Create repeatable QA infrastructure, finalize for Windows CLI use + future marketplace deployment.

### What Happens
1. **Test infrastructure**: Unit tests, E2E integration tests, stored in `tests/` with highest coding standards
2. **Claude command**: Single `/qa` command to run full system validation
3. **Final QA pass**: Run all automated + manual checks
4. **Local readiness**: Verify on Windows with Claude Code CLI
5. **Marketplace readiness**: Format for Anthropic submission
6. **Self-review**: Run `/review` on the agent's own outputs (dogfooding)
7. **Release**: Tag v1.0.0, create GitHub release

### Test Infrastructure
- `tests/validate_knowledge_base.py` — Schema validation (exists)
- `tests/validate_consistency.py` — Cross-file consistency (exists)
- `tests/test_skill_outputs.py` — Skill output validation against schemas (new)
- `tests/test_engagement_flow.py` — E2E engagement lifecycle (new)
- `tests/test_plugin_structure.py` — Plugin packaging validation (new)
- `/qa` command — Runs all of the above in sequence

## Immediate Next Actions (for Paul)

1. **Review Phase 7 plan** (being created now in plan mode)
2. **Approve or adjust** the plan before execution begins
3. **Run Phase 7** — execute the plan, iterating until quality bar met
4. **Phases 8-9** follow sequentially, each with its own plan-then-execute cycle

## Cross-Phase Alignment

- Phase 7 discovers issues -> Phase 8 documents the fixes -> Phase 9 automates the checks
- All three phases share the QA principle: fix everything before moving on
- Testing infrastructure built in Phase 9 codifies what was manually validated in Phase 7
- Documentation in Phase 8 captures what was learned in Phase 7
