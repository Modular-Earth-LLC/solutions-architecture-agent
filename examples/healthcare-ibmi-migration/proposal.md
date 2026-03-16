# Implementation Statement of Work

## IBMi Green Screen Modernization

**Client:** Regional Health Partners (RHP)
**Engagement ID:** eng-2026-001
**Engagement Type:** Modernization
**Prepared by:** Modular Earth LLC
**Date:** March 15, 2026
**Version:** 1.0
**Classification:** Confidential

---

**NOTICE:** This document constitutes a Statement of Work (SOW) for professional consulting services between Modular Earth LLC ("Service Provider") and Regional Health Partners ("Client"). This SOW is subject to mutual execution by authorized representatives of both parties. All terms herein are confidential and intended solely for the named parties.

---

## Table of Contents

1. [Engagement Description](#1-engagement-description)
2. [Business Objectives](#2-business-objectives)
3. [Technical Requirements](#3-technical-requirements)
4. [Team Leads and Roles](#4-team-leads-and-roles)
5. [Project Scope](#5-project-scope)
6. [Services Out of Scope](#6-services-out-of-scope)
7. [Change Order](#7-change-order)
8. [Anticipated Schedule](#8-anticipated-schedule)
9. [Project Rate](#9-project-rate)
10. [Payment Methods](#10-payment-methods)
11. [Assumptions](#11-assumptions)
12. [Signature Block](#12-signature-block)

---

## 1. Engagement Description

### Executive Summary

Modular Earth LLC ("Service Provider") will provide professional solutions architecture and implementation consulting services to Regional Health Partners ("Client") for the modernization of the Client's IBM AS/400 (IBMi) green screen application environment.

Regional Health Partners is an enterprise healthcare organization that currently operates 15+ mission-critical clinical and administrative applications on IBM AS/400 accessed via 5250 green screen terminals. Over 500 daily users across 3 facilities process approximately 50,000 transactions per day against a DB2/400 database containing 2M+ patient records. The system supports patient registration, scheduling, billing, pharmacy, laboratory orders, and clinical documentation workflows.

The Client's current environment presents significant operational, compliance, and competitive challenges:

- **Recruitment and retention:** The green screen terminal interface makes it difficult to recruit clinical and administrative staff willing to work with legacy technology, placing the Client at a competitive disadvantage against organizations with modern systems.
- **Regulatory compliance:** HIPAA audit findings on access control have identified critical gaps including the absence of multi-factor authentication (MFA), lack of granular role-based access control (RBAC), reliance on shared terminal logins, and incomplete audit trails for Protected Health Information (PHI) access.
- **Accessibility:** The 5250 terminal interface does not comply with ADA Section 508 requirements or WCAG accessibility standards.
- **Mobility:** Clinical staff working across 3 facilities have no mobile access to patient records or clinical workflows.
- **Training burden:** New hire onboarding requires 3 to 4 weeks of training solely for terminal navigation and function key memorization.
- **Workforce risk:** The Client's 2 RPG developers are both within 5 years of retirement, concentrating institutional knowledge of the legacy codebase in a shrinking team.

The Service Provider will design and implement a modern responsive web-based user interface layer that wraps the existing IBMi business logic via an API-first architecture. The engagement follows a Strangler Fig modernization pattern: the proven RPG business logic and DB2/400 data integrity are preserved while a modern React/Next.js frontend, NestJS API gateway, and comprehensive Identity and Access Management (IAM) system are built around the existing backend. This approach eliminates the risk of a full rewrite while delivering the modern user experience, HIPAA-compliant security controls, and mobile accessibility the Client requires.

The estimated annual cost of the current state -- including lost productivity, recruitment failures, compliance risk, and maintenance of legacy RPG expertise -- is approximately $800,000.

### Engagement Context

| Attribute | Value |
|-----------|-------|
| Client Legal Name | Regional Health Partners |
| Industry | Healthcare |
| Organization Size | Enterprise |
| AI Maturity | Beginner (no prior AI/ML initiatives) |
| Engagement Type | Modernization (Migration flow) |
| Architecture Pattern | Strangler Fig |
| Compliance Frameworks | HIPAA, HITECH, ADA Section 508 |
| Confidence Level | High |
| Go/No-Go Recommendation | Go with conditions |

---

## 2. Business Objectives

### Problem Statement

Regional Health Partners operates 15+ mission-critical clinical and administrative applications on IBM AS/400 (IBMi) accessed via 5250 green screen terminals. The organization needs modern web-based UIs with human-centered design, robust IAM (SSO, MFA, RBAC), mobile access for clinical staff, and HIPAA-compliant architecture -- while preserving existing RPG business logic and DB2/400 data integrity.

### Strategic Business Value

This modernization initiative delivers measurable business value across six dimensions:

1. **Workforce competitiveness:** Modern web interfaces eliminate the green screen barrier to recruitment, positioning the Client competitively in a tight healthcare labor market.
2. **Regulatory compliance:** SSO, MFA, RBAC, and comprehensive PHI audit trails close all current HIPAA audit findings and establish a defensible compliance posture.
3. **Operational efficiency:** Reducing new hire training time from weeks to days and enabling mobile workflows will improve staff productivity and satisfaction.
4. **Clinical mobility:** Tablet and smartphone access for nursing and physician staff across all 3 facilities enables point-of-care documentation and lookup.
5. **Future readiness:** An API-first architecture creates the foundation for future EHR integrations, health information exchange (HIE) participation, and AI-assisted capabilities.
6. **Risk mitigation:** Preserving IBMi business logic eliminates rewrite risk while establishing a knowledge transfer pathway before RPG developer retirement.

### Measurable Success Criteria

The following Key Performance Indicators (KPIs) define measurable success for this engagement. Each KPI includes a current baseline, target value, measurement method, and measurement timeframe.

| ID | Metric | Baseline | Target | Measurement | Timeframe |
|----|--------|----------|--------|-------------|-----------|
| SC-001 | Training time reduction | 21 days | 3 days | Days from first login to independent use, measured via competency assessment | Within 3 months of module go-live |
| SC-002 | Mobile access adoption | 0% | 75% | Percentage of clinical staff with 5+ mobile logins per week | 6 months post-launch |
| SC-003 | HIPAA audit compliance | 5 critical findings | 0 critical findings | Number of critical findings in annual HIPAA audit | Next scheduled audit post-implementation |
| SC-004 | Data migration integrity | 0 discrepancies | 0 discrepancies | Count of data discrepancies between legacy and modern systems during parallel run | Throughout migration period |
| SC-005 | System availability | 99.0% | 99.9% | Monthly uptime percentage excluding scheduled maintenance windows | Ongoing post-launch |
| SC-006 | User satisfaction | 3.2 / 10 | 8.0 / 10 | System Usability Scale (SUS) score, surveyed quarterly | 6 months post-launch |
| SC-007 | Accessibility compliance | 0% | 100% | Percentage of pages passing automated WCAG 2.1 AA audit (axe-core) | At each module go-live |

### Return on Investment

Based on the estimated annual cost of the current state ($800,000/year) and projected annual savings from modernization:

| Metric | Value |
|--------|-------|
| Annual savings estimate | $480,000 |
| Payback period | 30 months |
| 3-year ROI | 72% |

The 3-year total cost of ownership (TCO) is $1,405,560, inclusive of Year 1 implementation ($1,000,560), Year 2 operations ($210,000), and Year 3 operations ($195,000). Against projected annual savings of $480,000, the engagement achieves a positive return before the end of Year 3.

---

## 3. Technical Requirements

### Architecture Overview

The recommended architecture follows a Strangler Fig modernization pattern: a modern web application layer wraps the existing IBMi RPG programs via a REST API gateway, with a comprehensive IAM layer providing SSO, MFA, and RBAC. The IBMi AS/400 remains the system of record; DB2/400 continues to store all patient, clinical, billing, and operational data. No rip-and-replace.

**Architecture Recommendation:** Strangler fig modernization -- wrap IBMi RPG programs with REST API layer, build responsive React web UI, implement modern IAM with SSO/MFA -- phased module-by-module rollout preserving all existing business logic.

**Investment Range:** $750,000 - $1,200,000

### Technology Stack

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| **Frontend** | React 18 with Next.js 14 (SSR), Tailwind CSS | Largest talent pool in React ecosystem. Next.js provides server-side rendering for fast initial load. Strong accessibility tooling (react-aria, axe-core). Responsive design for mobile support. |
| **Backend** | TypeScript on Node.js 20 LTS, NestJS framework | Full-stack TypeScript reduces context switching. NestJS provides Spring-like structure with lighter runtime. Best IBM i Access client libraries (node-jt400). |
| **API Style** | REST | Standard, well-understood by healthcare integrators. Versioned APIs for gradual migration. |
| **Primary Data Store** | DB2/400 (existing, on-premises IBM AS/400) | System of record. All patient, clinical, billing, and operational data. Accessed via IBMi Data Access Layer. |
| **Session Cache** | Redis 7 (ElastiCache Multi-AZ) | Session management, token caching, API response caching for read-heavy queries. Reduces load on IBMi connection pool. |
| **Audit Store** | PostgreSQL (append-only audit schema) | Immutable audit log for PHI access events, authentication events, and data modifications. HIPAA compliance requirement. 7-year retention. |
| **User Directory** | PostgreSQL | User accounts, role mappings, session metadata. Synced with external IdP. |
| **IAM** | Keycloak (open-source) or AWS Cognito, SAML 2.0/OIDC | SSO federation with client IdP, MFA enforcement, RBAC with clinical role hierarchy. |
| **Cloud Provider** | AWS (HIPAA BAA) or Azure (HIPAA BAA) | HIPAA Business Associate Agreement available. US-East region. |
| **Compute** | ECS Fargate (serverless containers) | No cluster management overhead. Pay-per-use pricing. Auto-scaling. |
| **Deployment** | Blue-green via ECS with CodeDeploy | Zero-downtime deployments with automatic rollback on health check failure. |
| **Monitoring** | CloudWatch + Prometheus + Grafana + PagerDuty | Centralized observability with IBMi-specific metrics (connection pool, ODBC latency). |
| **Networking** | VPC with private subnets, VPN/Direct Connect to IBMi | Site-to-site encrypted connectivity. No public internet traversal for IBMi traffic. |
| **CDN** | CloudFront | Static asset delivery for frontend performance. |

### System Components

The architecture comprises 8 components designed for independent scaling, clear separation of concerns, and defense-in-depth security:

| ID | Component | Technology | Purpose |
|----|-----------|-----------|---------|
| C-001 | Web Application | React 18, Next.js 14, Tailwind CSS | Responsive web UI replacing green screen terminals. All 6 clinical modules plus admin dashboards. WCAG 2.1 AA compliant. |
| C-002 | API Gateway | NestJS, AWS/Azure API Gateway | Central entry point. Routes requests, enforces authentication, rate limiting, request validation. |
| C-003 | IBMi Data Access Layer (DAL) | Node.js, IBM i Access ODBC/JDBC, node-jt400 | Abstraction layer for all IBMi communication. Connection pooling, EBCDIC conversion, RPG program calls. Facade pattern. |
| C-004 | IAM / Authentication Service | Keycloak or AWS Cognito, SAML 2.0, OIDC | SSO, MFA, RBAC, session management. Clinical role mapping. |
| C-005 | Business Logic Services | NestJS microservices (6 modules) | Domain-specific service modules: Patient, Scheduling, Billing, Pharmacy, Lab, Clinical Documentation. |
| C-006 | Cache Layer | Redis 7, ElastiCache | Session storage, API response caching, token validation cache. Reduces IBMi connection pool load. |
| C-007 | Audit Logging Service | NestJS, PostgreSQL (append-only), SQS/RabbitMQ | Captures all PHI access events. Async write via message queue. Immutable storage. HIPAA compliance. |
| C-008 | Monitoring and Observability | Prometheus, Grafana, CloudWatch, PagerDuty | Health checks, performance metrics, error rate tracking, IBMi connectivity monitoring, SLA dashboards. |

### Functional Requirements

The following functional requirements define the MVP scope for this engagement. Requirements are prioritized using MoSCoW categories.

#### Must-Have Requirements

| ID | Title | Complexity | Description |
|----|-------|-----------|-------------|
| FR-001 | Modern web UI for patient registration | High | Replace 5250 green screen patient registration with responsive web interface. All existing registration fields and workflows with improved usability. WCAG 2.1 AA. |
| FR-002 | Modern web UI for scheduling | High | Replace green screen scheduling with visual calendar interface. Drag-and-drop, multi-facility view, provider availability. |
| FR-003 | Modern web UI for billing | Very High | Replace green screen billing with modern interface. Claim management, payment processing views, reporting dashboards. |
| FR-004 | Modern web UI for pharmacy | High | Replace green screen pharmacy module. Medication management, order verification, inventory tracking, controlled substance tracking. |
| FR-007 | Identity and Access Management | High | SSO (SAML 2.0/OIDC), MFA (TOTP, push, hardware token), RBAC with clinical role mapping, session management, audit trail. |
| FR-008 | API gateway for IBMi integration | Very High | REST API endpoints for all green screen functions. EBCDIC/DB2 to JSON transformation. Connection pooling, caching, versioning, rate limiting, circuit breakers. |
| FR-009 | Mobile-responsive clinical workflows | Medium | Touch-optimized tablet interface, smartphone access, offline patient lookup, barcode/QR scanning. |
| FR-010 | PHI audit trail and compliance logging | Medium | Log all PHI access. Immutable audit log storage. Report generation. Real-time anomaly alerting. |

#### Should-Have Requirements

| ID | Title | Complexity | Description |
|----|-------|-----------|-------------|
| FR-005 | Modern web UI for lab orders | Medium | Lab order entry with templates, result viewing with normal range highlighting, abnormal result alerting. |
| FR-006 | Modern web UI for clinical documentation | Very High | Structured clinical note templates, document version history, clinical image attachments. |
| FR-011 | Change management and training portal | Medium | In-app training guides, contextual help tooltips, feedback mechanisms, training progress tracking. |

#### Nice-to-Have Requirements

| ID | Title | Complexity | Description |
|----|-------|-----------|-------------|
| FR-012 | Reporting and analytics dashboard | Medium | Real-time operational metrics, customizable report builder, scheduled reports, role-based views. |

### Non-Functional Requirements

| Category | Requirement | Target |
|----------|------------|--------|
| **Performance** | Response time (P95) | 2,000 ms |
| **Performance** | Throughput | 100 requests/second |
| **Performance** | Concurrent users | 500 |
| **Availability** | System uptime | 99.9% |
| **Availability** | Planned maintenance window | Sundays 2:00 - 6:00 AM EST |
| **Scalability** | Current volume | 500 concurrent users, 50,000 transactions/day |
| **Scalability** | Projected growth | 10-15% annual |
| **Scalability** | Peak load multiplier | 2.5x |
| **Security** | Authentication | SAML 2.0, OIDC, MFA (TOTP/Push) |
| **Security** | Authorization | RBAC with clinical role hierarchy |
| **Security** | Data classification | Restricted (PHI) |
| **Security** | Encryption at rest | AES-256 |
| **Security** | Encryption in transit | TLS 1.2+ |
| **Security** | Field-level encryption | SSN, MRN |
| **Compliance** | Regulatory frameworks | HIPAA, HITECH, ADA Section 508 |
| **Data Residency** | Required regions | United States |
| **Data Residency** | Retention period | 2,555 days (7 years) for audit logs |

### Well-Architected Compliance Scores

The architecture has been evaluated against the AWS Well-Architected Framework (applicable to any cloud provider):

| Pillar | Score (0-10) | Notes |
|--------|:------------:|-------|
| Operational Excellence | 7.5 | Strong CI/CD, structured logging, monitoring. Gap: IBMi-specific runbooks and RPG developer knowledge transfer documentation needed. |
| Security | 8.5 | Zero Trust (SSO, MFA, RBAC), HIPAA compliance, PHI audit trails, encryption everywhere. Gap: penetration testing plan needed before go-live. |
| Reliability | 7.0 | Multi-AZ deployment, circuit breakers, retry patterns. Gap: IBMi is single point of failure (client-managed DR), connection pool limits constrain burst capacity. |
| Performance Efficiency | 7.0 | Redis caching reduces IBMi load, CDN for static assets. Gap: IBMi ODBC latency may bottleneck complex queries; performance testing with real data volumes required. |
| Cost Optimization | 7.5 | Fargate (pay-per-use), caching strategy, storage lifecycle policies. Gap: IBMi licensing costs not included (client-owned). |
| Sustainability | 6.5 | Serverless compute is efficient, caching reduces redundant processing. Gap: on-premises IBMi power consumption not addressed. |
| **Overall** | **7.3** | |

### Security Architecture Summary

The security architecture implements defense-in-depth across 5 layers:

**Layer 1 -- Perimeter:** AWS WAF with OWASP Top 10 managed rules, AWS Shield Standard for DDoS protection, CloudFront with geo-restriction (US-only), rate limiting (100 req/s per IP), TLS 1.2+ with HSTS.

**Layer 2 -- Network:** Dedicated VPC with public/private/data subnet tiers, least-privilege security groups per component, site-to-site VPN (IPsec AES-256-GCM) or Direct Connect for IBMi connectivity, VPC Flow Logs for forensics.

**Layer 3 -- Application:** Input validation at API Gateway and Business Logic layers, parameterized queries for all database access, Content Security Policy headers, dependency vulnerability scanning in CI/CD, SAST in build pipeline.

**Layer 4 -- Identity:** SSO via SAML 2.0/OIDC with external IdP, MFA enforced for all users, RBAC with clinical role hierarchy, 10-minute inactivity timeout for PHI sessions, short-lived JWTs (15-minute access, 8-hour refresh).

**Layer 5 -- Data:** AES-256 at rest via AWS KMS customer-managed keys, TLS 1.2+ in transit with mTLS between internal services, field-level encryption for SSN and MRN, PHI masking in application logs, 7-year audit log retention.

The STRIDE threat model identified 8 threats, all mitigated. Five open security findings require attention:

| ID | Severity | Finding | Recommendation |
|----|----------|---------|----------------|
| F-001 | Critical | No penetration testing plan exists for the modernized platform | Engage third-party pen test firm before Phase 1 go-live. Budget $30,000-$50,000. |
| F-002 | High | IBMi connection pool (50 concurrent) is a single bottleneck | Implement pool monitoring, request queuing, and graceful degradation mode. |
| F-003 | High | Mobile device management (MDM) policy not defined | Require MDM enrollment, enforce device encryption, integrate compliance with IAM. |
| F-004 | Medium | DR procedures not yet documented | Develop formal contingency plan with RTO/RPO validation before Phase 1 go-live. |
| F-005 | Low | No runtime container security scanning | Evaluate GuardDuty for ECS or equivalent as Phase 2 enhancement. |

### HIPAA Compliance Posture

The architecture addresses the following HIPAA Security Rule requirements with full or partial compliance:

- **164.312(a)(1) -- Access Control:** Compliant. RBAC with clinical role hierarchy, SSO, per-module authorization.
- **164.312(a)(2)(i) -- Unique User Identification:** Compliant. Individual accounts via IdP, no shared logins, unique IDs in JWT claims and audit records.
- **164.312(a)(2)(iii) -- Automatic Logoff:** Compliant. 10-minute inactivity timeout for PHI sessions.
- **164.312(b) -- Audit Controls:** Compliant. Immutable append-only audit log, 7-year retention, tamper-evident checksums.
- **164.312(c)(1) -- Integrity:** Compliant. TLS 1.2+, mTLS, AES-256, input validation, parameterized queries.
- **164.312(d) -- Person or Entity Authentication:** Compliant. MFA for all users, SSO federation, brute-force protection.
- **164.312(e)(1) -- Transmission Security:** Compliant. TLS 1.2+ all connections, IPsec VPN for IBMi, HSTS.
- **164.310(d)(1) -- Device and Media Controls:** Partial. Cloud infrastructure managed via IaC with encryption. Client responsible for on-premises IBMi device controls. MDM policy recommended for mobile devices.
- **164.308(a)(7)(i) -- Contingency Plan:** Partial. Multi-AZ, automated backups, blue-green deployments. Formal DR procedures to be documented during Phase 1.

---

## 4. Team Leads and Roles

The Service Provider will staff the following roles for the duration of the engagement. All team members will complete HIPAA security training before engagement kickoff.

### Team Composition

| Role | Count | Experience | Allocation | Duration | Key Responsibilities |
|------|:-----:|-----------|:----------:|:--------:|---------------------|
| **Solutions Architect** | 1 | Expert | 75% | 68 weeks | Overall system design and architecture governance. IBMi modernization strategy. Healthcare integration architecture (HL7/FHIR). Well-Architected reviews. Technical risk management. |
| **Full-Stack Developer** | 3 | Senior | 100% | 56 weeks | Modern web UI development replacing 5250 green screens. API layer development and service decomposition. Database migration tooling. Unit and integration tests. Frontend accessibility (WCAG 2.1 AA). |
| **IBMi/RPG Integration Specialist** | 1 | Expert | 100% | 48 weeks | RPG IV and COBOL program analysis and documentation. Business logic extraction and service wrapping. DB2/400 schema analysis and migration mapping. IBMi program call interfaces and API bridge. Dual-run validation. |
| **UX/HCD Designer** | 1 | Senior | 75% | 36 weeks | Clinical workflow analysis and user research. Green screen to web UI interaction mapping. Wireframes, prototypes, and design system. Usability testing. Accessibility compliance (WCAG 2.1 AA, Section 508). |
| **IAM Security Specialist** | 1 | Senior | 50% | 40 weeks | HIPAA security rule compliance architecture. IAM design (RBAC, MFA). PHI encryption strategy. Audit trail implementation. Penetration testing coordination. |
| **QA Engineer** | 1 | Senior | 100% | 44 weeks | Test strategy and plan development. Automated regression suite. Data migration validation. HIPAA compliance and security testing. UAT coordination. Performance and load testing. |
| **Project Manager** | 1 | Senior | 75% | 68 weeks | Agile ceremony facilitation and sprint planning. Stakeholder communication. Risk and issue management. Budget tracking. Vendor coordination. Change management. |
| **DevOps Engineer** | 1 | Senior | 75% | 52 weeks | CI/CD pipeline design and implementation. IaC (Terraform/Ansible). Container orchestration. Monitoring, logging, and alerting. HIPAA-compliant environment provisioning. DR and backup automation. |

### Team Size Summary

| Metric | Value |
|--------|-------|
| Total team members | 10 |
| Peak concurrent staff | 10 (during Core Development phase) |
| Total engagement hours | 8,640 hours (before risk buffer) |
| Engagement duration | 68 weeks |

### Client Team Requirements

The following Client personnel are required for the success of this engagement:

| Client Role | Commitment | Purpose |
|-------------|-----------|---------|
| RPG Developers (2) | Minimum 50% allocation | Knowledge transfer, API collaboration, business logic validation |
| IT Director | Weekly technical reviews | Technical approval, infrastructure coordination |
| CIO | Bi-weekly steering committee | Strategic direction, budget authority |
| CMO | Bi-weekly clinical impact review | Clinical workflow approval |
| Director of Nursing | Weekly sprint demos, UI design input | Nursing workflow validation |
| Clinical Staff (representatives) | Training sessions, UAT | User acceptance testing, feedback |
| Change Champions (per department) | Training rollout | Departmental adoption leadership |

---

## 5. Project Scope

### Phase Summary

The engagement is organized into 7 phases spanning 68 weeks. Phases overlap where dependencies permit parallel execution. Each phase includes defined deliverables, success criteria, and a decision gate before proceeding.

### Phase 1: Legacy Assessment and Knowledge Transfer

**Weeks 1-4 | Estimated Cost: $46,000**

| Week | Deliverables | Team Focus |
|------|-------------|------------|
| 1-2 | RPG program inventory for patient-facing subsystems; initial SME interviews for scheduling and registration | Solutions Architect (lead), IBMi SMEs (2), Business Analyst, Healthcare Domain Expert |
| 3-4 | Data flow mapping for HL7 and X12 interfaces; business rules documentation for claims and pharmacy modules; knowledge transfer recordings and runbooks | Solutions Architect, IBMi SME, Business Analyst |

**Phase Deliverables:**
- Legacy application inventory with complexity scores
- Business rules catalog extracted from RPG/CL source analysis
- Data flow diagrams for all IBMi subsystems
- Knowledge transfer recordings and runbooks

**Success Criteria:**
- 100% of active RPG programs cataloged with complexity ratings
- All critical business rules documented and validated by SMEs
- Data lineage traced for patient, claims, and scheduling subsystems

**Key Risks:**
- Tribal knowledge loss if key IBMi personnel depart before transfer completes
- Undocumented interfaces between RPG programs may be missed in inventory

---

### Phase 2: Foundation and Infrastructure

**Weeks 3-10 | Estimated Cost: $68,000**

| Week | Deliverables | Team Focus |
|------|-------------|------------|
| 3-5 | HIPAA-compliant cloud landing zone provisioned; CI/CD pipeline with container registry established | DevOps Engineers (2), Cloud Architect, Security Engineer |
| 6-8 | Database provisioning with encryption and backup policies; observability stack deployed with alerting thresholds | DevOps Engineers, DBA, Security Engineer |
| 9-10 | Infrastructure hardening complete; VPN/Direct Connect to IBMi operational; security configuration audit passed | Full team validation |

**Phase Deliverables:**
- Infrastructure-as-Code repository (Terraform/Pulumi)
- CI/CD pipeline definitions with security scanning gates
- Database instances provisioned with schema migration tooling
- Monitoring dashboards and alerting rules

**Success Criteria:**
- Infrastructure passes HIPAA configuration audit
- CI/CD pipeline deploys to dev environment in under 15 minutes
- Database failover tested with RPO < 1 minute, RTO < 5 minutes

**Key Risks:**
- HIPAA compliance requirements may delay infrastructure approval
- Network connectivity between on-premises IBMi and cloud may introduce latency

---

### Phase 3: IAM and Patient Registration MVP

**Weeks 8-18 | Estimated Cost: $148,000**

| Week | Deliverables | Team Focus |
|------|-------------|------------|
| 8-10 | Core IAM service with OIDC/SAML integration; legacy IBMi user profiles mapped to RBAC roles | Backend Engineers (3), Security Engineer, QA Engineer, IBMi SME |
| 11-13 | Patient registration API with FHIR R4 Patient resource; data migration pipeline for patient demographics | Backend Engineers, IBMi SME, QA Engineer |
| 14-16 | Patient search, merge/unmerge, duplicate detection; data migration dry run with accuracy validation | Backend Engineers, QA Engineer |
| 17-18 | MVP readiness testing; security penetration test; stakeholder demo | Full team |

**Phase Deliverables:**
- IAM service with SSO, MFA, and role-based access policies
- Patient Registration microservice with FHIR R4 API
- Data migration scripts for patient demographic records
- Integration test suite covering registration workflows

**Success Criteria:**
- IAM supports all 12 legacy user roles with equivalent permissions
- Patient Registration handles 100% of legacy workflows
- Data migration achieves 99.99% accuracy on patient demographic fields
- API response times under 200ms at P95 for registration lookups

**Decision Gate (DG-001): MVP Readiness -- Week 18**
- Patient Registration MVP passes all functional tests
- IAM roles validated against legacy access control matrix
- Data migration accuracy confirmed at 99.99%
- Security penetration test completed with no critical findings
- **Decider:** Steering Committee
- **Options:** Proceed to clinical modules | Extend MVP phase | Re-scope clinical modules

---

### Phase 4: Clinical Modules Development

**Weeks 16-40 | Estimated Cost: $312,000**

| Week | Deliverables | Team Focus |
|------|-------------|------------|
| 17-20 | Scheduling service with provider calendar and patient self-scheduling | Backend Engineers (4), Frontend Engineers (2), QA Engineers (2), Clinical SME, IBMi SME |
| 21-26 | Order entry service (CPOE) with clinical decision support hooks | Backend Engineers, Frontend Engineers, Clinical SME |
| 27-32 | Clinical documentation service with structured/unstructured note support | Backend Engineers, Frontend Engineers, QA Engineers |
| 33-38 | Pharmacy module with e-prescribing (NCPDP SCRIPT); lab orders module | Backend Engineers, Frontend Engineers, IBMi SME |
| 39-40 | Clinical analytics dashboard; mobile-responsive interface validation | Full development team |

**Phase Deliverables:**
- Scheduling Service with provider calendar and patient self-scheduling
- Order Entry Service (CPOE) with CDS hooks
- Clinical Documentation Service
- Pharmacy Module with e-prescribing integration
- Lab Orders Module
- Clinical analytics dashboard

**Success Criteria:**
- All clinical modules pass functional equivalence testing against legacy screens
- HL7 FHIR interfaces certified against ONC requirements
- Clinical workflows complete in equal or fewer steps than legacy green screen
- E-prescribing passes Surescripts certification testing

**Key Risks:**
- Clinical module complexity may exceed estimates due to undocumented business rules
- HL7 FHIR certification timeline may conflict with development schedule
- Pharmacy module e-prescribing adds third-party dependency (Surescripts)

---

### Phase 5: Parallel Run and Validation

**Weeks 38-52 | Estimated Cost: $132,000**

| Week | Deliverables | Team Focus |
|------|-------------|------------|
| 38-42 | Bidirectional data synchronization bridge deployed; parallel run initiated for patient registration and scheduling | QA Engineers (3), Backend Engineers (2), DBA, IBMi SME |
| 43-47 | Output comparison reports for clinical modules; user acceptance testing with clinical staff | QA Engineers, Clinical Trainers (2), Backend Engineers |
| 48-50 | Load testing at 2x peak census; performance optimization | QA Engineers, Backend Engineers, DevOps |
| 51-52 | UAT sign-off documentation; parallel run results compilation; go/no-go preparation | Full team |

**Phase Deliverables:**
- Parallel run data synchronization bridge (bidirectional)
- Output comparison reports for all migrated transactions
- UAT sign-off documentation from clinical department heads
- Load test results with capacity planning recommendations

**Success Criteria:**
- 99.95% transaction equivalence between legacy and modern systems over 4-week parallel run
- UAT pass rate exceeds 95% across all clinical workflows
- System sustains 2x peak load with P99 latency under 500ms
- Zero critical data discrepancies in patient-facing fields

**Decision Gate (DG-002): Parallel Run Go/No-Go -- Week 52**
- Transaction equivalence exceeds 99.95% threshold
- UAT sign-off from all department heads
- Load test confirms capacity for 2x peak
- No unresolved P1 or P2 defects
- **Decider:** Steering Committee + CISO
- **Options:** Proceed to cutover | Extend parallel run 4 weeks | Halt and remediate

---

### Phase 6: Cutover and Remaining Modules

**Weeks 50-62 | Estimated Cost: $144,000**

| Week | Deliverables | Team Focus |
|------|-------------|------------|
| 50-53 | Department-by-department cutover runbooks; pilot department cutover | Backend Engineers (3), DevOps Engineers (2), DBA, Clinical Trainers (2), PM |
| 54-57 | Billing and administrative modules deployed to production; second department cutover | Full team |
| 58-60 | Remaining department cutovers; legacy terminal decommission per department schedule | Full team |
| 61-62 | Final data reconciliation; legacy system decommission certificates; audit trail closure | Full team |

**Phase Deliverables:**
- Department-by-department cutover runbooks
- Billing and administrative modules in production
- Legacy system decommission certificates per department
- Final data reconciliation report with audit trail

**Success Criteria:**
- Each department cutover completes within designated maintenance window
- Billing module processes claims with zero regression vs. legacy
- All legacy data migrated with full audit trail and chain of custody
- Rollback exercised successfully in pre-production before each department cutover

**Key Risks:**
- Cutover window may be insufficient for high-transaction departments
- Remaining administrative modules may have undiscovered IBMi dependencies
- Staff availability during cutover weekends may be limited

---

### Phase 7: Stabilization and Optimization

**Weeks 60-68 | Estimated Cost: $100,560**

| Week | Deliverables | Team Focus |
|------|-------------|------------|
| 60-63 | Enhanced production monitoring; performance baseline established; hypercare support | SRE Engineer, Backend Engineer, DevOps Engineer |
| 64-66 | Performance optimization based on real-world usage; incident response playbook | SRE Engineer, Backend Engineer, Technical Writer |
| 67-68 | Knowledge transfer to client operations team; operations runbook delivery; project closeout | Full team (reduced) |

**Phase Deliverables:**
- Production stability report with SLA compliance metrics
- Performance optimization recommendations and implementations
- Operations runbook and incident response playbook
- Knowledge transfer completion certificates for client IT staff

**Success Criteria:**
- System availability exceeds 99.9% over 4-week stabilization window
- Mean time to resolution for P1 incidents under 30 minutes
- Client operations team independently resolves L1/L2 incidents
- All legacy IBMi systems fully decommissioned

**Decision Gate (DG-003): Legacy Decommission -- Week 65**
- All departments operating on modernized platform for minimum 2 weeks
- No rollbacks executed in production
- Client operations team passed competency assessment
- Data retention and archival requirements met
- **Decider:** CIO + Compliance Officer
- **Options:** Decommission legacy IBMi | Maintain in read-only mode 90 days | Delay decommission

---

### Estimated Cost by Phase Summary

| Phase | Weeks | Hours | Estimated Cost |
|-------|:-----:|:-----:|---------------:|
| P-001: Legacy Assessment and Knowledge Transfer | 1-4 | 720 | $46,000 |
| P-002: Foundation and Infrastructure | 3-10 | 960 | $68,000 |
| P-003: IAM and Patient Registration MVP | 8-18 | -- | $148,000 |
| P-004: Clinical Modules Development | 16-40 | 3,360 | $312,000 |
| P-005: Parallel Run and Validation | 38-52 | 1,200 | $132,000 |
| P-006: Cutover and Remaining Modules | 50-62 | 1,680 | $144,000 |
| P-007: Stabilization and Optimization | 60-68 | 720 | $100,560 |
| **Total** | **68 weeks** | **8,640** | **$950,560** |

*Note: Phase hours overlap due to parallel execution. Cost figures represent the estimated labor allocation per phase based on team composition, hourly rates, and allocation percentages. The total cost model including risk buffer, infrastructure, training, and third-party services is detailed in Section 9.*

---

## 6. Services Out of Scope

The following items are explicitly excluded from this engagement. Items designated as "future phase" may be addressed under a separate Statement of Work.

### Excluded Services

| # | Exclusion | Rationale |
|---|-----------|-----------|
| 1 | **Replacing IBMi backend or migrating off DB2/400** | This engagement wraps IBMi with modern UIs; it does not replace the backend. A full backend migration is a separate initiative with fundamentally different scope, risk, and budget. |
| 2 | **EHR system selection or implementation** | EHR selection is a strategic decision outside the scope of UI modernization. The API-first architecture produced by this engagement is designed to integrate with a future EHR. |
| 3 | **AI/ML features** | AI suitability assessment scored 3/10 for this phase. AI-assisted data entry, clinical decision support, and NLP are identified as future-phase capabilities once the modern UI and API platform are stable. |
| 4 | **Hardware procurement** | Existing infrastructure is assumed adequate. Server, network, and end-user device procurement is the Client's responsibility. |
| 5 | **Rewriting RPG business logic** | The architectural approach is to wrap existing RPG programs, not rewrite them. Business logic rewriting carries high defect risk and would increase budget 3-5x. |
| 6 | **COBOL batch job modernization** | COBOL batch jobs continue running on IBMi nightly schedule. A monitoring facade is provided, but no modifications to batch job code. |
| 7 | **Network infrastructure upgrades** | Network connectivity between IBMi and cloud infrastructure is assumed to be the Client's responsibility. The Service Provider will specify requirements. |
| 8 | **Code generation, deployment scripts, CI/CD execution, infrastructure provisioning, production operations** | Per the scope boundary between solutions architecture and engineering, ongoing operational responsibilities transfer to the Client's team at engagement close (see Phase 7 knowledge transfer). |
| 9 | **Mobile Device Management (MDM) implementation** | MDM policy and enrollment is recommended (per security finding F-003) but is the Client's responsibility to procure and manage. |
| 10 | **Third-party penetration testing** | The Service Provider will coordinate and specify requirements for penetration testing, but the third-party testing firm is engaged and paid by the Client separately. Estimated cost: $30,000 - $50,000. |

### Scope Justification

The scope focuses on maximum user impact (UI modernization + IAM) while minimizing risk by preserving proven IBMi business logic. Out-of-scope items are deferred to future phases to manage budget and timeline constraints. This approach delivers the highest-value capabilities first -- modern UIs, HIPAA compliance, and mobile access -- while creating the API foundation that makes future initiatives (EHR integration, AI, backend migration) feasible.

---

## 7. Change Order

### Change Management Process

Any modification to the scope, deliverables, timeline, or cost defined in this SOW requires a formal Change Order executed by authorized representatives of both parties.

### Change Order Procedure

1. **Change Request Initiation:** Either party may initiate a Change Request by submitting a written description of the proposed change, including the business justification, scope impact, timeline impact, and cost impact.

2. **Impact Assessment:** The Service Provider will assess the Change Request within 5 business days and provide a written impact assessment including:
   - Revised scope description
   - Revised timeline (if applicable)
   - Revised cost estimate (if applicable)
   - Impact on existing deliverables and milestones
   - Risk assessment of the change

3. **Approval:** The Change Request must be approved in writing by authorized representatives of both parties before work begins on the changed scope. Email approval from the designated signatories listed in Section 12 constitutes written approval.

4. **Execution:** Upon mutual approval, the Change Order becomes an amendment to this SOW. The revised scope, timeline, and cost become the new contractual baseline.

### Change Order Template

```
CHANGE ORDER #[NUMBER]
SOW Reference: eng-2026-001
Date: [DATE]

Description of Change:
[Detailed description of the scope change]

Business Justification:
[Why this change is needed]

Impact Assessment:
- Scope: [Added/removed/modified deliverables]
- Timeline: [Days/weeks added or reduced]
- Cost: [Additional cost or credit]
- Risk: [New or modified risks]

Revised Total Engagement Cost: $[AMOUNT]
Revised End Date: [DATE]

Approved by Service Provider: _________________ Date: _________
Approved by Client:           _________________ Date: _________
```

### Termination Clause

Either party may terminate this SOW by providing 10 business days written notice to the other party. Upon termination:

- The Client shall pay for all services rendered and expenses incurred through the termination effective date.
- The Service Provider shall deliver all work product completed as of the termination date, including partial deliverables and documentation.
- Confidentiality obligations and intellectual property provisions survive termination.
- The Service Provider will provide reasonable transition assistance for up to 5 business days following the termination effective date.

---

## 8. Anticipated Schedule

### Engagement Timeline

| Attribute | Value |
|-----------|-------|
| **Start Date** | April 6, 2026 |
| **Target End Date** | July 18, 2027 |
| **Total Duration** | 68 weeks |
| **Methodology** | Agile (2-week sprints with bi-weekly steering committee) |
| **Parallel Run Duration** | 14 weeks |

### Phase Timeline

```
2026                                                          2027
Apr  May  Jun  Jul  Aug  Sep  Oct  Nov  Dec  Jan  Feb  Mar  Apr  May  Jun  Jul
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
[P1 ]                                                                          Wk 1-4
  [  P2       ]                                                                Wk 3-10
        [     P3          ]                                                    Wk 8-18
              [          P4                              ]                      Wk 16-40
                                             [       P5            ]           Wk 38-52
                                                       [       P6        ]    Wk 50-62
                                                              [      P7     ] Wk 60-68
```

### Key Milestones

| ID | Milestone | Target Date | Phase | Gate Type |
|----|-----------|-------------|-------|-----------|
| M-001 | Legacy Assessment Complete | May 3, 2026 | P-001 | Review |
| M-002 | Infrastructure Ready for Development | June 7, 2026 | P-002 | Sign-off |
| M-003 | Patient Registration MVP Live | August 9, 2026 | P-003 | Demo |
| M-004 | MVP Readiness Gate Passed | August 9, 2026 | P-003 | Approval |
| M-005 | All Clinical Modules Feature-Complete | January 3, 2027 | P-004 | Demo |
| M-006 | Parallel Run Validation Passed | March 28, 2027 | P-005 | Approval |
| M-007 | Final Department Cutover Complete | June 20, 2027 | P-006 | Sign-off |
| M-008 | Legacy IBMi Decommissioned | July 18, 2027 | P-007 | Approval |

### Critical Path

The following phases form the critical path of the engagement. Delays in any critical-path phase will directly impact the target end date.

1. **P-001:** Legacy Assessment and Knowledge Transfer
2. **P-002:** Foundation and Infrastructure (overlaps P-001, starts week 3)
3. **P-003:** IAM and Patient Registration MVP (blocked by P-001 + P-002)
4. **P-004:** Clinical Modules Development (blocked by P-003)
5. **P-005:** Parallel Run and Validation (blocked by P-004)
6. **P-006:** Cutover and Remaining Modules (blocked by P-005 decision gate)
7. **P-007:** Stabilization and Optimization (blocked by P-006)

### Decision Gates

Three formal decision gates govern progression through the engagement:

| Gate | Week | Decision | Decider |
|------|:----:|----------|---------|
| DG-001: MVP Readiness | 18 | Proceed to clinical modules, extend MVP, or re-scope | Steering Committee |
| DG-002: Parallel Run Go/No-Go | 52 | Proceed to cutover, extend parallel run, or halt | Steering Committee + CISO |
| DG-003: Legacy Decommission | 65 | Decommission IBMi, maintain read-only 90 days, or delay | CIO + Compliance Officer |

### Data Migration Phases

Data migration follows a 4-phase approach aligned with the clinical module rollout:

| Phase | Name | Target Week | Estimated Records | Approach |
|-------|------|:-----------:|------------------:|----------|
| 1 | Patient Demographics and Master Data | Week 14 | 2.4M patient records | ETL with data quality cleansing and deduplication |
| 2 | Clinical History and Orders | Week 34 | 18M clinical records | Incremental migration with FHIR resource mapping |
| 3 | Billing, Claims, and Financial Data | Week 55 | 12M transaction records | Batch migration with reconciliation checkpoints |
| 4 | Archival and Historical Data | Week 62 | 40M archived records | Cold storage migration with indexed search |

### Communication Cadence

| Audience | Frequency | Format |
|----------|-----------|--------|
| Steering Committee | Bi-weekly | Written status report + briefing |
| Technical Leads | Weekly | Stand-up meeting |
| Board / Executive | Monthly | Executive summary |
| Clinical Staff | Per sprint demo schedule | Live demonstration |

### Scheduled Demos

| Week | Demo |
|:----:|------|
| 4 | Legacy assessment findings and migration roadmap presentation |
| 10 | Infrastructure walkthrough and security architecture review |
| 18 | Patient Registration MVP demo to clinical leadership |
| 28 | Scheduling and Order Entry modules demo |
| 40 | Full clinical suite demo and parallel run readiness review |
| 52 | Parallel run results and cutover go/no-go presentation |
| 62 | Post-cutover status and stabilization metrics review |
| 68 | Final project closeout and lessons learned |

### Rollback Plan

Each module has an independent rollback capability:

- **Module-level rollback:** Re-enable green screen access for that module, disable modern UI routing. Green screens remain operational throughout the migration period.
- **Full rollback:** Full rollback to pre-modernization state within 4-hour maintenance window by reverting API gateway routing.
- **Post-cutover safety:** Bidirectional sync bridge remains active for 2 weeks post-cutover per department.
- **Rollback triggers:** More than 5 P1 incidents in 24 hours, data integrity failure, or clinical safety concern.
- **Legacy standby:** IBMi maintained in warm standby until DG-003 legacy decommission gate is passed.

---

## 9. Project Rate

### Blended Rate Model

The engagement uses a blended hourly rate model based on the team composition and role-specific rates.

#### Role-Specific Rates

| Role | Count | Hourly Rate | Allocation | Duration (Weeks) | Total Cost |
|------|:-----:|------------:|:----------:|:----------------:|-----------:|
| Solutions Architect | 1 | $225 | 75% | 68 | $91,800 |
| Full-Stack Developer | 3 | $165 | 100% | 56 | $554,400 |
| IBMi/RPG Integration Specialist | 1 | $195 | 100% | 48 | $74,880 |
| UX/HCD Designer | 1 | $150 | 75% | 36 | $32,400 |
| IAM Security Specialist | 1 | $185 | 50% | 40 | $29,600 |
| QA Engineer | 1 | $140 | 100% | 44 | $49,280 |
| Project Manager | 1 | $160 | 75% | 68 | $65,280 |
| DevOps Engineer | 1 | $170 | 75% | 52 | $53,040 |

*All rates are based on US market averages for Q1 2026. Rates are subject to adjustment for specialized IBMi talent availability.*

#### Rate Summary

| Metric | Value |
|--------|------:|
| Lowest hourly rate | $140 (QA Engineer) |
| Highest hourly rate | $225 (Solutions Architect) |
| Total labor hours | 8,640 |
| **Total internal team cost** | **$750,680** |
| **Contractor cost (IBMi specialist)** | **$74,880** |
| **Training** | **$25,000** |
| **Total development cost** | **$850,560** |

### Infrastructure Costs

Monthly cloud infrastructure costs during and after the engagement:

| Service | Monthly Cost |
|---------|------------:|
| Cloud compute (ECS Fargate) | $3,200 |
| Managed database (RDS PostgreSQL) | $1,800 |
| Container orchestration | $900 |
| Monitoring and logging | $450 |
| Security services | $600 |
| Backup and DR | $550 |
| **Monthly infrastructure total** | **$7,500** |
| **First year infrastructure** | **$90,000** |

### Third-Party Service Costs

| Service | Monthly Cost |
|---------|------------:|
| HL7/FHIR integration engine | $1,200 |
| Identity provider | $800 |
| HIPAA compliance tooling | $500 |
| **Monthly third-party total** | **$2,500** |

### Total Cost Summary

| Category | Cost |
|----------|-----:|
| Development (internal team + contractors + training) | $850,560 |
| Infrastructure (first year) | $90,000 |
| Third-party services (first year) | $30,000 |
| **Total first year** | **$970,560** |
| Risk buffer (20%) | $170,112 |
| **Total first year with risk buffer** | **$1,140,672** |

*The 20% risk buffer reflects the high complexity of this engagement: legacy IBMi modernization with HIPAA compliance, scarce RPG talent, and zero-downtime cutover requirements. Legacy systems frequently surface undocumented business rules during extraction. The buffer will be drawn down only as specific risks materialize, and any unused buffer will not be invoiced.*

### Three-Year Total Cost of Ownership

| Year | Cost |
|------|-----:|
| Year 1 (implementation + infrastructure + third-party) | $1,000,560 |
| Year 2 (operations, support, infrastructure, third-party) | $210,000 |
| Year 3 (operations, support, infrastructure, third-party) | $195,000 |
| **3-Year TCO** | **$1,405,560** |

### Estimate Accuracy and Refinement

| Attribute | Value |
|-----------|-------|
| Estimation methodology | Bottom-up |
| Current estimate pass | Pass 2 (post-architecture) |
| Accuracy target | +/- 25% |
| Confidence level | Medium |

The estimate will be refined at two additional points:

1. **After Phase 1 (Legacy Assessment):** RPG codebase static analysis, DB2/400 schema audit, and HL7/FHIR interface inventory will inform a Pass 3 estimate with +/- 15% accuracy.
2. **After Phase 3 (MVP):** Actual velocity data from Phases 1-3 will inform a Pass 4 estimate for remaining phases with +/- 10% accuracy.

### Cost Optimization Opportunities

The following strategies may reduce costs if adopted:

| Strategy | Potential Savings | Trade-off |
|----------|:-----------------:|-----------|
| Phased green screen replacement (defer low-usage screens) | ~15% | Users on deferred screens continue using 5250 longer |
| RPG service wrapping over full rewrite | ~20% | Long-term maintenance debt; retained IBMi dependency |
| Offshore/nearshore blended team model | ~18% | Timezone coordination overhead; HIPAA BAA requirements |
| Open-source FHIR server (HAPI FHIR) | ~8% | Increased DevOps burden; no vendor SLA |
| Automated test generation from green screen recordings | ~10% | May not capture all edge cases |

---

## 10. Payment Methods

### Invoicing Schedule

The Service Provider will invoice the Client on a monthly basis, in arrears, for services rendered during the preceding calendar month.

### Invoice Details

Each monthly invoice will include:

- Itemized hours by role for the billing period
- Phase and sprint allocation for all hours billed
- Cumulative hours and spend against total engagement budget
- Infrastructure and third-party service pass-through costs (at cost, no markup)
- Remaining budget and projected completion cost
- Summary of deliverables completed during the billing period

### Payment Terms

| Term | Value |
|------|-------|
| Invoice frequency | Monthly, in arrears |
| Payment due | Net 30 from invoice date |
| Late payment interest | 1.5% per month on overdue balances |
| Currency | US Dollars (USD) |

### Accepted Payment Methods

- **ACH bank transfer** (preferred)
- **Wire transfer** (for amounts exceeding $50,000)
- **Corporate check** (with prior arrangement)

### Expense Policy

- Pre-approved travel expenses (airfare, lodging, ground transportation, meals) billed at cost with receipts, no markup.
- Travel requires advance written approval from the Client's designated project contact.
- Routine remote work expenses (software licenses, development tools) are included in hourly rates and not billed separately.

### Risk Buffer Billing

The 20% risk buffer ($170,112) is not billed proactively. Risk buffer hours are billed only when specific risk events materialize and the Service Provider documents the risk event, impact, and hours required. The Client's Project Manager will approve risk buffer draws before work begins. Any unused risk buffer is not invoiced.

### Infrastructure and Third-Party Pass-Through

Cloud infrastructure and third-party service costs are billed as pass-through at the Service Provider's actual cost, with no markup. The Client may elect to procure these services directly under their own accounts, in which case the Service Provider will provide specifications and the Client assumes procurement responsibility.

---

## 11. Assumptions

The following assumptions underpin the scope, timeline, and cost estimates in this SOW. If any assumption proves incorrect, the impact will be assessed and addressed through the Change Order process defined in Section 7.

### Client Environment Assumptions

1. IBMi system has available capacity for API layer connections (connection pooling via IBM i Access ODBC/JDBC).
2. Existing DB2/400 data is structurally sound and does not require major data cleansing. DB2/400 database contains fewer than 500 tables and 50M total records for initial migration scope.
3. Network connectivity between IBMi and modern application servers is adequate.
4. Client provides dedicated IBMi environment access for development and testing within 2 weeks of kickoff.
5. COBOL batch jobs will continue running unmodified on IBMi during and after modernization.
6. No more than 50 unique 5250 green screens require modernization in Phase 1.

### Client Personnel Assumptions

7. Client will provide dedicated RPG developer time (minimum 50%) for knowledge transfer and API collaboration.
8. Client IT staff available for 8-10 hours/week for knowledge transfer and legacy system documentation.
9. Client stakeholders are available for bi-weekly sprint demos and feedback.
10. Client will designate change champions in each clinical department for training rollout.

### Technical Assumptions

11. Existing RPG IV source code is available and version-controlled; no object-only programs without source.
12. Client will procure and configure identity provider (IdP) for SSO -- Service Provider provides integration specifications.
13. Client has existing Active Directory or compatible IdP for SSO integration.
14. Cloud infrastructure provider supports HIPAA-eligible services (AWS GovCloud, Azure Government, or equivalent).
15. HL7 v2 interfaces number 8-12; FHIR R4 interfaces number 3-5.

### Commercial Assumptions

16. Budget covers external consulting team but not Client internal staff costs.
17. HIPAA Business Associate Agreement (BAA) executed before any PHI data access.
18. Client accepts 4-week dual-run period with rollback capability before legacy decommission.
19. All team members pass HIPAA security training before engagement begins.
20. Rates are based on US market averages for Q1 2026; subject to adjustment for specialized IBMi talent.

### External Dependency Assumptions

21. HIPAA compliance pre-assessment from external auditor available by May 15, 2026.
22. Surescripts e-prescribing certification environment access available by September 1, 2026.
23. HL7 FHIR endpoint credentials from connected lab systems available by October 1, 2026.
24. Legacy IBMi source code repository access and documentation available by April 6, 2026 (engagement start).

---

## 12. Signature Block

This Statement of Work is executed by the authorized representatives of both parties. By signing below, each party agrees to the terms, scope, deliverables, timeline, and costs described herein.

This SOW, together with any referenced Master Services Agreement (MSA) between the parties, constitutes the complete agreement for the services described. In the event of conflict between this SOW and the MSA, the terms of the MSA shall govern unless this SOW explicitly states otherwise.

---

### Service Provider

**Modular Earth LLC**

| | |
|---|---|
| Signature: | __________________________________________ |
| Name: | |
| Title: | |
| Date: | |

---

### Client

**Regional Health Partners**

| | |
|---|---|
| Signature: | __________________________________________ |
| Name: | |
| Title: | |
| Date: | |

---

*This document was prepared by Modular Earth LLC for Regional Health Partners. All content is confidential and subject to human review before client delivery. Engagement ID: eng-2026-001. Document version: 1.0.*
