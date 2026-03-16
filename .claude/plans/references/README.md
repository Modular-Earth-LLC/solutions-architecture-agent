# Planning References Directory

> This directory is **git-ignored** (except this README and .gitkeep). All files here are local planning materials that inform phases but are NOT committed to the public repository.

## Purpose

This directory contains reference materials used across all 9 phases of the master plan refactoring. Future phases should consult these materials for:

- **Phase 2** (Requirements): Pre-sales lifecycle, SOW templates, discovery frameworks, AGADA requirements templates
- **Phase 3** (Technical Design): Architecture exemplars, diagram patterns, target architecture spec
- **Phase 5** (Skill Implementation): Exemplar deliverables as quality bar for each skill's output
- **Phase 6** (KB & Templates): Data model patterns, security patterns from Florence Healthcare engagement
- **Phase 7** (Validation): Real engagement scenarios for end-to-end testing (AGADA 0-to-1, migration assessments)
- **Phase 8** (Documentation): Pre-sales lifecycle for getting-started guides, engagement flow documentation

## File Index

### Planning Documents (markdown, committed context)

| File | Purpose | Used By |
|------|---------|---------|
| `master-plan.md` | (in parent dir) Master 9-phase refactoring plan | All phases |
| `agent-to-skill-mapping.md` | Maps 23 legacy agents to 9 target skills | Phases 1-5 |
| `target-architecture.md` | Target plugin structure and design decisions | Phases 3-5 |
| `anthropic-cloud-deployment.md` | Cloud deployment options for agent packaging | Phase 9 |
| `current-claude-code-setup.md` | Current operator environment details | Local reference |
| `reference-materials-index.md` | Complete index of all real-world SA materials with ratings | Phases 2, 5, 7 |
| `pre-sales-lifecycle.md` | Complete pre-sales process with SA agent augmentation map | Phases 2, 5, 8 |

### Case Study PDFs (git-ignored, for Phase 7 testing)

| File | Source | Description | Tests Skills |
|------|--------|-------------|-------------|
| `PAI-Take_Home_Exercise.pdf` | PAI | Product packaging automation case study | /requirements, /architecture, /estimate |
| `Solution Architect Case Study and Interview.pdf` | Interview prep | IBMi modernization + domain-driven design | /requirements, /integration-plan, /architecture |
| `AI-solutions_architecture-technical-design-principles.zip` | Internal | Technical design principles reference | All skills |

### Hyperbloom Exemplar Deliverables (git-ignored)

These are real, high-quality SA deliverables from Hyperbloom consulting engagements.

| File | Type | Quality | Tests Skills |
|------|------|---------|-------------|
| `hyperbloom-agada-architecture.pdf` | Full 23-page system architecture (healthcare/biotech) | Exemplar (5/5) | /architecture, /security-review, /data-model |
| `hyperbloom-agada-architecture-diagram.png` | Architecture diagram with VPC, security, blockchain | Exemplar (5/5) | /architecture |
| `hyperbloom-agada-project-plan.pdf` | 16-page Agile project plan with team comp + milestones | Exemplar (5/5) | /project-plan, /estimate |
| `hyperbloom-revelex-proposal.pdf` | 10-page 3-phase AI agent proposal | Exemplar (5/5) | /proposal, /architecture, /estimate |
| `hyperbloom-sow-template.pdf` | 12-page SOW template with placeholders | Gold template | /proposal |
| `hyperbloom-genomics-data-platform-diagram.png` | Data platform architecture (on-prem to cloud) | Strong (4/5) | /architecture, /data-model |

### Hyperbloom Florence Healthcare Materials (git-ignored)

Data modeling, protection, and disaster recovery patterns from a healthcare consulting engagement. Fills the /data-model and /security-review gaps.

| File | Type | Quality | Tests Skills |
|------|------|---------|-------------|
| `florence-mongo-dr-recommendations.docx` | DR plan, backup strategy, access control design | 5/5 | /data-model, /security-review |
| `florence-mongo-access-automation.docx` | Access automation architecture, security policy | 5/5 | /security-review, /integration-plan |
| `florence-db-access-workflow.pdf` | Jira->Terraform access governance workflow | 5/5 | /security-review, /integration-plan |

