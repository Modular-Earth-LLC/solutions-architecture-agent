# Improve Deployment Agent

**Target**: `ai_agents/deployment_agent.system.prompt.md`  
**Specialty**: Platform deployment guides, testing strategies, monitoring setup

**Framework**: See `knowledge_base/system_config.json` → `self_improvement_framework` for methodology, principles, and validation requirements.

---

## Agent-Specific Focus Areas

**What makes this agent effective:**

1. **Deployment Guide Quality**
   - Step-by-step instructions clear
   - Platform-specific guidance (Cursor, Claude Projects, AWS Bedrock)
   - Troubleshooting comprehensive

2. **Testing Strategy**
   - Unit, integration, E2E coverage
   - LLM-specific testing patterns
   - Validation frameworks

3. **Monitoring & Observability**
   - CloudWatch setup
   - Strands observability
   - Alerting configured

4. **Platform Coverage**
   - Cursor IDE integration
   - Claude Projects deployment
   - AWS Bedrock deployment
   - GitHub Copilot configuration

---

## Integration Requirements

- Reads `knowledge_base/design_decisions.json`
- References `system_config.json` → `technical_references` for deployment docs
- Coordinates with Testing agent
- Platform-specific patterns for Cursor, Claude, AWS

---

## Success Criteria

Beyond standard criteria (see system_config.json), ensure:

✅ Deployment guides work correctly  
✅ Testing strategies comprehensive  
✅ Monitoring setup complete  
✅ All platforms covered  
✅ Troubleshooting helpful

---

**Version**: 0.1 | **Updated**: 2025-01-12 | **Status**: Alpha - Untested, undergoing initial validation
