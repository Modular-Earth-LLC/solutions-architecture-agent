# Claude Code CLI Remediation Prompt

Use this prompt as-is in Claude Code CLI. Apply all fixes and enhancements below end-to-end.

## Mission
You are the implementation agent for the Solutions Architecture Agent repository. Fix all identified issues and implement listed enhancements with minimal, targeted diffs. Preserve architecture and scope boundaries.

## Hard Constraints
1. Do not change the core architecture (single agent + skills + sub-agents + blackboard KB).
2. Do not modify engagement output examples unless required by schema or test correctness.
3. Keep changes deterministic and explicit.
4. After each phase, run validation and record output.
5. No commented-out code.

## Critical Fixes (Release Blocking)

### C-001: Repair URL validation reliability
- Files:
1. tests/validate_urls.py
- Changes:
1. Replace permissive extraction regex with safer parsing and URL normalization.
2. Strip trailing punctuation/artifacts before checks.
3. Exclude non-documentation operational markdown (for example, `.claude/plans/archive/**`) or use explicit include paths.
4. Add deterministic reporting of skipped paths and normalized URLs.
- Acceptance criteria:
1. False-positive URLs containing trailing `"`, "`", or commas no longer fail.
2. `tests/validate_urls.py` fails only on truly inaccessible links.

### C-002: Align WA multi-cloud standard with system technical references
- Files:
1. knowledge_base/system_config.json
- Changes:
1. Add `technical_references.azure_openai` with WAF/security/reliability/core docs.
2. Add `technical_references.google_vertex` with architecture framework/security/AI docs.
3. Keep structure and style aligned with existing `aws_general` and other reference sections.
- Acceptance criteria:
1. `tests/validate_well_architected.py` passes.
2. No schema validation regressions.

## High Priority Fixes

### H-001: Expand CI to cover full QA matrix
- Files:
1. .github/workflows/validate-knowledge-base.yml
- Changes:
1. Install dependencies required for URL validation (`requests`) in CI.
2. Add steps for:
	- `python tests/validate_urls.py`
	- `python tests/validate_well_architected.py`
	- `python tests/test_unit_contracts.py`
	- `python tests/test_integration_flow.py`
	- `python tests/test_end_to_end_example.py`
- Acceptance criteria:
1. Workflow runs full matrix on PR and manual dispatch.

### H-002: Update metadata validation script inventory
- Files:
1. .repo-metadata.json
- Changes:
1. Update `maintenance.validation_scripts` to reflect all maintained QA scripts.
- Acceptance criteria:
1. Inventory matches repository test surface.

### H-003: Update contributor documentation test count and CI statement
- Files:
1. CONTRIBUTING.md
2. tests/README.md
- Changes:
1. Replace outdated "5 automated test scripts" language with current matrix.
2. Update CI section to reflect actual scripts run by workflow.
3. Add short section for unit/integration/e2e/WA validation scripts.
- Acceptance criteria:
1. Docs match current workflow and local commands.

### H-004: Make sub-agent output contracts deterministic
- Files:
1. agents/parallel-wa-reviewer.md
2. agents/stride-analyzer.md
- Changes:
1. Add explicit JSON output contract blocks with required keys and value constraints.
2. Keep existing semantic requirements but remove format ambiguity.
- Acceptance criteria:
1. Parent skills can parse sub-agent outputs predictably.

### H-005: Refresh stale schema design status header
- Files:
1. knowledge_base/schemas/SCHEMA_DESIGN.md
- Changes:
1. Update version/status header to reflect implemented state.
2. Preserve historical narrative with explicit "historical design context" note.
- Acceptance criteria:
1. Header no longer claims "not yet implemented."

### H-006: Add operational guardrail for LLM-as-judge limitation
- Files:
1. skills/review/SKILL.md
- Changes:
1. Add explicit mandatory human-review threshold language in completion rules.
2. Keep existing scope boundary (review support, not autonomous client delivery authority).
- Acceptance criteria:
1. Review skill instructions clearly enforce human gate where confidence is uncertain.

## Enhancements

### E-001: README first-screen improvement
- Files:
1. README.md
- Changes:
1. Add concise value-first opener and "who this is for" line.

### E-002: Add changelog baseline
- Files:
1. CHANGELOG.md
2. README.md (link)
- Changes:
1. Add Keep-a-Changelog-style file with v1.0.0 baseline.
2. Link changelog from README.

### E-003: Add URL validation scope policy file
- Files:
1. tests/url_validation_scope.json (new)
2. tests/validate_urls.py
- Changes:
1. Move include/exclude path policy into config file.
2. Keep validator deterministic and configurable.

## Execution Order
1. Phase 1: Critical fixes (C-001, C-002)
2. Phase 2: High-priority fixes (H-001 to H-006)
3. Phase 3: Enhancements (E-001 to E-003)
4. Phase 4: Full validation and summary

## Full Validation Commands
Run from repo root using venv python:
1. c:/dev/solutions-architecture-agent/.venv/Scripts/python.exe tests/validate_consistency.py
2. c:/dev/solutions-architecture-agent/.venv/Scripts/python.exe tests/validate_knowledge_base.py
3. c:/dev/solutions-architecture-agent/.venv/Scripts/python.exe tests/test_plugin_structure.py
4. c:/dev/solutions-architecture-agent/.venv/Scripts/python.exe tests/test_engagement_flow.py
5. c:/dev/solutions-architecture-agent/.venv/Scripts/python.exe tests/test_skill_independence.py
6. c:/dev/solutions-architecture-agent/.venv/Scripts/python.exe tests/validate_urls.py
7. c:/dev/solutions-architecture-agent/.venv/Scripts/python.exe tests/validate_well_architected.py
8. c:/dev/solutions-architecture-agent/.venv/Scripts/python.exe tests/test_unit_contracts.py
9. c:/dev/solutions-architecture-agent/.venv/Scripts/python.exe tests/test_integration_flow.py
10. c:/dev/solutions-architecture-agent/.venv/Scripts/python.exe tests/test_end_to_end_example.py

## Output Requirements
When done, return:
1. Change summary grouped by C/H/E IDs.
2. Modified file list.
3. Validation results for all ten commands.
4. Residual risks and follow-up recommendations.

## Quality Bar
1. No regressions in baseline QA scripts.
2. Expanded QA scripts all passing.
3. CI reflects documented test matrix.
4. Scope boundary preserved (design/review agent, not deployment implementation engine).
