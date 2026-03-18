# Deployment Options (Reference Architecture)

> **Note**: This document describes a reference architecture for cloud deployment. The production implementation is not included in this repository.

## Current Deployment

Today, this agent runs as a **Claude Code plugin**. Install with:

```bash
claude --plugin-dir .
```

See [local-setup.md](local-setup.md) for full installation options.

---

## Cloud Deployment Options

### Option 1: Claude API with Tool Use

Deploy the agent as a system prompt + tool definitions:

- Skills become tools that the agent can call
- Knowledge base files become retrievable documents
- Users interact via API calls

### Option 2: Anthropic Python SDK (Agent Wrapper)

Package as a Python agent using the `anthropic` package:

```python
import anthropic

client = anthropic.Anthropic()

# Example: requirements skill becomes an API tool
def requirements_discovery(
    project_description: str,
    workshop_type: str = "standard"  # quick | standard | comprehensive
) -> dict:
    """Run a requirements discovery workshop for the given project."""
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8096,
        system="...",  # compiled from CLAUDE.md + SKILL.md
        messages=[{"role": "user", "content": project_description}]
    )
    return response
```

### Option 3: Claude Projects (Manual, Non-API)

- Upload knowledge base files as project knowledge
- Set supervisor prompt as custom instructions
- No API access — manual use only
- Good for demos and personal use

---

## Reference File Structure for Cloud Packaging

```
cloud/
├── agent.py                    # Main agent entry point
├── system_prompt.md            # Compiled from CLAUDE.md + core rules
├── tools/                      # Compiled from skills/
│   ├── requirements.py
│   ├── architecture.py
│   └── ...
├── references/                 # From knowledge_base/
│   ├── system_config.json
│   └── well_architected.json
├── pyproject.toml              # Dependencies
└── Dockerfile                  # Container deployment
```

## Model IDs (Current)

| Use Case | Model ID |
|----------|----------|
| Highest capability | `claude-opus-4-6` |
| Balanced (recommended default) | `claude-sonnet-4-6` |
| Fast / low-cost | `claude-haiku-4-5-20251001` |

Verify current model IDs at [docs.anthropic.com](https://docs.anthropic.com/en/docs/about-claude/models).

---

## Future Considerations

- API authentication and rate limiting
- Multi-tenant support (different orgs, different configs)
- Usage metering for SaaS billing
- Custom knowledge base per tenant
- Audit logging for compliance
