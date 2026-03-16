# Claude Code CLI Execution Prompt: End-to-End Comprehensive Repository Review

Use this prompt as-is in Claude Code CLI to execute the full review lifecycle for this repository.

## Role
You are a Distinguished Software Architect and Staff+ code reviewer performing a complete LLM-as-judge audit of the Solutions Architecture Agent repository.

## Primary Objective
Execute all review phases completely, from baseline validation through final synthesis, and produce one final comprehensive review report.

## Hard Constraints
- Do NOT implement or apply fixes.
- Do NOT modify source files, tests, workflows, schemas, or documentation.
- Allowed writes are limited to review artifacts under .claude/plans only.
- If you identify defects, record them with precise remediation instructions, but do not edit code.
- Preserve repository scope boundary: this project designs solutions, it does not implement deployment/runtime systems.

## Repository Context
- Repo: solutions-architecture-agent
- Branch: main
- Date context: 2026-03-16
- Platform: Claude Code plugin architecture with skills and sub-agents

## Canonical Input Instructions
Read and follow all of these before review work:
1. CLAUDE.md
2. .github/copilot-instructions.md
3. .claude/rules/guiding-principles.md
4. .claude/rules/knowledge-base.md
5. .claude/rules/security.md
6. .claude/rules/skills.md
7. .claude/plans/copilot-comprehensive-review-prompt.md

## Phase Execution Plan
Execute all phases in order. Complete each phase before moving forward unless a phase is explicitly marked parallelizable.

### Phase 0: Scope Lock and Assumptions
1. Confirm review coverage includes all 8 categories in .claude/plans/copilot-comprehensive-review-prompt.md.
2. Record assumptions and ambiguities before analysis starts:
- Schema-count interpretation rules.
- URL validator CI inclusion status.
- Any prompt-to-repository path/name mismatches.
3. Create a working notes file:
- .claude/plans/comprehensive-review-working-notes-2026-03-16.md

### Phase 1: Baseline Validation Evidence
Run these commands with the workspace virtual environment Python executable and capture outputs in the working notes file:
1. c:/dev/solutions-architecture-agent/.venv/Scripts/python.exe tests/validate_consistency.py
2. c:/dev/solutions-architecture-agent/.venv/Scripts/python.exe tests/validate_knowledge_base.py
3. c:/dev/solutions-architecture-agent/.venv/Scripts/python.exe tests/test_plugin_structure.py
4. c:/dev/solutions-architecture-agent/.venv/Scripts/python.exe tests/test_engagement_flow.py
5. c:/dev/solutions-architecture-agent/.venv/Scripts/python.exe tests/test_skill_independence.py
6. c:/dev/solutions-architecture-agent/.venv/Scripts/python.exe tests/validate_urls.py

For each command, record:
- status: pass/fail
- summary counts
- key failing items and affected files

### Phase 2: Focused Review Pass A (Category 1 + Category 8)
Review architecture and minimalism/elegance across:
- ARCHITECTURE.md
- CLAUDE.md
- DESIGN_RATIONALE.md
- .repo-metadata.json
- .claude-plugin/plugin.json
- knowledge_base/schemas/*.schema.json
- knowledge_base/system_config.json

Evaluate:
- Blackboard pattern correctness and coupling boundaries
- $depends_on graph integrity
- schema strictness/permissiveness tradeoffs
- manifest quality and convention alignment
- over-engineering, unnecessary complexity, removable components

### Phase 3: Focused Review Pass B (Category 2 + Category 3)
Review skill and sub-agent quality across:
- skills/*/SKILL.md (all 9)
- agents/parallel-wa-reviewer.md
- agents/stride-analyzer.md

Evaluate:
- frontmatter correctness
- six-section structure adherence
- prerequisite handling is advisory, not blocking
- workflow clarity and actionability
- output rule precision for schema-compliant JSON
- repetition and possible consolidation
- least-privilege tool grants
- ultrathink usage appropriateness
- prompt anti-patterns

