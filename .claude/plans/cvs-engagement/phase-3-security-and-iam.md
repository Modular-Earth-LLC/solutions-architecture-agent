# Phase 3: Security, IAM, and Compliance

Use ultrathink for this phase. Engage extended reasoning before every major output.

Perform deep web research using WebSearch before making any technical claims. Cite all sources with URLs. Cross-validate across multiple sources. IAM may be the focus of one full 45-minute interview — this section must be exceptionally thorough, with sufficient depth to sustain 45 minutes of focused questioning from a security/IAM specialist.

## Objective

Design the comprehensive security architecture, IAM strategy, and compliance framework for CVS Health's Legacy System Transformation. This phase produces:
1. `knowledge_base/security_review.json` via `/security-review` — STRIDE threat model, compliance mapping, defense-in-depth
2. A detailed IAM strategy document addressing the dedicated key consideration
3. AI-specific security controls (for the GenAI/ML pipeline — dual competency thread)
4. Quality review of all artifacts

This phase addresses the **IAM Strategy** key consideration and the security dimensions of all other considerations. It also demonstrates Paul's security competency for the GenAI pipeline (AI-specific controls: prompt injection, output validation, responsible AI).

## Input Dependencies

- `knowledge_base/architecture.json` — Phase 2 architecture (needed for threat modeling)
- `knowledge_base/integration_plan.json` — Phase 2 integration plan (attack surface analysis)
- `knowledge_base/data_model.json` — Phase 2 data model (data classification)
- `knowledge_base/requirements.json` — Phase 0 requirements (compliance requirements)
- `outputs/cvs-legacy-transformation/research-findings.md` — Phase 0 research (Cluster 4: Healthcare IAM)
- `outputs/cvs-legacy-transformation/honesty-map.md` — Paul's security experience mapping

## Prior Phase Context

Read ALL completed phase context summaries before executing:
- `.claude/plans/cvs-engagement/context/phase-*-context.md`

Adapt this plan based on findings, corrections, and insights from prior phases. Pay special attention to:
- Phase 0's healthcare IAM research (Cluster 4) — what standards apply?
- Phase 2's GCP service selections — IAM must align with chosen services
- Phase 2's integration patterns — what is the attack surface?
- Phase 2's GenAI pipeline architecture — what AI-specific security controls are needed?
- Phase 1's accessibility requirements — auth flows must be accessible
- Any assumption corrections from prior phases

**Phase 2 Insights for Security & IAM**:
- Architecture uses Cloud Identity Platform with SAML 2.0/OIDC federation to CVS enterprise IdP (AD/Okta)
- 23 PHI/PII fields inventoried in data_model.json — use for STRIDE information disclosure analysis
- VPC Service Controls perimeter defined around all HIPAA-regulated services
- Partner Interconnect + HA VPN (<5ms encryption overhead) for IBMi connectivity — attack surface for STRIDE
- GenAI pipeline has dedicated service account (genai-pipeline@) with least-privilege — no raw PHI access
- CDC pipeline (Precisely Connect) reads IBM i journals — journal receiver access permissions need review
- Apigee X handles OAuth 2.0 token validation, rate limiting — API gateway security posture
- Cloud DLP for PHI detection before GenAI model inference — de-identification pipeline
- HIPAA retention: 6 years for audit logs, 7 years for claims (state pharmacy board requirements)
- CMEK with separate key rings per data classification (PHI vs operational vs AI artifacts)
- Three architecture options (GCP/AWS/Modern Cloud) — security review should focus on recommended GCP option but note security trade-offs across options
- Hybrid RBAC + ABAC model described conceptually — Phase 3 should design specific role-to-entity access matrix
- Cross-cloud auth needed: GCP ↔ Azure myPBM (review finding RF-010)
- WCAG 2.2 AA 3.3.8: accessible authentication (no CAPTCHAs) — impacts login flow security controls

