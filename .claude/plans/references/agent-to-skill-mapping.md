# Agent-to-Skill Mapping Reference

This file maps the current 23 agent prompts to their target skill equivalents for the single-agent refactoring.

## Supervisor Layer (becomes the core system prompt)

| Current Agent | Target | Notes |
|---------------|--------|-------|
| `supervisor_agent.system.prompt.md` | Core system prompt (CLAUDE.md or root prompt) | Routing logic becomes skill dispatch |

## Top-Level Domain Agents (become primary skills)

| Current Agent | Target Skill | Invocation |
|---------------|-------------|------------|
| `requirements_agent` | `/requirements` | User-invocable |
| `architecture_agent` | `/architecture` | User-invocable |
| `deployment_agent` | `/deployment` | User-invocable |
| `optimization_agent` | `/optimize` | User-invocable |
| `prompt_engineering_agent` | `/prompt-engineering` | User-invocable |

## Engineering Supervisor (becomes orchestration logic in skills)

| Current Agent | Target | Notes |
|---------------|--------|-------|
| `engineering_supervisor_agent` | Embedded in skill dispatch | No standalone skill needed |

## Engineering Specialists (become reference-backed skills)

| Current Agent | Target Skill | Invocation |
|---------------|-------------|------------|
| `streamlit_ui_agent` | `/build-streamlit` | User-invocable |
| `claude_code_agent` | `/build-claude-code` | User-invocable |
| `claude_workspaces_agent` | `/build-claude-workspace` | User-invocable |
| `anthropic_agents_sdk_agent` | `/build-agent-sdk` | User-invocable |
| `mcp_services_agent` | `/build-mcp` | User-invocable |
| `langchain_agent` | `/build-langchain` | User-invocable |
| `knowledge_engineering_agent` | `/knowledge-engineering` | Both |
| `data_engineering_agent` | `/data-engineering` | User-invocable |
| `aws_bedrock_agentcore_agent` | `/build-bedrock-agentcore` | User-invocable |
| `aws_bedrock_strands_agent` | `/build-bedrock-strands` | User-invocable |
| `aws_infrastructure_agent` | `/aws-infra` | User-invocable |
| `aws_security_networking_agent` | `/aws-security` | User-invocable |
| `claude_projects_agent` | `/build-claude-project` | User-invocable |
| `testing_qa_agent` | `/testing` | User-invocable |
| `github_copilot_agent` | `/build-copilot` | User-invocable |
| `cursor_ide_agent` | `/build-cursor` | User-invocable |

## Priority Order for Migration

1. **Phase 1 (Core)**: requirements, architecture, deployment — the solutions architecture lifecycle
2. **Phase 2 (Anthropic)**: claude_code, anthropic_agents_sdk, mcp_services, claude_projects — Anthropic platform skills
3. **Phase 3 (AWS)**: aws_infrastructure, aws_security, aws_bedrock_* — cloud platform skills
4. **Phase 4 (Remaining)**: All other specialist skills
