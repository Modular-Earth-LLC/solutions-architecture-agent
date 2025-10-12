# System Architecture

**Multi-agent AI development framework** featuring supervisor-worker architecture pattern, shared knowledge base state management, and two-tier deployment model supporting three primary platforms: Cursor IDE, Claude Projects, and GitHub Copilot.

## Core Architecture

### Supervisor-Worker Pattern

```
User Request
     ↓
Supervisor Agent (Orchestrator)
     ↓
     ├─→ Requirements Agent           → Discovery, requirements
     ├─→ Architecture Agent            → Design, tech stack, estimates
     ├─→ Engineering Supervisor Agent  → Engineering orchestration (Two-Layer)
     │   ├─→ Streamlit UI Agent              → Streamlit interfaces
     │   ├─→ Claude Integration Agent        → Claude SDK
     │   ├─→ LangChain Agent                 → Workflow orchestration
     │   ├─→ Knowledge Engineering Agent     → Vector DBs, RAG
     │   ├─→ Data Engineering Agent          → SQLite, pandas
     │   ├─→ AWS Bedrock Agent Engineering   → Bedrock Agents, AgentCore
     │   ├─→ AWS Infrastructure Agent        → ECS, CDK, CloudWatch
     │   ├─→ AWS Security & Networking       → IAM, VPC, Cognito
     │   ├─→ Claude Projects Agent           → Claude Projects deployment
     │   ├─→ Testing & QA Agent              → pytest, validation
     │   ├─→ GitHub & GitHub Copilot Agent   → GitHub, Actions, Copilot, CI/CD
     │   └─→ Cursor IDE Agent                → Cursor, .cursorrules, custom modes
     ├─→ Deployment Agent              → Platform deployment coordination
     ├─→ Optimization Agent            → System improvement
     └─→ Prompt Engineering Agent      → Prompt creation, optimization

Shared Knowledge Base
├─→ system_config.json     → Platform constraints, team info
├─→ user_requirements.json → Customer needs, use cases
└─→ design_decisions.json  → Architecture decisions, costs

Tech Stack Focus: Python, Streamlit, Anthropic Claude, AWS Bedrock, LangChain
```

### Agent Responsibilities

| Agent | Primary Function | Reads | Writes |
|-------|-----------------|-------|--------|
| **Supervisor** | Orchestration, routing | All files | None (routes only) |
| **Requirements** | Discovery, validation | system_config.json | user_requirements.json |
| **Architecture** | System design, planning | user_requirements.json, system_config.json | design_decisions.json |
| **Engineering Supervisor** | Engineering orchestration | All KB files | None (coordinates only) |
| **Streamlit UI** | Streamlit interface development | design_decisions.json | UI code |
| **Claude Integration** | Claude SDK implementation | design_decisions.json | Integration code |
| **LangChain** | Workflow orchestration | design_decisions.json | Workflow code |
| **Knowledge Engineering** | Vector DBs, RAG systems | design_decisions.json | Knowledge base code |
| **Data Engineering** | SQLite, pandas, analytics | design_decisions.json | Data layer code |
| **AWS Bedrock Agent Eng** | Bedrock Agents, AgentCore | design_decisions.json | Bedrock configs |
| **AWS Infrastructure** | ECS, CDK, CloudWatch | design_decisions.json | Infrastructure code |
| **AWS Security** | IAM, VPC, Cognito, Guardrails | design_decisions.json | Security configs |
| **Claude Projects** | Claude Projects deployment | All KB files | Deployment guides |
| **Testing & QA** | pytest, quality assurance | All code | Test suites |
| **GitHub & GitHub Copilot** | GitHub.com, Actions, Copilot, CI/CD | All code | GitHub configs, workflows |
| **Cursor IDE** | Cursor IDE, .cursorrules, custom modes | All code | Cursor configs |
| **Deployment** | Platform deployment coordination | design_decisions.json | Deployment guides |
| **Optimization** | System improvement | All files | Recommendations |
| **Prompt Engineering** | Prompt creation | Optional: knowledge base | Prompts, optimization reports |

