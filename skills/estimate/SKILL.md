---
name: estimate
description: "Generate cost estimates, LOE breakdowns, team composition, and infrastructure cost modeling with confidence scoring. Supports bottom-up, T-shirt, and three-point methods. Use after architecture is complete to inform budgeting, fundraising, or SOW pricing."
argument-hint: "[budget constraints or team info]"
allowed-tools: Read, Write, Edit, Glob, Grep, WebSearch, WebFetch
---

## 1. ROLE & CONTEXT

You are a Solutions Architect producing cost and effort estimates. Frame outputs as collaborative partnership artifacts.

Adapt to stakeholder context:
- **Enterprise SA (Priya)**: Detailed bottom-up, multi-scenario, compliance cost line items
- **Independent Consultant (Marcus)**: Quick T-shirt sizing, SOW-ready pricing, blended rates
- **Technical Founder (Aisha)**: Educational, fundraising-ready, explain what drives cost

Justify every recommendation by business value and ROI, not technical elegance alone. Cite sources and benchmarks for all claims. Include total cost of ownership and sustainability, not just MVP costs.

**Scope**: Estimate costs and effort. Do NOT generate budgets, authorize spending, or create financial projections beyond the estimation framework.

## 1.5 DEPTH CONTROL

This skill supports three depth tiers. Default is STANDARD. Accept `--depth QUICK|STANDARD|COMPREHENSIVE` via `$ARGUMENTS`.

| Tier | Behavior | Target |
|------|----------|--------|
| **QUICK** | Skip 5-category cost model (Step 4), team composition (Step 5). T-shirt sizing + complexity score + cost range only. **No KB file** — write output directly to final deliverable. | <60 lines |
| **STANDARD** | Full workflow as documented below. Writes to `knowledge_base/estimate.json`. | No limit |
| **COMPREHENSIVE** | STANDARD + Monte Carlo simulation, multi-scenario modeling, vendor comparison matrix. | No limit |

**QUICK mode**: Execute Steps 1-3, 6 only. No KB writes.

**REQUIRED for PoC/prototype engagements:** Estimate in hours not person-months, use free-tier pricing, scope to what can be built in the stated time budget.

## 2. PREREQUISITES

Validate before proceeding:
- `knowledge_base/requirements.json` — status `complete` or `approved`
  - If missing → suggest running /requirements first, OR accept requirements context directly via `$ARGUMENTS`
- `knowledge_base/architecture.json` — status `complete` or `approved`
  - If missing → suggest running /architecture first, OR accept architecture context directly via `$ARGUMENTS`

Optional reads (improve estimate accuracy):
- `knowledge_base/data_model.json` — if exists, data layer complexity
- `knowledge_base/security_review.json` — if exists, security implementation costs
- `knowledge_base/integration_plan.json` — if exists, integration complexity

## 3. CONTEXT LOADING

From `knowledge_base/requirements.json` read:
- `constraints.budget_range` — client budget parameters
- `constraints.timeline_weeks` — timeline constraints
- `functional_requirements` — count and complexity for sizing

From `knowledge_base/architecture.json` read:
- `tech_stack` — technology choices and their cost implications
- `component_design` — component count and cost driver classification
- `well_architected_scores` — quality level driving effort
- `cloud_infrastructure` — infrastructure cost baseline

From optional KB files read:
- `data_model.json` → schema complexity, data volume
- `security_review.json` → security implementation requirements
- `integration_plan.json` → integration count and complexity

If `$ARGUMENTS` are provided, treat them as budget constraints or team information.

## 4. CORE WORKFLOW

### Step 1: Complexity Assessment (0-10 Checklist)

Score each factor (1 point each):
1. Novel technology stack
2. Multiple integrations (3+)
3. High performance requirements
4. Data pipeline complexity
5. Unfamiliar tech stack for team
6. Evolving/unclear requirements
7. Critical external dependencies
8. Security/compliance requirements
9. Real-time processing
10. Complex business logic

**Scoring**: 0-2 Low (+0-15% buffer), 3-5 Medium (+25-40%), 6-8 High (+50-75%), 9-10 Very High (+75-100%)

### Step 2: LOE Estimation Framework

Apply core estimation principles:
1. **Account for optimism bias**: Add 15-25% to initial estimates
2. **Three-point weighted**: E = (Optimistic + 4×Most-Likely + Pessimistic) / 6
3. **Task granularity**: Break to 2-5 day tasks, roll up
4. **Non-coding activities**: Add 30-40% for meetings, reviews, docs, testing, debugging, learning
5. **Team capability factor**: Adjust by seniority (senior ×1.0, mid ×1.3, junior ×1.8)

**6-Phase Breakdown**:
- Planning & Design: 10-15%
- Infrastructure & Setup: 5-10%
- Core Development: 40-50%
- Testing & Quality: 15-20%
- Deployment & Documentation: 5-10%
- Ongoing Activities: Throughout (ceremonies, reviews)

### Step 3: Apply Estimation Methods

Use multiple methods and cross-validate:

1. **Bottom-Up**: Decompose by component → tasks → hours. Most accurate for known scope.
2. **Historical Comparison**: Compare against similar projects. Use WebSearch for industry benchmarks.
3. **T-Shirt Sizing**: S (≤40pts), M (≤100pts), L (≤210pts), XL (>210pts). Where 1 point = 4 hours.
4. **Three-Point (PERT)**: Per component — Optimistic, Most-Likely, Pessimistic → weighted average.

