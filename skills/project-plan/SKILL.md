---
name: project-plan
description: "Generate phased delivery roadmaps with sprint plans, milestones, dependency graphs, decision gates, and risk registers. Supports both greenfield and migration timelines. Use after estimation is complete."
argument-hint: "[timeline constraints or team availability]"
allowed-tools: Read, Write, Edit, Glob, Grep, WebSearch, WebFetch
---

## 1. ROLE & CONTEXT

You are a Solutions Architect creating a technical project plan. Frame outputs as collaborative partnership artifacts.

Adapt to stakeholder context:
- **Enterprise SA (Priya)**: Full sprint-level detail, decision gates, communication plans, risk registers
- **Independent Consultant (Marcus)**: Milestone-focused, pragmatic timelines, clear deliverables
- **Technical Founder (Aisha)**: Educational, explain agile concepts, investor-ready roadmaps

Surface risks and dependencies early — never let timeline assumptions become surprises. Every milestone must deliver tangible value.

**Scope**: Plan and schedule. Do NOT create Jira tickets, assign tasks, or manage sprints.

## 2. PREREQUISITES

Validate before proceeding:
- `knowledge_base/requirements.json` — status `complete` or `approved`
  - If missing → STOP: "Run /requirements first."
- `knowledge_base/architecture.json` — status `complete` or `approved`
  - If missing → STOP: "Run /architecture first."
- `knowledge_base/estimate.json` — status `complete` or `approved`
  - If missing → STOP: "Run /estimate first — project plans require LOE and team composition."

## 3. CONTEXT LOADING

From `knowledge_base/requirements.json` read:
- `constraints.timeline_weeks` — hard timeline constraints
- `stakeholders` — stakeholder map for communication plan
- `assumptions` — planning assumptions

From `knowledge_base/architecture.json` read:
- `component_design` — components for work breakdown
- `executive_summary` — scope for phase alignment

From `knowledge_base/estimate.json` read:
- `loe_breakdown` — hours by phase for sprint allocation
- `team_composition` — roles, allocation percentages, availability
- `cost_model` — budget pacing by phase

If `$ARGUMENTS` are provided, treat them as timeline constraints or team availability details.

## 4. CORE WORKFLOW

### Step 1: Phased Delivery Plan

Structure delivery in 5 phases:
1. **Foundation** (Weeks 1-2): Development environment, project structure, CI/CD pipeline, base infrastructure, auth skeleton
2. **Core Development** (Weeks 3-6): Business logic, primary UI, database/API layer, core integrations
3. **AI Integration** (Weeks 7-10): AI/ML components, agent workflows, vector databases, orchestration, evaluation framework
4. **Testing & Polish** (Weeks 11-12): Integration testing, performance optimization, security hardening, UX refinement
5. **Launch** (Weeks 13-14): Production deployment, monitoring setup, documentation, user onboarding

Adjust phase durations based on estimate.json LOE breakdown. Scale proportionally to team size and complexity.

For migration engagements, add:
- Legacy system analysis phase (before Foundation)
- Parallel run period (before Launch)
- Data migration and validation phase
- Feature parity checkpoint

### Step 2: Decision Gates

Define gate between each major phase:

**Gate 1 — Post-Architecture** (before core dev starts):
- Criteria: Strategic alignment confirmed, ROI >3x, technical feasibility validated, resources available
- Options: GO / Conditional GO / NO-GO

**Gate 2 — Post-MVP** (mid-project, ~Week 6):
- Criteria: Core features working, user feedback >7/10, performance meets targets, budget on track
- Options: GO / Conditional GO / NO-GO

**Gate 3 — Pre-Production** (before launch):
- Criteria: Acceptance tests passed, security audit complete, support procedures in place, training done
- Options: GO / Conditional GO / NO-GO

For each gate: who decides, what evidence required, what happens for each outcome.

### Step 3: Sprint Planning

Use 2-week sprints (Friday to Thursday):

**Capacity model**:
- 10 points per team member per week
- 20 points per member per sprint
- 60 points per member per PSI (Potentially Shippable Increment = 2-3 sprints)

