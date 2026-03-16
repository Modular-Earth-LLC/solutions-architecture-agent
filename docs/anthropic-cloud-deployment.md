# Anthropic Cloud Platform Deployment Reference

## Platform Options

### Claude API with Tool Use
- Deploy the agent as a system prompt + tool definitions
- Skills become tools that the agent can call
- Knowledge base files become retrievable documents
- Users interact via API calls

### Claude Agent SDK
- Package as a Python agent using `claude_agent_sdk`
- Skills map to agent tools/functions
- Can run as a hosted service or serverless function
- Supports streaming, multi-turn conversations, and tool use

### Claude Projects (Manual, Non-API)
- Upload knowledge base files as project knowledge
- Set supervisor prompt as custom instructions
- No API access — manual use only
- Good for demos and personal use

## Mapping: Local Skills to Cloud Tools

Each `.claude/skills/<name>/SKILL.md` maps to a cloud tool definition:

```python
# Example: requirements skill becomes an API tool
@tool
def requirements_discovery(
    project_description: str,
    workshop_type: str = "standard"  # quick | standard | comprehensive
) -> RequirementsDocument:
    """Run a requirements discovery workshop for the given project."""
    ...
```

## File Structure for Cloud Packaging

```
cloud/
├── agent.py                    # Main agent entry point
├── system_prompt.md            # Compiled from CLAUDE.md + core rules
├── tools/                      # Compiled from .claude/skills/
│   ├── requirements.py
│   ├── architecture.py
│   └── ...
├── references/                 # From knowledge_base/
│   ├── system_config.json
│   └── well_architected.json
├── pyproject.toml              # Dependencies
└── Dockerfile                  # Container deployment
```

## Future Considerations

- API authentication and rate limiting
- Multi-tenant support (different orgs, different configs)
- Usage metering for SaaS billing
- Custom knowledge base per tenant
- Audit logging for compliance