**Phase 1 Insights for Security & IAM**:
- WCAG 2.2 AA 3.3.8 (Accessible Authentication): login flow must not require cognitive function tests (CAPTCHAs)
- IT Administrator persona (Raj Patel) needs unified IAM dashboard showing both IBMi + cloud user profiles during transition
- CVS has 120+ accessibility professionals — accessible auth flows are table stakes, not differentiators
- DUR alert overrides require reason selection for audit trail — this feeds into HIPAA compliance logging
- GenAI PA recommendations require access control: who can see AI-generated content, who can override

## Context Files

**Paul's Security Experience** (base: `C:\dev\paulprae-com`):
- `docs/security.md` — Paul's security architecture patterns
- `data/generated/career-data.json` — for security-relevant experience

**Paloist Security** (base: `C:\dev\paloist-core`):
- `docs/security-and-privacy.md` — example security architecture Paul has produced

**Agent Config**:
- `.claude/rules/guiding-principles.md` — principles 18-21 (Security & Trust), 22-27 (AI & Data)
- `knowledge_base/system_config.json` — Well-Architected Security pillar definition (READ-ONLY)
- `.claude/plans/references/sa-best-practices-research-2026.md` — security frameworks section

**Assignment**:
- `.claude/plans/references/solution-architect-case-study-and-interview.md` — key consideration 2 (IAM Strategy)
- `.claude/plans/references/CVS - GenAI Data Scientist Job Description .pdf` — AI security context

## Research Directives

### Cluster 1: Healthcare IAM Deep Dive
- `GCP Identity Platform enterprise healthcare IAM 2025 2026`
- `SMART on FHIR OAuth 2.0 healthcare identity standards`
- `healthcare RBAC ABAC attribute-based access control pharmacy`
- `single sign-on SSO healthcare enterprise legacy integration`
- `privileged access management PAM healthcare IBMi AS/400`

### Cluster 2: Healthcare Compliance Frameworks
- `HIPAA Security Rule technical safeguards 2025 2026 updates`
- `HITECH Act requirements healthcare IT systems`
- `PCI DSS pharmacy payment processing requirements`
- `state pharmacy privacy laws controlled substance DEA requirements`
- `SOC 2 Type II healthcare technology compliance`

### Cluster 3: Zero Trust in Healthcare
- `zero trust architecture healthcare enterprise implementation`
- `Google BeyondCorp zero trust model healthcare application`
- `microsegmentation healthcare legacy modern hybrid environment`
- `continuous authentication healthcare pharmacy systems`

### Cluster 4: AI/ML Security Controls
- `LLM security OWASP Top 10 LLM applications 2025 2026`
- `prompt injection prevention healthcare LLM pipeline`
- `AI output validation guardrails healthcare clinical data`
- `responsible AI governance framework healthcare enterprise`
- `GCP Vertex AI security controls model governance`

### Cluster 5: Legacy System Security
- `IBMi AS/400 security profiles user authorities modernization`
- `legacy mainframe to cloud security migration patterns`
- `API gateway security OAuth2 mTLS legacy system integration`
- `data encryption at rest in transit IBMi to cloud migration`

## Execution Steps

### Step 1: Read All Context and Input Files
Read Phase 0, 1, and 2 outputs, Paul's security docs, and the assignment. Focus on:
- The architecture's attack surface (from architecture.json and integration_plan.json)
- Data classification requirements (from data_model.json)
- Compliance requirements (from requirements.json)
- Paul's demonstrated security patterns (from security.md and security-and-privacy.md)

### Step 2: Execute Web Research
Run all 5 research clusters. Focus on:
- GCP-native IAM capabilities and healthcare compliance
- HIPAA technical safeguard requirements
- Zero trust patterns applicable to hybrid IBMi-to-cloud environments
- AI-specific security controls (OWASP Top 10 for LLMs)
- IBMi security model and migration patterns

### Step 3: Run `/security-review`
Invoke the `/security-review` skill with context:
- Architecture from architecture.json (recommended option)
- Integration plan from integration_plan.json
- Data model from data_model.json
- Requirements from requirements.json
- GenAI pipeline architecture details

