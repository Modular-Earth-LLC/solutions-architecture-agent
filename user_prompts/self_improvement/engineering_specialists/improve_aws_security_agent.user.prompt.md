# Improve AWS Security & Networking Agent

**Target**: `ai_agents/aws_security_networking_agent.system.prompt.md`  
**Specialty**: IAM, VPC, Cognito, Secrets Manager, security best practices

**Framework**: See `knowledge_base/system_config.json` → `self_improvement_framework` for methodology, principles, and validation requirements.

---

## Agent-Specific Focus Areas

**What makes this agent effective:**

1. **IAM Excellence**
   - Least privilege policies
   - Role-based access control
   - Secure policy design

2. **Network Security**
   - VPC configurations secure
   - Security groups tight
   - Network isolation proper

3. **Auth & Secrets**
   - Cognito setup correct
   - Secrets Manager integrated
   - Authentication flows secure

---

## Integration Requirements

- References `ai_agents/shared/validation_framework.md`
- Coordinates with Infrastructure and AgentCore agents
- Follows AWS security best practices
- Validates security configurations

---

## Success Criteria

Beyond standard criteria (see system_config.json), ensure:

✅ IAM policies least-privilege  
✅ Network security tight  
✅ Authentication secure  
✅ Secrets managed properly  
✅ Validation framework fully integrated

---

**Version**: 2.0 | **Updated**: 2025-01-12 | **Agent-Agnostic**: Works with Optimization or Prompt Engineering agents
