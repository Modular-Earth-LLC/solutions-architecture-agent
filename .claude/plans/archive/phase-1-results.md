# Phase 1: Inventory & Pattern Extraction Results

> Generated: 2026-03-15 | Phase: 1 of 9

---

## Executive Summary

**Scope**: Full inventory and pattern extraction from 175 files (~47,600 lines) in a 23-agent multi-agent system being consolidated into 1 agent + 9 skills.

**Disposition Counts**:
| Disposition | Files | Lines |
|---|---|---|
| DELETE | 109 | 35,418 |
| MERGE (into skills, then delete) | 14 | 7,097 |
| KEEP | 17 | ~1,390 + 3 binaries |
| REFACTOR | 15 | ~3,700 |

**Projected post-cleanup**: ~52 files, ~8,000-12,000 lines (~75% reduction).

**Extraction Results**: 6 parallel agents extracted **112 unique patterns** from all 23 agent prompts + 14 user prompts:
- Agent B (Orchestration): 17 patterns from supervisor agents
- Agent C (SA Lifecycle): 25+ patterns from requirements, architecture, deployment, optimization agents + 14 user prompts
- Agent D (LLM/Platform): 36 patterns from Claude Code, Workspaces, SDK, MCP, Prompt Eng, LangChain agents
- Agent E (AWS/DevOps): 29 patterns from AWS Infra/Security/Bedrock/Strands, Testing QA agents
- Agent F (Specialized): 30 patterns from Streamlit, Data Eng, Knowledge Eng, Claude Projects, Copilot, Cursor agents

**All 9 target skills have mapped patterns**. All 23 agents have patterns extracted. No external filesystem references in output.

---

## File Inventory

### Root Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `CLAUDE.md` | Core agent identity and configuration | 72 | REFACTOR | Rewrite as single SA agent identity (<200 lines) with plugin structure | New CLAUDE.md per Phase 5 |
| `README.md` | Repository overview, quick start, agent inventory | 365 | REFACTOR | Rewrite for plugin paradigm: 9 skills, scope boundary | New README.md per Phase 8 |
| `ARCHITECTURE.md` | System architecture doc for 23-agent pattern | 392 | REFACTOR | Rewrite for plugin architecture: skill dispatch, KB data flow | New ARCHITECTURE.md per Phase 8 |
| `CONTRIBUTING.md` | Contributor guide for multi-agent framework | 815 | REFACTOR | Rewrite for plugin contribution: skill creation, testing | New CONTRIBUTING.md per Phase 8 |
| `SECURITY.md` | Security vulnerability reporting policy | 27 | KEEP | Standard security policy, vendor-neutral | -- |
| `LICENSE` | MIT License, Modular Earth LLC | 21 | KEEP | No changes needed | -- |
| `.repo-metadata.json` | Version, agent/prompt counts, tech stack | 101 | REFACTOR | Update for plugin structure: 9-skill inventory | Reflect plugin structure |
| `.gitignore` | Git ignore patterns | 106 | REFACTOR | Add plugin-specific ignores, remove obsolete patterns | Minor updates |
| `.cursorrules` | Cursor IDE documentation writing rules | 151 | DELETE | Cursor IDE not target platform | -- |
| `supervisor_agent.system.prompt.md` | Main supervisor orchestrator for 23-agent system | 1612 | DELETE | Replaced by single agent + skill dispatch | Patterns extracted to Orchestration section |

### `.claude/` Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `.claude/settings.json` | Project permissions and hooks config | 37 | REFACTOR | Update permissions for plugin structure | Align with new hooks/ |
| `.claude/settings.local.json` | Local permission overrides (git-ignored) | 7 | KEEP | Local-only | -- |
| `.claude/agents/.gitkeep` | Placeholder for agents directory | 0 | KEEP | Will hold subagent definitions | -- |
| `.claude/hooks/protect-sensitive-files.sh` | PreToolUse hook blocking edits to .env and private/ | 19 | REFACTOR | Move to `hooks/` at plugin root | `hooks/` |
| `.claude/skills/.gitkeep` | Placeholder for skills in .claude/ | 0 | DELETE | Skills go in `skills/` at plugin root | -- |