The security review should cover:

**STRIDE Threat Model**:
- **Spoofing** — identity threats in hybrid IBMi/cloud environment
- **Tampering** — data integrity across legacy/modern boundary
- **Repudiation** — audit logging across systems
- **Information Disclosure** — PHI/PII exposure in transit and at rest
- **Denial of Service** — availability of critical pharmacy systems
- **Elevation of Privilege** — privilege escalation in hybrid auth model

**Compliance Mapping**:
- HIPAA Security Rule (Administrative, Physical, Technical safeguards)
- HITECH Act
- PCI DSS (pharmacy payment processing)
- DEA regulations (controlled substance tracking)
- State-specific pharmacy privacy laws
- SOC 2 Type II

**Defense-in-Depth Architecture**:
- Network security (VPC, firewall, microsegmentation)
- Application security (WAF, input validation, output encoding)
- Data security (encryption, tokenization, masking)
- Identity security (IAM, MFA, SSO)
- Monitoring and detection (SIEM, anomaly detection)

**AI-Specific Security Controls**:
- Prompt injection prevention
- Output validation and guardrails
- Model access control
- Training data security
- Responsible AI governance
- Bias detection and mitigation

### Step 4: Write IAM Strategy Document
Write to: `outputs/cvs-legacy-transformation/iam-strategy.md`

This is the deepest section because IAM may be the focus of one full 45-minute interview. The IAM strategy document must sustain 45 minutes of focused questioning from a security/IAM specialist. Structure:

```markdown
# IAM Strategy — CVS Legacy Transformation

## 1. IAM Architecture Overview
[Visual: Mermaid diagram of identity flows]

## 2. Identity Provider Strategy
- GCP Identity Platform as central IdP
- Federation with existing CVS enterprise directory (Active Directory / Azure AD)
- IBMi user profile migration and mapping
- Service account management for system-to-system auth

## 3. Authentication Architecture
- Multi-factor authentication (MFA) approach
- Single sign-on (SSO) across legacy and modern interfaces
- Session management in hybrid environment
- Passwordless authentication roadmap
- Accessibility-compliant auth flows (from Phase 1)

## 4. Authorization Model
- Role-Based Access Control (RBAC) base layer
- Attribute-Based Access Control (ABAC) for fine-grained decisions
- Policy engine (Google IAM / Open Policy Agent)
- Pharmacy-specific access patterns (DEA, controlled substances)
- Cross-system authorization consistency (IBMi ↔ modern)

## 5. Zero Trust Implementation
- BeyondCorp model adaptation for CVS
- Device trust and posture assessment
- Continuous authentication and authorization
- Microsegmentation between legacy and modern zones

## 6. Privileged Access Management
- Break-glass procedures for pharmacy systems
- Just-in-time (JIT) access for administrative functions
- Privileged session monitoring and recording
- IBMi elevated authority management

## 7. AI/ML Pipeline Access Control
- Model access governance
- Data access controls for clinical data pipeline
- API authentication for GenAI endpoints
- Output access controls (who can see AI-generated content)

## 8. Migration Strategy
- Phase 1: SSO bridge (legacy + modern coexistence)
- Phase 2: Identity consolidation (migrate IBMi profiles)
- Phase 3: Full zero trust (modern-only auth)
- Rollback procedures at each phase

## 9. Audit and Compliance
- Comprehensive audit logging
- Access review and recertification cadence
- Compliance reporting automation
- Incident response for identity-related events

## 10. Metrics and KPIs
- Mean time to provision / deprovision
- MFA adoption rate
- Failed authentication rate and response
- Privileged access usage patterns
- Compliance audit pass rate
```

### Step 5: Validate KB and Update Engagement
After `/security-review` produces `knowledge_base/security_review.json`:
1. Run `python tests/validate_knowledge_base.py` to validate against schemas
2. Update `knowledge_base/engagement.json`: set `lifecycle_state.security_review.status` to `complete`

