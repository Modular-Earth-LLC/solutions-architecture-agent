# Create AI Engineering Documentation

**Purpose**: Create professional documentation for Python+Streamlit+Claude+AWS AI systems targeted at developers new to AI engineering on AWS, Anthropic, Cursor, and GitHub platforms.

**Target Audience**: Developers learning AI development with Python+Streamlit+Claude+AWS+MCP  
**Platforms**: AWS Bedrock, Anthropic Claude, Cursor IDE, GitHub  
**Tech Stack**: Python, Streamlit, Claude, AWS, MCP, LangChain  
**Agent**: Prompt Engineering Agent or Cursor IDE Agent

---

## Mission

Transform documentation for AI engineering systems into clear, practical guides that help developers new to AI quickly become productive with Python+Streamlit+Claude+AWS development.

**Target Developers**:
- AWS developers learning Bedrock (AgentCore, Strands)
- Anthropic Claude users building multi-agent systems
- Cursor IDE users optimizing AI development
- GitHub developers setting up AI CI/CD
- Python developers new to LLMs and AI agents

---

## Core Principles for AI System Documentation

### 1. Platform-Specific Guidance

**AWS Developers Need**:
- Clear AgentCore setup (Gateway, Identity, Runtime, Memory)
- Strands SDK patterns and observability
- IAM roles and security configuration
- CDK infrastructure examples

**Anthropic Developers Need**:
- Claude API integration patterns
- Multi-agent orchestration examples
- MCP server implementation
- Token usage and cost optimization

**Cursor Users Need**:
- .cursorrules for AI projects
- Custom chat mode setup (23 agents)
- Composer workflows
- AI-assisted coding patterns

**GitHub Users Need**:
- GitHub Actions for AI projects (test LLMs, deploy to Bedrock)
- GitHub Copilot optimization
- Security scanning (CodeQL for AI code)
- CI/CD for ML/AI workflows

### 2. AI-Specific Concepts

**Explain clearly for newcomers**:
- What are AI agents? (simple definition + example)
- Multi-agent systems (supervisor-worker pattern)
- RAG (Retrieval-Augmented Generation)
- Vector databases (semantic search)
- Model Context Protocol (tool integration)
- LangChain (workflow orchestration)

### 3. Quick Start Focused

**Get developers productive in <15 minutes**:
1. Clone/install
2. Configure API keys (.env template)
3. Run first example (Streamlit+Claude chat)
4. See results immediately
5. Next steps clearly laid out

### 4. Reference Centralized Knowledge

**Point to system_config.json**:
```markdown
## Technical References

All documentation links centralized in `knowledge_base/system_config.json`:
- Anthropic Claude: 11 references
- AWS Bedrock: 7 references (+ 6 AgentCore + 4 Strands)
- LangChain, Streamlit, GitHub, Cursor: Complete references
- Research papers: TRM, MetaGPT, efficient reasoning
- Design patterns: Supervisor-worker, TRM validation, etc.

See system_config.json → technical_references for all URLs.
```

---

## Required Sections

### 1. Overview (AI System Focus)

```markdown
## Overview

[System name] is a Python+Streamlit+Claude+AWS AI application that [specific capability].

**What it does**:
- [Primary capability]
- [Key feature 1]
- [Key feature 2]

**Tech Stack**:
- **UI**: Streamlit (Python)
- **LLM**: Anthropic Claude (via anthropic SDK)
- **Orchestration**: LangChain
- **Deployment**: AWS Bedrock (AgentCore or Strands)
- **Data**: SQLite + ChromaDB/FAISS
- **Tools**: MCP servers, GitHub Actions, Cursor IDE

**Architecture**: [Single agent | Multi-agent supervisor-worker | RAG system | etc.]
```

### 2. Quick Start (AI-Specific)

```markdown
## Quick Start (15 minutes)

### Prerequisites
- Python 3.12+
- Anthropic API key ([get one here](https://console.anthropic.com/))
- AWS account (for Bedrock deployment)

### Setup
1. Clone and install:
   ```bash
   git clone [repo]
   cd [project]
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Configure environment:
   ```bash
   cp .env.example .env
   # Edit .env and add:
   # ANTHROPIC_API_KEY=your-key-here
   ```

3. Run Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```

4. Open browser at http://localhost:8501

5. Try it: Type "Hello!" in the chat

**Expected**: Claude responds in chat interface

**Next**: Explore [specific features] or deploy to AWS Bedrock
```

### 3. Architecture (AI Systems)

```markdown
## Architecture

**Pattern**: [Supervisor-Worker | Sequential Chain | RAG | etc.]

[Simple ASCII diagram showing agent flow]

**Components**:
- **Streamlit UI**: Chat interface, file upload, analytics
- **Claude Integration**: anthropic SDK, streaming, tool use
- **LangChain**: Workflow orchestration, memory management
- **Vector Database**: ChromaDB for RAG (if applicable)
- **AWS Deployment**: ECS/Bedrock with AgentCore/Strands

**Data Flow**: User → Streamlit → Claude API → [Processing] → Response

See `system_config.json` → `technical_references` → `design_patterns` for pattern details.
```

### 4. Tech Stack Details

```markdown
## Tech Stack

**Core Technologies** (from system_config.json):
- Python 3.12+
- Streamlit (UI framework)
- Anthropic Claude (claude-3-5-sonnet, haiku, opus)
- LangChain (orchestration)
- AWS Bedrock (deployment)

**Framework Choice** (if multi-agent):
- [ ] Claude Workspaces (Anthropic hosted)
- [ ] AWS Bedrock AgentCore (Gateway/Identity/Runtime/Memory)
- [ ] AWS Bedrock Strands (open-source, observable)

**Data Storage**:
- SQLite (application data)
- ChromaDB or FAISS (vector search for RAG)

See `system_config.json` → `technical_references` for all documentation links.
```