**Key patterns extracted**:
- Multi-tier access approval workflow (Jira Kanban -> Atlantis -> Terraform -> AWS/MongoDB)
- Time-bounded JIT access with automated revocation
- Audit trail architecture (CloudTrail + CloudWatch)
- Healthcare data classification taxonomy (Account/User/Study data, PHI, Special Categories)
- Replica set architecture for RTO/RPO requirements
- CRUD operation logging and alerting for destructive operations

> Source: `C:\Users\paulp\OneDrive - Hyperbloom Ventures Inc\Data Science Practice\Florence Healthcare`

### AGADA Requirements Analysis Templates (git-ignored)

6 professional requirements templates + 1 academic research paper covering the complete requirements lifecycle. Fills a massive /requirements methodology gap.

| File | Type | Quality | Methodology |
|------|------|---------|-------------|
| `agada-rad-template.docx` | RAD process template | 5/5 | 3-phase: Prepare -> Elicit -> Record & Score. Temporal framing questions. |
| `agada-pm-requirements-template.docx` | PM requirements gathering | 5/5 | 10-section template with stakeholder scenarios, risk mgmt, tech architecture |
| `agada-system-requirements-template.docx` | Government/PDM system requirements | 5/5 | 9 mandatory sections including current system analysis, capacity planning |
| `agada-requirements-excel-template.xls` | Prioritized scope framework | 5/5 | 4-type classification (Functional/Technical/Operational/Transitional), Core/Essential/Desired priority |
| `agada-ieee830-srs-template.doc` | IEEE 830 SRS template | 4/5 | ANSI/IEEE standard with analysis models (sequence diagrams, DFDs, STDs) |
| `agada-maguire-bevan-ura-research.pdf` | IFIP user requirements analysis | 4/5 | 4-stage academic methodology with context-of-use analysis framework |

**Key patterns extracted** (9 gaps filled in /requirements skill):
1. Guided discovery prompt sequences (RAD temporal framing)
2. Four-type requirement classification (Functional/Technical/Operational/Transitional)
3. Context-of-use analysis framework (users, tasks, technical/physical/org environment)
4. Explicit scope boundaries (in-scope/out-of-scope with justification)
5. Expanded non-functional requirements (10+ categories vs current 4)
6. Stakeholder analysis with critical success factors and persona mapping
7. Acceptance criteria with testable validation plans
8. Governance sections (version control, approval, change management)
9. Requirements traceability (forward and backward)

> Source: `C:\Users\paulp\OneDrive - Hyperbloom Ventures Inc\Data Science Practice\AGADA Biosciences\User Requirements Templates`

### AVAHI Templates and Frameworks (git-ignored)

PII-free templates and frameworks from AVAHI consulting engagements.

| File | Type | Quality | Tests Skills |
|------|------|---------|-------------|
| `avahi-rapid-assessment-templates.xlsx` | 150+ structured discovery questions across 7 categories | Gold standard (5/5) | /requirements |
| `avahi-qualifying-questions-genai.xlsx` | BANT framework + GenAI discovery questions | Excellent (5/5) | /requirements |
| `avahi-genai-discovery-sow-template.docx` | Clean SOW template with placeholders (no PII) | Excellent (5/5) | /proposal |
| `avahi-deal-stage-raci.pdf` | RACI chart for deal stages (pre-sales lifecycle) | Excellent (5/5) | /project-plan, /requirements |
| `avahi-rapid-funding-guide.pdf` | AWS funding tiers and eligible activities | Strong (4/5) | /estimate, /proposal |
| `avahi-enterprise-search-sow-template.pdf` | Enterprise search SOW (OpenSearch, Bedrock, NL2SQL) | Strong (4/5) | /architecture, /integration-plan |
| `avahi-nl2sql-sow-template.pdf` | NL2SQL solution SOW template | Strong (4/5) | /architecture, /data-model |
| `avahi-medical-scribing-sow-template.pdf` | HIPAA healthcare medical scribing SOW | Strong (4/5) | /architecture, /security-review |