### Step 6: Run `/review` on Security Artifacts
Review:
- `knowledge_base/security_review.json`
- IAM strategy document (self-review against criteria)

Target >= 7.5/10 across all dimensions. Iterate if below threshold.

## Honesty Rules

1. **IAM experience** → Paul has worked WITHIN IAM systems but hasn't designed enterprise IAM from scratch. Frame as: "Having operated within enterprise IAM environments at [company], I understand the operational requirements. For this engagement, I've designed the IAM strategy based on [framework/standard]..."
2. **Security architecture** → map to Paul's actual security work from security.md and security-and-privacy.md
3. **HIPAA specifics** → cite the actual regulation sections (§164.312 for Technical Safeguards, etc.)
4. **GCP security services** → researched for this engagement. Cite GCP documentation.
5. **AI security controls** → Paul has built AI systems, which gives context for AI security. Reference OWASP Top 10 for LLMs.
6. **Zero trust** → researched. Cite Google BeyondCorp and NIST SP 800-207.
7. **IBMi security** → entirely researched. Every claim must have a source.
8. **Compliance claims** → cite specific regulation sections, not general statements

## Quality Gate

- Run `/review` on `knowledge_base/security_review.json`
- Minimum score: >= 7.5/10 across all 5 dimensions (completeness, technical soundness, well-architected, clarity, feasibility)
- Note: `/security-review` uses `stride-analyzer` sub-agents for parallel STRIDE category analysis
- STRIDE threat model must cover all 6 categories with specific threats
- Compliance mapping must cite specific regulation sections
- IAM strategy must address all 10 sections in the outline
- AI-specific security controls must reference OWASP Top 10 for LLMs
- GCP security services must be accurately described
- Zero trust model must be contextually appropriate (not generic)
- IAM strategy document provides sufficient depth for a 45-minute interview

## Exit Criteria

Before proceeding to Phase 4:
- [ ] `knowledge_base/security_review.json` produced and reviewed
- [ ] IAM strategy document written with all 10 sections
- [ ] STRIDE threat model complete for hybrid IBMi/cloud architecture
- [ ] Compliance mapping covers HIPAA, HITECH, PCI DSS, DEA
- [ ] AI-specific security controls documented
- [ ] Zero trust implementation plan with phases
- [ ] `/review` score >= 7.5/10 on security review
- [ ] All assumptions numbered (A-3-NNN series)
- [ ] `engagement.json` lifecycle_state updated for security_review
- [ ] KB validation passes: `python tests/validate_knowledge_base.py`

## Context Handoff

After execution completes, save context for future phases:

1. **Write context summary** to `.claude/plans/cvs-engagement/context/phase-3-context.md` using the Context Summary Template (see master-plan.md)

2. **Update ALL remaining phase plan files** with:
   - Security requirements that Phase 4 needs to estimate (security infrastructure costs, compliance audit costs)
   - IAM migration phases that Phase 4 needs for project planning
   - AI security controls that Phase 5 needs for methodology documentation
   - Compliance frameworks that Phase 6 needs for document assembly
   - Any new security-driven architecture changes that affect Phase 4's scope
   - Corrected or new assumptions

3. **Update master-plan.md** if any structural changes to the engagement

4. **Commit** all context and plan updates to git with message: `docs(plans): complete Phase 3 security and IAM, update future plans`

## Human Checkpoint

Paul: review the following before proceeding to Phase 4:
- Security review: `knowledge_base/security_review.json`
  - Is the STRIDE threat model thorough enough for a 45-minute focused interview?
  - Are the compliance mappings accurate?
- IAM strategy: `outputs/cvs-legacy-transformation/iam-strategy.md`
  - Does this section stand up to deep questioning from an IAM specialist?
  - Is the zero trust approach appropriate for CVS's hybrid environment?
  - Are the AI-specific controls meaningful (not checkbox security)?
- Does the honesty framing feel right? ("worked within IAM" vs. "designed from scratch")
- Updated future phase plans (review changes from this phase's learnings)
- Context summary accuracy
