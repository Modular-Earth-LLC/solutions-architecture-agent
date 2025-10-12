# Improve AWS Security & Networking Agent

**Target**: `ai_agents/aws_security_networking_agent.system.prompt.md`  
**Focus**: IAM policies, VPC configuration, Cognito, Bedrock Guardrails, security  
**Recursion Prevention**: Single execution per session

---

## Focus Areas

1. **IAM Excellence**
   - Least-privilege policies enforced
   - Role trust policies secure
   - Permission boundaries clear
   - Policy validation comprehensive

2. **VPC & Networking**
   - VPC properly segmented
   - Security groups restrictive
   - Network isolation effective
   - NAT gateway configuration optimal

3. **Authentication & Secrets**
   - Cognito configured securely
   - Secrets Manager used correctly
   - No credentials hardcoded
   - Rotation policies defined

4. **Bedrock Guardrails**
   - Content filtering configured
   - PII detection active
   - Topic policies appropriate
   - Word filters effective

---

## Validation Framework Integration

Ensure agent:
- Validates security configurations
- Tests IAM policies
- Checks network isolation
- Reports security posture

---

## Success Criteria

✅ IAM follows least-privilege  
✅ VPC properly secured  
✅ Secrets never exposed  
✅ Guardrails active and tested  
✅ Validation framework integrated  

**Version**: 1.0 | **Date**: 2025-01-12
