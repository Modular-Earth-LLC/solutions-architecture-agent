# Engineering Agents Guide

**Purpose**: Comprehensive guide to the 12 specialized engineering agents for building Python+Streamlit+Claude+AWS AI systems.

**Last Updated**: 2025-01-12  
**Architecture**: Two-Layer Supervision (Engineering Supervisor coordinates specialists)  
**Update**: GitHub & Cursor split into separate specialized agents for deeper platform integration

---

## Table of Contents

- [Overview](#overview)
- [Engineering Supervisor Agent](#engineering-supervisor-agent)
- [The 11 Engineering Specialists](#the-11-engineering-specialists)
- [When to Use Each Agent](#when-to-use-each-agent)
- [Common Engineering Workflows](#common-engineering-workflows)
- [Tech Stack & Standards](#tech-stack--standards)

---

## Overview

The Engineering domain has been decomposed from a monolithic "Engineering Agent" into a **sophisticated multi-agent system** with 1 orchestrator and 12 hyper-specialized agents. This mirrors how real software engineering teams are structured, with each agent representing a senior specialist engineer.

**Why 12 Agents?** Modern AI development with Python+Streamlit+Claude+AWS requires deep expertise across:
- **UI/UX**: Streamlit interface patterns
- **LLM Integration**: Claude SDK, LangChain orchestration
- **Data**: Application databases (SQLite) and knowledge bases (vector DBs)
- **AWS**: Bedrock Agents, infrastructure (ECS/CDK), security (IAM/VPC)
- **Platforms**: Claude Projects deployment
- **Quality**: Testing, validation, QA
- **DevOps**: Git workflows, CI/CD, Cursor configuration

---

## Engineering Supervisor Agent

**File**: `ai_agents/engineering_supervisor_agent.system.prompt.md`

**Role**: Orchestrates all 11 engineering specialists, routing requests and coordinating multi-agent workflows.

**Responsibilities**:
- Analyze engineering requests and route to appropriate specialist(s)
- Coordinate sequential workflows (UI → Backend → Testing → Deployment)
- Coordinate parallel workflows (UI || Backend || Data || AWS Infrastructure)
- Maintain context across specialist handoffs
- Does NOT implement code (purely orchestration)

**When Main Supervisor Routes Here**:
- Any engineering/implementation request
- "Build a Streamlit app with Claude"
- "Deploy to AWS Bedrock"
- "Set up database and testing"

**Then Engineering Supervisor Routes To**: Appropriate specialist(s) based on specific technical needs

---

## The 12 Engineering Specialists

### Category A: UI/UX Engineering (1 agent)

#### 1. Streamlit UI Development Agent
**File**: `ai_agents/streamlit_ui_agent.system.prompt.md`

**Specialization**: Streamlit interfaces, chat UIs, session state, file uploads, data visualization

**Tech Stack**: Streamlit, st.chat_message, st.session_state, st.cache_data

**Core Capabilities**:
- Build production Streamlit chat interfaces
- Implement session state management for conversations
- Create file upload components
- Design multi-page applications
- Add sidebar configuration controls
- Integrate data visualization (pandas dataframes, charts)

**When to Use**:
- "Build Streamlit chat interface"
- "Create file upload for documents"
- "Add configuration sidebar"
- "Design multi-page Streamlit app"
- Any UI/UX work for Streamlit

**User Prompts** (4):
- `build_chat_interface.user.prompt.md`
- `implement_file_upload.user.prompt.md`
- `create_multi_page_app.user.prompt.md`
- `add_sidebar_configuration.user.prompt.md`

---

### Category B: LLM Engineering (2 agents)

#### 2. Anthropic Claude Integration Agent
**File**: `ai_agents/claude_integration_agent.system.prompt.md`

**Specialization**: Claude SDK, API patterns, streaming, function calling, error handling, cost tracking

**Tech Stack**: anthropic Python SDK, asyncio

**Core Capabilities**:
- Initialize Claude client securely
- Implement synchronous and streaming message APIs
- Handle errors with retry logic
- Track usage and costs
- Implement rate limiting
- Support async/await patterns
- Claude tool use / function calling

**When to Use**:
- "Integrate Claude SDK"
- "Implement streaming responses"
- "Add Claude API error handling"
- "Track Claude usage and costs"
- Any direct Claude API integration

**User Prompts** (2):
- `integrate_claude_sdk.user.prompt.md`
- `implement_streaming.user.prompt.md`

#### 3. LangChain Orchestration Agent
**File**: `ai_agents/langchain_agent.system.prompt.md`

**Specialization**: LangChain workflows, LCEL chains, agents, memory, tool use

**Tech Stack**: LangChain, LangChain-Anthropic, LCEL

**Core Capabilities**:
- Build LCEL chains with pipe operators
- Implement conversation memory (buffer, summary, window)
- Create tool-calling agents
- Build RAG chains
- Multi-agent orchestration with LangChain
- Streaming with callbacks
- Error handling and fallbacks

**When to Use**:
- "Build LangChain workflow"
- "Create RAG chain"
- "Implement multi-step processing"
- "Add conversation memory"
- "Build agent with tools"

**User Prompts** (2):
- `build_rag_chain.user.prompt.md`
- `create_multi_step_chain.user.prompt.md`

---

### Category C: Data Engineering (2 agents)

#### 4. Knowledge Engineering Agent
**File**: `ai_agents/knowledge_engineering_agent.system.prompt.md`

**Specialization**: Vector databases, RAG, embeddings, semantic search, AI knowledge systems

**Tech Stack**: ChromaDB, FAISS, AWS Bedrock Knowledge Bases, embeddings

**Core Capabilities**:
- Set up vector databases (ChromaDB, FAISS)
- Build document ingestion pipelines
- Implement semantic search
- Create RAG systems
- Configure AWS Bedrock Knowledge Bases
- Optimize retrieval strategies

**When to Use**:
- "Set up vector database"
- "Implement RAG system"
- "Ingest documents for knowledge base"
- "Configure semantic search"
- Anything related to AI knowledge and retrieval

**User Prompts** (2):
- `setup_vector_database.user.prompt.md`
- `ingest_documents.user.prompt.md`

#### 5. Data Engineering Agent
**File**: `ai_agents/data_engineering_agent.system.prompt.md`

**Specialization**: SQLite databases, pandas, numpy, data pipelines, application data

**Tech Stack**: SQLite, pandas, numpy, JSON/YAML/CSV

**Core Capabilities**:
- Design SQLite database schemas
- Implement data access layers (repository pattern)
- Process data with pandas
- Create analytics and reporting
- Handle JSON/YAML configuration
- Validate and clean data

**When to Use**:
- "Design database schema"
- "Process data with pandas"
- "Create usage analytics"
- "Build data access layer"
- Traditional application data engineering

**User Prompts** (2):
- `design_sqlite_schema.user.prompt.md`
- `process_data_with_pandas.user.prompt.md`

---

### Category D: AWS Engineering (3 agents)

#### 6. AWS Bedrock Agent Engineering Agent
**File**: `ai_agents/aws_bedrock_agent_engineering_agent.system.prompt.md`

**Specialization**: AWS Bedrock Agents, AgentCore framework, Strands SDK, multi-agent orchestration

**Tech Stack**: boto3, Bedrock Agents API, AgentCore, Strands

**Core Capabilities**:
- Create and configure Bedrock Agents
- Set up action groups (Lambda-backed tools)
- Associate knowledge bases with agents
- Configure guardrails
- Implement multi-agent orchestration on Bedrock
- Deploy with AgentCore framework

**When to Use**:
- "Create Bedrock Agent"
- "Configure action groups"
- "Build multi-agent system on Bedrock"
- "Set up AgentCore architecture"

**User Prompts** (1):
- `create_bedrock_agent.user.prompt.md`

#### 7. AWS Infrastructure Agent
**File**: `ai_agents/aws_infrastructure_agent.system.prompt.md`

**Specialization**: AWS CDK (Python), ECS/Fargate, Lambda, S3, CloudWatch, infrastructure as code

**Tech Stack**: AWS CDK (Python), boto3, ECS, Lambda, S3

**Core Capabilities**:
- Build AWS CDK infrastructure (Python)
- Deploy Streamlit apps to ECS/Fargate
- Create Lambda functions
- Configure S3 storage
- Set up CloudWatch monitoring
- Implement auto-scaling

**When to Use**:
- "Deploy to AWS ECS"
- "Create CDK infrastructure"
- "Set up Lambda functions"
- "Configure CloudWatch monitoring"

**User Prompts** (2):
- `deploy_to_ecs.user.prompt.md`
- `create_cdk_infrastructure.user.prompt.md`

#### 8. AWS Security & Networking Agent
**File**: `ai_agents/aws_security_networking_agent.system.prompt.md`

**Specialization**: IAM, VPC, Cognito, Secrets Manager, Guardrails, security policies

**Tech Stack**: IAM, VPC, Cognito, Secrets Manager, AWS Guardrails

**Core Capabilities**:
- Create IAM roles and policies (least-privilege)
- Configure VPC and security groups
- Set up Cognito authentication
- Manage secrets with Secrets Manager
- Configure Bedrock Guardrails (content filtering, PII protection)

**When to Use**:
- "Configure IAM roles for Bedrock"
- "Set up VPC networking"
- "Implement Cognito authentication"
- "Create guardrails for content moderation"

**User Prompts** (1):
- `configure_iam_roles.user.prompt.md`

---

### Category E: Platform Deployment (1 agent)

#### 9. Claude Projects Deployment Agent
**File**: `ai_agents/claude_projects_agent.system.prompt.md`

**Specialization**: Claude Projects platform, knowledge base setup, custom instructions

**Tech Stack**: Claude Projects, Project Knowledge API

**Core Capabilities**:
- Prepare custom instructions for Claude Projects
- Organize knowledge base files
- Deploy applications to Claude Projects
- Migration from local Streamlit to Claude Projects

**When to Use**:
- "Deploy to Claude Projects"
- "Prepare knowledge base for Claude Projects"
- "Migrate Streamlit app to Claude Projects"

**User Prompts** (1):
- `deploy_to_claude_projects.user.prompt.md`

---

### Category F: Quality & DevOps (3 agents)

#### 10. Testing & QA Agent
**File**: `ai_agents/testing_qa_agent.system.prompt.md`

**Specialization**: pytest, unit/integration tests, data quality, UAT, validation frameworks

**Tech Stack**: pytest, unittest, mocking

**Core Capabilities**:
- Create pytest test suites
- Write unit tests for AI components
- Build integration tests for workflows
- Test data quality
- Validate RAG system accuracy
- Implement performance benchmarking
- User acceptance testing

**When to Use**:
- "Create test suite"
- "Test Claude integration"
- "Validate RAG quality"
- "Benchmark performance"

**User Prompts** (2):
- `create_pytest_suite.user.prompt.md`
- `validate_rag_quality.user.prompt.md`

#### 11. GitHub & GitHub Copilot Agent
**File**: `ai_agents/github_copilot_agent.system.prompt.md`

**Specialization**: GitHub.com platform, GitHub Copilot, GitHub Actions, CI/CD, background agents, security scanning

**Tech Stack**: Git, GitHub, GitHub Copilot, GitHub Actions, CodeQL, Dependabot

**Core Capabilities**:
- Initialize GitHub repositories with comprehensive .gitignore
- Configure GitHub Copilot for VS Code
- Build GitHub Actions CI/CD pipelines (test, lint, deploy, security)
- Set up background automation (scheduled tasks, dependency updates)
- Configure GitHub Advanced Security (CodeQL, secret scanning)
- Implement branch protection and collaboration workflows
- Leverage GitHub Copilot @workspace commands
- Set up reusable workflows

**When to Use**:
- "Setup GitHub repository"
- "Create GitHub Actions CI/CD"
- "Configure GitHub Copilot"
- "Set up security scanning"
- "Create background automation"
- Anything GitHub.com or GitHub Copilot related

**User Prompts** (2):
- `setup_github_repo.user.prompt.md`
- `configure_github_actions.user.prompt.md`

#### 12. Cursor IDE Agent
**File**: `ai_agents/cursor_ide_agent.system.prompt.md`

**Specialization**: Cursor IDE, .cursorrules, custom chat modes, Composer, CMD+K, codebase indexing

**Tech Stack**: Cursor IDE, .cursorrules, custom modes, Cursor AI features

**Core Capabilities**:
- Create comprehensive .cursorrules for Python AI projects
- Configure custom chat modes for multi-agent system
- Optimize Cursor Composer workflows
- Configure CMD+K inline editing patterns
- Set up codebase indexing (.cursorignore)
- Configure Cursor settings for Python development
- Create project templates for quick starts
- Leverage Cursor AI features (prediction, chat, @workspace)

**When to Use**:
- "Configure .cursorrules"
- "Set up Cursor custom modes"
- "Optimize Cursor for AI development"
- "Create Cursor project templates"
- Anything Cursor IDE specific

**User Prompts** (1):
- `configure_cursorrules.user.prompt.md`

---

## When to Use Each Agent

### Quick Decision Guide

**I need to...**
| Task | Use This Agent |
|------|----------------|
| Build chat UI | Streamlit UI Agent |
| Integrate Claude API | Claude Integration Agent |
| Create multi-step workflow | LangChain Agent |
| Set up RAG system | Knowledge Engineering Agent |
| Design database | Data Engineering Agent |
| Deploy to Bedrock Agents | AWS Bedrock Agent Engineering Agent |
| Deploy to ECS | AWS Infrastructure Agent |
| Configure security | AWS Security & Networking Agent |
| Deploy to Claude Projects | Claude Projects Agent |
| Write tests | Testing & QA Agent |
| Setup GitHub/CI/CD | GitHub & GitHub Copilot Agent |
| Configure Cursor IDE | Cursor IDE Agent |

**Still not sure?** → Start with **Engineering Supervisor Agent** who will analyze your request and route to the right specialist(s).

---

## Common Engineering Workflows

### Workflow 1: Build Complete Streamlit + Claude App

```
1. Engineering Supervisor receives request
2. Routes to specialists:
   
   Phase 1 (Parallel):
   ├─ Streamlit UI Agent → Build chat interface
   ├─ Claude Integration Agent → Implement Claude SDK
   └─ Data Engineering Agent → Design database schema
   
   Phase 2 (Sequential):
   └─ Testing & QA Agent → Create test suite
   
   Phase 3 (Sequential):
   └─ GitHub & Cursor Agent → Setup repository

Deliverable: Working Streamlit app with Claude integration
```

### Workflow 2: Deploy AI System to AWS Bedrock

```
1. Engineering Supervisor receives request
2. Routes to specialists:
   
   Phase 1 (Parallel - Infrastructure Setup):
   ├─ AWS Infrastructure Agent → Create ECS/CDK
   ├─ AWS Security Agent → Configure IAM/VPC
   └─ AWS Bedrock Agent Engineering Agent → Create Bedrock Agents
   
   Phase 2 (Sequential - Integration):
   └─ AWS Infrastructure Agent → Connect components
   
   Phase 3 (Sequential - Validation):
   └─ Testing & QA Agent → Validate deployment

Deliverable: Production AWS deployment
```

### Workflow 3: Build RAG System

```
1. Engineering Supervisor receives request
2. Routes to specialists:
   
   Phase 1 (Sequential - Foundation):
   └─ Knowledge Engineering Agent → Setup vector database
   
   Phase 2 (Sequential - Orchestration):
   └─ LangChain Agent → Build RAG chain
   
   Phase 3 (Parallel - Integration):
   ├─ Streamlit UI Agent → Add document upload UI
   └─ Claude Integration Agent → Connect Claude to chain
   
   Phase 4 (Sequential - Quality):
   └─ Testing & QA Agent → Validate RAG accuracy

Deliverable: Production RAG system
```

### Workflow 4: Full Production Deployment

```
1. Engineering Supervisor receives request
2. Routes to specialists:
   
   Phase 1: Application Development
   ├─ Streamlit UI Agent
   ├─ Claude Integration Agent
   ├─ LangChain Agent
   ├─ Data Engineering Agent
   └─ Knowledge Engineering Agent
   
   Phase 2: AWS Infrastructure
   ├─ AWS Infrastructure Agent
   ├─ AWS Security Agent
   └─ AWS Bedrock Agent Engineering Agent
   
   Phase 3: Quality & DevOps
   ├─ Testing & QA Agent
   └─ GitHub & Cursor Agent
   
   Phase 4: Deployment
   └─ Claude Projects Agent OR AWS deployment complete

Deliverable: Production-ready AI system
```

---

## Tech Stack & Standards

### Official Tech Stack

**Language & Framework**:
- Python 3.12+
- Streamlit (UI framework - NO React/HTML/CSS)

**LLM & Orchestration**:
- Anthropic Claude (claude-3-5-sonnet-20241022, haiku, opus)
- LangChain (workflow orchestration)

**Data & Storage**:
- SQLite (application database)
- ChromaDB or FAISS (vector database)
- pandas, numpy (data processing)
- JSON/YAML/CSV (configuration and data)

**AWS Services**:
- AWS Bedrock (Agents, AgentCore, Knowledge Bases, Guardrails)
- ECS/Fargate (container deployment)
- Lambda (serverless functions)
- S3 (storage)
- CloudWatch (monitoring)
- IAM, VPC, Cognito (security)
- AWS CDK Python (infrastructure as code)

**Development Tools**:
- GitHub (version control)
- GitHub Actions (CI/CD)
- Cursor IDE (development environment)
- pytest (testing)

**Explicitly AVOIDED**:
- ❌ JavaScript, Node.js
- ❌ React, HTML, CSS
- ❌ Complex databases (PostgreSQL, MongoDB)
- ❌ Non-AWS cloud providers in this specialized system

### Why This Stack?

**Focus = Excellence**: By specializing in Python+Streamlit+Claude+AWS, these agents deliver world-class results in this niche rather than mediocre results across all technologies.

**Junior Engineer Friendly**: Streamlined stack means faster onboarding, clearer learning paths, and confident deployment.

**Production-Grade**: This stack powers real production AI systems. Proven, battle-tested, and supported by comprehensive documentation from Anthropic and AWS.

**Cursor Ecosystem**: These tools are popular with Cursor users, ensuring tight IDE integration and community support.

---

## Best Practices

### Agent Collaboration Patterns

**Sequential Handoff**: When output of Agent A is input for Agent B
```
Streamlit UI Agent → Claude Integration Agent → Testing Agent
```

**Parallel Execution**: When agents work on independent components
```
UI Agent || Backend Agent || Data Agent → Integration
```

**Hybrid Pattern**: Combination of sequential and parallel
```
Design Review → (UI || Backend || AWS) → Integration → Testing
```

### Code Quality Standards

All engineering agents enforce:
- **PEP 8 compliance**
- **Type hints required**
- **Docstrings required** (Google style)
- **>80% test coverage**
- **Environment variables for secrets** (never hardcode)
- **Error handling with retries**
- **Logging for debugging**

### Testing Requirements

Every component must have:
- Unit tests (pytest)
- Integration tests (end-to-end)
- Data quality validation
- Performance benchmarks
- User acceptance tests

### Security Standards

All implementations must:
- Use AWS Secrets Manager or .env (never hardcode)
- Follow least-privilege IAM policies
- Validate all user inputs
- Implement rate limiting
- Configure Bedrock Guardrails
- Enable CloudWatch logging

---

## Integration with Other Top-Level Agents

**Engineering Supervisor coordinates with**:

- **Requirements Agent** → Receives business requirements
- **Architecture Agent** → Receives architecture designs
- **Prompt Engineering Agent** → Delegates all prompt creation
- **Deployment Agent** → Hands off for cross-platform deployment
- **Optimization Agent** → Receives improvement recommendations

**Key Relationship: Engineering ↔ Prompt Engineering**

Engineering specialists **NEVER create prompts**. All prompt creation is delegated to the Prompt Engineering Agent:

```
Engineering Supervisor identifies need for Claude system prompts
         ↓
Routes to Prompt Engineering Agent
         ↓
Prompt Engineering Agent creates production-quality prompts
         ↓
Engineering Supervisor integrates prompts into prototype
```

---

## Getting Help

### Which Engineering Agent Do I Need?

**Start with Engineering Supervisor Agent** if unsure. It will analyze your request and route to the appropriate specialist(s).

**Direct routing** (if you know exactly what you need):
- UI work → Streamlit UI Agent
- Claude API → Claude Integration Agent
- Workflows → LangChain Agent
- Knowledge/RAG → Knowledge Engineering Agent
- Data/DB → Data Engineering Agent
- Bedrock Agents → AWS Bedrock Agent Engineering Agent
- Infrastructure → AWS Infrastructure Agent
- Security → AWS Security & Networking Agent
- Claude Projects → Claude Projects Agent
- Testing → Testing & QA Agent
- GitHub/CI/CD → GitHub & GitHub Copilot Agent
- Cursor config → Cursor IDE Agent

---

## Evolution from v1.0

**What Changed:**

**v1.0 (Original)**:
- 1 monolithic "Engineering Agent" tried to do everything
- Generic tech stack support (Python, Node.js, React, etc.)
- All implementation in one 1,102-line agent

**v2.0 (Current - Refactored)**:
- 12 hyper-specialized engineering agents
- Focused tech stack: Python+Streamlit+Claude+AWS
- Each agent is expert in 1-2 technologies
- Two-layer supervision for better organization
- GitHub & Cursor split into separate specialists (better platform integration)
- 60-100+ user prompts for comprehensive task coverage

**Migration Path**:
- Old `engineering_agent.system.prompt.md` → Deleted (archived to `tmp/`)
- Replaced by `engineering_supervisor_agent.system.prompt.md` + 12 specialists
- All capabilities preserved and enhanced
- New capabilities added (AgentCore, Strands, GitHub background agents, Cursor Composer)

---

**Version**: 2.0  
**Last Updated**: 2025-01-12  
**Agent Count**: 12 specialized engineering agents + 1 Engineering Supervisor  
**Update**: GitHub & Cursor split for better specialization  
**Related Documentation**:
- `README.md` - Framework overview
- `ARCHITECTURE.md` - System architecture
- `docs/agent-architecture-and-collaboration.md` - All agents guide
- `docs/workflow_guide.md` - Complete workflows

---

**Remember**: Each engineering agent is a senior specialist in their domain. Use the Engineering Supervisor to coordinate complex workflows, or invoke specialists directly for focused tasks.
