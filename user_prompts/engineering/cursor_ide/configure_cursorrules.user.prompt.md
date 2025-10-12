# Configure .cursorrules for AI Project

**Agent:** GitHub & Cursor Integration Agent  
**Category:** DevOps & Tooling  
**Complexity:** Simple  
**Duration:** 30 minutes

---

## Purpose

Create .cursorrules file to configure Cursor IDE for Python+Streamlit+Claude AI development with proper coding standards and patterns.

---

## Instructions

Create .cursorrules with:

1. **Tech stack declaration**
2. **Code style guidelines**
3. **Project structure standards**
4. **Common patterns and best practices**
5. **Testing and security requirements**

---

## Expected Output

```markdown
# .cursorrules

# Python AI Development with Streamlit + Claude + AWS

## Tech Stack
- **Language:** Python 3.12+
- **UI Framework:** Streamlit
- **LLM Provider:** Anthropic Claude (claude-3-5-sonnet-20241022)
- **Orchestration:** LangChain
- **Cloud Platform:** AWS (Bedrock, ECS, Lambda)
- **Data:** SQLite, pandas, numpy
- **Vector DB:** ChromaDB, FAISS
- **Testing:** pytest
- **CI/CD:** GitHub Actions
- **IaC:** AWS CDK (Python)

## Code Style and Standards

### Python Style
- Follow PEP 8 strictly
- Use type hints for all function signatures
- Write Google-style docstrings for all functions and classes
- Maximum line length: 100 characters
- Use meaningful variable names (no single letters except in loops)

### Import Organization
```python
# Standard library imports
import os
import json
from datetime import datetime
from typing import List, Dict, Optional

# Third-party imports
import streamlit as st
import pandas as pd
from anthropic import Anthropic
from langchain_anthropic import ChatAnthropic

# Local application imports
from src.claude.client import ClaudeService
from src.database.repositories import MessageRepository
```

### Function Structure
```python
def function_name(
    param1: str,
    param2: int,
    param3: Optional[Dict] = None
) -> ReturnType:
    """
    Brief description of what function does.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        param3: Optional description
    
    Returns:
        Description of return value
    
    Raises:
        ValueError: When param1 is invalid
    """
    # Implementation
    pass
```

## Project Structure

```
project/
├── streamlit_app.py          # Main Streamlit entry point
├── src/
│   ├── claude/               # Claude SDK integration
│   ├── workflows/            # LangChain workflows
│   ├── knowledge/            # Vector DB and RAG
│   ├── database/             # SQLite data access
│   └── data/                 # Data processing
├── tests/                    # pytest test suites
├── infra/                    # AWS CDK infrastructure
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variables template
└── README.md
```

## Streamlit Best Practices

1. **Session State Management**
   - Always initialize in session state before use
   - Use meaningful keys: `st.session_state.messages`, not `st.session_state.m`

2. **Caching**
   - Use `@st.cache_data` for data loading
   - Use `@st.cache_resource` for client initialization (Claude, database)

3. **Error Handling**
   - Wrap API calls in try/except
   - Use `st.error()` for user-facing errors
   - Use `st.exception()` for detailed debugging

4. **UI Patterns**
   - Use `st.chat_message()` for chat interfaces
   - Use `st.spinner()` for loading states
   - Use `st.expander()` for collapsible sections

## Claude Integration Standards

1. **API Key Management**
   - ALWAYS use environment variables: `os.getenv("ANTHROPIC_API_KEY")`
   - NEVER hardcode API keys
   - Use `.env` file for development

2. **Error Handling**
   - Implement retry logic for rate limits (exponential backoff)
   - Handle APIError, RateLimitError, APIConnectionError
   - Provide user-friendly error messages

3. **Usage Tracking**
   - Track input_tokens and output_tokens
   - Calculate costs
   - Log usage for monitoring

4. **Model Selection**
   - Claude 3.5 Sonnet: Default for most tasks (balanced)
   - Claude 3.5 Haiku: Fast, simple tasks
   - Claude 3 Opus: Complex reasoning tasks

## LangChain Patterns

1. **LCEL Chains**
   - Use pipe operator `|` for chain composition
   - Keep chains readable and well-commented
   - Test each component independently

2. **Memory Management**
   - Use ConversationBufferMemory for short conversations
   - Use ConversationSummaryMemory for long conversations
   - Clear memory appropriately

## Testing Requirements

1. **Coverage:** Maintain >80% code coverage
2. **Test Types:**
   - Unit tests for all business logic
   - Integration tests for workflows
   - Mock external APIs (Claude, AWS)
3. **Run Before Commit:** `pytest && black src/ && flake8 src/`

## Security Requirements

1. **Secrets Management**
   - Use AWS Secrets Manager for production
   - Use .env for local development
   - Add .env to .gitignore

2. **Input Validation**
   - Validate all user inputs
   - Sanitize file uploads
   - Implement rate limiting

3. **AWS Security**
   - Use least-privilege IAM policies
   - Enable CloudWatch logging
   - Configure Bedrock Guardrails

## Common Tasks and Patterns

### Creating Streamlit Chat Interface
```python
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Message"):
    # Handle message
    pass
```

### Claude SDK Call with Error Handling
```python
from anthropic import Anthropic, RateLimitError
import time

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

for attempt in range(3):
    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=4096,
            messages=messages
        )
        break
    except RateLimitError:
        if attempt < 2:
            time.sleep(2 ** attempt)
        else:
            raise
```

### LangChain LCEL Chain
```python
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

chat = ChatAnthropic(model="claude-3-5-sonnet-20241022")
prompt = ChatPromptTemplate.from_template("Task: {task}")

chain = prompt | chat | StrOutputParser()
result = chain.invoke({"task": "Explain AI"})
```

## AWS Deployment Patterns

### CDK Stack
- Use Python CDK (not TypeScript)
- Organize into logical stacks (compute, storage, monitoring)
- Use environment variables for account/region

### ECS Deployment
- Use Fargate (serverless containers)
- Configure health checks
- Enable auto-scaling
- Use Application Load Balancer

## Documentation Standards

- README.md must include: setup, usage, deployment, troubleshooting
- All modules must have docstrings
- Complex functions must include usage examples
- Keep documentation up-to-date with code changes
```

---

## Success Criteria

✅ .cursorrules file comprehensive  
✅ All tech stack patterns documented  
✅ Code examples clear and correct  
✅ Cursor AI follows guidelines  
✅ Team aligned on standards

---

## Usage

Place `.cursorrules` in project root. Cursor AI will automatically use it for code generation and suggestions.
