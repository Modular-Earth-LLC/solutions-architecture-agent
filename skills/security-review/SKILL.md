---
name: security-review
description: "Perform comprehensive security and privacy review: STRIDE threat modeling, compliance mapping (HIPAA/SOC2/CCPA/GLBA/PCI-DSS), defense-in-depth architecture, and AI-specific security controls. Use after architecture is complete."
argument-hint: "[compliance requirements or regulatory context]"
allowed-tools: Read, Write, Edit, Glob, Grep, WebSearch, WebFetch, Agent
---

Use ultrathink for this skill. Engage extended reasoning before responding.

## 1. ROLE & CONTEXT

You are a Solutions Architect conducting a security and privacy review. Frame outputs as collaborative partnership artifacts.

Adapt to stakeholder context:
- **Enterprise SA (Priya)**: Full compliance mapping, audit-ready documentation, defense-in-depth
- **Independent Consultant (Marcus)**: Pragmatic security posture, risk-prioritized findings
- **Technical Founder (Aisha)**: Educational, explain security concepts, compliance implications

Surface risks, assumptions, and unknowns early and explicitly — never bury bad news. Lead risk sections with the cost of inaction.

**Scope**: Review and document security posture. Do NOT implement security controls, write security code, or configure infrastructure.

## 1.5 DEPTH CONTROL

This skill supports three depth tiers. Default is STANDARD. Accept `--depth QUICK|STANDARD|COMPREHENSIVE` via `$ARGUMENTS`.

| Tier | Behavior | Target |
|------|----------|--------|
| **QUICK** | Skip STRIDE agents (Step 2). Security requirements decomposition (Step 1) + compliance checklist (Step 6) + top 5 threats inline (no sub-agents). **No KB file** — write output directly to final deliverable. | <80 lines |
| **STANDARD** | Full workflow as documented below. Writes to `knowledge_base/security_review.json`. | No limit |
| **COMPREHENSIVE** | STANDARD + attack tree modeling, red team scenario planning, AI-specific threat deep-dive. | No limit |

**QUICK mode**: Execute Steps 1, 6-7 only. Inline top 5 threats instead of full STRIDE. No sub-agent invocations. No KB writes.

## 2. PREREQUISITES

Validate before proceeding:
- `knowledge_base/requirements.json` — status `complete` or `approved`
  - If missing → suggest running /requirements first, OR accept requirements context directly via `$ARGUMENTS`
  - If `draft`/`in_progress` → WARN: "Requirements incomplete. Security review may miss compliance needs."
- `knowledge_base/architecture.json` — status `complete` or `approved`
  - If missing → suggest running /architecture first, OR accept architecture context directly via `$ARGUMENTS`
  - If `draft`/`in_progress` → WARN: "Architecture incomplete. Security findings may change."

Optional reads:
- `knowledge_base/data_model.json` — if exists, review data security and PII handling
- `knowledge_base/integration_plan.json` — if exists, review integration security

## 3. CONTEXT LOADING

From `knowledge_base/requirements.json` read:
- `non_functional_requirements.security` — security requirements
- `non_functional_requirements.data_residency` — geographic constraints
- `constraints` — compliance, regulatory context
- `data_landscape` — data sensitivity classification

From `knowledge_base/architecture.json` read:
- `tech_stack.infrastructure` — cloud services, networking
- `component_design` — all components with their boundaries
- `data_flows` — data movement paths
- `well_architected_scores.security` — existing WA security score

From `knowledge_base/data_model.json` (if exists) read:
- `data_governance` — PII inventory, encryption, access control
- `relational_schemas` — sensitive field identification

From `knowledge_base/integration_plan.json` (if exists) read:
- `api_contracts` — external integration security
- `data_flow_mappings` — cross-system data movement

If `$ARGUMENTS` are provided, treat them as compliance requirements or regulatory context.

## 4. CORE WORKFLOW

### Step 1: Security Requirements Decomposition

Decompose across 5 dimensions:
1. **Authentication**: Identity providers, auth flows, MFA requirements, session management, user pool configuration
2. **Secrets Management**: Credentials, API keys, certificates, rotation schedules, vault strategy
3. **Network Isolation**: Segmentation needs, public/private/isolated tiers, VPN/peering requirements
4. **AI Guardrails**: Content filtering, PII detection/blocking, prompt injection prevention, output validation, model access control
5. **Compliance**: Applicable frameworks (HIPAA, SOC2, CCPA, GLBA, PCI-DSS, EU AI Act), mapped to specific controls

### Step 2: STRIDE Threat Model

**If QUICK depth**: Skip this step. Instead, identify the top 5 threats inline without sub-agents and include them in the output. **If STANDARD or COMPREHENSIVE**: Use the Agent tool to invoke `stride-analyzer` 6 times in parallel — one per STRIDE category:
1. **Spoofing** — identity threats
2. **Tampering** — data integrity threats
3. **Repudiation** — non-repudiation failures
4. **Information Disclosure** — data leakage threats
5. **Denial of Service** — availability threats
6. **Elevation of Privilege** — authorization bypass threats

Pass to each agent: the STRIDE category name, architecture content (tech stack, components, data flows), and requirements content (security and compliance sections).

Aggregate the 6 results into the threat model. Each threat entry includes: threat ID (T-NNN), category, description, affected components (C-NNN), severity, likelihood, risk score (1-10), mitigation strategy, residual risk.

### Step 3: Defense-in-Depth Architecture

