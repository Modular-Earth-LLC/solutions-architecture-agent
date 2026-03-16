# NEXT STEPS — Phases 8-9 Roadmap

**Date**: 2026-03-16
**Status**: Phase 7 complete. Phase 8 ready to plan.

## Phase 7: Integration Testing & Optimization — COMPLETE

**Result**: All exit criteria met. See `phase-7-results.md` for full details.

- 11/11 KB schema validations PASS, 5/5 consistency checks PASS
- 4 reviews all PASS (scores: 8.4, 8.1, 8.1, 7.9; avg 8.125)
- 2 issues found and fixed (both generic): `$depends_on` consistency, integration_plan DAG ordering
- All Phase 6 deferred issues (A1-A6) resolved
- Error paths verified (D1-D4)
- Case study: IBMi/AS/400 healthcare modernization (migration flow, HIPAA, 500+ users)

### Key Learnings for Downstream Phases
1. **Skills work end-to-end** — all 9 skills produce schema-valid output in correct flow order
2. **Sub-agents not yet tested at runtime** — parallel-wa-reviewer and stride-analyzer output formats validated via schema, but Agent tool invocation deferred
3. **Plugin not yet tested as installed plugin** — skills executed manually; need `claude --plugin-dir .` validation
4. **WebSearch not exercised** — technology recommendations from training data only; real engagements should verify
5. **Proposal output is substantial** (972 lines) — quality is high but needs human review before any client delivery
6. **KB files get large** — security_review ~300 lines, architecture ~200 lines; selective section loading (already in proposal SKILL.md) should be a pattern

## Phase 8: Documentation, Packaging & Plans Cleanup

**Goal**: Make the plugin installable, documented, and clean. Archive development artifacts.

### What Happens
1. **Plugin installation testing**: `claude --plugin-dir .` — verify all 9 skills discoverable as `solutions-architecture-agent:skill-name`
2. **Sub-agent runtime testing**: Invoke parallel-wa-reviewer and stride-analyzer via Agent tool
3. **Documentation overhaul**: Rewrite README.md, ARCHITECTURE.md, CONTRIBUTING.md, docs/getting-started.md
4. **Plans cleanup**: Archive old development plans, keep interview references and results files
5. **Plugin manifest verification**: `.claude-plugin/plugin.json` matches .repo-metadata.json
6. **GitHub configuration**: PR template, issue templates, CODEOWNERS
7. **Phase 6 deferred doc issues**: Fix tests/README.md references, add IaC section to architecture template

### Phase 7 Findings That Inform Phase 8
- Envelope fields note (A1) should be documented in CONTRIBUTING.md for skill authors
- Schema-to-SKILL.md alignment rules should be in CONTRIBUTING.md
- Integration_plan can run before architecture in migration flow — document in engagement lifecycle docs
- KB test data from Phase 7 can serve as example outputs in documentation

### Exit Criteria
- [ ] Plugin loads via `claude --plugin-dir .`
- [ ] All 9 skills invocable with plugin prefix
- [ ] Sub-agents tested at runtime
- [ ] README under 200 lines, clear quick-start
- [ ] ARCHITECTURE.md with Mermaid diagrams
- [ ] CONTRIBUTING.md sufficient to add a 10th skill
- [ ] All documentation free of external filesystem references
- [ ] .repo-metadata.json version matches plugin.json

## Phase 9: QA Automation & Release Readiness

**Goal**: Automate QA, finalize for release.

### What Happens
1. **Test infrastructure**: `tests/test_plugin_structure.py` (plugin packaging), `tests/test_engagement_flow.py` (E2E lifecycle)
2. **`/qa` skill**: Single command to run all validation
3. **Second case study**: Validate genericity with a greenfield AI project
4. **Self-review dogfooding**: Run `/review` on the agent's own architecture docs
5. **Release**: Tag v1.0.0, create GitHub release, test install from GitHub URL

### Phase 7 Findings That Inform Phase 9
- Phase 7's manual validation process should be automated into test scripts
- The $depends_on DAG check and schema validation are already solid — extend, don't rewrite
- Review score thresholds (>= 7.5 PASS, 5.0-7.4 CONDITIONAL, < 5.0 FAIL) should be codified
- A second case study (greenfield, different domain) would prove genericity

## Immediate Next Action

1. **Plan Phase 8** — enter plan mode, design detailed implementation plan
2. **Execute Phase 8** — documentation, packaging, plugin testing
3. **Plan + Execute Phase 9** — QA automation and release