## Two-Tier Architecture

### Tier 1: This Repository (Development Workspace)

**Execution Environment**: Cursor IDE • Claude Projects • GitHub Copilot (VS Code)
**Purpose**: AI engineering assistance for developers  
**Components**: 6 specialized agents + Supervisor + User prompts

**Platform Options:**

**Cursor IDE Installation**:
```bash
.\scripts\deploy_cursor.ps1    # Windows
./scripts/deploy_cursor.sh     # Linux/Mac
```

**Claude Projects Installation**:
- Upload knowledge base files to Project Knowledge
- Add supervisor prompt to Custom Instructions

**GitHub Copilot Installation**:
- Configure `.github/copilot-instructions.md` with supervisor prompt
- Use Copilot Chat in VS Code

**Usage**: Agents run as custom chat modes (Cursor), project assistants (Claude), or Copilot instructions (VS Code)

### Tier 2: Generated Systems (External Deployment)

**Execution Environment**: Cursor IDE • Claude Projects • GitHub Copilot • AWS Bedrock • Self-hosted platforms
**Purpose**: Production AI systems for end users  
**Components**: Complete systems created by Tier 1 agents

**Deployment**: Platform-specific (guided by Deployment Agent)

### Visual Distinction

```
┌───────────────────────────────────────────────┐
│ TIER 1: YOUR WORKSPACE (This Repository)     │
│ Runs on: Cursor • Claude Projects • Copilot  │
│                                               │
│ ┌───────────────────────────────────────┐    │
│ │ Supervisor Agent                      │    │
│ │   ├─ Requirements Agent               │    │
│ │   ├─ Architecture Agent               │    │
│ │   ├─ Engineering Agent                │    │
│ │   ├─ Deployment Agent                 │    │
│ │   ├─ Optimization Agent               │    │
│ │   └─ Prompt Engineering Agent         │    │
│ └───────────────────────────────────────┘    │
│                                               │
│ Knowledge Base: JSON state files             │
└───────────────────────────────────────────────┘
                      ↓
                  Generates
                      ↓
┌───────────────────────────────────────────────┐
│ TIER 2: GENERATED SYSTEMS (External)          │
│ Deploy to: OpenAI • Claude • Bedrock • Self-hosted │
│                                               │
│ ┌───────────────────────────────────────┐    │
│ │ Financial Operations Assistant        │    │
│ │   • AWS Bedrock deployment            │    │
│ │   • 2-agent system                    │    │
│ └───────────────────────────────────────┘    │
│                                               │
│ ┌───────────────────────────────────────┐    │
│ │ Customer Support Bot                  │    │
│ │   • Claude Projects deployment        │    │
│ │   • Single agent + knowledge base     │    │
│ └───────────────────────────────────────┘    │
└───────────────────────────────────────────────┘
```

## Knowledge Base Architecture

### File Structure

**system_config.json**
```json
{
  "platform_constraints": {...},
  "team_info": {...},
  "well_architected_framework": {...}
}
```

**user_requirements.json**
```json
{
  "problem_statement": "...",
  "success_criteria": [...],
  "ai_suitability": {...}
}
```

**design_decisions.json**
```json
{
  "architecture": {...},
  "tech_stack": [...],
  "cost_estimate": {...},
  "project_plan": {...}
}
```

### Access Patterns

1. **Requirements Phase**: Requirements Agent writes user_requirements.json
2. **Architecture Phase**: Architecture Agent reads requirements, writes design_decisions.json
3. **Engineering Phase**: Engineering Agent reads both files to generate code
4. **Deployment Phase**: Deployment Agent reads design_decisions.json for deployment
5. **Optimization Phase**: Optimization Agent reads all files for analysis

## Workflow Patterns

### Complete System Development

