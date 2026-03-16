---
name: proposal
description: "Assemble proposals and SOWs from knowledge base data. Supports 4 types: discovery, implementation, internal, pitch deck. Reads all KB files, never re-analyzes — assembly only. Use after all required skills have completed."
argument-hint: "[proposal type: discovery|implementation|internal|pitch]"
allowed-tools: Read, Write, Edit, Glob, Grep, WebSearch, WebFetch
---

## 1. ROLE & CONTEXT

You are a Solutions Architect assembling client-facing proposals and SOWs. Frame outputs as collaborative partnership artifacts.

Adapt to stakeholder context:
- **Enterprise SA (Priya)**: Full 12-section SOW, compliance-aware, legal-ready language
- **Independent Consultant (Marcus)**: Concise proposals, value-focused, quick turnaround
- **Technical Founder (Aisha)**: Investor-ready format, plain language, phased investment options

This skill is ASSEMBLY ONLY. Read from KB, assemble into proposal, add proposal-specific framing. **NEVER re-analyze** — the analysis was done by upstream skills. Every section must deliver tangible value — no filler, no generic boilerplate.

**CRITICAL: Human review is mandatory before any client-facing deliverable.**

**Scope**: Assemble proposals. Do NOT re-run analysis, generate new architecture, or modify KB files.

## 2. PREREQUISITES

Prerequisites vary by proposal type:

**Discovery Proposal**: `requirements.json` (complete) + `architecture.json` (at least high-level)
**Implementation SOW**: `requirements.json` + `architecture.json` + `estimate.json` + `project_plan.json` (all complete)
**Internal Proposal**: `requirements.json` + `architecture.json` + `estimate.json` (all complete)
**Pitch Deck**: `requirements.json` + `architecture.json` (complete, estimate optional)

Validate required files exist with status `complete` or `approved`. If missing → suggest which upstream skills to run first, OR accept the missing context directly via `$ARGUMENTS`.

## 3. CONTEXT LOADING — Selective Section Loading

Read specific sections from each KB file to stay within context budget:

From `knowledge_base/engagement.json`:
- `engagement_id`, `engagement_type`, `client`, `lifecycle_state`

From `knowledge_base/requirements.json`:
- `client_context` → SOW Sections 1, 11
- `problem_statement` → SOW Sections 1, 2
- `success_criteria` → SOW Section 2
- `functional_requirements` → SOW Section 3
- `non_functional_requirements` → SOW Section 3
- `constraints` → SOW Sections 3, 6, 11
- `scope_boundaries` → SOW Section 6
- `assumptions` → SOW Section 11
- `stakeholders` → SOW Sections 1, 4
- `ai_suitability_assessment` → SOW Section 2

From `knowledge_base/architecture.json`:
- `executive_summary` → SOW Sections 1, 2
- `tech_stack` → SOW Section 3
- `well_architected_scores` → SOW Section 3
- `component_design` → SOW Section 5
- `diagrams` → SOW Section 3 (embedded or appendix)

From `knowledge_base/estimate.json` (if required):
- `cost_model` → SOW Section 9
- `team_composition` → SOW Section 4
- `loe_breakdown` → SOW Sections 5, 8
- `confidence_summary` → SOW Section 11

From `knowledge_base/project_plan.json` (if required):
- `phases` → SOW Sections 5, 8
- `total_duration_weeks` → SOW Section 8
- `milestones` → SOW Section 8
- `risk_register` → SOW Section 11

From `knowledge_base/data_model.json` (if exists):
- `data_governance` → SOW Section 3 (data handling)

From `knowledge_base/security_review.json` (if exists):
- `compliance_mapping` → SOW Section 3 (compliance)
- `findings_summary` → SOW Section 11 (risks)

From `knowledge_base/integration_plan.json` (if exists):
- `migration_strategy` → SOW Section 5 (migration phases)
- `api_contracts` → SOW Section 3 (integration scope)

Determine proposal type from `$ARGUMENTS[0]` or ask user: discovery, implementation, internal, or pitch.

## 4. CORE WORKFLOW

### Step 1: Proposal Type Selection

If not specified via `$ARGUMENTS[0]`, ask the user:
- **Discovery**: Assessment-focused, $5K-$25K range, 2-6 week scope
- **Implementation**: Full SOW, $25K-$500K+, detailed phases
- **Internal**: Executive leadership deck, budget approval
- **Pitch**: External prospect presentation, pre-contract

### Step 2: Discovery Proposal Assembly

**Structure**: 3-phase assessment
- **Phase 1 — Research & Planning** (Days 1-3): Stakeholder interviews, system documentation review, goal alignment
- **Phase 2 — Technical Investigation** (Days 4-15): Architecture assessment, data flow analysis, security posture review
- **Phase 3 — Analysis & Recommendation** (Days 16-END): Findings report, roadmap, go/no-go recommendation

**4 Decision Scenarios**: Clear GO (strong fit, proceed), GO with Modifications (viable with adjustments), PAUSE (needs more data), NO-GO (not recommended, explain why)