### Source Directories (NOT copied, read on-demand)

These directories on the operator's machine can be read during Phase 7 testing but are NOT copied here:

| Path | Content | Use |
|------|---------|-----|
| `C:\Users\paulp\OneDrive - Modular Earth LLC (1)\AI\Knowledge Bases\Sales Copilot Training Data` | Hyperbloom SA materials (31 files) | Phase 7 testing scenarios |
| `C:\Users\paulp\OneDrive\Businesses\Modular Earth\Clients\AVAHI\int-sales-engineering-agent-knowledge-base` | AVAHI consulting materials (62 files) | Phase 7 industry diversity testing |

## Recommended Phase 7 Test Scenarios

### Scenario 1: Healthcare Platform (0-to-1)
**Source**: AGADA engagement (Hyperbloom)
**Input**: AGADA SOW scope
**Flow**: /requirements -> /architecture -> /data-model -> /security-review -> /estimate -> /project-plan -> /proposal -> /review
**Compare against**: hyperbloom-agada-architecture.pdf, hyperbloom-agada-project-plan.pdf

### Scenario 2: Cloud Migration Assessment
**Source**: Bluebird/SmartTrix (AVAHI)
**Input**: Migration assessment scope
**Flow**: /requirements -> /integration-plan -> /architecture -> /security-review -> /estimate -> /project-plan -> /proposal -> /review
**Compare against**: AVAHI migration SOWs

### Scenario 3: GenAI Agent Platform (0-to-1)
**Source**: Revelex AI (Hyperbloom)
**Input**: AI booking agent scope
**Flow**: /requirements -> /architecture -> /data-model -> /estimate -> /project-plan -> /proposal -> /review
**Compare against**: hyperbloom-revelex-proposal.pdf

### Scenario 4: Discovery-Only Assessment
**Source**: AInnocence (AVAHI)
**Input**: Assessment scope
**Flow**: /requirements -> /architecture -> /security-review -> /proposal
**Compare against**: AInnocence assessment SOW

### Scenario 5: Multi-Industry Quick Discovery
**Source**: RAPID templates (AVAHI)
**Input**: Qualifying questions
**Flow**: /requirements (all 3 tiers)
**Compare against**: avahi-rapid-assessment-templates.xlsx

## Skill Coverage from Reference Materials

| Skill | Exemplar Available? | Primary Sources |
|-------|-------------------|----------------|
| /requirements | **YES (STRONG)** | RAPID templates (150+ questions), 6 AGADA requirements templates (RAD, PM, IEEE 830, system requirements), qualifying questions, Maguire-Bevan research methodology |
| /architecture | **YES (STRONG)** | AGADA architecture (23pp), architecture diagram, SmartTrix IaC, 20+ AVAHI SOWs |
| /estimate | **YES** | SOW templates with pricing, Revelex phased costs ($90K), consulting delivery model (three-pass estimation) |
| /project-plan | **YES (STRONG)** | AGADA project plan (16pp), consulting service delivery model (sprint methodology, capacity model) |
| /proposal | **YES (STRONG)** | Revelex proposal, SOW templates (Hyperbloom + AVAHI), pre-sales lifecycle |
| /data-model | **YES** | Florence Healthcare MongoDB topology, replica set architecture, healthcare data classification taxonomy, JMARK NL2SQL |
| /security-review | **YES** | Florence Healthcare access governance workflow, JIT access automation, audit trail architecture, DPA structure, AGADA security layer, HIPAA SOWs |
| /integration-plan | **MODERATE** | Florence Jira->Terraform pipeline, enterprise search template, migration SOWs |
| /review | **NONE (expected)** | AI-generated capability with no pre-AI analog; methodology defined in extracted patterns |

## PII Warning

Many files in this directory contain client names, consultant names, rates, and contact information. These files are git-ignored and must NEVER be committed. When referencing content in public-facing outputs:
- Anonymize client names (e.g., "HealthCo", "Client A")
- Remove all personal contact info
- Redact specific rates and pricing
- Use patterns and structures, not verbatim content