```
1. User → Supervisor Agent: "Build financial operations assistant"
2. Supervisor → Requirements Agent
   → Gathers needs, writes user_requirements.json
3. Requirements → Architecture Agent (automatic handoff)
   → Designs system, writes design_decisions.json
4. Architecture → Engineering Agent
   → Builds prototype, generates code
5. Engineering → Deployment Agent
   → Creates deployment guide
6. User executes deployment → System runs on target platform
```

### System Improvement

```
1. User → Optimization Agent: "Analyze my system"
2. Optimization Agent reads knowledge base
3. Identifies improvement opportunities
4. May invoke Engineering Agent for code changes
5. Hands off to Deployment Agent if deployment needed
```

### Prompt Engineering

```
1. User → Prompt Engineering Agent: "Create code review assistant"
2. Agent gathers requirements interactively
3. Generates platform-optimized prompt
4. Validates character limits
5. Delivers copy-paste ready output
```

## Agent Collaboration

### Cross-Agent Communication

**Via Knowledge Base**: Agents read/write JSON files for persistent state  
**Via Supervisor**: Explicit handoffs through orchestration  
**Via User**: User can manually route between agents

### Example Collaboration

```
Optimization Agent identifies prompt needs
     ↓
Invokes Prompt Engineering Agent
     ↓
Prompt Engineering creates improved prompt
     ↓
Engineering Agent implements in code
     ↓
Deployment Agent deploys update
```

## File Organization

```
multi-agent-ai-development-framework/
├── supervisor_agent.system.prompt.md    # Main supervisor (entry point)
├── REFACTORING_COMPLETE.md             # Quick status reference
├── ai_agents/                           # Specialized agents (23 total)
│   ├── requirements_agent.system.prompt.md
│   ├── architecture_agent.system.prompt.md
│   ├── deployment_agent.system.prompt.md
│   ├── optimization_agent.system.prompt.md
│   ├── prompt_engineering_agent.system.prompt.md
│   ├── engineering_supervisor_agent.system.prompt.md    # Engineering orchestrator (16 specialists)
│   ├── streamlit_ui_agent.system.prompt.md             # Streamlit UI specialist
│   ├── claude_code_agent.system.prompt.md              # Claude autonomous coding
│   ├── claude_workspaces_agent.system.prompt.md        # Claude multi-agent orchestration
│   ├── anthropic_agents_sdk_agent.system.prompt.md     # Anthropic Agents SDK
│   ├── mcp_services_agent.system.prompt.md             # Model Context Protocol
│   ├── langchain_agent.system.prompt.md                # LangChain workflows
│   ├── knowledge_engineering_agent.system.prompt.md    # Vector DBs, RAG
│   ├── data_engineering_agent.system.prompt.md         # SQLite, pandas
│   ├── aws_bedrock_agentcore_agent.system.prompt.md    # AgentCore (Gateway/Identity/Runtime/Memory)
│   ├── aws_bedrock_strands_agent.system.prompt.md      # Strands SDK, observability
│   ├── aws_infrastructure_agent.system.prompt.md       # ECS, CDK, CloudWatch
│   ├── aws_security_networking_agent.system.prompt.md  # IAM, VPC, Cognito, Guardrails
│   ├── claude_projects_agent.system.prompt.md          # Claude Projects deployment
│   ├── testing_qa_agent.system.prompt.md               # pytest, validation
│   ├── github_copilot_agent.system.prompt.md           # GitHub.com, Actions, Copilot
│   ├── cursor_ide_agent.system.prompt.md               # Cursor IDE, .cursorrules
│   └── shared/
│       └── validation_framework.md                     # TRM patterns, benchmarks
├── user_prompts/                        # Task instructions by category (~60 prompts)
│   ├── architecture/                    # 6 prompts
│   ├── requirements/                    # 4 prompts
│   ├── engineering/                     # 22 prompts (across 12 specialist categories)
│   ├── deployment/                      # 2 prompts
│   ├── self_improvement/                # 24 prompts (7 top-level + 17 engineering specialists)
│   │   └── engineering_specialists/     # 17 specialist improvement prompts
│   ├── prompt_engineering/              # 6 prompts
│   └── proposals/                       # 4 prompts
├── knowledge_base/                      # JSON state management
│   ├── system_config.json               # Platform config, 150+ technical refs (v2.0.0)
│   ├── user_requirements.json           # Business requirements
│   ├── design_decisions.json            # Architecture decisions
│   ├── schemas/                         # JSON schemas for validation
│   │   ├── system_config.schema.json
│   │   ├── user_requirements.schema.json
│   │   └── design_decisions.schema.json
│   └── README.md                        # Knowledge base guide
├── docs/                                # Complete documentation (GitHub Pages-ready)
├── docs/                                # Technical documentation
├── templates/                           # Reusable templates
└── outputs/                             # Agent-generated content (created during use)
```