### 5. Development Guide (Platform-Specific)

**For Cursor IDE Users**:
```markdown
## Development in Cursor IDE

1. Open project in Cursor
2. Cursor reads `.cursorrules` automatically
3. Use custom chat modes (configure 23 engineering agents)
4. CMD+K for inline AI edits
5. Composer for multi-file operations

See `ai_agents/cursor_ide_agent.system.prompt.md` for full setup.
```

**For GitHub Users**:
```markdown
## GitHub Integration

1. Push to GitHub repository
2. GitHub Actions auto-runs CI/CD (`.github/workflows/`)
3. Tests run automatically on PRs
4. Deploy to AWS on merge to main
5. Dependabot keeps dependencies updated

See `ai_agents/github_copilot_agent.system.prompt.md` for setup.
```

**For AWS Deployment**:
```markdown
## AWS Bedrock Deployment

**Option A: AgentCore** (Enterprise)
- Converts APIs to MCP tools (Gateway)
- Secure authentication (Identity)
- Serverless execution (Runtime)
- Persistent state (Memory)

**Option B: Strands** (Observable)
- Open-source SDK
- X-Ray tracing
- Reasoning patterns (ChainOfThought, ReAct)
- Production deployment

See `system_config.json` → `technical_references` → `aws_bedrock_agentcore` and `aws_bedrock_strands`.
```

### 6. Common Patterns (AI-Specific)

```markdown
## Common AI Development Patterns

### Chat Interface with Claude
```python
import streamlit as st
from anthropic import Anthropic

if "messages" not in st.session_state:
    st.session_state.messages = []

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Message"):
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        messages=[...],
        max_tokens=4096
    )
    # Display response
```

### RAG with LangChain
```python
from langchain_anthropic import ChatAnthropic
from langchain_community.vectorstores import Chroma

# Setup vector store
vectorstore = Chroma(...)
retriever = vectorstore.as_retriever()

# RAG chain
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | ChatAnthropic(model="claude-3-5-sonnet-20241022")
    | StrOutputParser()
)
```

See `ai_agents/shared/validation_framework.md` for quality standards.
```

### 7. Learning Resources

```markdown
## Learning Path for AI Development

**New to AI Development? Start Here**:

1. **Understand Core Concepts** (30 min)
   - Read: What are LLMs, agents, RAG?
   - See: `docs/getting-started.md`

2. **Learn Python AI Stack** (2-4 hours)
   - Streamlit basics
   - Anthropic Claude API
   - LangChain fundamentals
   - See: `system_config.json` → `technical_references`

3. **Build First App** (1-2 hours)
   - Use Streamlit UI Agent
   - Integrate Claude with Claude Integration Agent
   - Deploy to Claude Projects

4. **Add Advanced Features** (ongoing)
   - RAG with Knowledge Engineering Agent
   - Multi-agent with Claude Workspaces Agent
   - AWS deployment with Bedrock agents

**Resources** (from system_config.json):
- Anthropic docs: `technical_references.anthropic_claude.*`
- AWS Bedrock: `technical_references.aws_bedrock.*`
- Research papers: `technical_references.research_papers.*`
```

---

## Validation & Quality

### Before Publishing Documentation

Use validation framework:
```markdown
## Documentation Validation

✅ **Quality Checks**:
- All code examples tested and work
- All links verified (check system_config.json)
- Platform-specific guidance accurate
- Learning path clear for AI newcomers

✅ **AI-Specific Validation**:
- API keys explained (.env template)
- Model selection guidance clear
- Token costs mentioned
- Rate limits documented
- Error handling examples included

See `ai_agents/shared/validation_framework.md` for quality standards.
```

---

## Output Template

```markdown
# [AI System Name]

[One-sentence description for AI system with tech stack]

**Tech Stack**: Python | Streamlit | Anthropic Claude | AWS Bedrock | [Other]  
**Pattern**: [Single Agent | Multi-Agent | RAG | etc.]  
**Deployment**: Claude Projects | AWS Bedrock AgentCore | AWS Bedrock Strands

## Quick Start

[5 steps to running AI system locally - <15 min]

## Architecture

[AI system architecture with agent diagram if multi-agent]

## Tech Stack

[Detailed stack with links to system_config.json → technical_references]

## Development

**Cursor IDE**: [Setup guide]  
**GitHub**: [CI/CD setup]  
**AWS**: [Deployment options]

## Learning Resources

[Path for developers new to AI - points to centralized references]

## Troubleshooting

[Common AI development issues: API keys, rate limits, costs, model selection]
```

---

## Success Criteria

✅ **Platform-Appropriate**: Guidance for AWS, Anthropic, Cursor, GitHub  
✅ **AI-Focused**: Explains agents, RAG, LLMs, multi-agent patterns  
✅ **Quick Start**: Developers productive in <15 minutes  
✅ **References Centralized**: Points to system_config.json  
✅ **Newcomer-Friendly**: Clear for those new to AI  
✅ **Production-Ready**: Can deploy immediately after reading

---

**Version**: 2.0  
**Date**: 2025-01-12  
**Focus**: AI engineering with Python+Streamlit+Claude+AWS+MCP  
**Target**: Developers new to AI on AWS, Anthropic, Cursor, GitHub platforms