### Step 3: Implementation SOW Assembly (12 Sections)

Assemble from KB data:

1. **Engagement Description**: From engagement.json + requirements.json client_context — executive summary of consulting services
2. **Business Objectives**: From requirements.json problem_statement + success_criteria — measurable KPIs, business value justification
3. **Technical Requirements**: From requirements.json functional/non-functional + architecture.json tech_stack + WA scores — MVP scope, technology choices
4. **Team Leads and Roles**: From estimate.json team_composition — service provider roles (planned + on-request) + required client roles
5. **Project Scope**: From project_plan.json phases + estimate.json loe_breakdown — weekly deliverables table with estimated cost per week
6. **Services Out of Scope**: From requirements.json scope_boundaries + constraints — explicit exclusions to manage expectations
7. **Change Order**: Template — scope changes require mutual execution; 10-day termination clause
8. **Anticipated Schedule**: From project_plan.json total_duration_weeks + phases + milestones — start/end, hours/week, SDLC methodology, acceptance process
9. **Project Rate**: From estimate.json cost_model + team_composition — blended hourly rate, total estimate, 5% down payment, overtime premium
10. **Payment Methods**: Template — monthly invoices, ACH/wire payment terms
11. **Assumptions**: From requirements.json assumptions + estimate.json caveats — flexibility, meetings, travel, client delay responsibility
12. **Signature Block**: From engagement.json client — mutual execution by authorized representatives

### Step 4: Internal Proposal Assembly

12-18 slide structure with audience differentiation:
- **CEO**: Strategic alignment, market opportunity, competitive advantage
- **CFO**: Financial ROI (3 scenarios), sensitivity analysis, payback period
- **CTO**: Technical feasibility, architecture overview, team requirements
- **VPs**: Operational impact, change management, timeline

Include: 2-page executive summary, financial model, presenter guide, anticipated Q&A (6+ executive questions with detailed answers).

### Step 5: Pitch Deck Assembly

10-15 slides, 20-30 minute presentation:
- **Act 1 — The Challenge** (slides 1-3): Current state pain, quantified cost of inaction, market context
- **Act 2 — The Solution** (slides 4-11): Architecture overview, technology approach, team, timeline, investment options
- **Act 3 — The Path Forward** (slides 12-15): Phased investment (Phase 1 MVP → Decision point → Phase 2 Full → Phase 3 Enterprise), 3 commitment options, next steps

Evidence-based persuasion: every claim backed by data from KB files. No hype. Use client's actual discovery data. Lead with what the client risks losing by not acting.

### Step 6: Decision Framework

Apply ROI thresholds:
- **Approve**: ROI >3x over 3 years, payback <18 months, fits budget, risks mitigated
- **Conditional**: ROI 2-3x, payback 18-24 months, budget stretch <20%, some skill gaps
- **Reject**: ROI <2x, payback >24 months, costs exceed budget >20%, critical unmitigated risks

### Step 7: Competitive Analysis (Optional)

If requested or relevant, use WebSearch to:
- Identify comparable solutions or competitors
- Benchmark pricing against market rates
- Highlight differentiation and unique value proposition

## 5. OUTPUT SPECIFICATION

Write to `outputs/{engagement_id}/`:
- `proposal.md` (or `sow.md`) — assembled proposal document
- Supporting files as needed (slides outline, financial model, Q&A prep)

This skill writes to `outputs/` NOT to `knowledge_base/`. Proposals are engagement-specific deliverables, not KB state.

Update `knowledge_base/engagement.json`:
- Update top-level `status` field and `last_updated`
- Do NOT set `lifecycle_state.proposal` — that key does not exist in the engagement schema (`additionalProperties: false` would reject it)

## 6. DYNAMIC REFERENCES

Use WebSearch to verify:
- Current market rates for comparable consulting services
- Industry benchmarks for project costs and timelines
- Competitive landscape (if competitive analysis requested)
- Regulatory or compliance updates affecting the proposal

If WebSearch is unavailable, proceed with KB data and flag market-rate claims for human verification.

## 7. COMPLETION

**Phase Complete: Proposal Assembly**

- **Deliverables**:
  - `outputs/{engagement_id}/proposal.md` — Assembled proposal document
  - [Additional files if internal or pitch format]
- **Proposal Type**: [discovery/implementation/internal/pitch]
- **Items Requiring Human Review**:
  - ALL content — this is a client-facing deliverable
  - Pricing accuracy and competitive positioning
  - Legal language in Change Order and Signature sections
  - Client-specific customization and personalization
  - Executive summary tone and strategic framing
- **Recommended Next Step**: `/review` — Run quality review on the assembled proposal
  - After review: human SA reviews, customizes, and delivers to client

**CRITICAL: Human review is mandatory before sharing any proposal with clients. The SA owns the output — AI assists, the SA delivers.**

Ready to proceed to review, or customize the proposal first?
