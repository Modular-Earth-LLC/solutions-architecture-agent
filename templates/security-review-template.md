# Security & Privacy Review

Output template aligned with `/security-review` skill output fields and `security_review.schema.json`.

## Depth Tier Guidance

| Tier | Required Sections | Optional Sections | Target Length |
|------|-----------------|------------------|---------------|
| QUICK | Threat Model (top 5 inline), Compliance checklist | All others | < 2 pages |
| STANDARD | Threat Model (STRIDE full), Defense-in-Depth, Compliance | AI Controls (if applicable) | 4-8 pages |
| COMPREHENSIVE | All sections | None | 8-15 pages |

## STRIDE Categories

| Letter | Category | Description |
|--------|----------|-------------|
| **S** | Spoofing | Impersonating a user, service, or system component |
| **T** | Tampering | Unauthorized modification of data or code |
| **R** | Repudiation | Denying that an action was performed (no audit trail) |
| **I** | Information Disclosure | Unintended data exposure |
| **D** | Denial of Service | Making a service unavailable |
| **E** | Elevation of Privilege | Gaining unauthorized access level |

## AI Threat to STRIDE Mapping

| AI-Specific Threat | STRIDE Category | Mitigation |
|-------------------|-----------------|------------|
| Prompt injection | Tampering (T) | Input validation, system prompt hardening |
| Model poisoning | Tampering (T) + Spoofing (S) | Data provenance, model signing |
| Jailbreaking | Elevation of Privilege (E) | Guardrails, content classifiers |
| Data exfiltration via model output | Information Disclosure (I) | Output filters, PII detection |
| Denial of model service | Denial of Service (D) | Rate limiting, circuit breakers |
| Model inversion attacks | Information Disclosure (I) | Differential privacy, output sanitization |

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

## Security Architecture

Comprehensive security controls mapping to the `security_architecture` schema field.

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

## IAM Design

Per-service least-privilege mappings (maps to `iam_design` schema field).

| Service/Component | Role | Permissions | Scope | Notes |
|-------------------|------|-------------|-------|-------|
| [Service] | [Role name] | [Permission set] | [Resource scope] | [Justification] |

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
