<role>
You are a senior engineer performing a controlled repository restructuring into a Claude Code plugin.
</role>

<instructions>
Phase 4: Cleanup & Restructure.

Read these files IN ORDER:
1. .claude/plans/technical-design.md — Section 1 (target directory layout), Section 9 (plugin manifest), Section 11 (Phase 4 Handoff with detailed checklist)
2. .claude/plans/phase-1-results.md — "Deletion Plan" section and "File Inventory" tables for all DELETE/MERGE dispositions

CRITICAL: Section 11 of technical-design.md has the complete Phase 4 execution checklist. Follow it step by step.

Execute IN ORDER:

1. **Create target directories** (from technical-design.md Section 1):
   - skills/requirements/, skills/architecture/, skills/estimate/, skills/project-plan/
   - skills/proposal/, skills/data-model/, skills/security-review/, skills/integration-plan/, skills/review/
   - agents/
   - hooks/
   - .claude-plugin/
   - outputs/ (for /proposal output, with .gitkeep)

2. **Create .claude-plugin/plugin.json** with the exact manifest from technical-design.md Section 9.2

3. **Delete files marked DELETE** in phase-1-results.md:
   - ALL files in ai_agents/ (22 files)
   - supervisor_agent.system.prompt.md
   - ALL files in user_prompts/engineering/ (19 files)
   - ALL files in user_prompts/self_improvement/ (28 files)
   - ALL files in user_prompts/deployment/ (3 files)
   - ALL files in user_prompts/prompt_engineering/ (5 files)
   - ALL contents of outputs/ directory (15 files, keep outputs/ dir with .gitkeep)
   - .cursorrules
   - knowledge_base/user_requirements.json
   - knowledge_base/design_decisions.json
   - knowledge_base/schemas/user_requirements.schema.json
   - knowledge_base/schemas/design_decisions.schema.json
   - docs/deployment-guide.md, docs/engineering-agents-guide.md
   - docs/github-copilot-optimization.md, docs/examples/email-automation.md
   - templates/development-checklist.md
   - tests/workflow_validation_checklist.md
   - .claude/rules/agent-prompts.md (path scope targets deleted directory)
   - .claude/rules/refactoring-direction.md (temporary guidance, no longer needed)
   - .claude/skills/.gitkeep (skills go in skills/ at plugin root)

4. **Remove empty directories** after deletions:
   - ai_agents/
   - user_prompts/ (and all subdirectories)
   - Any empty subdirectories

5. **Move content** (if any exists at source):
   - .claude/skills/* → skills/ at plugin root
   - .claude/hooks/* → hooks/ at plugin root

6. **Update .gitignore** — CRITICAL for PII protection (NFR-017, NFR-018):
   Add these patterns:
   ```
   # Knowledge base engagement data (may contain PII)
   knowledge_base/*.json
   !knowledge_base/system_config.json

   # Proposal outputs (client-specific)
   outputs/

   # Local settings
   .claude/settings.local.json

   # Reference materials (git-ignored, may contain proprietary content)
   .claude/plans/references/*
   !.claude/plans/references/.gitkeep
   !.claude/plans/references/README.md
   ```

7. **Update .repo-metadata.json** for plugin structure:
   - skill_count: 9
   - agent_count: 2
   - Remove old multi-agent counts
   - Preserve version number

8. **Remove ALL external filesystem references** from remaining tracked files:
   - Search for: C:\dev\, \\wsl.localhost\, D:\dev\
   - Remove or replace with relative paths

9. **Verify final state**:
   - Run git status to show all changes
   - Verify all target directories from Section 1 exist
   - Verify no orphan files remain
   - Verify no external filesystem references in tracked files

KB FILE NAME NORMALIZATION (from technical-design.md Decision 6):
If any remaining file references old KB names, update them:
- security_assessment.json → security_review.json
- integration_map.json → integration_plan.json
- estimates.json → estimate.json
</instructions>

<constraints>
- Do NOT delete KEEP or REFACTOR files.
- Do NOT delete .claude/plans/ — planning artifacts are permanent.
- Do NOT delete knowledge_base/system_config.json or knowledge_base/schemas/SCHEMA_DESIGN.md.
- Do NOT write CLAUDE.md, SKILL.md files, or agent definitions — those are Phase 5.
- Do NOT write KB JSON data files or schema files — those are Phase 6.
- Keep knowledge_base/, templates/, tests/ structures intact (delete only specific files listed above).
- Verify phase-1 deletion plan was human-approved (it was — Phase 1 completed and pushed to main).
</constraints>

<git>
git add -A
git commit -m "Phase 4: Repository restructured as Claude Code plugin"
</git>

<human_checkpoint>
Present:
- Deleted file count and total lines removed
- Created directories and new files
- Modified configuration files
- .gitignore changes for PII protection
- git status showing all changes
- Confirmation: zero external filesystem references in tracked files
- Confirmation: target directory structure matches technical-design.md Section 1

Wait for human review before Phase 5.
</human_checkpoint>
