# Phase 3 Context Summary — Security, IAM, and Compliance

> **Completed**: 2026-03-16
> **Status**: complete

## Key Findings

- **30 STRIDE threats identified** across all 6 categories with CVS-specific attack vectors (DEA EPCS prescriber spoofing, NCPDP NPI fraud, formulary tier manipulation, IBM i adopted-authority exploitation, CDC pipeline data integrity)
- **23 critical, 7 high severity threats** — no medium or low severity, reflecting the sensitivity of PBM data (PHI, controlled substances, financial claims)
- **21 compliance controls mapped** across 6 frameworks (HIPAA §164.312, HITECH, PCI-DSS 4.0, DEA 21 CFR 1311, SOC 2, NIST SP 800-207) with specific regulation section citations
- **8 open findings** requiring implementation before go-live, including 2 critical (IBM i journal bridge for unified audit, break-glass access procedure)
- **GenAI pipeline has dedicated security controls**: Cloud DLP as synchronous blocking gate (pre and post-inference), structured output enforcement via Gemini controlled generation, ensemble disagreement detection (Gemini vs MedGemma), cryptographic signing of pipeline outputs, VPC-SC perimeter isolation
- **IBM i security integration is the highest-risk area**: *ALLOBJ/*SECADM authority mapping, IWS adopted-authority exposure, journal-based audit bridging, and CDC agent permissions all require IBM i-side changes constrained by RPG/CL developer scarcity
- **Zero trust implementation is phased**: BeyondCorp principles adopted, VPC-SC and IAM in place, but full device trust and continuous evaluation planned across 3 phases
- **Cross-cloud auth (GCP ↔ Azure myPBM)** requires explicit PHI minimization at egress boundary and unified audit trail via Pub/Sub → Azure Event Hub bridge
- **DEA EPCS controls need CSP integration**: Prescriber identity proofing requires contracting with a DEA-approved Credential Service Provider (Imprivata, Exostar) before Phase 1 go-live
- **Supabase service_role key (Option C) is the highest single-point-of-failure**: bypasses all RLS, must never appear in client-side code

## Artifacts Produced

| File | Description |
|------|-------------|
| `knowledge_base/security_review.json` | 30 STRIDE threats, 21 compliance controls, 5-layer defense-in-depth, AI security controls, 8 open findings |
| `outputs/cvs-legacy-transformation/iam-strategy.md` | 10-section IAM strategy covering all 3 architecture options, 5 Mermaid diagrams, 3 appendices |
| `knowledge_base/reviews.json` | R-005 review: 8.2/10 PASS |
| `knowledge_base/engagement.json` | Updated: security_review status=complete v1.0, review_summary total=5 |

## Decisions Made

- **5 service accounts with explicit least-privilege**: bff-service@, genai-pipeline@, cdc-pipeline@, apigee-runtime@, monitoring-sa@ — each with resource-level (not project-level) IAM bindings
- **genai-pipeline@ has ZERO direct PHI access**: enforced by VPC-SC perimeter and IAM deny policies. PHI flows through a dedicated DLP gate service before reaching the GenAI pipeline.
- **Dual-sink audit logging**: Cloud Logging (infrastructure-immutable) + BigQuery (append-only, queryable) — provides both tamper-evidence and analytical capability
- **Hash-chained controlled substance audit logs**: SHA-256 chain with WORM storage for DEA 21 CFR 1311 compliance
- **Step-up authentication at PA decision point**: WebAuthn/TOTP re-verification required when pharmacist commits PA_REVIEW action, not just at session start
- **Event sourcing for formulary changes**: immutable append-only log with dual-control approval for tier modifications
- **3-phase IAM migration**: SSO Bridge (months 1-6) → Identity Consolidation (months 7-12) → Full Zero Trust (months 13-18)

## Surprises and Pivots

- **IBM i security vulnerabilities are actively exploited**: CVE-2024-27275 (adopted authority bypass, CVSS 7.4), CVE-2025-36004 (privilege escalation, CVSS 8.8), CVE-2025-33103 (TCP/IP privilege escalation) — all discovered during STRIDE analysis and require patching before IWS exposure
- **GCP Dual Run clarification carries into security**: Since Dual Run is for z/OS (not IBM i), the parallel validation engine uses custom Apigee request mirroring — this changes the security surface (shadow traffic PHI duplication is a disclosure risk, T-311 in full STRIDE analysis)
- **DLP is not a silver bullet**: Security Boulevard (Dec 2024) documents that current DLP solutions are inadequate for LLM transaction monitoring — structured output enforcement via controlled generation is the primary control, DLP is defense-in-depth
- **Role name inconsistency**: Security review introduced different role names (PHARMACIST, PLAN_ADMIN, FORMULARY_MANAGER, AUDITOR, SYSTEM_ADMIN) vs data_model.json (CLAIMS_PROCESSOR, BENEFITS_ANALYST, IT_ADMINISTRATOR, MANAGER, SYSTEM_SERVICE). P1 finding — needs alignment.

## Assumptions

### New
- A-3-001: CVS enterprise IdP (AD/Okta) supports SAML 2.0 SP-initiated flows with assertion ID replay prevention
- A-3-002: CVS will contract with a DEA-approved Credential Service Provider for EPCS identity proofing before Phase 1 go-live
- A-3-003: IBM i RPG/CL developers are available to modify IWS service program ownership and add correlation ID logging (constrained resource)
- A-3-004: CVS legal/compliance team will review and approve the 3-phase IAM migration plan
- A-3-005: Cloud Identity Platform PAM (Privileged Access Manager) will be GA before Phase 1 go-live
- A-3-006: Precisely Connect supports HMAC-SHA256 message signing on CDC output (needs vendor confirmation)
- A-3-007: CVS has an existing SIEM or is willing to procure one (Chronicle, Splunk) for security event correlation

## Insights for Future Phases

- **Phase 4 (Estimation)**: Security infrastructure costs per option: GCP (Cloud Armor Enterprise ~$3K/mo, VPC-SC included, Cloud DLP pay-per-scan, Secret Manager $0.06/version/mo), AWS (Shield Advanced $3K/mo, WAF per-rule pricing), Modern Cloud (Cloudflare Enterprise, Supabase Team+HIPAA $599+$350/mo). IAM migration effort: 3 phases over 18 months, requires IBM i-side developer time for journal bridge and IWS modifications. Compliance audit costs: SOC 2 Type II audit $10-25K, penetration testing $15-35K (per Paloist security budget), DEA EPCS third-party audit every 2 years.
- **Phase 5 (AI Methodology)**: AI security controls should be documented as a key differentiator — OWASP LLM Top 10 alignment, structured output enforcement, DLP blocking gates, ensemble disagreement detection, HITL mandatory for all PA decisions. These demonstrate Paul's understanding of responsible AI in healthcare contexts.
- **Phase 6 (Assembly)**: Security review + IAM strategy are dedicated sections in the proposal. The IAM strategy document is designed as a standalone interview artifact that sustains 45 minutes of focused questioning. Include STRIDE threat summary table and compliance posture dashboard.
- **Phase 7 (Interview Prep)**: For the IAM interview question ("What approach will you take to implement a robust IAM system..."): the IAM strategy document includes a structured answer in Appendix A. Key talking points: zero trust with BeyondCorp, hybrid RBAC+ABAC, 3-phase migration with rollback, DEA EPCS compliance, GenAI pipeline PHI isolation. For "How did you design IAM for three platforms?": compare Cloud Identity Platform vs Cognito vs Supabase Auth across all 10 sections. Frame through AWS IAM expertise: "I've architected IAM at enterprise scale on AWS and translated those patterns to GCP and Supabase."

## Paul's Feedback

- [Pending — Paul has not yet reviewed Phase 3 outputs]