## Deployment Architecture

### Tier 1 Deployment (This Framework)

**Target**: Cursor IDE custom chat modes  
**Method**: Copy `.system.prompt.md` files to Cursor Settings → Chat → Custom Modes  
**Scope**: Single developer or team using Cursor

**Setup**:
1. Open Cursor → Settings → Chat → Custom Modes
2. Create new mode, paste `supervisor_agent.system.prompt.md`
3. Enable "All tools"
4. Repeat for specialized agents as needed

### Tier 2 Deployment (Generated Systems)

**Targets**: OpenAI, Claude, Bedrock, Cursor, self-hosted platforms  
**Method**: Platform-specific (guided by Deployment Agent)  
**Scope**: End users, production systems

**Process**:
1. Engineering Agent generates system components
2. Deployment Agent creates deployment guide
3. User executes platform-specific deployment
4. System runs on target platform

## Security Architecture

### Tier 1 Security (Development)
- No external API dependencies (runs locally in Cursor)
- File access limited to repository directory
- Knowledge base files stored locally
- No data transmission outside IDE

### Tier 2 Security (Deployment)
- Platform-specific security models
- Deployment Agent provides security guidance
- Architecture Agent considers security requirements
- Well-Architected Framework compliance

## Performance Characteristics

### Agent Response Time
- Supervisor routing: Immediate
- Requirements gathering: 5-10 minutes (interactive)
- Architecture design: 10-15 minutes
- Engineering prototyping: 15-30 minutes
- Deployment planning: 5-10 minutes

### Knowledge Base Performance
- JSON file I/O: Negligible overhead
- State persistence: Automatic
- Cross-agent handoff: Seamless with full context

## Extensibility

### Adding New Agents
1. Create `.system.prompt.md` file in `ai_agents/`
2. Define responsibilities and knowledge base access
3. Update Supervisor Agent routing logic
4. Add corresponding user prompts
5. Document in agent-relationships.md

### Adding User Prompts
1. Create `.user.prompt.md` in appropriate category
2. Follow existing prompt structure
3. Reference correct knowledge base files
4. Test with target agent

## References

- **README.md**: Quick start and system overview
- **docs/getting-started.md**: Step-by-step walkthrough
- **docs/workflow_guide.md**: Complete workflow documentation
- **docs/agent-architecture-and-collaboration.md**: Comprehensive agent guide and collaboration patterns
- **docs/agent-design-patterns.md**: Reusable AI agent design patterns
- **outputs/README.md**: Output directory structure and organization

## Version

**Current**: 2.0 (Engineering Agent Deep Specialization)  
**Framework Platform**: Cursor IDE • GitHub Copilot • Claude Projects  
**Generated System Platforms**: Claude Projects • AWS Bedrock (hyper-specialized)  
**Tech Stack Focus**: Python, Streamlit, Anthropic Claude (5 specialists), AWS Bedrock (2 specialists), MCP, LangChain  
**Agent Count**: 23 specialized agents (1 Supervisor + 22 specialists in two-layer architecture)  
**Last Major Update**: 2025-01-12 - Engineering Agent decomposed into 16 hyper-specialized agents
- Anthropic Claude: 5 specialists (Code, Workspaces, Agents SDK, MCP, Projects)
- AWS Bedrock: 2 specialists (AgentCore, Strands)
- GitHub & Cursor: Split into separate specialists