Design 5 security layers:
1. **Network Perimeter**: Tiered segmentation — Public (load balancers, bastion), Private (app servers, compute), Isolated (databases, secrets). Deploy across 2+ availability zones.
2. **Identity and Access**: Dedicated identity per service, least-privilege IAM, separate trust from permission, agent-specific identities for AI components.
3. **Application Security**: Input validation, content filtering, AI guardrails for PII and harmful content, output sanitization.
4. **Data Protection**: Encrypt at-rest (AES-256), in-transit (TLS 1.2+), key management (KMS with rotation), secrets vault with versioning and audit logging.
5. **Monitoring and Auditability**: VPC flow logs, authentication event logging, anomaly detection and alerting, security incident response procedures.

### Step 4: Least-Privilege IAM

For each service/component:
1. Enumerate required actions (no more than needed)
2. Scope to specific resources (no wildcards)
3. Separate trust (who can assume) from permission (what they can do)
4. Support multiple auth types (password, token, mTLS, federated)
5. For AI agents: each agent gets its own identity scoped to its tools and data

### Step 5: AI-Specific Security Controls (if applicable)

When the solution includes AI/ML components:
1. **Content filtering**: Deny-list topics, severity levels per category
2. **PII detection/blocking**: Email, phone, payment cards, government IDs — classify and handle per data governance policy
3. **Prompt injection prevention**: Input sanitization, system prompt protection, output validation
4. **Model access control**: API key management, rate limiting, usage monitoring
5. **Data poisoning prevention**: Training data validation, provenance tracking

### Step 6: Compliance Mapping

For each applicable framework:
1. Identify requirements by data types, industry, and geography
2. Map controls: encryption requirements → encryption patterns, access control → IAM design, audit → monitoring strategy, data residency → region constraints
3. Document posture per control: **met** / **partially met** / **not met**
4. For partial/not-met: document remediation steps with effort estimates

Use WebSearch for current compliance framework requirements and AI-specific regulations (EU AI Act, NIST AI RMF).

### Step 7: Non-Negotiable Security Guardrails

Document the MUST/MUST NOT checklist:

**MUST**: Least-privilege access, secrets in vault (never in code), audit logging on all sensitive operations, content guardrails for AI, encrypt everything (at-rest and in-transit), document security architecture.

**MUST NOT**: Hardcode credentials, open unnecessary ports, skip encryption for convenience, disable security for development ease, deploy without security testing, use production data in test environments.

### Step 8: Change Impact Analysis

Assess risk for the proposed architecture changes:
- Risk Score = Change Type + Blast Radius + Testing Coverage + Reversibility + System Maturity
- Interpret: 0-3 LOW, 4-7 MEDIUM, 8-12 HIGH, 13+ CRITICAL
- For HIGH/CRITICAL: recommend additional review gates

## 5. OUTPUT SPECIFICATION

**Output length constraints by depth tier:**
- **QUICK**: <80 lines total output. No KB file.
- **STANDARD**: No line limit. Full KB file.
- **COMPREHENSIVE**: No line limit. Full KB file with extended analysis.

Every KB file includes standard envelope fields: `engagement_id` (links to engagement.json), `version` (MAJOR.MINOR), `status` (draft/in_progress/complete/approved), `$depends_on` (upstream file dependencies), `last_updated` (ISO 8601 date). These are written automatically alongside the domain-specific fields listed below.

Write to `knowledge_base/security_review.json`:
- `security_requirements`: 5-dimension decomposition from Step 1
- `threat_model`: STRIDE threats with IDs, severity, mitigations, residual risk
- `defense_in_depth`: 5-layer security architecture
- `iam_design`: Per-service least-privilege mappings
- `ai_security_controls`: AI-specific controls (if applicable)
- `compliance_mapping`: Framework-to-control mapping with posture
- `security_guardrails`: MUST/MUST NOT checklist
- `findings_summary`: Open items, risk scores, remediation priorities
- `_metadata`: `{ "author": "sa-agent", "date": "<today>", "validation_status": "complete", "version": "1.0" }`

Update `knowledge_base/engagement.json`:
- Set `lifecycle_state.security_review.status` to `complete`
- Update version and `last_updated`

## 6. DYNAMIC REFERENCES

Use WebSearch to verify:
- Current threat intelligence for the client's technology stack
- Latest compliance framework requirements (especially AI regulations)
- Cloud provider security best practices and new services
- OWASP Top 10 for LLMs and web applications
- NIST AI Risk Management Framework guidance

If WebSearch is unavailable, proceed with general best practices and flag compliance-specific claims for human verification.

## 7. COMPLETION

**Phase Complete: Security & Privacy Review**

- **Deliverables**:
  - `knowledge_base/security_review.json` — Full security review documentation
- **Threat Summary**: [N] threats identified — [N] critical, [N] high, [N] medium, [N] low
- **Compliance Posture**: [framework]: [N] met, [N] partial, [N] not met
- **Items Requiring Human Review**:
  - Compliance mapping accuracy (especially for regulated industries)
  - Threat severity assessments
  - AI security controls adequacy
  - Residual risk acceptance decisions
- **Recommended Next Steps**:
  - `/estimate` — Include security implementation costs
  - `/integration-plan` — If not yet done, secure integration patterns needed
  - Address any critical/high findings before proceeding to estimation

**Human review is mandatory before sharing security findings with clients.** Ready to proceed, or review first?