### `.claude/rules/` Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `.claude/rules/guiding-principles.md` | 34 core technology values (unscoped) | 55 | KEEP | Foundational; referenced by @import | -- |
| `.claude/rules/agent-prompts.md` | Path-scoped rules for ai_agents/** | 16 | DELETE | Path scope targets deleted directory | -- |
| `.claude/rules/knowledge-base.md` | Path-scoped rules for knowledge_base/** | 13 | REFACTOR | Update for new 10-file KB schema | Updated KB rules per Phase 5 |
| `.claude/rules/refactoring-direction.md` | Refactoring from 23 agents to 1+9 | 24 | DELETE | Temporary guidance; remove after Phase 4 | -- |
| `.claude/rules/security.md` | Path-scoped rules for private/ | 15 | KEEP | Security rules remain valid | -- |

### `.claude/plans/` Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `.claude/plans/master-plan.md` | Master plan for 9-phase refactoring | 817 | KEEP | Active planning document | -- |
| `.claude/plans/master-planning-prompt.md` | Prompt used to generate master plan | 412 | KEEP | Historical reference | -- |
| `.claude/plans/phase-1-results.md` | This file | -- | KEEP | Phase 1 deliverable | -- |

### `.claude/plans/references/` Directory (git-ignored)

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `.claude/plans/references/.gitkeep` | Placeholder | 0 | KEEP | Preserves directory | -- |
| `.claude/plans/references/agent-to-skill-mapping.md` | Legacy agent to target skill mapping | 45 | KEEP | Active refactoring reference | -- |
| `.claude/plans/references/anthropic-cloud-deployment.md` | Cloud deployment options | 61 | KEEP | Future reference | -- |
| `.claude/plans/references/current-claude-code-setup.md` | Current operator environment | 49 | KEEP | Local reference (git-ignored) | -- |
| `.claude/plans/references/target-architecture.md` | Target plugin structure | 54 | KEEP | Active reference | -- |
| `.claude/plans/references/AI-solutions_architecture-technical-design-principles.zip` | Technical design principles | binary | KEEP | Planning reference (git-ignored) | -- |
| `.claude/plans/references/PAI-Take_Home_Exercise.pdf` | PAI exercise case study | binary | KEEP | Test scenario reference (git-ignored) | -- |
| `.claude/plans/references/Solution Architect Case Study and Interview.pdf` | SA case study | binary | KEEP | Test scenario reference (git-ignored) | -- |

### `.github/` Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `.github/copilot-instructions.md` | GitHub Copilot workspace instructions | 88 | REFACTOR | Remove multi-agent references, add skill guidance | Align with new architecture |
| `.github/pull_request_template.md` | PR description template | 17 | REFACTOR | Update checklist for skill validation | Minor updates |
| `.github/ISSUE_TEMPLATE/bug_report.md` | Bug report issue template | 24 | REFACTOR | Replace agent references with skill references | Minor updates |
| `.github/ISSUE_TEMPLATE/feature_request.md` | Feature request issue template | 19 | REFACTOR | Replace agent references with skill/plugin references | Minor updates |
| `.github/workflows/validate-knowledge-base.yml` | GitHub Actions for KB validation | 61 | REFACTOR | Update for 10-file KB schema | Update validation targets |
| `.github/CODEOWNERS` | Code ownership assignments | 15 | REFACTOR | Remove `ai_agents/`, add `skills/`, `agents/`, `hooks/` | Update ownership paths |

### `.vscode/` Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `.vscode/extensions.json` | Recommended VS Code extensions | 13 | KEEP | Editor tooling, still useful | -- |
| `.vscode/settings.json` | VS Code workspace settings | 41 | REFACTOR | Remove `.system.prompt.md` associations; add SKILL.md | Update file associations |
| `.vscode/tasks.json` | VS Code tasks for validation | 46 | REFACTOR | Update for plugin context | Minor updates |

### `ai_agents/` Directory (22 files -- ALL DELETE)

All 22 agent system prompts are DELETE after pattern extraction. Patterns preserved in Extracted Patterns section below.

| Path | Purpose | Lines | Disposition | Target |
|------|---------|-------|-------------|--------|
| `ai_agents/requirements_agent.system.prompt.md` | Requirements discovery agent | 1125 | DELETE | Patterns -> /requirements |
| `ai_agents/architecture_agent.system.prompt.md` | System architecture design (6-step) | 1312 | DELETE | Patterns -> /architecture + /estimate |
| `ai_agents/optimization_agent.system.prompt.md` | System analysis and improvement | 3131 | DELETE | Patterns -> /review |
| `ai_agents/deployment_agent.system.prompt.md` | Platform deployment | 676 | DELETE | Out of SA scope |
| `ai_agents/prompt_engineering_agent.system.prompt.md` | Prompt creation/optimization | 942 | DELETE | Out of SA scope; techniques extracted |
| `ai_agents/engineering_supervisor_agent.system.prompt.md` | Engineering orchestration | 611 | DELETE | Out of SA scope |
| `ai_agents/knowledge_engineering_agent.system.prompt.md` | Vector DB, RAG, knowledge base | 277 | DELETE | Patterns -> /data-model |
| `ai_agents/data_engineering_agent.system.prompt.md` | Data layer (SQLite, pandas) | 402 | DELETE | Out of SA scope; data patterns extracted |
| `ai_agents/aws_security_networking_agent.system.prompt.md` | AWS IAM, VPC, Cognito | 396 | DELETE | Patterns -> /security-review (agnostic) |
| `ai_agents/aws_infrastructure_agent.system.prompt.md` | AWS ECS, CDK, CloudWatch | 342 | DELETE | Out of SA scope; infra patterns extracted |
| `ai_agents/aws_bedrock_agentcore_agent.system.prompt.md` | AWS Bedrock AgentCore | 919 | DELETE | Out of SA scope; AI platform patterns extracted |
| `ai_agents/aws_bedrock_strands_agent.system.prompt.md` | AWS Bedrock Strands SDK | 737 | DELETE | Out of SA scope; orchestration patterns extracted |
| `ai_agents/claude_code_agent.system.prompt.md` | Claude Code autonomous coding | 982 | DELETE | Out of SA scope |
| `ai_agents/claude_projects_agent.system.prompt.md` | Claude Projects deployment | 298 | DELETE | Out of SA scope |
| `ai_agents/claude_workspaces_agent.system.prompt.md` | Claude multi-agent orchestration | 917 | DELETE | Out of SA scope |
| `ai_agents/anthropic_agents_sdk_agent.system.prompt.md` | Anthropic Agents SDK | 873 | DELETE | Out of SA scope |
| `ai_agents/mcp_services_agent.system.prompt.md` | Model Context Protocol services | 938 | DELETE | Out of SA scope |
| `ai_agents/langchain_agent.system.prompt.md` | LangChain workflow orchestration | 649 | DELETE | Out of SA scope |
| `ai_agents/streamlit_ui_agent.system.prompt.md` | Streamlit UI development | 673 | DELETE | Out of SA scope |
| `ai_agents/cursor_ide_agent.system.prompt.md` | Cursor IDE configuration | 1591 | DELETE | Out of SA scope |
| `ai_agents/github_copilot_agent.system.prompt.md` | GitHub Copilot and CI/CD | 1686 | DELETE | Out of SA scope |
| `ai_agents/testing_qa_agent.system.prompt.md` | Testing and QA (pytest) | 410 | DELETE | Out of SA scope; QA patterns extracted |

**Subtotal**: 22 files, 19,887 lines.

### `knowledge_base/` Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `knowledge_base/system_config.json` | Read-only system configuration | 779 | REFACTOR | Evolve schema: remove implementation refs, add SA config | New system_config.json per Phase 6 |
| `knowledge_base/user_requirements.json` | User requirements from discovery | 247 | DELETE | Replaced by new `requirements.json` | New requirements.json |
| `knowledge_base/design_decisions.json` | Architecture decisions (monolithic) | 525 | DELETE | Split into architecture.json, estimates.json, project_plan.json, etc. | Split across new KB files |
| `knowledge_base/README.md` | KB usage guide for 3-file model | 288 | REFACTOR | Rewrite for 10-file engagement-centered topology | New KB README |
| `knowledge_base/schemas/system_config.schema.json` | JSON Schema for system_config | 375 | REFACTOR | Update for new schema | New schema |
| `knowledge_base/schemas/user_requirements.schema.json` | JSON Schema for user_requirements | 251 | DELETE | Replaced by new requirements.schema.json | New schema |
| `knowledge_base/schemas/design_decisions.schema.json` | JSON Schema for design_decisions | 290 | DELETE | Replaced by multiple new schemas | New schemas |
| `knowledge_base/schemas/.repo-metadata.schema.json` | JSON Schema for .repo-metadata | 46 | REFACTOR | Update for plugin metadata | New schema |
| `knowledge_base/schemas/SCHEMA_DESIGN.md` | Schema design for 10-file KB | 2419 | KEEP | Active design reference for Phase 6 | -- |

### `templates/` Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `templates/architecture-template.md` | Architecture deliverable template | 99 | REFACTOR | Update for /architecture skill output | Align with skill |
| `templates/requirements-template.md` | Requirements deliverable template | 80 | REFACTOR | Update for /requirements skill output | Align with skill |
| `templates/security-checklist.md` | Security validation checklist | 67 | REFACTOR | Update for /security-review; make technology-agnostic | Align with skill |
| `templates/development-checklist.md` | Development quality checks | 69 | DELETE | Out of SA scope (implementation) | -- |

### `tests/` Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `tests/validate_knowledge_base.py` | Validates KB JSON against schemas | 162 | REFACTOR | Update for 10-file KB schema | Update for new schemas |
| `tests/validate_consistency.py` | Counts agents/prompts, updates metadata | 282 | REFACTOR | Rewrite to count skills, update metadata | Update for plugin structure |
| `tests/validate_urls.py` | Validates external URLs in markdown | 183 | KEEP | URL validation still useful | -- |
| `tests/README.md` | Testing framework documentation | 270 | REFACTOR | Update for plugin testing | Align with new test scope |
| `tests/workflow_validation_checklist.md` | Manual multi-agent workflow testing | 310 | DELETE | Multi-agent testing obsolete | -- |

### `docs/` Directory

| Path | Purpose | Lines | Disposition | Reason | Target |
|------|---------|-------|-------------|--------|--------|
| `docs/README.md` | Documentation index | 116 | REFACTOR | Rewrite for plugin docs structure | New docs index |
| `docs/getting-started.md` | First-time user guide | 121 | REFACTOR | Rewrite for plugin installation, skill invocation | New getting-started |
| `docs/deployment-guide.md` | Multi-platform deployment | 88 | DELETE | Out of SA scope | -- |
| `docs/engineering-agents-guide.md` | 16 engineering agent reference | 109 | DELETE | Engineering agents deleted | -- |
| `docs/workflow_guide.md` | Complete workflow documentation | 114 | REFACTOR | Rewrite for SA skill workflow | New workflow guide |
| `docs/executive_overview.md` | Business value proposition | 92 | REFACTOR | Update for SA agent value prop | Align messaging |
| `docs/human-ai-collaboration.md` | Human vs. agent responsibilities | 140 | REFACTOR | Update for SA scope boundary | Align with scope |
| `docs/github-copilot-optimization.md` | Copilot workspace setup | 75 | DELETE | Platform-specific, not relevant | -- |
| `docs/examples/email-automation.md` | Example: email automation | 117 | DELETE | Multi-agent implementation example | -- |

### `outputs/` Directory (15 files -- ALL DELETE)

| Path | Purpose | Lines | Disposition |
|------|---------|-------|-------------|
| `outputs/README.md` | Output directory structure | 348 | DELETE |
| `outputs/architecture/.gitkeep` | Placeholder | 0 | DELETE |
| `outputs/deployments/.gitkeep` | Placeholder | 0 | DELETE |
| `outputs/optimizations/.gitkeep` | Placeholder | 0 | DELETE |
| `outputs/proposals/.gitkeep` | Placeholder | 0 | DELETE |
| `outputs/prototypes/.gitkeep` | Placeholder | 0 | DELETE |
| `outputs/requirements/.gitkeep` | Placeholder | 0 | DELETE |
| `outputs/agent_testing/TESTING_SUMMARY.md` | Agent test results summary | 252 | DELETE |
| `outputs/agent_testing/architecture_agent_test.md` | Architecture agent test | 207 | DELETE |
| `outputs/agent_testing/engineering_agent_test.md` | Engineering agent test | 256 | DELETE |
| `outputs/agent_testing/optimization_agent_test.md` | Optimization agent test | 192 | DELETE |
| `outputs/agent_testing/prompt_engineering_agent_test.md` | Prompt eng agent test | 241 | DELETE |
| `outputs/agent_testing/requirements_agent_test.md` | Requirements agent test | 248 | DELETE |
| `outputs/agent_testing/supervisor_agent_test.md` | Supervisor agent test | 136 | DELETE |
| `outputs/optimizations/ai-engineering-assistant/system-optimization-report-2025-10-10.md` | Optimization report | 559 | DELETE |

### `private/` Directory

| Path | Purpose | Lines | Disposition |
|------|---------|-------|-------------|
| `private/README.md` | Security guidelines for sensitive data | 286 | KEEP |
| `private/.gitignore` | Gitignore for private directory | 34 | KEEP |
| `private/sensitive-ai-agent-outputs/.gitignore` | Gitignore for sensitive outputs | 27 | KEEP |

### `user_prompts/requirements/` Directory (4 files -- ALL MERGE)

| Path | Purpose | Lines | Disposition | Target |
|------|---------|-------|-------------|--------|
| `user_prompts/requirements/quick_discovery.user.prompt.md` | Quick 15-min discovery | 690 | MERGE | skills/requirements/SKILL.md |
| `user_prompts/requirements/standard_discovery.user.prompt.md` | Standard 30-45 min discovery | 326 | MERGE | skills/requirements/SKILL.md |
| `user_prompts/requirements/comprehensive_workshop.user.prompt.md` | Comprehensive 90-min workshop | 311 | MERGE | skills/requirements/SKILL.md |
| `user_prompts/requirements/extract_requirements.user.prompt.md` | Extract from unstructured notes | 536 | MERGE | skills/requirements/SKILL.md |

### `user_prompts/architecture/` Directory (6 files -- ALL MERGE)

| Path | Purpose | Lines | Disposition | Target |
|------|---------|-------|-------------|--------|
| `user_prompts/architecture/tech_stack_selection.user.prompt.md` | Tech stack selection | 151 | MERGE | skills/architecture/SKILL.md |
| `user_prompts/architecture/architecture_diagram_generation.user.prompt.md` | Diagram generation (Mermaid/ASCII) | 754 | MERGE | skills/architecture/SKILL.md |
| `user_prompts/architecture/team_composition.user.prompt.md` | Team composition planning | 318 | MERGE | skills/estimate/SKILL.md |
| `user_prompts/architecture/loe_estimation.user.prompt.md` | LOE estimation | 462 | MERGE | skills/estimate/SKILL.md |
| `user_prompts/architecture/cost_estimation.user.prompt.md` | Cost estimation and analysis | 319 | MERGE | skills/estimate/SKILL.md |
| `user_prompts/architecture/project_plan_generation.user.prompt.md` | Project plan generation | 216 | MERGE | skills/project-plan/SKILL.md |

### `user_prompts/proposals/` Directory (4 files -- ALL MERGE)

| Path | Purpose | Lines | Disposition | Target |
|------|---------|-------|-------------|--------|
| `user_prompts/proposals/discovery_proposal_assembly.user.prompt.md` | Discovery proposal | 335 | MERGE | skills/proposal/SKILL.md |
| `user_prompts/proposals/implementation_proposal_assembly.user.prompt.md` | Implementation proposal | 551 | MERGE | skills/proposal/SKILL.md |
| `user_prompts/proposals/internal_proposal_assembly.user.prompt.md` | Internal proposal | 984 | MERGE | skills/proposal/SKILL.md |
| `user_prompts/proposals/pitch_deck_assembly.user.prompt.md` | Pitch deck | 1144 | MERGE | skills/proposal/SKILL.md |

### `user_prompts/deployment/` Directory (3 files -- ALL DELETE)

| Path | Purpose | Lines | Disposition |
|------|---------|-------|-------------|
| `user_prompts/deployment/platform_deployment.user.prompt.md` | Platform deployment guide | 870 | DELETE |
| `user_prompts/deployment/testing_strategy.user.prompt.md` | Testing strategy generation | 787 | DELETE |
| `user_prompts/deployment/create_ai_engineering_documentation.user.prompt.md` | AI engineering docs | 85 | DELETE |

### `user_prompts/prompt_engineering/` Directory (5 files -- ALL DELETE)

| Path | Purpose | Lines | Disposition |
|------|---------|-------|-------------|
| `user_prompts/prompt_engineering/improve_system_of_prompts.user.prompt.md` | System-wide prompt improvement | 367 | DELETE |
| `user_prompts/prompt_engineering/reduce_prompt_redundancy.user.prompt.md` | Reduce redundancy | 128 | DELETE |
| `user_prompts/prompt_engineering/improve_prompt_with_human_in_the_loop.user.prompt.md` | HITL prompt improvement | 44 | DELETE |
| `user_prompts/prompt_engineering/add_change_to_prompt_if_valid.user.prompt.md` | Validate prompt changes | 53 | DELETE |
| `user_prompts/prompt_engineering/configure_system_prompt_for_github_copilot_chatmode.user.prompt.md` | Copilot chat mode | 57 | DELETE |

### `user_prompts/engineering/` Directory (19 files -- ALL DELETE)

All out of SA scope (implementation, code generation, infrastructure).

| Path | Lines | Disposition |
|------|-------|-------------|
| `user_prompts/engineering/prototype_generation.user.prompt.md` | 655 | DELETE |
| `user_prompts/engineering/aws_bedrock/create_bedrock_agent.user.prompt.md` | 150 | DELETE |
| `user_prompts/engineering/aws_infrastructure/create_cdk_infrastructure.user.prompt.md` | 138 | DELETE |
| `user_prompts/engineering/aws_infrastructure/deploy_to_ecs.user.prompt.md` | 168 | DELETE |
| `user_prompts/engineering/aws_security/configure_iam_roles.user.prompt.md` | 134 | DELETE |
| `user_prompts/engineering/claude_integration/implement_streaming.user.prompt.md` | 121 | DELETE |
| `user_prompts/engineering/claude_integration/integrate_claude_sdk.user.prompt.md` | 153 | DELETE |
| `user_prompts/engineering/claude_projects/deploy_to_claude_projects.user.prompt.md` | 106 | DELETE |
| `user_prompts/engineering/cursor_ide/configure_cursorrules.user.prompt.md` | 284 | DELETE |
| `user_prompts/engineering/knowledge_engineering/ingest_documents.user.prompt.md` | 171 | DELETE |
| `user_prompts/engineering/knowledge_engineering/setup_vector_database.user.prompt.md` | 144 | DELETE |
| `user_prompts/engineering/langchain/build_rag_chain.user.prompt.md` | 120 | DELETE |
| `user_prompts/engineering/langchain/create_multi_step_chain.user.prompt.md` | 156 | DELETE |
| `user_prompts/engineering/streamlit_ui/add_sidebar_configuration.user.prompt.md` | 134 | DELETE |
| `user_prompts/engineering/streamlit_ui/build_chat_interface.user.prompt.md` | 144 | DELETE |
| `user_prompts/engineering/streamlit_ui/create_multi_page_app.user.prompt.md` | 104 | DELETE |
| `user_prompts/engineering/streamlit_ui/implement_file_upload.user.prompt.md` | 76 | DELETE |
| `user_prompts/engineering/testing/create_pytest_suite.user.prompt.md` | 140 | DELETE |
| `user_prompts/engineering/testing/validate_rag_quality.user.prompt.md` | 183 | DELETE |

### `user_prompts/self_improvement/` Directory (28 files -- ALL DELETE)

All meta-improvement prompts for legacy multi-agent system. No unique patterns worth extracting.

| Path | Lines | Disposition |
|------|-------|-------------|
| `user_prompts/self_improvement/README.md` | 256 | DELETE |
| `user_prompts/self_improvement/detect_errors_and_fix_references.user.prompt.md` | 1116 | DELETE |
| `user_prompts/self_improvement/improve_ai_engineering_assistant.user.prompt.md` | 97 | DELETE |
| `user_prompts/self_improvement/improve_all_documentation.user.prompt.md` | 669 | DELETE |
| `user_prompts/self_improvement/improve_architecture_agent.user.prompt.md` | 72 | DELETE |
| `user_prompts/self_improvement/improve_deployment_agent.user.prompt.md` | 57 | DELETE |
| `user_prompts/self_improvement/improve_engineering_supervisor.user.prompt.md` | 47 | DELETE |
| `user_prompts/self_improvement/improve_knowledge_base_architecture.user.prompt.md` | 69 | DELETE |
| `user_prompts/self_improvement/improve_optimization_agent.user.prompt.md` | 169 | DELETE |
| `user_prompts/self_improvement/improve_prompt_engineering_agent.user.prompt.md` | 56 | DELETE |
| `user_prompts/self_improvement/improve_requirements_agent.user.prompt.md` | 56 | DELETE |
| `user_prompts/self_improvement/improve_supervisor_agent.user.prompt.md` | 51 | DELETE |
| 16 engineering specialist improvement prompts (51 lines each) | 816 | DELETE |

---

## Extracted Patterns by Target Skill

All patterns extracted inline. After this phase, the source agent files will be deleted. This is the last extraction opportunity.

---

### /requirements Patterns

#### R1: Progressive Discovery Methodology (3-Tier)

**Sources**: requirements_agent, quick_discovery, standard_discovery, comprehensive_workshop user prompts

Three discovery tiers selected by complexity assessment:

| Tier | Duration | Best For |
|------|----------|----------|
| **Quick** | 15 min | Solo-entrepreneurs, 1-5 people, clear problems, simple automation, first AI project |
| **Standard** | 30-45 min | Small/medium teams (5-20), moderate complexity, 6-12 week timelines |
| **Comprehensive** | 90 min | Large orgs (20+), multi-agent systems, >$100K projects, compliance/regulatory |

**Tier Selection Logic**:
1. Problem complexity? Simple -> Quick; Standard -> Standard; Complex/multi-stakeholder -> Comprehensive
2. Who are stakeholders? Solo -> Quick; Small team -> Standard; Multiple departments -> Comprehensive
3. Urgency? Fast -> Quick; Normal -> Standard; Need buy-in -> Comprehensive
4. AI experience? First project -> Quick/Standard; Experienced -> Standard/Comprehensive

#### R2: Progressive Questioning Pattern (6-Step Funnel)

1. **Context (Broad)**: "Tell me about your business/role/organization."
2. **Problem Identification**: "What takes the most time that feels repetitive?"
3. **Workflow Deep-Dive**: "Walk me through [specific task] from start to finish."
4. **Quantification**: "How often does this happen? How long does each instance take?"
5. **Technical Context**: "What systems/tools do you currently use? Integration requirements?"
6. **Vision**: "What does success look like? How will you measure improvement?"

#### R3: AI Suitability Classification Framework

- **HIGH Priority** (Build first): Digital, repetitive tasks. >5 hrs/week. Patterns: Specialist Agent, Document Generator, Research & Synthesis.
- **MEDIUM Priority** (Human oversight): Judgment within parameters. 2-5 hrs/week. Patterns: Review & Validation, Adaptive Agent.
- **LOW Priority** (Human-led): Strategic decisions, novel problems, relationship-building. Variable, high-value.

**6-Question Test**: Is it digital? Is it repetitive? Are there clear rules? How much time consumed? What's the cost of error? Is there structured data?

#### R4: Real-Time Pain Point Classification

During discovery, classify pain points immediately:
```
PAIN POINT IDENTIFIED: [Description]
Classification: HIGH - [Reason]
Time impact: [X hours/week]
Suggested follow-up: "[Question]"
Potential solution: [Agent pattern]
Estimated savings: [X hours/week]
```

#### R5: Requirements Extraction from Unstructured Notes

4-step process: Load notes -> Extract across 7 categories (context, use cases, workflows, business value, technical requirements, scope, risks) -> Gap identification with priority tiers (High = need before architecture; Medium = can gather during design; Optional) -> Generate structured output with completeness score (COMPLETE/PARTIAL/INCOMPLETE).

**Rule**: NEVER fabricate information. Only extract what is stated or clearly implied. Mark gaps with "[TO BE DETERMINED]".

#### R6: Workshop Facilitation (Comprehensive Tier)

Pre-session prep (30-60 min): Review context, prepare customized questions, prepare 3-5 relevant AI examples.

6 sections: Opening (5 min) -> Industry & Market (15 min) -> Brand Voice (15 min) -> Go-to-Market (15 min) -> Core Service Delivery Workflows (25 min, MOST CRITICAL) -> Business Objectives (10 min) -> Technology Stack (10 min) -> Wrap-Up (5 min).

Key for Brand Voice: "This determines how AI agents communicate. If you build a formal agent for a casual brand, it will feel wrong."

For Workflows: Capture complete workflow diagram with time estimates per step for top 2-3 services.

#### R7: Stakeholder-Adaptive Communication

| Stakeholder Type | Method | Style | Focus |
|---|---|---|---|
| Solo/Small Business | Quick Discovery | Simple, actionable | Time savings, ROI |
| Corporate Teams | Standard/Comprehensive | Professional | Compliance, strategic value |
| Non-Technical | Avoid jargon, use analogies | Business outcomes | UX benefits |
| Technical | Technical terms OK | Deeper integration | Architecture, standards |

#### R8: Completeness Validation

After gathering, validate with checklist: Business problem defined? Current state documented? Success criteria established? Performance requirements? Integration details? Score: COMPLETE/PARTIAL/INCOMPLETE. List all gaps with suggested follow-up questions.

---

### /architecture Patterns

#### A1: 6-Step Design Process (Multi-Shot)

Input: requirements.json. Each step reads outputs of all prior steps.

1. **Tech Stack Selection** -> writes tech_stack to KB
2. **Architecture Diagram Generation** -> writes architecture_design to KB
3. **Team Composition Planning** -> writes team_composition to KB
4. **LOE Estimation** -> writes estimates to KB
5. **Cost Estimation** -> writes costs to KB
6. **Project Plan Generation** -> writes project_plan to KB

In target: Steps 1-2 -> /architecture, Steps 3-5 -> /estimate, Step 6 -> /project-plan.

Key principle: "Architecture is not a one-time activity but an evolving discipline."

#### A2: Technology Stack Selection Methodology

**Input parameters**: Product type, core functionality, AI capabilities, team capabilities (size + experience level per domain: NOVICE/INTERMEDIATE/EXPERT), constraints (budget, timeline, compliance, integration needs), performance requirements, decision criteria prioritized.

**Output**: Primary stack with rationale per layer, alternative options with trade-offs, cost breakdown per option, team readiness assessment, risk analysis, migration/scaling path (MVP -> production), decision matrix.

**Categories**: AI/ML Platforms, Backend, Frontend, Cloud, DevOps & Monitoring.

#### A3: Architecture Diagram Generation

**5 platform options**: ASCII Art, Lucidchart, Google Draw, draw.io, Mermaid (recommended).

**3 input dimensions**: Level of Detail (high-level 5-8 boxes / standard 10-15 / detailed 15+), Focus Areas (overall/security/data flow/integration/deployment), Target Audience (technical/leadership/mixed).

**Well-Architected Visualization** (mandatory elements per pillar):
- Security: VPC boundaries, auth points, encryption markers, compliance zones
- Reliability: Fault-tolerant components, backup/DR, health checks
- Performance: Caching layers, load balancers, auto-scaling
- Cost: Right-sized representations
- Operational Excellence: Monitoring/logging, CI/CD
- Sustainability: Serverless/managed services noted

**5 GenAI Diagram Patterns**: Simple LLM Wrapper, RAG Pipeline, Multi-Agent, Agentic Workflow (Tool Use), Conversational AI with Memory.

#### A4: Cascade Analysis for Design Updates

When updating a prior decision, trace dependencies:
1. Identify primary change and affected KB section
2. Trace downstream: What other steps depend on this?
3. For each affected step: what needs updating, why, which skill to re-run
4. Recommend sequence with time estimates
5. Offer: targeted updates (faster) vs. full re-runs (more thorough)

#### A5: Dual-Audience Output Generation

Every deliverable serves two audiences:
- **Technical Builders**: Detailed specs, implementation guidance, tool/framework recommendations
- **Business Leaders**: Executive summaries (5-min read), ROI, risk assessment, go/no-go

Format: Executive Summary -> Technical Details -> Business Impact translation.

#### A6: Cloud Infrastructure Architecture Planning

Before defining infrastructure, answer 5 questions:
1. What services are needed? (compute, storage, networking, observability)
2. What deployment pattern? (container-based, serverless, hybrid)
3. What monitoring required? (logs, metrics, traces)
4. What backup/DR needs? (RTO/RPO, cross-region, failover)
5. What cost constraints? (budget ceilings, per-request targets, reserved vs on-demand)

#### A7: High Availability and Disaster Recovery

- Multi-zone deployment (minimum 2 AZs)
- Zone-aware load balancing
- Storage versioning with lifecycle policies
- Desired-count > 1 for services
- Alarms on health metrics (CPU > 80%, error rate, latency P99)

#### A8: Auto-Scaling Architecture

- Horizontal scaling: min/max instances, target utilization (70%), cooldown periods
- Serverless for event-driven workloads (scales to zero)
- Right-sizing: start minimal (1 vCPU/2GB), adjust from metrics

#### A9: Cost-Aware Infrastructure Design

1. Right-size compute (start minimal, scale from data)
2. Serverless for spiky/event-driven workloads
3. Storage lifecycle policies (hot -> warm -> cold -> delete)
4. Minimize expensive components (NAT gateways, dedicated instances)
5. Log retention policies (7 days dev, 30-90 days prod)
6. Reserved capacity for stable workloads

#### A10: Three Pillars of Observability

1. **Logging**: Centralized aggregation, structured logs, retention per environment
2. **Metrics**: CPU, memory, latency (avg/P95/P99), error rates, AI-specific (tokens, invocations)
3. **Distributed Tracing**: Request-level tracing across services, trace duration, error rate, service map

#### A11: AI/ML Platform Component Architecture

Four components for enterprise AI agent platforms:
1. **Tool Gateway**: Converts APIs to agent-consumable tool interfaces
2. **Identity Layer**: Agent-to-service and user-to-agent auth
3. **Execution Runtime**: Serverless/container for agent code
4. **Persistent Memory**: Session and cross-session state persistence

#### A12: Multi-Agent Orchestration Patterns (for designing client systems)

Four patterns SA should recommend when appropriate:
1. **Supervisor-Worker**: Routes requests to specialized workers
2. **Chain of Thought**: Step-by-step explicit reasoning
3. **ReAct**: Reason-Act-Observe cycles with tool use
4. **Plan and Execute**: Plan first, execute sequentially

Selection: Simple Q&A -> Single agent; Multi-domain -> Supervisor-Worker; Tool-heavy -> ReAct; Complex multi-step -> Plan and Execute.

#### A13: Component-Based UI Architecture

- Main entry point configures app shell
- Component decomposition by function
- Dedicated component directory with exports
- Centralized state initialization with explicit defaults
- Cache strategy: data caching (TTL) vs. resource caching (lifecycle)

#### A14: Infrastructure as Code Principles

- All infrastructure defined declaratively in code
- Stack-based grouping: Compute, Storage, Networking, Monitoring, Security
- Environment parameterization (dev/staging/prod)
- Immutable deployments (deploy new alongside old, shift traffic, decommission)

---

### /estimate Patterns

#### E1: LOE Estimation Framework

**Core Principles**:
1. Account for Optimism Bias (15-25% underestimation constant)
2. Multiple Scenarios: Weighted estimate = (Optimistic + 4*Most-Likely + Pessimistic) / 6
3. Break down to 2-5 day tasks, roll up
4. Include Non-Coding Activities (30-40% of total): meetings, code reviews, docs, testing, debugging, learning
5. Factor in Team Capabilities (senior vs mid vs junior)

**Key Laws**: Hofstadter's Law, The 90-90 Rule, Brook's Law.

**Uncertainty Buffers**:
- Known Knowns: No extra buffer
- Known Unknowns: +25-50%
- Unknown Unknowns: +50-100%

**6-Phase Template**: Planning & Design (10-15%) -> Infrastructure & Setup (5-10%) -> Core Development (40-50%) -> Testing & Quality (15-20%) -> Deployment & Documentation (5-10%) -> Ongoing Activities (throughout).

**4 Estimation Methods**: Bottom-Up (most accurate), Historical Comparison, T-Shirt Sizing (quick), Three-Point Estimation.

**Complexity Assessment (0-10 checklist)**: Novel technology, multiple integrations (3+), high performance, data pipeline complexity, unfamiliar stack, evolving requirements, critical dependencies, security/compliance, real-time processing, complex business logic. Scores: 0-2 Low, 3-5 Medium (+25-40%), 6-8 High (+50-75%), 9-10 Very High (+75-100%).

#### E2: Cost Estimation Methodology

**5 Categories**:
1. Development Costs: Personnel (70-80%), Tools (5-10%), Infrastructure (10-15%)
2. Operational Costs (Monthly): Cloud, third-party services, team
3. AI-Specific: LLM API usage (per-token x volume), vector DB, GPU instances
4. TCO (3-Year): Year 1 (dev + infra), Year 2-3 (infra + growth)
5. ROI: Break-even (months), revenue projections, profit margins, payback period

**Optimization Strategies**: Remote teams (-30%), contractors for specialists (-20%), auto-scaling, reserved instances (-30-50%), model selection (smaller for simple tasks), response caching, batch processing.

#### E3: Team Composition Methodology

**By company stage**:
- Startup (0-10): 4-6 core. AI/ML Lead + 2 Full-Stack + PM (founder) + Designer (part-time).
- Growth (10-50): 8-15. Add Backend Dev, DevOps, AI PM, QA.
- Scale (50+): 15+. Add Data Engineer, AI Research Scientist, Eng Manager.

**Hiring Priority**: HIGH (Month 1: AI/ML Eng, Full-Stack, Backend), MEDIUM (Months 2-3: AI PM, DevOps, UX), LOW (Months 4-6: Data Eng, QA).

**Budget**: Engineering 70%, Product 15%, Design 10%, DevOps 5%.

#### E4: Confidence & Escalation Scoring

- **High (>80%)**: Present estimate directly
- **Medium (50-80%)**: Present with caveats and assumptions
- **Low (<50%)**: Flag for human review, explain uncertainty sources

Always include: point estimate with range, key assumptions, risk factors, industry benchmark comparison.

#### E5: Cost and Resource Tracking Pattern

Track per operation: input size, output size, model used, latency. Maintain configurable pricing table. Calculate cost per operation. Aggregate by user/time/operation type. Surface cost info alongside results for transparency.

---

### /project-plan Patterns

#### PP1: Phased Delivery (MVP -> Enhancement -> Scale)

**5-Phase Standard Template**:
1. Foundation (Weeks 1-2): Dev environment, project structure, CI/CD, infrastructure
2. Core Development (Weeks 3-6): Business logic, UI, database/APIs, auth
3. AI Integration (Weeks 7-10): AI/ML, agent workflows, vector DBs, orchestration, evaluation
4. Testing & Polish (Weeks 11-12): Testing, performance, security hardening, UX
5. Launch (Weeks 13-14): Production deployment, monitoring, onboarding

**Sprint Planning**: 2-week sprints with features mapped and estimated effort.

**Resource Allocation**: Per developer: role, hours/week, specific tasks.

#### PP2: Decision Gates

- Gate 1 (Post-Architecture): Approve dev budget? Criteria: strategic alignment, ROI >3x, feasibility, resources.
- Gate 2 (Post-MVP, Week 6): Continue? Criteria: core working, user feedback >7/10, performance meets targets.
- Gate 3 (Pre-Production, Week 10): Deploy? Criteria: acceptance tests passed, security audit complete, support in place.

Each gate: GO / Conditional GO / NO-GO options.

#### PP3: Risk Categories with Mitigations

- **Technical**: AI model performance, integration failures, scalability, data quality
- **Resource**: Key person risk, skill gaps, budget overruns, scope creep
- **Timeline**: AI development delays, integration complexity, testing bottlenecks, external dependencies

Each risk has specific mitigation strategies.

---

### /proposal Patterns

#### P1: Discovery Proposal Assembly

**When**: Significant technical uncertainty; need to validate before full investment.
**Duration**: 2-6 weeks. Investment: $5K-$25K.

**3-Phase Assessment**: Research & Planning (Days 1-3) -> Technical Investigation (Days 4-15) -> Analysis & Recommendation (Days 16-END).

**4 Decision Scenarios**: Clear GO, GO with Modifications, PAUSE, NO-GO.

**Key principle**: ASSEMBLY from KB, not re-analysis. READ from KB, ASSEMBLE into proposal, ADD proposal-specific content.

#### P2: Implementation Proposal Assembly

**Prerequisites**: requirements.json complete, architecture.json complete, estimates complete.

**KB-to-Proposal Mapping**:
- requirements.json -> Business Case, Financial section, KPIs, Risk Assessment
- architecture.json -> Technical Approach, System Design, Resource Requirements, Timeline, Financial Investment, Implementation Roadmap, Risk Assessment
- system_config.json -> Approval Signatures, Budget constraints, Strategic alignment

**Decision Framework**:
- Approve if: ROI >3x/3yr, payback <18mo, fits budget, aligns strategy, risks mitigated
- Conditional if: ROI 2-3x, payback 18-24mo, budget stretch <20%, some skill gaps
- Reject if: ROI <2x, payback >24mo, costs exceed budget >20%, critical unmitigated risks

#### P3: Internal Proposal (Executive Leadership)

12-18 slide presentation + 2-page exec summary + financial model + presenter guide.

**Audience differentiation**: CEO (strategic alignment), CFO (financial ROI), CTO (technical feasibility), VPs (operational impact).

**18-Slide Structure**: Title -> Strategic Alignment -> Problem (quantified FTE-hours) -> Business Case -> Architecture -> Tech Stack -> Team -> Timeline -> Change Management -> Risk -> Compliance -> Success Metrics -> Financial Deep-Dive (3 scenarios, sensitivity analysis) -> Organizational Impact -> Risk Register -> Implementation Governance -> Success Gates -> The Ask.

Includes anticipated Q&A prep (6+ executive questions with detailed answers).

#### P4: Pitch Deck Assembly (External)

10-15 slides, 20-30 min presentation.

**Narrative Arc**: Act 1 (The Challenge, slides 1-3) -> Act 2 (The Solution, slides 4-11) -> Act 3 (The Path Forward, slides 12-15).

**Evidence-Based Persuasion**: Every claim needs evidence. No hype. Use client's actual discovery data. Translate technical to business.

**Phased investment** to lower barrier: Phase 1 MVP (smaller) -> Decision point -> Phase 2 Full -> Phase 3 Enterprise. Offer 3 commitment options.

---

### /data-model Patterns

#### DM1: Entity-Relationship Schema Design

1. Enumerate entities needing persistent storage
2. Define relationships (one-to-many, many-to-many) with foreign keys
3. Add data type constraints and check constraints
4. Identify frequent query patterns, create covering indexes
5. Include audit fields: created_at, updated_at
6. Design migration-friendly schemas

#### DM2: Vector Database Schema Design

1. **Collection design**: One collection per knowledge domain
2. **Chunking**: Recursive character splitting (1000 chars, 200 overlap)
3. **Metadata schema**: Source document ID, page/section, ingestion timestamp, content type, domain tags
4. **Embedding model selection**: Based on dimensionality, language support, retrieval benchmarks
5. **Relevance filtering**: Score thresholds (cosine similarity >= 0.7)
6. **Retrieval parameters**: Configurable k (top results) per use case

#### DM3: Knowledge Pipeline Architecture

Multi-stage: Document Loading (format-specific loaders) -> Text Preprocessing (clean, normalize, split) -> Embedding Generation -> Vector Storage -> Retrieval Interface (queries -> ranked, scored results with source attribution).

Each stage independently testable with well-defined intermediate formats.

#### DM4: Data Validation Framework

Rule-based validation with declarative rules: required fields, type checks, range constraints, pattern matching. Validate at boundary between external input and internal storage. Rules can be defined in configuration files.

#### DM5: Knowledge Base Organization

- Index document listing all files, purpose, and category
- Categories: core domain, worked examples, reference data, documentation
- Format standardization (markdown, CSV, PDF)
- Size validation against platform constraints
- Version tracking of source materials

#### DM6: Repository Pattern for Data Access

Encapsulate storage/retrieval behind repository classes. Standard CRUD plus domain-specific queries. Parameterized queries exclusively. Return typed data objects, not raw rows.

#### DM7: Data Requirements Capture

From requirements: data sources, volume, structure (structured vs unstructured), quality concerns, retention requirements. From architecture: data layer design (primary DB, caching, vector DB, object storage), data flows.

---

### /security-review Patterns

#### SR1: Security Requirements Decomposition (5 Dimensions)

1. **Authentication needs**: Identity providers, auth flows, MFA, user pool configs
2. **Secrets to manage**: Credentials, API keys, certificates, rotation schedules
3. **Network isolation**: Segmentation, public/private/isolated tiers
4. **Content filtering / AI guardrails**: PII categories, harmful content, domain restrictions
5. **Compliance requirements**: HIPAA, PCI-DSS, SOC2, CCPA, GLBA -> map to controls

#### SR2: Defense-in-Depth Architecture (5 Layers)

1. **Network perimeter**: Segment into public, private, isolated tiers
2. **Identity and access**: Dedicated identity per service, least-privilege
3. **Application security**: Content filtering, AI guardrails for PII and harmful content
4. **Data protection**: Encrypt at rest/transit, secrets vault with rotation
5. **Monitoring and auditability**: Flow logs, auth event logging, anomaly alerting

#### SR3: Least-Privilege IAM

1. Enumerate required actions per service (no more)
2. Scope to specific resources (no wildcards)
3. Separate trust from permission
4. Support multiple auth types (password, token, mTLS, federated)
5. Agent-specific: each AI agent gets own identity scoped to its tools/data

#### SR4: Tiered Network Segmentation

| Tier | Placement | Allowed Traffic |
|------|-----------|----------------|
| Public | Load balancers, bastion | Inbound from internet on specific ports |
| Private | App servers, compute | Inbound from public only; outbound via NAT |
| Isolated | Databases, secrets | Inbound from private only; no internet |

Deploy across minimum 2 availability zones.

#### SR5: Encryption Strategy

- **At rest**: AES-256 or equivalent, managed keys with auto-rotation
- **In transit**: TLS 1.2+, including internal service-to-service
- **Key management**: Dedicated KMS, separate keys by environment and classification
- **Secrets**: Dedicated vault with versioning, rotation, audit logging

#### SR6: AI-Specific Security Controls

1. Content filtering: deny-list topics, severity levels per category
2. PII detection/blocking: email, phone, payment cards, government IDs
3. Word/phrase filtering: managed and custom lists
4. Agent authentication: verify identity at each interaction

#### SR7: Compliance Requirements Mapping

1. Identify applicable frameworks by data types/industry/geography
2. Map controls: encryption -> encryption patterns, access control -> IAM, audit -> monitoring, data residency -> regions
3. Document compliance posture: met/partially met/not met with remediation

#### SR8: Non-Negotiable Security Guardrails

**MUST**: Least-privilege, secrets in vault, audit logging, content guardrails for AI, encrypt everything, document security arch.

**MUST NOT**: Hardcode credentials, open unnecessary ports, skip encryption, disable security for convenience, deploy without security testing, use prod data in tests.

#### SR9: Change Impact Analysis & Risk Scoring

Risk Score = Change Type (Cosmetic +1 to Architecture +8) + Blast Radius (Minimal +1 to Extensive +5) + Testing Coverage (Well-tested -2 to Poor +3) + Reversibility (Easy -1 to Irreversible +4) + System Maturity (Dev 0 to Prod-critical +5).

Interpretation: 0-3 LOW, 4-7 MEDIUM, 8-12 HIGH, 13+ CRITICAL.

---

### /integration-plan Patterns

#### IP1: API-to-Tool Gateway

1. Catalog existing APIs (gather OpenAPI specs)
2. Auto-generate tool definitions from API endpoints
3. Centralize authentication (gateway handles downstream auth)
4. Rate limiting and throttling at gateway
5. Protocol translation (MCP/gRPC <-> REST/SOAP)

#### IP2: Event-Driven Integration

- Define event sources (API calls, file uploads, schedules, queues)
- Serverless handlers with configured memory/timeout
- All handlers idempotent
- Dead letter queues for failed events

#### IP3: Secure Service-to-Service Integration

1. Unique identity per service
2. Explicit permission grants per integration point
3. Credentials in secrets vault, auto-rotated
4. Audit trail: caller, target, action, result

#### IP4: Data Pipeline Architecture (Storage Lifecycle)

- Versioning on all shared data stores
- Lifecycle: Hot (standard) -> Warm (lower-cost after N days) -> Cold (cheapest after M days) -> Delete
- Schema validation at ingestion
- Partition by time/tenant/category

#### IP5: Document Ingestion Pipeline

Format-specific loaders -> Text splitting (recursive, configurable) -> Metadata enrichment (provenance tracking) -> Batch/single processing -> Idempotency (track ingested documents by hash).

#### IP6: Data Access Layer Integration

4 layers: UI -> Business Logic -> Data Access -> External Services. Interface contracts at each boundary. Delegation pattern (UI never calls DB/APIs directly). Error translation at each layer.

#### IP7: Phased Integration Approach

Phase 1 (MVP): CSV exports, simple approaches -> validate value.
Phase 2 (Enhancement): Full API integration.
Start simple, validate, then invest in deeper integration.

#### IP8: CI/CD Pipeline Architecture

6 stages: Code Quality -> Testing (>80% coverage) -> Security Scanning -> Build -> Deploy (immutable) -> Monitor. Reusable workflow templates. Scheduled automation (dependency audits, branch cleanup).

---

### /review Patterns

#### RV1: LLM-as-Judge Methodology (3 Iterations)

- Iteration 1: Discover -> Assess -> Implement -> Validate
- Iteration 2: Judge evaluation -> Identify gaps -> Refine -> Re-validate
- Iteration 3: Final polish if needed

Self-evaluate: What worked? What could be better? Edge cases? Quality gaps? If score 9.0+, stop early.

#### RV2: Test-Refine-Merge (TRM) Validation

1. Generate 2-3 candidate approaches
2. Validate each against same benchmarks
3. Select highest-scoring
4. Recursively improve (max 3 iterations)
5. Present only after passing all quality gates (85% overall)

#### RV3: Three-Dimensional Assessment

1. **Technical Excellence**: Prompt engineering, multi-agent coordination, code quality, platform optimization
2. **Operational Excellence**: Performance (token efficiency, response time), Cost (model selection, infra sizing), Reliability (fault tolerance, monitoring)
3. **Well-Architected Framework**: 6 pillars (0-10 each) + GenAI Lens

Thresholds: 9+ excellent, 7+ good, 5+ acceptable, 3+ needs improvement, <3 critical.

#### RV4: Multi-Dimensional Quality Scoring

5 core dimensions (each 1-10):
- **Completeness**: Covers all requirements?
- **Technical Soundness**: Design decisions defensible?
- **Well-Architected Alignment**: Framework criteria met?
- **Clarity**: Understandable to target audience?
- **Feasibility**: Implementable within constraints?

#### RV5: Prioritized Improvement Planning

4 tiers: P0 Quick Wins (High Impact/Low Effort, do first) -> P1 Strategic (High/High, plan carefully) -> P2-P3 Refinements (lower priority).

Each improvement: current state with evidence, impact (H/M/L), benefit (quantified), effort (hours), risk, implementation steps, validation criteria.

#### RV6: Dual-Persona Validation

1. **Builder** creates deliverable with best-effort quality
2. **Tester** reviews adversarially -- finds gaps, inconsistencies, missing requirements. Tester NEVER improves, only exposes what instructions produce.
3. **Reconciliation**: Merge findings, prioritize fixes, produce improved version.

#### RV7: Quality KPI Framework

| KPI | Target |
|-----|--------|
| Test pass rate | 100% critical paths |
| Response time | < defined SLA |
| Token efficiency | Output < ceiling per query |
| LLM consistency | Same core answer across N runs |
| Schema compliance | 100% records validate |
| Security | 0 critical/high vulnerabilities |
| Overall quality | >85% across dimensions |

#### RV8: Test Strategy Decomposition

5 analysis dimensions: What needs testing? (unit/integration/E2E/UAT) -> Quality metrics? (coverage >80%, latency SLAs, accuracy) -> Test data? (samples, expected outputs, edge cases) -> Edge cases? (rate limiting, timeout, malformed input) -> Validation criteria? (pass/fail thresholds).

#### RV9: Testing Pyramid

```
        /  UAT  \           <- Few: Business scenario validation
       / Perform \          <- Few: Latency, throughput, token efficiency
      / Integration\        <- Moderate: Component interactions
     /  Data Quality \      <- Moderate: Schema validation
    /    Unit Tests    \    <- Many: Individual functions, mocked deps
```

#### RV10: LLM Response Quality Validation

5 dimensions for AI outputs: Relevance (expected key terms present), Tone consistency (matches persona), Consistency (same answer across repetitions), Token efficiency (below ceiling), Safety (no PII/harmful content).

---

## Cross-Cutting Patterns

These patterns apply across multiple skills and should be embedded in the overall agent design.

### CC1: Well-Architected Framework Compliance (Multi-Cloud)

6 pillars evaluated for every architecture:
1. **Operational Excellence**: IaC, automated deployments, runbooks, continuous improvement
2. **Security**: Defense-in-depth, least-privilege, encryption, secrets management, zero trust
3. **Reliability**: Multi-zone, automated failover, health checks, RTO/RPO targets
4. **Performance Efficiency**: Right-sized compute, auto-scaling, caching, performance testing
5. **Cost Optimization**: Right-sizing, serverless, lifecycle policies, reserved capacity
6. **Sustainability** (+ AI/GenAI Lens): Token efficiency, model selection, content safety, responsible AI

AWS: 6 pillars + GenAI Lens + Responsible AI Lens + ML Lens. Azure: 5 pillars + AI workload section. GCP: 5 pillars + AI/ML perspective.

### CC2: Orchestration -- KB-Mediated State Sharing (Blackboard Pattern)

Skills communicate only through the knowledge base. Each skill has explicit READ/WRITE permissions:

| Skill | Reads | Writes |
|---|---|---|
| /requirements | (user input) | requirements.json |
| /architecture | requirements, integration_map | architecture.json |
| /data-model | requirements, architecture, integration_map | data_model.json |
| /security-review | requirements, architecture, data_model, integration_map | security_assessment.json |
| /integration-plan | requirements, architecture | integration_map.json |
| /estimate | requirements, architecture, data_model, security, integration_map | estimates.json |
| /project-plan | requirements, architecture, estimates | project_plan.json |
| /proposal | ALL KB files (read-only) | outputs/ (not KB) |
| /review | ALL KB files (read-only) | reviews.json |

### CC3: Orchestration -- Intent-Based Skill Dispatch

Analyze every request across 5 dimensions: (1) user objective, (2) domain, (3) current phase, (4) target skill, (5) context needed.

Prerequisite validation before dispatch: check required upstream KB state exists. If missing: identify gaps, recommend upstream skill, offer to accept direct input.

Ambiguity handling: present 2-4 options mapped to skills, never guess.

### CC4: Orchestration -- Lifecycle Flows

**0-to-1**: /requirements -> /architecture -> /data-model -> /security-review -> /estimate -> /project-plan -> /proposal -> /review

**Migration**: /requirements -> /integration-plan -> /architecture -> /data-model -> /security-review -> /estimate -> /project-plan -> /proposal -> /review

Phase-skip flexibility: allowed if KB state exists; never silently skip gaps.

### CC5: Orchestration -- Human Checkpoints

After every skill completion:
1. Summarize: "Phase N Complete: [what was accomplished]"
2. List deliverables with KB locations
3. Identify next phase and skill
4. Confirm: "Ready to proceed?" or "Review first?"

Git workflow reinforces: execute -> commit -> HUMAN REVIEWS -> push.

### CC6: Prompt Engineering Techniques

| Technique | Improvement | Use In |
|---|---|---|
| Chain-of-Thought (CoT) | 25-40% | Complex reasoning across all skills |
| Step-Back Prompting | 15-20% | Principled analysis before specifics |
| MODP | 26% | Multi-option decision processes |
| Tree-of-Thoughts | 20-35% | Architecture alternatives, data model options |
| Dual-Persona | -- | /review (Builder creates, Tester validates) |
| Progressive-Hint | 20% | Iterative refinement in /review |
| Self-Consistency | 40-50% | Security review, architecture validation |
| Decomposed Prompting | 30% error reduction | Breaking complex tasks into sub-tasks |
| Positive Instruction Framing | -- | All skills: "do this" over "don't do that" |

Use `ultrathink` in: /architecture, /data-model, /security-review, /review.

### CC7: Scope Boundary Enforcement (SA vs Engineering)

| This Agent Does | Engineering Agent Does (Future) |
|---|---|
| Requirements discovery | Code generation |
| System architecture | Deployment scripts |
| Data modeling | CI/CD pipelines |
| Security review | Prompt engineering (for target systems) |
| Integration planning | Testing implementation |
| Cost estimation | Infrastructure provisioning |
| Project planning | Monitoring setup |
| Proposal assembly | Production operations |

If user requests implementation: acknowledge need, explain scope, note for future Engineering Agent.

### CC8: Technology-Agnostic Enforcement

- No hard-coded APIs or vendor references in skills
- Describe capabilities abstractly, not by vendor name
- Use WebSearch for latest technology knowledge (dynamic, not static)
- Recommend best-fit based on requirements and trade-offs
- Never default to a specific cloud provider, framework, or tool

### CC9: Cascade Impact Detection

When requirements or architecture change mid-engagement:
1. Read current KB state + updated inputs
2. Identify downstream impacts (which deliverables need re-running?)
3. Recommend re-running affected skills in dependency order
4. Execute cascade updates with human approval at each step

### CC10: Confidence Scoring (Universal)

All estimates and assessments include confidence levels:
- COMPLETE/PARTIAL/INCOMPLETE for requirements
- HIGH/MEDIUM/LOW for estimates
- 0-10 scoring for Well-Architected pillars
- Percentage scores for review dimensions

Low confidence always triggers human escalation.

---

## Deletion Plan

### Summary by Directory

| Directory | Files | Lines | Justification |
|---|---|---|---|
| `ai_agents/` | 22 | 19,887 | All agent prompts replaced by 9 skills; patterns extracted |
| `supervisor_agent.system.prompt.md` | 1 | 1,612 | Supervisor pattern replaced by single agent + dispatch |
| `user_prompts/engineering/` | 19 | 3,281 | Out of SA scope (implementation) |
| `user_prompts/self_improvement/` | 28 | 3,536 | Multi-agent self-improvement eliminated |
| `user_prompts/deployment/` | 3 | 1,742 | Out of SA scope (deployment) |
| `user_prompts/prompt_engineering/` | 5 | 649 | Out of SA scope (implementation) |
| `outputs/` (all contents) | 15 | 2,439 | Multi-agent test results obsolete |
| Misc (cursorrules, rules, KB, templates, tests, docs) | 16 | 2,272 | Various: scope boundary, platform-specific, replaced by new |
| **TOTAL DELETE** | **109** | **35,418** | |

### MERGE then Delete

| Source | Lines | Target Skill |
|---|---|---|
| `user_prompts/requirements/` (4 files) | 1,863 | skills/requirements/SKILL.md |
| `user_prompts/architecture/` (6 files) | 2,220 | skills/architecture/SKILL.md + estimate + project-plan |
| `user_prompts/proposals/` (4 files) | 3,014 | skills/proposal/SKILL.md |
| **TOTAL MERGE** | **14 files, 7,097 lines** | **5 target skills** |

### Total Removal

DELETE (109) + MERGE (14) = **123 files, 42,515 lines removed**.

---

## Disposition Summary

| Disposition | Files | Lines | % of Files |
|---|---|---|---|
| DELETE | 109 | 35,418 | 62.3% |
| MERGE (then delete) | 14 | 7,097 | 8.0% |
| KEEP | 17 | ~1,390 + binaries | 9.7% |
| REFACTOR | 15 | ~3,700 | 8.6% |
| .gitkeep (structure) | 16 | 0 | 9.1% |
| Binary (git-ignored) | 3 | -- | 1.7% |
| NEW (this file) | 1 | -- | 0.6% |
| **TOTAL** | **175** | **~47,605** | **100%** |

### Post-Cleanup Projection

| Category | Files | Notes |
|---|---|---|
| KEEP (unchanged) | 17 | LICENSE, SECURITY.md, guiding-principles.md, etc. |
| REFACTOR (modified) | 15 | CLAUDE.md, README.md, KB files, templates, tests, etc. |
| NEW (Phase 4+) | ~20+ | plugin.json, 9 SKILL.md, 7 new KB JSON, schemas, templates |
| **Projected total** | **~52** | Down from 175 (~70% fewer files) |

**Lines**: ~42,515 removed, ~5,000-8,000 added = **~75% net reduction**.

---

## Uncertain Dispositions (ALL RESOLVED)

All 5 items resolved during Phase 1 human review:

| File | Decision | When | Rationale |
|------|----------|------|-----------|
| `.claude/rules/refactoring-direction.md` | Keep until Phase 4, then DELETE | Phase 4 | Still useful as context for new sessions during Phases 2-3 |
| `outputs/` directory | DELETE all contents in Phase 4 | Phase 4 | Skills create subdirectories dynamically; old test results have no reuse value |
| `.github/CODEOWNERS` | REFACTOR paths in Phase 4 | Phase 4 | Mechanical update: ai_agents/ -> skills/, agents/, hooks/ |
| `docs/executive_overview.md` | Keep separate, REFACTOR in Phase 8 | Phase 8 | Different audience than README; update messaging for SA plugin value prop |
| `docs/human-ai-collaboration.md` | Absorb into CLAUDE.md + docs in Phase 5/8 | Phase 5/8 | Content distributed to agent identity (CLAUDE.md) and user docs (getting-started) |

---

## Gap Analysis

Patterns each skill needs but no agent fully provided. Gaps marked FILLED were addressed by real-world reference materials added during Phase 1.

| Target Skill | Gap | Status | Mitigation |
|---|---|---|---|
| /data-model | **Neurosymbolic AI architecture** -- ontology + LLM integration | Open | WebSearch at invocation; SCHEMA_DESIGN.md has forward-looking topology |
| /data-model | **Standalone data model exemplar** | **FILLED** | Florence Healthcare MongoDB topology, replica set architecture, healthcare data classification taxonomy added to references/ |
| /security-review | **Standalone threat model exemplar** | **FILLED** | Florence Healthcare access governance workflow, JIT access automation, audit trail architecture, DPA structure added to references/ |
| /security-review | **Privacy-by-design patterns** (GDPR Art 25) | **PARTIALLY FILLED** | Florence DPA covers GDPR/HIPAA/CCPA with annexes; extend with WebSearch |
| /requirements | **Requirements elicitation methodology depth** | **FILLED** | 6 AGADA requirements templates added covering RAD process, IEEE 830, PM gathering, system requirements, prioritized scope, and Maguire-Bevan academic methodology |
| /integration-plan | **Strangler fig pattern** for migration | Open | WebSearch; well-documented industry pattern |
| /integration-plan | **Legacy system bridging** (COBOL, mainframe) | Open | Dynamic via WebSearch -- client-specific and evolving |
| /integration-plan | **Jira-to-infrastructure automation exemplar** | **FILLED** | Florence Healthcare Jira->Atlantis->Terraform->AWS pipeline added to references/ |
| /project-plan | **Migration-specific timelines** | Open | Build from /integration-plan output + industry practices |
| /review | **Exemplar-level quality rubric** | Open | Create in Phase 6 as reference document for /review skill |
| /proposal | **Competitive analysis section** | Open | Add as optional section using WebSearch for market research |
| All skills | **Multi-session state management** | Open | Design in Phase 3 -- KB files on disk handle this |
| All skills | **Error recovery** | Open | Design in Phase 3 -- checkpoint/resume patterns |
| All skills | **Pre-sales lifecycle integration** | **FILLED** | Complete pre-sales process with SA agent augmentation map written to references/pre-sales-lifecycle.md |

**Summary**: 6 of 13 gaps FILLED by real-world reference materials. 7 remaining gaps have clear mitigations (WebSearch, Phase 3 design, Phase 6 creation).

---

## Verification Checklist

- [x] All 175 files have a disposition (KEEP/DELETE/REFACTOR/MERGE)
- [x] All 23 agents (22 in ai_agents/ + 1 supervisor) have patterns extracted
- [x] All 9 target skills have mapped patterns:
  - /requirements: 8 patterns (R1-R8)
  - /architecture: 14 patterns (A1-A14)
  - /estimate: 5 patterns (E1-E5)
  - /project-plan: 3 patterns (PP1-PP3)
  - /proposal: 4 patterns (P1-P4)
  - /data-model: 7 patterns (DM1-DM7)
  - /security-review: 9 patterns (SR1-SR9)
  - /integration-plan: 8 patterns (IP1-IP8)
  - /review: 10 patterns (RV1-RV10)
  - Cross-cutting: 10 patterns (CC1-CC10)
- [x] No external filesystem references in output
- [x] Deletion plan accounts for every DELETE file (109 + 14 MERGE = 123)
- [x] Gap analysis identifies 9 gaps with mitigations

---

## Human Checkpoint

**Review the following before approving Phase 1**:

1. **Disposition counts**: 109 DELETE + 14 MERGE + 17 KEEP + 15 REFACTOR = 175 files accounted for
2. **Projected repo**: ~52 files, ~8,000-12,000 lines (75% reduction)
3. **Extracted patterns**: 78 skill-specific + 10 cross-cutting = 88 named patterns (from 112 total extracted by agents, deduplicated)
4. **Uncertain items**: 5 flagged (see table above)
5. **Gaps**: 9 identified with mitigations
6. **All 23 agent prompts have patterns extracted inline** -- safe to delete in Phase 4

**Ready for Phase 2**: Requirements & Workflow Design.
