# Engineering Agents Guide

**Version**: 0.1.0-alpha | **Status**: Alpha

Quick reference for 16 hyper-specialized engineering agents.

---

## Engineering Supervisor

**Routes tasks to appropriate specialist(s)**

Request anything → Supervisor identifies which specialist(s) → Coordinates multi-specialist work

---

## The 16 Specialists

### Anthropic Claude (5 agents)

**Claude Code Agent** - `ai_agents/claude_code_agent.system.prompt.md`
- Autonomous code generation, multi-file refactoring, code review
- Use for: Generate code, refactor projects, review code quality

**Claude Workspaces Agent** - `ai_agents/claude_workspaces_agent.system.prompt.md`
- Multi-agent orchestration, supervisor-worker patterns
- Use for: Complex multi-agent systems, workflow coordination

**Anthropic Agents SDK Agent** - `ai_agents/anthropic_agents_sdk_agent.system.prompt.md`
- Formal Anthropic SDK, tool use, prompt caching
- Use for: SDK-based agents, tool integration, optimization

**MCP Services Agent** - `ai_agents/mcp_services_agent.system.prompt.md`
- Model Context Protocol servers, tool/resource/prompt providers
- Use for: MCP server development, tool integration

**Claude Projects Agent** - `ai_agents/claude_projects_agent.system.prompt.md`
- Claude Projects platform deployment
- Use for: Deploy to Claude Projects, configure artifacts

### AWS Bedrock (2 agents)

**AWS Bedrock AgentCore Agent** - `ai_agents/aws_bedrock_agentcore_agent.system.prompt.md`
- Gateway, Identity, Runtime, Memory, Code Interpreter
- Use for: Enterprise AWS deployments, AgentCore components

**AWS Bedrock Strands Agent** - `ai_agents/aws_bedrock_strands_agent.system.prompt.md`
- Strands SDK, observability, reasoning patterns (COT, ReAct, PlanAndExecute)
- Use for: Observable agents, production monitoring

### UI & Data (3 agents)

**Streamlit UI Agent** - `ai_agents/streamlit_ui_agent.system.prompt.md`
- Streamlit interfaces, chat UIs, session state
- Use for: Build Streamlit apps, chat interfaces

**Knowledge Engineering Agent** - `ai_agents/knowledge_engineering_agent.system.prompt.md`
- Vector databases (ChromaDB, FAISS), RAG, semantic search
- Use for: RAG systems, knowledge bases

**Data Engineering Agent** - `ai_agents/data_engineering_agent.system.prompt.md`
- SQLite, pandas, data transformation, CSV/JSON
- Use for: Data pipelines, database design

### Orchestration (1 agent)

**LangChain Agent** - `ai_agents/langchain_agent.system.prompt.md`
- LCEL chains, RAG patterns, tool integration
- Use for: LangChain workflows, complex chains

### AWS Infrastructure & Security (2 agents)

**AWS Infrastructure Agent** - `ai_agents/aws_infrastructure_agent.system.prompt.md`
- ECS, Lambda, CDK, CloudWatch, IaC
- Use for: AWS infrastructure, deployment automation

**AWS Security & Networking Agent** - `ai_agents/aws_security_networking_agent.system.prompt.md`
- IAM, VPC, Cognito, Secrets Manager, security
- Use for: AWS security, network config, authentication

### DevOps & Tools (3 agents)

**Testing & QA Agent** - `ai_agents/testing_qa_agent.system.prompt.md`
- pytest, test generation, validation
- Use for: Generate tests, quality assurance

**GitHub & Copilot Agent** - `ai_agents/github_copilot_agent.system.prompt.md`
- GitHub Actions, CI/CD, Copilot configuration
- Use for: CI/CD pipelines, GitHub integration

**Cursor IDE Agent** - `ai_agents/cursor_ide_agent.system.prompt.md`
- .cursorrules, custom modes, Composer
- Use for: Cursor IDE configuration, developer experience

---

## When to Use Which Specialist

**Build Streamlit chat app**: Streamlit UI + Claude Code  
**Multi-agent system**: Claude Workspaces + multiple specialists  
**AWS deployment**: AWS Infrastructure + AWS Security  
**RAG system**: Knowledge Engineering + LangChain  
**Testing**: Testing & QA  
**CI/CD**: GitHub & Copilot

**Most tasks**: Just ask Supervisor, it routes correctly

---