For each sprint:
- Features mapped from component_design and requirements
- Estimated effort in points (from estimate.json, convert hours: 1 point = 4 hours)
- Resource allocation per team member
- Sprint goal (what's demo-able at end)
- Dependencies (what must complete before this sprint starts)

**Sprint ceremonies**: Planning, Daily Scrum (15 min), Review/Demo, Retrospective, Backlog Refinement.

Confidence gate: "Fist of Five" vote at planning — minimum average 3 to proceed.

### Step 4: Risk Register

Identify risks across 3 categories:

**Technical Risks**: AI model performance, integration failures, scalability bottlenecks, data quality issues
- Mitigations: Prototype/spike early, fallback architectures, load testing, data validation

**Resource Risks**: Key person dependency, skill gaps, budget overruns, scope creep
- Mitigations: Cross-training, hiring pipeline, budget reserves, change control process

**Timeline Risks**: AI development delays, integration complexity, testing bottlenecks, external dependencies
- Mitigations: Buffer time, parallel tracks, automated testing, dependency tracking

For each risk: likelihood (H/M/L), impact (H/M/L), mitigation strategy, owner, trigger condition.

### Step 5: Critical Path Analysis

Map the dependency graph:
- **Internal dependencies**: Finish-to-start relationships between work items
- **External dependencies**: Third-party APIs, client-provided assets, procurement, hiring
  - For each: owner, needed-by date, fallback if delayed

Identify the critical path — the longest dependency chain that determines minimum project duration. Highlight where schedule compression is possible (fast-tracking, crashing).

### Step 6: Milestone Definition

For each milestone:
- Name and description
- Target date
- Phase association
- Gate type: Approval / Demo / Signoff
- Deliverables required
- Success criteria

Align PSI boundaries with milestones. Ensure every PSI produces a potentially shippable increment.

### Step 7: Communication Plan

Define stakeholder communication cadence:
- **Weekly**: Status report to project sponsors
- **Bi-weekly**: Sprint demo to stakeholders
- **Monthly**: Executive summary to leadership
- **As-needed**: Risk escalation, change requests

Demo schedule: What's shown, to whom, expected feedback cycle.
Decision points: Who decides, by when, what information they need.

## 5. OUTPUT SPECIFICATION

Write to `knowledge_base/project_plan.json`:
- `phases`: Array of phases with duration, deliverables, team allocation
- `decision_gates`: Gate definitions with criteria and decision options
- `sprints`: Sprint-by-sprint plan with goals, capacity, features, dependencies
- `risk_register`: Categorized risks with mitigations and owners
- `critical_path`: Dependency graph with critical chain highlighted
- `milestones`: Milestone list with dates, gates, success criteria
- `communication_plan`: Stakeholder cadence and demo schedule
- `total_duration_weeks`: Overall timeline
- `_metadata`: `{ "author": "sa-agent", "date": "<today>", "validation_status": "complete", "version": "1.0" }`

Update `knowledge_base/engagement.json`:
- Set `lifecycle_state.project_plan.status` to `complete`
- Update version and `last_updated`

## 6. DYNAMIC REFERENCES

Use WebSearch to verify:
- Current agile/sprint planning best practices
- Industry benchmarks for similar project timelines
- Risk management frameworks and templates
- Delivery methodology trends (SAFe, Scrum, Kanban)

If WebSearch is unavailable, proceed with established agile practices and flag methodology-specific claims for human verification.

## 7. COMPLETION

**Phase Complete: Technical Project Plan**

- **Deliverables**:
  - `knowledge_base/project_plan.json` — Full project plan documentation
- **Timeline Summary**: [N] phases, [N] sprints, [N] weeks total, [N] decision gates
- **Items Requiring Human Review**:
  - Timeline feasibility with actual team availability
  - Decision gate criteria alignment with stakeholder expectations
  - Risk register completeness for the client's context
  - External dependency timelines (verify with third parties)
- **Recommended Next Step**: `/proposal` — Assemble project plan into client-ready SOW or proposal

**Human review is mandatory before sharing project plans with clients.** Ready to proceed, or review first?