### Phase 4: Focused Review Pass C (Category 4 + Category 6)
Review testing and DevOps across:
- tests/*.py
- .github/workflows/validate-knowledge-base.yml
- hooks/hooks.json
- .gitignore
- .vscode/tasks.json

Evaluate:
- structural test completeness and edge cases
- missing behavioral/runtime tests
- CI workflow quality and omissions
- pre-commit protections
- automation gaps and operational risk

### Phase 5: Focused Review Pass D (Category 5 + Category 7)
Review docs and security/privacy across:
- README.md
- CONTRIBUTING.md
- ARCHITECTURE.md
- DESIGN_RATIONALE.md
- CODE_OF_CONDUCT.md
- SECURITY.md
- docs/*.md
- examples/README.md
- tests/README.md
- knowledge_base/README.md
- knowledge_base/schemas/SCHEMA_DESIGN.md
- .claude/rules/security.md
- hooks/hooks.json
- .gitignore
- private/README.md

Evaluate:
- completeness, correctness, staleness, and duplication
- broken links and unsupported claims
- security posture for client-sensitive data handling
- hardcoded secrets/PII/path leakage risks

### Phase 6: One Full Comprehensive Pass
Run one complete cross-category pass over the entire repository after Phases 2-5 are done.

Goal:
- find cross-category interactions missed in focused passes
- deduplicate repeated issues
- normalize severity and remediation language

### Phase 7: Synthesis and Final Report
Create one final report at:
- .claude/plans/comprehensive-review-v1.0.0-2026-03-16.md

The report MUST use this exact structure:

# Comprehensive Review: Solutions Architecture Agent v1.0.0

## Summary
[2-3 sentence overall assessment]
[Overall quality score: 1-10]
[Top 3 strengths]
[Top 3 systemic weaknesses]

## Critical Issues (Must Fix Before Release)
### C-001: [Title]
- File: [exact path]
- Lines: [line range]
- Problem: [specific description]
- Impact: [why this matters]
- Fix: [exact recommended change]

## High Priority Issues (Should Fix)
### H-001: [Title]
- File: [exact path]
- Lines: [line range]
- Problem: [specific description]
- Impact: [why this matters]
- Fix: [exact recommended change]

## Medium Priority Issues (Recommended)
### M-001: [Title]
- File: [exact path]
- Lines: [line range]
- Problem: [specific description]
- Impact: [why this matters]
- Fix: [exact recommended change]

## Low Priority / Polish
### L-001: [Title]
- File: [exact path]
- Lines: [line range]
- Problem: [specific description]
- Impact: [why this matters]
- Fix: [exact recommended change]

## Enhancement Opportunities
### E-001: [Title]
- Description: [what could be added/improved]
- Value: [why it matters]
- Effort: [low/medium/high]

## Files Reviewed
[Complete list of every file reviewed with line counts]

## Baseline Validation Evidence
[One subsection per Phase 1 script with command, status, and key output]

### Release Gate Decision
- Gate rule: BLOCK if any unresolved Critical or High issues exist
- Decision: [BLOCKED/NOT BLOCKED]
- Rationale: [explicit list of unresolved Critical/High IDs]

## Issue Quality Rules (Mandatory)
- Every finding must reference a specific file and location.
- Every finding must include a recommended solution.
- Group related findings; avoid duplicate issue spam.
- Distinguish defects from improvements.
- Keep recommendations implementation-ready but do not apply changes.
- Do not suggest scope-violating features (no implementation/deployment scope creep).
- Do not include duration/time-estimate promises.
- Do not include commented-out-code recommendations.

## Severity Rubric
- Critical: release/safety/security correctness risks that block release
- High: major reliability, integrity, maintainability, or governance risks
- Medium: important quality gaps with manageable short-term risk
- Low: polish/readability/consistency opportunities

## Parallelization Guidance
After Phase 1, run Phases 2-5 in parallel if tools support it. Keep separate notes per phase, then merge in Phase 6.

## Completion Checklist
- [ ] All required instruction files read
- [ ] All six baseline validators executed and captured
- [ ] Categories 1-8 reviewed
- [ ] Full comprehensive pass completed
- [ ] Findings deduplicated and severity-normalized
- [ ] Final report written to .claude/plans/comprehensive-review-v1.0.0-2026-03-16.md
- [ ] Release gate decision documented

## Final Output Requirement
When execution is complete, return a concise completion summary that includes:
1. total findings by severity
2. top 5 systemic risks
3. release gate decision
4. path to the final report file
