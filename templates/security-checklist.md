# Security & Privacy Review Template

Output template aligned with `/security-review` skill output fields and `security_review.schema.json`.

---

## Security Requirements

[5-dimension decomposition: confidentiality, integrity, availability, authentication, authorization]

---

## Threat Model

- **Methodology**: [STRIDE / PASTA / DREAD / attack_tree / custom]
- **Scope**: [What is covered by the threat model]

### Threats

| ID | Category | Description | Severity | Likelihood | Risk Score | Mitigation | Residual Risk | Status |
|----|----------|-------------|----------|------------|------------|------------|---------------|--------|
| T-001 | [STRIDE category] | [Description] | critical/high/medium/low | high/medium/low | [1-10] | [Mitigation] | high/medium/low/negligible | identified/mitigated/accepted/transferred |

---

## Defense in Depth

[5-layer security architecture: perimeter, network, host, application, data]

---

## IAM Design

[Per-service least-privilege mappings]

### Authentication
- **Method**: [SSO, MFA, etc.]
- **MFA Required**: [yes/no]
- **Session Management**: [JWT, cookies, etc.]

### Authorization
- **Model**: [RBAC, ABAC, etc.]
- **Roles**: [List]
- **Enforcement Point**: [Where enforced]

### Network Security
- **VPC Design**: [Architecture]
- **Security Groups**: [Rules]
- **WAF**: [Enabled/disabled]
- **DDoS Protection**: [Service]

### Encryption
- **At Rest**: [Method and key management]
- **In Transit**: [Protocol]
- **Key Management**: [Service]

### Secrets Management
[How secrets are stored and rotated]

### Logging & Monitoring
- **Audit Log**: [Service]
- **Application Log**: [Service and retention]
- **Alerting**: [Rules]

---

## AI Security Controls

- [ ] **Prompt Injection Protection**: [Methods]
- [ ] **Output Filtering**: [Methods]
- [ ] **Model Access Control**: [Policy]
- [ ] **Data Poisoning Prevention**: [Strategy]
- [ ] **Hallucination Mitigation**: [Controls]

---

## Compliance Mapping

| Framework | Requirement | Status | Evidence | Notes |
|-----------|------------|--------|----------|-------|
| [SOC2/GDPR/HIPAA/etc.] | [Requirement] | compliant/partial/non_compliant/not_applicable | [Evidence] | [Notes] |

---

## Security Guardrails

### MUST
- [ ] [Required security control 1]
- [ ] [Required security control 2]

### MUST NOT
- [ ] [Prohibited practice 1]
- [ ] [Prohibited practice 2]

---

## Findings Summary

- **Critical**: [N]
- **High**: [N]
- **Medium**: [N]
- **Low**: [N]

### Open Items

| ID | Severity | Finding | Recommendation | Owner | Due Date |
|----|----------|---------|----------------|-------|----------|
| F-001 | [Severity] | [Finding] | [Recommendation] | [Owner] | [YYYY-MM-DD] |