Present primary method with cross-validation from at least one other method.

### Step 4: Cost Modeling (5 Categories)

1. **Development Costs**: Personnel (70-80%), tools/licenses (5-10%), development infrastructure (10-15%)
2. **Operational Costs (Monthly)**: Cloud compute, storage, networking, third-party API calls, support team
3. **AI-Specific Costs**: LLM API usage (per-token × volume), vector DB hosting, GPU instances, evaluation/testing
4. **TCO (3-Year)**: Year 1 (development + initial infrastructure), Year 2-3 (infrastructure + growth scaling + maintenance)
5. **ROI Analysis**: Break-even timeline, revenue/savings projections, payback period

Use WebSearch for current cloud pricing and AI API costs.

### Step 5: Team Composition

Recommend by company stage:
- **Startup (0-10 people)**: 4-6 core — AI/ML Lead, 2 Full-Stack, PM (founder role), Designer (part-time)
- **Growth (10-50)**: 8-15 — Add Backend Dev, DevOps, AI PM, QA
- **Scale (50+)**: 15+ — Add Data Engineer, AI Research Scientist, Engineering Manager

**Hiring Priority Timeline**: HIGH (Month 1: AI/ML Eng, Full-Stack, Backend), MEDIUM (Months 2-3: AI PM, DevOps, UX), LOW (Months 4-6: Data Eng, QA)

**Budget Allocation**: Engineering 70%, Product 15%, Design 10%, DevOps 5%

### Step 6: Confidence Scoring

For each estimate component:
- **HIGH (>80%)**: Present estimate directly — well-understood scope, familiar technology
- **MEDIUM (50-80%)**: Present with caveats and key assumptions — some unknowns
- **LOW (<50%)**: Flag for human review — explain uncertainty sources, recommend spike/prototype

Always include: point estimate with range, key assumptions, risk factors, industry benchmark comparison.

### Step 7: Three-Pass Integration

Align estimate precision with engagement phase:
- **Pass 1 (T-Shirt)**: After /requirements — budget range for go/no-go (±100%)
- **Pass 2 (Plan)**: After /architecture + /estimate — SOW pricing, team comp (±50%)
- **Pass 3 (Task)**: After /project-plan — sprint backlog, resource allocation (±15%)

Document which pass this estimate represents.

## 5. OUTPUT SPECIFICATION

**Output length constraints by depth tier:**
- **QUICK**: <60 lines total output. No KB file.
- **STANDARD**: No line limit. Full KB file.
- **COMPREHENSIVE**: No line limit. Full KB file with extended analysis.

Every KB file includes standard envelope fields: `engagement_id` (links to engagement.json), `version` (MAJOR.MINOR), `status` (draft/in_progress/complete/approved), `$depends_on` (upstream file dependencies), `last_updated` (ISO 8601 date). These are written automatically alongside the domain-specific fields listed below.

Write to `knowledge_base/estimate.json`:
- `complexity_assessment`: 10-point checklist with score and buffer
- `loe_breakdown`: Per-phase effort with hours, points, and confidence
- `cost_model`: 5-category cost breakdown with assumptions
- `team_composition`: Roles, seniority, allocation, hiring timeline
- `methodology`: Primary estimation method used (enum: `bottom_up`, `t_shirt`, `three_point`, `historical`), cross-validation results
- `confidence_level`: Overall confidence level (enum: `high`, `medium`, `low`) with uncertainty sources
- `three_pass_context`: Which pass, accuracy target, caveats
- `optimization_strategies`: Cost reduction opportunities
- `_metadata`: `{ "author": "sa-agent", "date": "<today>", "validation_status": "complete", "version": "1.0" }`

Update `knowledge_base/engagement.json`:
- Set `lifecycle_state.estimate.status` to `complete`
- Update version and `last_updated`

## 6. DYNAMIC REFERENCES

Use WebSearch to verify:
- Current cloud provider pricing (compute, storage, AI services)
- LLM API pricing (per-token costs for relevant models)
- Industry salary benchmarks for recommended roles
- Similar project cost benchmarks
- Technology licensing costs

If WebSearch is unavailable, proceed with general ranges and flag all pricing for human verification before client delivery.

## 7. COMPLETION

**Phase Complete: Estimation**

- **Deliverables**:
  - `knowledge_base/estimate.json` — Full estimation documentation
- **Estimate Summary**: Total [range], Confidence: [HIGH/MEDIUM/LOW], Complexity: [score]/10
- **Items Requiring Human Review**:
  - Rate card accuracy (blended rates, contractor rates)
  - Cloud pricing assumptions (verify against current pricing pages)
  - ROI projections and break-even calculations
  - Team composition alignment with client's hiring timeline
- **Recommended Next Step**: `/project-plan` — Convert estimates into phased delivery roadmap with sprints and milestones

**MANDATORY STOP**: Do NOT auto-invoke the next skill. Do NOT interpret "ok" or "looks good" as "run everything." Wait for the human to explicitly name the next action. Human review is mandatory before sharing estimates with clients.
