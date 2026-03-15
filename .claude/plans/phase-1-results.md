# Phase 1: Inventory & Pattern Extraction Results

> Generated: 2026-03-15 | Phase: 1 of 9

---

## File-by-File Disposition Table

### Root Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `CLAUDE.md` | Core agent identity and configuration for Claude Code | 72 | REFACTOR | Rewrite as single SA agent identity (<200 lines) with plugin structure, scope boundary, skill reference | New CLAUDE.md per Phase 5 spec |
| `README.md` | Repository overview, quick start, agent inventory | 365 | REFACTOR | Rewrite for plugin paradigm: SA lifecycle focus, 9 skills, scope boundary (design only, not implementation) | New README.md per Phase 8 spec |
| `ARCHITECTURE.md` | System architecture doc for 23-agent supervisor-worker pattern | 392 | REFACTOR | Rewrite for plugin architecture: skill dispatch, KB data flow, context hierarchy, Mermaid diagrams | New ARCHITECTURE.md per Phase 8 spec |
| `CONTRIBUTING.md` | Contributor guide for multi-agent framework | 815 | REFACTOR | Rewrite for plugin contribution: how to create/modify skills, testing, PR process | New CONTRIBUTING.md per Phase 8 spec |
| `SECURITY.md` | Security vulnerability reporting policy | 27 | KEEP | Standard security policy, vendor-neutral, still applicable | — |
| `LICENSE` | MIT License, Modular Earth LLC | 21 | KEEP | No changes needed | — |
| `.repo-metadata.json` | Single source of truth for version, agent/prompt counts, tech stack | 101 | REFACTOR | Update for plugin structure: remove 23-agent counts, add 9-skill inventory, update tech stack | Reflect plugin structure |
| `.gitignore` | Git ignore patterns for outputs, env, Python, Node, IDEs | 106 | REFACTOR | Add plugin-specific ignores (`.claude-plugin/` dev artifacts), remove obsolete output patterns | Minor updates |
| `.cursorrules` | Cursor IDE documentation writing rules | 151 | DELETE | Cursor IDE is not the target platform; patterns are generic markdown rules not specific to SA scope | Extract any unique patterns before deletion |
| `supervisor_agent.system.prompt.md` | Main supervisor orchestrator for 23-agent system | 1612 | DELETE | Supervisor-worker pattern replaced by single agent + skill dispatch. Patterns extracted below | Extract: routing logic, workflow coordination, scope boundary language |

### `.claude/` Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `.claude/settings.json` | Claude Code project permissions and hooks config | 37 | REFACTOR | Update permissions for plugin structure; update hook paths | Align with new hooks/ directory |
| `.claude/settings.local.json` | Local permission overrides (git-ignored) | 7 | KEEP | Local-only, no changes needed | — |
| `.claude/agents/.gitkeep` | Placeholder for future agents directory | 0 | KEEP | Will hold subagent definitions (parallel-reviewer.md, etc.) | — |
| `.claude/hooks/protect-sensitive-files.sh` | PreToolUse hook blocking edits to .env and private/ files | 19 | REFACTOR | Move to `hooks/` at plugin root per target structure; may need to update to `hooks/hooks.json` format | `hooks/` |
| `.claude/skills/.gitkeep` | Placeholder for skills in .claude/ | 0 | DELETE | Skills go in `skills/` at plugin root, not `.claude/skills/` | — |

