# eng-2026-004: UAT Checklist — Deliverable Verification

Use this checklist to verify all key deliverables before the interview panel presentation.

## Legend
- **Confidence**: HIGH = well-grounded in verified research/experience | MEDIUM = sound reasoning but limited external validation | LOW = requires your expert judgment
- **Priority**: MUST = verify before interview | SHOULD = verify if time permits | COULD = nice to have

---

## 1. Assignment Requirement Coverage

| # | Requirement | Slide | Status | Priority |
|---|------------|-------|--------|----------|
| 1.1 | System context diagram showing PA request flow | 3-4 | Verify diagram renders, all components labeled | MUST |
| 1.1a | Major components labeled (systems, services, data stores) | 3-4 | Check component table completeness | MUST |
| 1.1b | Integration mechanisms labeled (APIs, queues, file transfer) | 3-4 | Check edge labels on Mermaid diagram | MUST |
| 1.2a | Inbound PA Request Ingestion design | 5-6 | Verify fax/portal/EDI flows are clear | MUST |
| 1.2b | Clinical Data Access with FHIR/HL7 role specified | 7 | Verify FHIR/HL7 table is accurate | MUST |
| 1.3 | Top 3 security risks with specific mitigations | 8-9 | Verify mitigations are architectural patterns (not generic) | MUST |
| 2.1 | Executive summary for CIO/C-Suite | 2 | Read aloud — does it resonate for a non-technical audience? | MUST |
| 2.2 | 12-week roadmap with decision points | 10 | Verify phases match assignment suggestion | MUST |
| 3.1 | MLOps architecture (drift + feedback loop) | 11 | Verify PSI/KS claims are technically accurate | MUST |
| 3.2 | Multi-tenant vs multi-instance justification | 12 | Verify trade-off table is balanced | MUST |

---

## 2. Technical Accuracy — Areas Requiring Your Review

### HIGH CONFIDENCE (verified by research agents)
- [x] AWS services exist and are production-ready (10/10 verified)
- [x] CMS-0057-F deadlines and requirements (verified from CMS.gov)
- [x] FHIR R4 resource types for Da Vinci PAS (verified from HL7.org)
- [x] HIPAA Security Rule sections cited correctly
- [x] Numerical consistency across all deliverables

### MEDIUM CONFIDENCE — Review These
| # | Item | Why Review | What to Check |
|---|------|-----------|---------------|
| MC-1 | **Autonomize AI platform capabilities** | Based on web research, not hands-on experience. "3 of top 5 health plans" is vendor-sourced. | Verify Genesis Platform, PA Copilot, AI Studio features match what you'll be told in the interview. Ask about deployment model (Azure vs. AWS). |
| MC-2 | **60% auto-determination target** | Industry benchmarks suggest 50-76% is achievable, but depends heavily on clinical case mix and LOB. | Is 60% conservative enough for a first LOB? Autonomize AI's Altais case study claims 50% — our target is only slightly higher. |
| MC-3 | **$33K/month infrastructure estimate** | Based on published AWS on-demand pricing. Enterprise pricing typically 20-30% lower. Textract volume ($5K/month) depends on actual fax page count. | Sanity check: does $33K/month feel right for this scale? Your Arine experience with similar scale data processing is the best benchmark. |
| MC-4 | **SageMaker PSI support** | KS test is natively supported. PSI requires custom monitoring container. Our architecture references both. | Verify you're comfortable explaining this distinction in the interview. Could mention Wasserstein Distance as alternative. |
| MC-5 | **SMART on FHIR implementation on AWS** | AWS provides reference architecture (Cognito + HealthLake) but it's not a turnkey managed service. Requires customization. | Verify you're comfortable explaining this as "reference architecture + custom integration" not "turn-key feature." |

### LOW CONFIDENCE — Definitely Review These
| # | Item | Why Review | What to Check |
|---|------|-----------|---------------|
| LC-1 | **Autonomize AI deployment on AWS** | Research shows Autonomize AI emphasizes Azure deployments (Azure Marketplace listing, Pegasus Program). Our architecture assumes AWS connectivity via PrivateLink. | Ask Autonomize AI directly: do they support AWS-hosted deployments? Or is cross-cloud connectivity (Azure ↔ AWS PrivateLink) the actual pattern? This could change the deployment view diagram. |
| LC-2 | **Inter-agent security within Genesis Platform** | STRIDE Spoofing T-005 flagged that inter-agent authentication within Autonomize AI's platform is a black box. We can't verify their internal security posture. | In the interview, frame this as a contractual requirement: "We'd need to validate inter-agent authentication controls as part of the BAA." Shows security depth without claiming knowledge you don't have. |
| LC-3 | **TriZetto Facets API capabilities** | We assumed REST API + JDBC access for eligibility. Real Facets deployments vary significantly by payer. | If asked about Facets integration specifics, acknowledge this is configurable and would be validated during the Discovery phase (Week 1-2). |
| LC-4 | **12-week timeline feasibility** | Aggressive for full integration build + security hardening + UAT. Achievable if Autonomize AI provides turnkey PA Copilot. Risk: legacy DB connectors could take longer than estimated. | Your experience with similar enterprise integrations is the best judge. Is 4 weeks for core integration build realistic with 4 senior devs? |
| LC-5 | **Hourly rates in estimate** | $150-$250/hr rates based on US market consulting rates. Not cited from a specific source. | Verify these feel right for the roles described. Autonomize AI may have different rate expectations for their team. |

---

## 3. Presentation Quality

| # | Check | Priority | Status |
|---|-------|----------|--------|
| P-1 | Read all speaker notes aloud — do they flow for a 1-hour panel? | MUST | |
| P-2 | Render all 6 Mermaid diagrams to PNG/SVG — do they look professional? | MUST | |
| P-3 | Does the executive summary (Slide 2) stand alone for a CIO audience? | MUST | |
| P-4 | Are security mitigations specific (tokenization, PrivateLink) not generic ("use encryption")? | MUST | |
| P-5 | Does the MLOps slide (11) demonstrate senior/principal-level depth? | SHOULD | |
| P-6 | Does the multi-tenant slide (12) clearly justify the trade-off decision? | SHOULD | |
| P-7 | Are all numbers consistent across slides (2.5M/month, 45M members, 60% target, etc.)? | MUST | Verified |
| P-8 | Does the intro (Slide 1) establish your credibility effectively? | SHOULD | |

---

## 4. Cross-Deliverable Consistency

| # | Check | Files | Status |
|---|-------|-------|--------|
| C-1 | Requirements FRs map to architecture components | requirements.json → architecture.json | Verified |
| C-2 | Architecture components map to estimate LOE | architecture.json → estimate.json | Verified |
| C-3 | Estimate phases match project plan phases | estimate.json → project_plan.json | Verified |
| C-4 | Project plan milestones match proposal roadmap | project_plan.json → proposal.md | Verified |
| C-5 | Security threats map to proposal security slide | security_review.json → proposal.md Slide 8-9 | Verified |
| C-6 | All KB files pass schema validation | `python tests/validate_knowledge_base.py` | 10/10 PASS |

---

## 5. Sign-Off

| Reviewer | Date | Status | Notes |
|----------|------|--------|-------|
| AI Agent (Claude Opus 4.6) | 2026-03-21 | PASS (8.8/10) | All checks automated. Low-confidence items flagged above. |
| Paul Prae | | | |