### `.claude/rules/` Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `.claude/rules/guiding-principles.md` | 34 core technology values governing all work (unscoped) | 55 | KEEP | Foundational principles; referenced by @import in CLAUDE.md | — |
| `.claude/rules/agent-prompts.md` | Path-scoped rules for editing agent system prompts (ai_agents/**) | 16 | DELETE | Path scope targets `ai_agents/` which will be deleted; agent editing rules no longer relevant | — |
| `.claude/rules/knowledge-base.md` | Path-scoped rules for KB JSON editing (knowledge_base/**) | 13 | REFACTOR | Update file references from old 3-file KB to new 10-file KB schema | Updated KB rules per Phase 5 |
| `.claude/rules/refactoring-direction.md` | Explains refactoring from 23 agents to 1 agent + 9 skills | 24 | DELETE | Temporary refactoring guidance; remove after refactoring completes (Phase 4+) | — |
| `.claude/rules/security.md` | Path-scoped rules for private/ and credential files | 15 | KEEP | Security rules remain valid for plugin structure | — |

### `.claude/plans/` Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `.claude/plans/master-plan.md` | Master plan for 9-phase refactoring | 817 | KEEP | Active planning document; guides all phases | — |
| `.claude/plans/master-planning-prompt.md` | Prompt used to generate the master plan | 412 | KEEP | Historical reference for planning methodology | — |

### `.claude/plans/references/` Directory (git-ignored)

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `.claude/plans/references/.gitkeep` | Placeholder for git-ignored reference dir | 0 | KEEP | Preserves directory in git | — |
| `.claude/plans/references/agent-to-skill-mapping.md` | Maps 23 legacy agents to 9 target skills | 45 | KEEP | Active refactoring reference | — |
| `.claude/plans/references/anthropic-cloud-deployment.md` | Cloud deployment options for agent packaging | 61 | KEEP | Future reference for marketplace/cloud deployment | — |
| `.claude/plans/references/current-claude-code-setup.md` | Current operator environment (plugins, MCP servers) | 49 | KEEP | Local reference (git-ignored); contains operator-specific paths | — |
| `.claude/plans/references/target-architecture.md` | Target plugin structure and design decisions | 54 | KEEP | Active refactoring reference | — |
| `.claude/plans/references/AI-solutions_architecture-technical-design-principles.zip` | ZIP of technical design principles documents | binary | KEEP | Planning reference material (git-ignored) | — |
| `.claude/plans/references/PAI-Take_Home_Exercise.pdf` | PAI exercise case study for testing | binary | KEEP | Test scenario reference (git-ignored) | — |
| `.claude/plans/references/Solution Architect Case Study and Interview.pdf` | SA case study for testing | binary | KEEP | Test scenario reference (git-ignored) | — |

### `.github/` Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `.github/copilot-instructions.md` | GitHub Copilot workspace instructions | 88 | REFACTOR | Update for plugin structure: remove multi-agent references, add skill-based guidance | Align with new architecture |
| `.github/pull_request_template.md` | PR description template | 17 | REFACTOR | Update checklist: remove agent prompt validation, add skill validation | Minor updates |
| `.github/ISSUE_TEMPLATE/bug_report.md` | Bug report issue template | 24 | REFACTOR | Update: replace agent/prompt references with skill references | Minor updates |
| `.github/ISSUE_TEMPLATE/feature_request.md` | Feature request issue template | 19 | REFACTOR | Update: replace agent references with skill/plugin references | Minor updates |
| `.github/workflows/validate-knowledge-base.yml` | GitHub Actions workflow for KB JSON validation | 61 | REFACTOR | Update for 10-file KB schema; enable on push (currently disabled) | Update validation targets |

| `.github/CODEOWNERS` | GitHub code ownership assignments (default + ai_agents/ + KB paths) | 15 | REFACTOR | Update paths: remove `ai_agents/` and `supervisor_agent`, add `skills/`, `agents/`, `hooks/` | Update ownership paths |

### `.vscode/` Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `.vscode/extensions.json` | Recommended VS Code extensions | 13 | KEEP | Editor-agnostic developer tooling; still useful | — |
| `.vscode/settings.json` | VS Code workspace settings for prompt editing | 41 | REFACTOR | Remove `.system.prompt.md` and `.user.prompt.md` file associations; add SKILL.md | Update file associations |
| `.vscode/tasks.json` | VS Code tasks for running validation scripts | 46 | REFACTOR | Update task names and descriptions for plugin context | Minor updates |

### `ai_agents/` Directory (22 files)

All 22 agent system prompts are **DELETE** after pattern extraction. These are the legacy multi-agent system prompts being consolidated into 9 skills.

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `ai_agents/requirements_agent.system.prompt.md` | Requirements discovery and elicitation agent | 1125 | DELETE | Patterns extracted to `/requirements` skill | MERGE patterns into `skills/requirements/SKILL.md` |
| `ai_agents/architecture_agent.system.prompt.md` | System architecture design agent (6-step process) | 1312 | DELETE | Design process extracted to `/architecture` + `/estimate` skills | MERGE patterns into `skills/architecture/SKILL.md` and `skills/estimate/SKILL.md` |
| `ai_agents/optimization_agent.system.prompt.md` | System analysis and improvement agent | 3131 | DELETE | Quality review patterns extracted to `/review` skill | MERGE patterns into `skills/review/SKILL.md` |
| `ai_agents/deployment_agent.system.prompt.md` | Platform deployment coordination agent | 676 | DELETE | Out of SA scope (implementation/deployment) | Patterns already captured in master plan |
| `ai_agents/prompt_engineering_agent.system.prompt.md` | Prompt creation and optimization agent | 942 | DELETE | Out of SA scope (implementation) | Prompt engineering techniques extracted below |
| `ai_agents/engineering_supervisor_agent.system.prompt.md` | Engineering orchestration agent | 611 | DELETE | Out of SA scope (implementation orchestration) | Eliminated in target architecture |
| `ai_agents/knowledge_engineering_agent.system.prompt.md` | Vector DB, RAG, knowledge base agent | 277 | DELETE | Patterns extracted to `/data-model` skill | MERGE patterns into `skills/data-model/SKILL.md` |
| `ai_agents/data_engineering_agent.system.prompt.md` | SQLite, pandas, data layer agent | 402 | DELETE | Out of SA scope (implementation) | — |
| `ai_agents/aws_security_networking_agent.system.prompt.md` | AWS IAM, VPC, Cognito security agent | 396 | DELETE | Security patterns extracted to `/security-review` skill (technology-agnostic) | MERGE patterns into `skills/security-review/SKILL.md` |
| `ai_agents/aws_infrastructure_agent.system.prompt.md` | AWS ECS, CDK, CloudWatch agent | 342 | DELETE | Out of SA scope (implementation); AWS-specific | — |
| `ai_agents/aws_bedrock_agentcore_agent.system.prompt.md` | AWS Bedrock AgentCore agent | 919 | DELETE | Out of SA scope (implementation); AWS-specific | — |
| `ai_agents/aws_bedrock_strands_agent.system.prompt.md` | AWS Bedrock Strands SDK agent | 737 | DELETE | Out of SA scope (implementation); AWS-specific | — |
| `ai_agents/claude_code_agent.system.prompt.md` | Claude Code autonomous coding agent | 982 | DELETE | Out of SA scope (implementation) | — |
| `ai_agents/claude_projects_agent.system.prompt.md` | Claude Projects deployment agent | 298 | DELETE | Out of SA scope (deployment) | — |
| `ai_agents/claude_workspaces_agent.system.prompt.md` | Claude multi-agent orchestration agent | 917 | DELETE | Out of SA scope (implementation) | — |
| `ai_agents/anthropic_agents_sdk_agent.system.prompt.md` | Anthropic Agents SDK agent | 873 | DELETE | Out of SA scope (implementation) | — |
| `ai_agents/mcp_services_agent.system.prompt.md` | Model Context Protocol services agent | 938 | DELETE | Out of SA scope (implementation) | — |
| `ai_agents/langchain_agent.system.prompt.md` | LangChain workflow orchestration agent | 649 | DELETE | Out of SA scope (implementation) | — |
| `ai_agents/streamlit_ui_agent.system.prompt.md` | Streamlit UI development agent | 673 | DELETE | Out of SA scope (implementation) | — |
| `ai_agents/cursor_ide_agent.system.prompt.md` | Cursor IDE configuration agent | 1591 | DELETE | Out of SA scope (IDE tooling) | — |
| `ai_agents/github_copilot_agent.system.prompt.md` | GitHub Copilot and CI/CD agent | 1686 | DELETE | Out of SA scope (implementation) | — |
| `ai_agents/testing_qa_agent.system.prompt.md` | Testing and QA agent (pytest, validation) | 410 | DELETE | Out of SA scope (implementation) | — |

**Subtotal**: 22 files, 19,887 lines -- all DELETE after pattern extraction.

### `knowledge_base/` Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `knowledge_base/system_config.json` | Read-only system configuration with tech refs, Well-Architected defs | 779 | REFACTOR | Evolve to new schema: remove implementation-specific refs, add SA-specific config, update Well-Architected for 6 pillars + all lenses | New `system_config.json` per Phase 6 |
| `knowledge_base/user_requirements.json` | User requirements gathered during discovery | 247 | DELETE | Replaced by new `requirements.json` with richer schema (problem statement, pain points, AI suitability, stakeholders) | New `requirements.json` |
| `knowledge_base/design_decisions.json` | Architecture decisions, costs, project plan (monolithic) | 525 | DELETE | Split into 5+ separate files: `architecture.json`, `estimates.json`, `project_plan.json`, `data_model.json`, etc. | Split across new KB files |
| `knowledge_base/README.md` | Knowledge base usage guide for 3-file model | 288 | REFACTOR | Rewrite for 10-file engagement-centered KB topology | New KB README |
| `knowledge_base/schemas/system_config.schema.json` | JSON Schema for system_config.json | 375 | REFACTOR | Update for new system_config schema | New schema |
| `knowledge_base/schemas/user_requirements.schema.json` | JSON Schema for user_requirements.json | 251 | DELETE | Replaced by new `requirements.schema.json` | New schema |
| `knowledge_base/schemas/design_decisions.schema.json` | JSON Schema for design_decisions.json | 290 | DELETE | Replaced by multiple new schemas (architecture, estimates, etc.) | New schemas |
| `knowledge_base/schemas/.repo-metadata.schema.json` | JSON Schema for .repo-metadata.json | 46 | REFACTOR | Update for new plugin metadata structure | New schema |
| `knowledge_base/schemas/SCHEMA_DESIGN.md` | Schema design document for 10-file KB topology | 2419 | KEEP | Active design reference for Phase 6 KB implementation; already forward-looking | — |

### `templates/` Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `templates/architecture-template.md` | Output template for architecture deliverables | 99 | REFACTOR | Update for `/architecture` skill output format; remove agent references | Align with skill output |
| `templates/requirements-template.md` | Output template for requirements deliverables | 80 | REFACTOR | Update for `/requirements` skill output format | Align with skill output |
| `templates/security-checklist.md` | Security validation checklist for AI systems | 67 | REFACTOR | Update for `/security-review` skill; make technology-agnostic | Align with skill output |
| `templates/development-checklist.md` | Development quality checks before deployment | 69 | DELETE | Development/deployment checklists are out of SA scope (implementation) | — |

### `tests/` Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `tests/validate_knowledge_base.py` | Validates KB JSON files against schemas | 162 | REFACTOR | Update for 10-file KB schema set; add new file validations | Update for new schemas |
| `tests/validate_consistency.py` | Counts agents/prompts and updates .repo-metadata.json | 282 | REFACTOR | Rewrite to count skills instead of agents; update metadata structure | Update for plugin structure |
| `tests/validate_urls.py` | Validates external URLs in markdown files | 183 | KEEP | URL validation still useful; technology-agnostic | — |
| `tests/README.md` | Testing framework documentation | 270 | REFACTOR | Update for plugin testing: skill validation, KB validation, integration tests | Align with new test scope |
| `tests/workflow_validation_checklist.md` | Manual testing checklist for multi-agent workflows | 310 | DELETE | Multi-agent workflow testing obsolete; replaced by skill-based testing in Phase 7 | — |

### `docs/` Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `docs/README.md` | Documentation index/navigation page | 116 | REFACTOR | Rewrite for plugin documentation structure | New docs index |
| `docs/getting-started.md` | First-time user guide (15-min walkthrough) | 121 | REFACTOR | Rewrite for plugin installation: `--plugin-dir`, skill invocation, engagement flows | New getting-started guide |
| `docs/deployment-guide.md` | Platform deployment guide (Cursor, Claude Projects, Copilot) | 88 | DELETE | Deployment is out of SA scope; plugin installation replaces multi-platform deployment | Replaced by getting-started |
| `docs/engineering-agents-guide.md` | Reference for 16 engineering specialist agents | 109 | DELETE | Engineering agents deleted; no equivalent in target architecture | — |
| `docs/workflow_guide.md` | Complete workflow documentation (Req -> Deploy lifecycle) | 114 | REFACTOR | Rewrite for SA skill workflow: engagement flows (0-to-1, migration) | New workflow guide |
| `docs/executive_overview.md` | Business value proposition and ROI analysis | 92 | REFACTOR | Update for SA agent value prop: design acceleration, not implementation acceleration | Align messaging |
| `docs/human-ai-collaboration.md` | Guide for human vs. agent responsibilities | 140 | REFACTOR | Update for SA scope: agent designs, human reviews; remove implementation/deployment references | Align with scope boundary |
| `docs/github-copilot-optimization.md` | GitHub Copilot workspace setup guide | 75 | DELETE | Copilot-specific optimization guide; not relevant to plugin-first architecture | — |
| `docs/examples/email-automation.md` | Example: email automation system design | 117 | DELETE | Example uses multi-agent implementation patterns (code generation); needs SA-only examples | Replaced by Phase 7 test scenarios |

### `outputs/` Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `outputs/README.md` | Output directory structure and organization guide | 348 | DELETE | Output structure references multi-agent prototypes, deployments, code generation; out of SA scope | — |
| `outputs/architecture/.gitkeep` | Placeholder for architecture outputs | 0 | DELETE | Outputs directory restructured in target | — |
| `outputs/deployments/.gitkeep` | Placeholder for deployment outputs | 0 | DELETE | Deployment out of scope | — |
| `outputs/optimizations/.gitkeep` | Placeholder for optimization outputs | 0 | DELETE | Directory structure changes | — |
| `outputs/proposals/.gitkeep` | Placeholder for proposal outputs | 0 | DELETE | Directory structure changes | — |
| `outputs/prototypes/.gitkeep` | Placeholder for prototype outputs | 0 | DELETE | Prototyping out of scope | — |
| `outputs/requirements/.gitkeep` | Placeholder for requirements outputs | 0 | DELETE | Directory structure changes | — |
| `outputs/agent_testing/TESTING_SUMMARY.md` | Test results for 6 agents on Cursor/Claude Projects | 252 | DELETE | Multi-agent testing results; historical only, no reusable patterns | — |
| `outputs/agent_testing/architecture_agent_test.md` | Architecture agent test results | 207 | DELETE | Multi-agent test results; historical | — |
| `outputs/agent_testing/engineering_agent_test.md` | Engineering agent test results | 256 | DELETE | Multi-agent test results; historical | — |
| `outputs/agent_testing/optimization_agent_test.md` | Optimization agent test results | 192 | DELETE | Multi-agent test results; historical | — |
| `outputs/agent_testing/prompt_engineering_agent_test.md` | Prompt engineering agent test results | 241 | DELETE | Multi-agent test results; historical | — |
| `outputs/agent_testing/requirements_agent_test.md` | Requirements agent test results | 248 | DELETE | Multi-agent test results; historical | — |
| `outputs/agent_testing/supervisor_agent_test.md` | Supervisor agent test results | 136 | DELETE | Multi-agent test results; historical | — |
| `outputs/optimizations/ai-engineering-assistant/system-optimization-report-2025-10-10.md` | System-wide optimization report | 559 | DELETE | Historical optimization of multi-agent system; quality metrics outdated | — |

### `private/` Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `private/README.md` | Security guidelines for sensitive data storage | 286 | KEEP | Privacy-preserving workspace documentation; vendor-neutral | — |
| `private/.gitignore` | Gitignore for private directory contents | 34 | KEEP | Protects sensitive files from accidental commits | — |
| `private/sensitive-ai-agent-outputs/.gitignore` | Gitignore for sensitive AI outputs | 27 | KEEP | Protects sensitive AI-generated content | — |

### `user_prompts/requirements/` Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `user_prompts/requirements/quick_discovery.user.prompt.md` | Quick 30-min discovery workshop prompt | 690 | MERGE | Progressive discovery tiers merge into `/requirements` skill | `skills/requirements/SKILL.md` |
| `user_prompts/requirements/standard_discovery.user.prompt.md` | Standard 60-min discovery workshop prompt | 326 | MERGE | Progressive discovery tiers merge into `/requirements` skill | `skills/requirements/SKILL.md` |
| `user_prompts/requirements/comprehensive_workshop.user.prompt.md` | Comprehensive 90-min discovery workshop prompt | 311 | MERGE | Progressive discovery tiers merge into `/requirements` skill | `skills/requirements/SKILL.md` |
| `user_prompts/requirements/extract_requirements.user.prompt.md` | Extract requirements from unstructured notes | 536 | MERGE | Requirements extraction pattern merges into `/requirements` skill | `skills/requirements/SKILL.md` |

### `user_prompts/architecture/` Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `user_prompts/architecture/tech_stack_selection.user.prompt.md` | Technology stack selection prompt | 151 | MERGE | Tech selection merges into `/architecture` skill | `skills/architecture/SKILL.md` |
| `user_prompts/architecture/architecture_diagram_generation.user.prompt.md` | Architecture diagram generation (Mermaid/ASCII) | 754 | MERGE | Diagram generation merges into `/architecture` skill (diagrams sub-mode) | `skills/architecture/SKILL.md` |
| `user_prompts/architecture/team_composition.user.prompt.md` | Team composition planning prompt | 318 | MERGE | Team planning merges into `/estimate` skill | `skills/estimate/SKILL.md` |
| `user_prompts/architecture/loe_estimation.user.prompt.md` | Level of effort estimation prompt | 462 | MERGE | LOE estimation merges into `/estimate` skill | `skills/estimate/SKILL.md` |
| `user_prompts/architecture/cost_estimation.user.prompt.md` | Cost estimation and analysis prompt | 319 | MERGE | Cost analysis merges into `/estimate` skill | `skills/estimate/SKILL.md` |
| `user_prompts/architecture/project_plan_generation.user.prompt.md` | Project plan generation prompt | 216 | MERGE | Project planning merges into `/project-plan` skill | `skills/project-plan/SKILL.md` |

### `user_prompts/proposals/` Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `user_prompts/proposals/discovery_proposal_assembly.user.prompt.md` | Discovery proposal assembly prompt | 335 | MERGE | Proposal assembly merges into `/proposal` skill | `skills/proposal/SKILL.md` |
| `user_prompts/proposals/implementation_proposal_assembly.user.prompt.md` | Implementation proposal assembly prompt | 551 | MERGE | Proposal assembly merges into `/proposal` skill | `skills/proposal/SKILL.md` |
| `user_prompts/proposals/internal_proposal_assembly.user.prompt.md` | Internal proposal assembly prompt | 984 | MERGE | Proposal assembly merges into `/proposal` skill | `skills/proposal/SKILL.md` |
| `user_prompts/proposals/pitch_deck_assembly.user.prompt.md` | Pitch deck assembly prompt | 1144 | MERGE | Proposal assembly merges into `/proposal` skill | `skills/proposal/SKILL.md` |

### `user_prompts/deployment/` Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `user_prompts/deployment/platform_deployment.user.prompt.md` | Platform deployment guide generation | 870 | DELETE | Out of SA scope (deployment/implementation) | — |
| `user_prompts/deployment/testing_strategy.user.prompt.md` | Testing strategy generation | 787 | DELETE | Out of SA scope (implementation) | — |
| `user_prompts/deployment/create_ai_engineering_documentation.user.prompt.md` | AI engineering documentation creation | 85 | DELETE | Out of SA scope (implementation) | — |

### `user_prompts/prompt_engineering/` Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `user_prompts/prompt_engineering/improve_system_of_prompts.user.prompt.md` | System-wide prompt improvement workflow | 367 | DELETE | Out of SA scope (prompt engineering is implementation) | — |
| `user_prompts/prompt_engineering/reduce_prompt_redundancy.user.prompt.md` | Reduce redundancy across prompts | 128 | DELETE | Out of SA scope | — |
| `user_prompts/prompt_engineering/improve_prompt_with_human_in_the_loop.user.prompt.md` | Human-in-the-loop prompt improvement | 44 | DELETE | Out of SA scope | — |
| `user_prompts/prompt_engineering/add_change_to_prompt_if_valid.user.prompt.md` | Validate and apply prompt changes | 53 | DELETE | Out of SA scope | — |
| `user_prompts/prompt_engineering/configure_system_prompt_for_github_copilot_chatmode.user.prompt.md` | Configure system prompt for Copilot chat mode | 57 | DELETE | Out of SA scope; platform-specific | — |

### `user_prompts/engineering/` Directory (19 files)

All 19 engineering user prompts are **DELETE** -- they are out of SA scope (implementation, code generation, infrastructure).

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `user_prompts/engineering/prototype_generation.user.prompt.md` | Prototype code generation prompt | 655 | DELETE | Implementation scope | — |
| `user_prompts/engineering/aws_bedrock/create_bedrock_agent.user.prompt.md` | Create AWS Bedrock agent | 150 | DELETE | Implementation scope | — |
| `user_prompts/engineering/aws_infrastructure/create_cdk_infrastructure.user.prompt.md` | Create AWS CDK infrastructure | 138 | DELETE | Implementation scope | — |
| `user_prompts/engineering/aws_infrastructure/deploy_to_ecs.user.prompt.md` | Deploy to AWS ECS | 168 | DELETE | Implementation scope | — |
| `user_prompts/engineering/aws_security/configure_iam_roles.user.prompt.md` | Configure AWS IAM roles | 134 | DELETE | Implementation scope | — |
| `user_prompts/engineering/claude_integration/implement_streaming.user.prompt.md` | Implement Claude streaming | 121 | DELETE | Implementation scope | — |
| `user_prompts/engineering/claude_integration/integrate_claude_sdk.user.prompt.md` | Integrate Claude SDK | 153 | DELETE | Implementation scope | — |
| `user_prompts/engineering/claude_projects/deploy_to_claude_projects.user.prompt.md` | Deploy to Claude Projects | 106 | DELETE | Implementation scope | — |
| `user_prompts/engineering/cursor_ide/configure_cursorrules.user.prompt.md` | Configure .cursorrules | 284 | DELETE | Implementation scope | — |
| `user_prompts/engineering/knowledge_engineering/ingest_documents.user.prompt.md` | Document ingestion pipeline | 171 | DELETE | Implementation scope | — |
| `user_prompts/engineering/knowledge_engineering/setup_vector_database.user.prompt.md` | Set up vector database | 144 | DELETE | Implementation scope | — |
| `user_prompts/engineering/langchain/build_rag_chain.user.prompt.md` | Build RAG chain with LangChain | 120 | DELETE | Implementation scope | — |
| `user_prompts/engineering/langchain/create_multi_step_chain.user.prompt.md` | Create multi-step LangChain chain | 156 | DELETE | Implementation scope | — |
| `user_prompts/engineering/streamlit_ui/add_sidebar_configuration.user.prompt.md` | Add Streamlit sidebar config | 134 | DELETE | Implementation scope | — |
| `user_prompts/engineering/streamlit_ui/build_chat_interface.user.prompt.md` | Build Streamlit chat interface | 144 | DELETE | Implementation scope | — |
| `user_prompts/engineering/streamlit_ui/create_multi_page_app.user.prompt.md` | Create Streamlit multi-page app | 104 | DELETE | Implementation scope | — |
| `user_prompts/engineering/streamlit_ui/implement_file_upload.user.prompt.md` | Implement Streamlit file upload | 76 | DELETE | Implementation scope | — |
| `user_prompts/engineering/testing/create_pytest_suite.user.prompt.md` | Create pytest test suite | 140 | DELETE | Implementation scope | — |
| `user_prompts/engineering/testing/validate_rag_quality.user.prompt.md` | Validate RAG quality metrics | 183 | DELETE | Implementation scope | — |

### `user_prompts/self_improvement/` Directory (28 files)

All 28 self-improvement prompts are **DELETE** -- they are meta-improvement prompts for the legacy multi-agent system.

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `user_prompts/self_improvement/README.md` | Self-improvement prompt index and usage guide | 256 | DELETE | Multi-agent self-improvement system eliminated | — |
| `user_prompts/self_improvement/detect_errors_and_fix_references.user.prompt.md` | Detect and fix cross-reference errors | 1116 | DELETE | Multi-agent reference fixing obsolete | — |
| `user_prompts/self_improvement/improve_ai_engineering_assistant.user.prompt.md` | System-wide improvement prompt | 97 | DELETE | Multi-agent improvement system eliminated | — |
| `user_prompts/self_improvement/improve_all_documentation.user.prompt.md` | Documentation improvement prompt | 669 | DELETE | Multi-agent docs improvement obsolete | — |
| `user_prompts/self_improvement/improve_architecture_agent.user.prompt.md` | Architecture agent improvement | 72 | DELETE | Agent deleted | — |
| `user_prompts/self_improvement/improve_deployment_agent.user.prompt.md` | Deployment agent improvement | 57 | DELETE | Agent deleted | — |
| `user_prompts/self_improvement/improve_engineering_supervisor.user.prompt.md` | Engineering supervisor improvement | 47 | DELETE | Agent deleted | — |
| `user_prompts/self_improvement/improve_knowledge_base_architecture.user.prompt.md` | KB architecture improvement | 69 | DELETE | KB being redesigned from scratch | — |
| `user_prompts/self_improvement/improve_optimization_agent.user.prompt.md` | Optimization agent improvement | 169 | DELETE | Agent deleted | — |
| `user_prompts/self_improvement/improve_prompt_engineering_agent.user.prompt.md` | Prompt engineering agent improvement | 56 | DELETE | Agent deleted | — |
| `user_prompts/self_improvement/improve_requirements_agent.user.prompt.md` | Requirements agent improvement | 56 | DELETE | Agent deleted | — |
| `user_prompts/self_improvement/improve_supervisor_agent.user.prompt.md` | Supervisor agent improvement | 51 | DELETE | Agent deleted | — |
| `user_prompts/self_improvement/engineering_specialists/improve_anthropic_agents_sdk.user.prompt.md` | Anthropic SDK agent improvement | 51 | DELETE | Agent deleted | — |
| `user_prompts/self_improvement/engineering_specialists/improve_aws_bedrock_agentcore.user.prompt.md` | Bedrock AgentCore improvement | 51 | DELETE | Agent deleted | — |
| `user_prompts/self_improvement/engineering_specialists/improve_aws_bedrock_strands.user.prompt.md` | Bedrock Strands improvement | 51 | DELETE | Agent deleted | — |
| `user_prompts/self_improvement/engineering_specialists/improve_aws_infrastructure_agent.user.prompt.md` | AWS infrastructure agent improvement | 51 | DELETE | Agent deleted | — |
| `user_prompts/self_improvement/engineering_specialists/improve_aws_security_agent.user.prompt.md` | AWS security agent improvement | 51 | DELETE | Agent deleted | — |
| `user_prompts/self_improvement/engineering_specialists/improve_claude_code_agent.user.prompt.md` | Claude Code agent improvement | 56 | DELETE | Agent deleted | — |
| `user_prompts/self_improvement/engineering_specialists/improve_claude_projects_agent.user.prompt.md` | Claude Projects agent improvement | 51 | DELETE | Agent deleted | — |
| `user_prompts/self_improvement/engineering_specialists/improve_claude_workspaces_agent.user.prompt.md` | Claude Workspaces agent improvement | 51 | DELETE | Agent deleted | — |
| `user_prompts/self_improvement/engineering_specialists/improve_cursor_ide_agent.user.prompt.md` | Cursor IDE agent improvement | 51 | DELETE | Agent deleted | — |
| `user_prompts/self_improvement/engineering_specialists/improve_data_engineering_agent.user.prompt.md` | Data engineering agent improvement | 51 | DELETE | Agent deleted | — |
| `user_prompts/self_improvement/engineering_specialists/improve_github_copilot_agent.user.prompt.md` | GitHub Copilot agent improvement | 51 | DELETE | Agent deleted | — |
| `user_prompts/self_improvement/engineering_specialists/improve_knowledge_engineering_agent.user.prompt.md` | Knowledge engineering agent improvement | 51 | DELETE | Agent deleted | — |
| `user_prompts/self_improvement/engineering_specialists/improve_langchain_agent.user.prompt.md` | LangChain agent improvement | 51 | DELETE | Agent deleted | — |
| `user_prompts/self_improvement/engineering_specialists/improve_mcp_services_agent.user.prompt.md` | MCP services agent improvement | 51 | DELETE | Agent deleted | — |
| `user_prompts/self_improvement/engineering_specialists/improve_streamlit_ui_agent.user.prompt.md` | Streamlit UI agent improvement | 51 | DELETE | Agent deleted | — |
| `user_prompts/self_improvement/engineering_specialists/improve_testing_qa_agent.user.prompt.md` | Testing QA agent improvement | 51 | DELETE | Agent deleted | — |

---

## Extracted Patterns

These patterns are extracted inline from the legacy agent prompts and user prompts. After this phase, the source files will be deleted, so all valuable knowledge is preserved here.

### Pattern 1: Progressive Discovery (from requirements_agent + user_prompts/requirements/)

**Source**: `requirements_agent.system.prompt.md`, `quick_discovery.user.prompt.md`, `standard_discovery.user.prompt.md`, `comprehensive_workshop.user.prompt.md`

**Pattern**: Tiered discovery workshops with progressive depth:
- **Quick (30 min)**: Problem statement, key pain points, initial AI suitability assessment. 5-7 targeted questions.
- **Standard (60 min)**: Full requirements elicitation, stakeholder mapping, success criteria, constraints. 12-15 structured questions.
- **Comprehensive (90 min)**: Deep-dive including competitive analysis, data landscape, integration points, migration considerations, organizational readiness. 20+ questions across 6 dimensions.

**Workflow**:
1. Assess engagement complexity to recommend tier
2. Conduct structured interview with progressive questioning
3. Classify pain points by AI suitability (high/medium/low/not suitable)
4. Validate completeness against checklist
5. Write structured output to `requirements.json`

**Target**: `skills/requirements/SKILL.md`

### Pattern 2: 6-Step Design Process (from architecture_agent + user_prompts/architecture/)

**Source**: `architecture_agent.system.prompt.md`, all 6 architecture user prompts

**Pattern**: Sequential architecture design following TDSP-inspired process:
1. **Tech Stack Selection**: Evaluate options against requirements, constraints, team skills; produce comparison matrix with rationale
2. **Architecture Diagram Generation**: Create system diagrams in Mermaid and ASCII; support high-level, detailed component, and deployment views
3. **Team Composition**: Define roles, skills needed, team structure, skill gap analysis
4. **LOE Estimation**: Break work into phases with T-shirt sizing, confidence levels (high/medium/low), and risk factors
5. **Cost Estimation**: Infrastructure costs, team costs, licensing, total cost of ownership with monthly/annual projections
6. **Project Plan Generation**: Phase-based roadmap with milestones, dependencies, decision gates

**In target architecture**: Steps 1-2 map to `/architecture`, Steps 3-5 map to `/estimate`, Step 6 maps to `/project-plan`.

**Target**: `skills/architecture/SKILL.md`, `skills/estimate/SKILL.md`, `skills/project-plan/SKILL.md`

### Pattern 3: Well-Architected Compliance (from architecture_agent, optimization_agent, system_config.json)

**Source**: `architecture_agent.system.prompt.md`, `optimization_agent.system.prompt.md`, `knowledge_base/system_config.json`

**Pattern**: Every architecture design evaluated against multi-cloud Well-Architected frameworks:
- **AWS**: 6 pillars (Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability) + GenAI Lens (model selection, prompt engineering, RAG, multi-agent, responsible AI) + Responsible AI Lens + ML Lens
- **Azure**: 5 pillars + dedicated AI workload section with maturity models
- **GCP**: 5 pillars + AI/ML cross-pillar perspective

**Application**: Score each pillar 1-10, identify gaps, recommend improvements. Used in both `/architecture` design and `/review` quality assessment.

**Target**: All skills (cross-cutting concern), primarily `skills/architecture/SKILL.md` and `skills/review/SKILL.md`

### Pattern 4: Generate-Validate-Improve (TRM) (from optimization_agent)

**Source**: `optimization_agent.system.prompt.md` (3131 lines -- largest agent)

**Pattern**: Test-Time Recursive Majority (TRM) validation cycle:
1. **Generate**: Produce candidate deliverable
2. **Validate**: Score against quality rubric (completeness, technical soundness, well-architected alignment, clarity, feasibility)
3. **Improve**: Apply feedback, re-generate with improvements
4. **Re-validate**: Score again, iterate up to 3 rounds

**Scoring dimensions** (each 1-10):
- Completeness: Does it cover all requirements?
- Technical Soundness: Are the design decisions defensible?
- Well-Architected Alignment: Does it meet framework criteria?
- Clarity: Is it understandable to the target audience?
- Feasibility: Can it be implemented within constraints?

**Target**: `skills/review/SKILL.md` (LLM-as-judge, 3 iterations)

### Pattern 5: Confidence & Escalate (from architecture_agent, cost/LOE prompts)

**Source**: `architecture_agent.system.prompt.md`, `cost_estimation.user.prompt.md`, `loe_estimation.user.prompt.md`

**Pattern**: All estimates include confidence scoring with threshold-based human escalation:
- **High confidence (>80%)**: Present estimate directly
- **Medium confidence (50-80%)**: Present estimate with caveats and assumptions
- **Low confidence (<50%)**: Flag for human review, explain uncertainty sources

Estimates always include:
- Point estimate with range (optimistic/pessimistic)
- Key assumptions
- Risk factors that could change the estimate
- Comparison to industry benchmarks when available

**Target**: `skills/estimate/SKILL.md`

### Pattern 6: Proposal Assembly from KB (from user_prompts/proposals/)

**Source**: All 4 proposal user prompts (discovery, implementation, internal, pitch)

**Pattern**: Assembly of executive deliverables by reading structured KB state:
1. Read all relevant KB files (requirements, architecture, estimates, project plan)
2. Select proposal template (discovery / implementation / internal / pitch deck)
3. Map KB data to template sections
4. Generate executive-appropriate language (adjust technical depth by audience)
5. Include evidence-based recommendations with justifications

**Proposal types**:
- **Discovery Proposal**: Scope, approach, timeline, cost for a discovery engagement
- **Implementation Proposal**: Full technical proposal with architecture, estimates, plan
- **Internal Proposal**: Business case for internal stakeholders (ROI-focused)
- **Pitch Deck**: High-level presentation format (problem, solution, approach, team, timeline, cost)

**Target**: `skills/proposal/SKILL.md`

### Pattern 7: Prompt Engineering Techniques (from prompt_engineering_agent, optimization_agent)

**Source**: `prompt_engineering_agent.system.prompt.md`, `optimization_agent.system.prompt.md`

**Pattern**: Techniques for producing high-quality SA deliverables:
- **Chain-of-Thought (CoT)**: Step-by-step reasoning for complex design decisions (25-40% improvement on reasoning tasks)
- **Step-Back Prompting**: Abstract from specifics to general principles before solving (15-20% improvement)
- **MODP (Multiple Output Decision Procedure)**: Generate multiple candidates, evaluate each, select best (26% improvement)
- **Tree-of-Thoughts**: Explore branching design alternatives with backtracking (20-35% improvement)
- **ultrathink**: Extended reasoning for deep analysis (architecture, data modeling, security review, quality review)

**Application in skills**: Use `ultrathink` in `/architecture`, `/data-model`, `/security-review`, `/review`.

**Target**: Applied across all skills; explicitly invoked in complex skills

### Pattern 8: Dual-Persona Validation (from optimization_agent, testing_qa_agent)

**Source**: `optimization_agent.system.prompt.md`, `testing_qa_agent.system.prompt.md`

**Pattern**: Builder generates, Tester validates:
1. **Builder persona**: Creates deliverable with best-effort quality
2. **Tester persona**: Reviews with adversarial mindset -- finds gaps, inconsistencies, missing requirements
3. **Reconciliation**: Merge findings, prioritize fixes, produce improved version

**Target**: Embedded within `skills/review/SKILL.md` (LLM-as-judge pattern)

### Pattern 9: Phased Delivery with Decision Gates (from architecture_agent, project_plan prompt)

**Source**: `architecture_agent.system.prompt.md`, `project_plan_generation.user.prompt.md`

**Pattern**: All project plans follow phased delivery:
- **Phase 1 (MVP/Foundation)**: Core functionality, minimum viable architecture, proof of value
- **Phase 2 (Enhancement)**: Extended features, performance optimization, security hardening
- **Phase 3 (Scale)**: Production readiness, monitoring, scaling, operational maturity

Each phase has:
- Clear deliverables and success criteria
- Decision gate (go/no-go) before proceeding
- Cost and timeline estimates
- Risk assessment
- Dependencies on prior phases

**Target**: `skills/project-plan/SKILL.md`

### Pattern 10: Security-First Design (from aws_security_networking_agent, security-checklist)

**Source**: `aws_security_networking_agent.system.prompt.md`, `templates/security-checklist.md`

**Pattern**: Security integrated into every design decision (technology-agnostic):
- **Zero Trust**: Verify explicitly, use least privilege, assume breach
- **Defense in depth**: Multiple security layers (network, application, data, identity)
- **Encryption**: At rest and in transit, key management strategy
- **Compliance mapping**: Map requirements to frameworks (HIPAA, SOC2, CCPA, GLBA, etc.)
- **Threat modeling**: STRIDE-based threat identification and mitigation
- **IAM**: Role-based access control, just-in-time access, MFA
- **Data protection**: Classification, retention, disposal, PII handling
- **Incident response**: Detection, response, recovery procedures

**Target**: `skills/security-review/SKILL.md`

---

## Deletion Plan

### Files to Delete (by directory)

| Directory | File Count | Total Lines | Justification |
|-----------|-----------|-------------|---------------|
| `ai_agents/` | 22 | 19,887 | All agent system prompts replaced by 9 skills; patterns extracted above |
| `supervisor_agent.system.prompt.md` | 1 | 1,612 | Supervisor-worker pattern replaced by single agent + skill dispatch |
| `user_prompts/engineering/` | 19 | 3,281 | Out of SA scope (implementation) |
| `user_prompts/self_improvement/` | 28 | 3,536 | Multi-agent self-improvement system eliminated |
| `user_prompts/deployment/` | 3 | 1,742 | Out of SA scope (deployment) |
| `user_prompts/prompt_engineering/` | 5 | 649 | Out of SA scope (prompt engineering is implementation) |
| `outputs/` (all contents) | 15 | 2,439 | Multi-agent test results and output structure obsolete |
| `.cursorrules` | 1 | 151 | Cursor IDE not target platform |
| `.claude/skills/.gitkeep` | 1 | 0 | Skills go in `skills/` at root, not `.claude/skills/` |
| `.claude/rules/agent-prompts.md` | 1 | 16 | Path scope targets deleted `ai_agents/` |
| `.claude/rules/refactoring-direction.md` | 1 | 24 | Temporary guidance; remove after refactoring |
| `knowledge_base/user_requirements.json` | 1 | 247 | Replaced by new `requirements.json` |
| `knowledge_base/design_decisions.json` | 1 | 525 | Split into multiple new KB files |
| `knowledge_base/schemas/user_requirements.schema.json` | 1 | 251 | Replaced by new schema |
| `knowledge_base/schemas/design_decisions.schema.json` | 1 | 290 | Replaced by new schemas |
| `templates/development-checklist.md` | 1 | 69 | Implementation scope |
| `tests/workflow_validation_checklist.md` | 1 | 310 | Multi-agent workflow testing obsolete |
| `docs/deployment-guide.md` | 1 | 88 | Out of SA scope |
| `docs/engineering-agents-guide.md` | 1 | 109 | Engineering agents deleted |
| `docs/github-copilot-optimization.md` | 1 | 75 | Platform-specific, not relevant |
| `docs/examples/email-automation.md` | 1 | 117 | Multi-agent implementation example |
| **TOTAL DELETE** | **109** | **35,418** | |

### Files to MERGE then Delete

These files are deleted after their content merges into target skills:

| Source | Lines | Target Skill |
|--------|-------|-------------|
| `user_prompts/requirements/` (4 files) | 1,863 | `skills/requirements/SKILL.md` |
| `user_prompts/architecture/` (6 files) | 2,220 | `skills/architecture/SKILL.md` + `skills/estimate/SKILL.md` + `skills/project-plan/SKILL.md` |
| `user_prompts/proposals/` (4 files) | 3,014 | `skills/proposal/SKILL.md` |
| **TOTAL MERGE** | **14 files, 7,097 lines** | **→ 5 skills** |

---

## Disposition Summary

| Disposition | File Count | Total Lines | Percentage (files) |
|-------------|-----------|-------------|-------------------|
| **DELETE** | 109 | 35,418 | 62.3% |
| **MERGE** (then delete) | 14 | 7,097 | 8.0% |
| **KEEP** | 17 | ~1,390 + binaries | 9.7% |
| **REFACTOR** | 15 | ~3,700 | 8.6% |
| **NEW** (phase-1-results.md) | 1 | — | 0.6% |
| **BINARY** (git-ignored refs) | 3 | — | 1.7% |
| **.gitkeep** (structure only) | 16 | 0 | 9.1% |
| **TOTAL** | **175** | **~47,605** | **100%** |

Note: 175 is the pre-existing file count (before phase-1-results.md was created). The .gitkeep files are counted within their directory dispositions above. Binary reference files are git-ignored planning materials.

### After Cleanup (projected)

| Category | Files | Notes |
|----------|-------|-------|
| KEEP (unchanged) | 17 | LICENSE, SECURITY.md, guiding-principles.md, security.md, settings.local.json, plans/, references/, private/, validate_urls.py, extensions.json, SCHEMA_DESIGN.md, .claude/agents/.gitkeep |
| REFACTOR (modified) | 15 | CLAUDE.md, README.md, ARCHITECTURE.md, CONTRIBUTING.md, .repo-metadata.json, .gitignore, settings.json, hooks, KB files, templates, tests, .github (CODEOWNERS, copilot-instructions, PR template, issue templates, workflow), .vscode |
| NEW (Phase 4+) | ~20+ | .claude-plugin/plugin.json, 9 skills/*/SKILL.md, agents/, hooks/hooks.json, 7 new KB JSON files, new schemas, new templates |
| **Projected total** | **~52** | Down from 175 files; significantly reduced complexity |

### Lines Removed vs. Added

- **Lines removed**: ~42,515 (DELETE + MERGE sources)
- **Lines refactored**: ~3,700 (existing files updated)
- **Lines added (estimated)**: ~5,000-8,000 (9 skills, 7 new KB files, schemas, templates, docs)
- **Net reduction**: ~35,000-37,000 lines (~75% reduction)

---

## Top 10 Extracted Patterns

1. **Progressive Discovery** -- Tiered workshops (quick/standard/comprehensive) with AI suitability scoring
2. **6-Step Design Process** -- Tech Stack, Diagrams, Team, LOE, Cost, Project Plan
3. **Well-Architected Compliance** -- Multi-cloud 6-pillar + GenAI Lens evaluation
4. **Generate-Validate-Improve (TRM)** -- 3-iteration quality cycle with 5-dimension scoring
5. **Confidence & Escalate** -- Estimates with confidence bands and human escalation thresholds
6. **Proposal Assembly from KB** -- 4 proposal types assembled from structured state
7. **Prompt Engineering Techniques** -- CoT, Step-Back, MODP, Tree-of-Thoughts, ultrathink
8. **Dual-Persona Validation** -- Builder generates, Tester validates
9. **Phased Delivery with Decision Gates** -- MVP, Enhancement, Scale with go/no-go gates
10. **Security-First Design** -- Zero Trust, defense-in-depth, STRIDE, compliance mapping

---

## Uncertain Dispositions

| File | Uncertainty | Recommendation |
|------|------------|----------------|
| `.claude/rules/refactoring-direction.md` | DELETE now or after Phase 4? | **Recommend: DELETE in Phase 4** -- still useful during Phases 2-3 |
| `outputs/` directory structure | DELETE entire directory or keep empty structure? | **Recommend: DELETE all contents**, remove from .gitignore; skills write to `outputs/` dynamically |
| `.github/CODEOWNERS` | 15 lines; verified. Paths reference `ai_agents/` and `supervisor_agent` which will be deleted | **REFACTOR** -- update paths to `skills/`, `agents/`, `hooks/` |
| `docs/executive_overview.md` | Could be merged into README or kept separate | **Recommend: REFACTOR** -- useful for business audiences, update messaging for SA scope |
| `docs/human-ai-collaboration.md` | Overlaps with CLAUDE.md scope boundary | **Recommend: REFACTOR** -- valuable content about human review expectations |

---

## Human Checkpoint

**File counts by disposition** (175 pre-existing files):
- DELETE: 109 files (35,418 lines)
- MERGE: 14 files (7,097 lines) -- content absorbed into skills, then files deleted
- KEEP: 17 files (~1,390 lines + 3 binary reference files)
- REFACTOR: 15 files (~3,700 lines)

**Projected repo after cleanup**: ~50 files, ~8,000-12,000 lines (down from 175 files, ~47,605 lines)

**Top 10 extracted patterns**: All 10 patterns documented inline above with source attribution and target skill mapping.

**Uncertain dispositions**: 5 items flagged for human review (see table above).

**Ready for Phase 2**: Requirements & Workflow Design. All patterns needed for skill definition are captured in this document.
