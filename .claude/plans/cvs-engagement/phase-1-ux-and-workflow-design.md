# Phase 1: Business Workflow and UX Design

Use ultrathink for this phase. Engage extended reasoning before every major output.

Perform deep web research using WebSearch before making any design claims. Cite all sources with URLs. Cross-validate across multiple sources.

## Objective

Design the user experience and business workflow layer for CVS Health's Legacy System Transformation. This phase produces a UX design document that addresses the **Human-Centered Design (HCD)** key consideration and informs the technical architecture in Phase 2. It leverages Paul's Cognitive Science background as a genuine differentiator.

**Interview depth target**: HCD is one of the 3 interview deep-dive topics — a dedicated 45-minute interview will focus on HCD and Change Management. The UX design document must sustain 45 minutes of HCD-focused questioning from a UX leader or organizational change specialist.

**Produces**:
1. A comprehensive UX design document with personas, journey maps, wireframe descriptions, and design principles
2. Workflow mapping from green screen to modern UI patterns
3. Accessibility and usability strategy

This is a design document phase — no KB skill invocations. The output feeds directly into Phase 2 (architecture) and Phase 6 (assembly).

## Input Dependencies

- `outputs/cvs-legacy-transformation/research-findings.md` — Phase 0 research (especially Clusters 5, 6, 7, 9)
- `outputs/cvs-legacy-transformation/honesty-map.md` — Paul's experience mapping
- `knowledge_base/requirements.json` — requirements from Phase 0

## Prior Phase Context

Read ALL completed phase context summaries before executing:
- `.claude/plans/cvs-engagement/context/phase-*-context.md`

Adapt this plan based on findings, corrections, and insights from prior phases. Pay special attention to:
- Phase 0's research on HCD in healthcare IT (Cluster 5)
- Phase 0's PBM domain knowledge (Cluster 7)
- Phase 0's green screen user adoption research (Cluster 6)
- Any corrections to assumptions about CVS's user base

## Context Files

**Paul's Brand and Voice** (base: `C:\dev\paulprae-com`):
- `data/sources/knowledge/brand/identity.json` — brand identity
- `data/sources/knowledge/brand/communication-styles.json` — communication styles
- `data/sources/knowledge/brand/values.json` — values
- `data/generated/career-data.json` — for Cognitive Science background and UX-relevant experience

**Agent Config**:
- `.claude/rules/guiding-principles.md` — principles 1-8 (Human-Centered), 10 (KISS), 17 (Ship)

**Assignment**:
- `.claude/plans/references/solution-architect-case-study-and-interview.md` — HCD requirements

## Research Directives

### Cluster 1: Green Screen to Modern UI Patterns
- `green screen terminal emulation to web UI migration UX patterns`
- `AS/400 5250 screen scraping vs API modernization UX`
- `legacy terminal to responsive web design healthcare`

### Cluster 2: Healthcare Pharmacy UX Best Practices
- `pharmacy workflow UX design best practices`
- `clinical pharmacist user interface design patterns`
- `healthcare worker efficiency UX design keyboard shortcuts power users`

### Cluster 3: Accessibility in Healthcare Applications
- `WCAG 2.2 healthcare application accessibility requirements`
- `Section 508 compliance healthcare IT systems`
- `accessible design pharmacy benefits management applications`

### Cluster 4: CVS Health Brand and Design Language
- `CVS Health brand guidelines design system`
- `CVS Health digital experience mobile app design`
- `CVS Health accessibility commitment digital platforms`

### Cluster 5: Progressive Disclosure and Power User Patterns
- `progressive disclosure enterprise application design`
- `power user shortcuts enterprise web application green screen migration`
- `keyboard navigation enterprise application accessibility`

## Execution Steps

### Step 1: Read All Context and Input Files
Read Phase 0 outputs, Paul's brand files, and the assignment. Focus on:
- The persona types identified in requirements
- The green screen workflows currently in use
- Paul's Cognitive Science background (key differentiator)
- Phase 0's HCD research findings

### Step 2: Execute Web Research
Run research across 3 tiers, prioritized by Paul's knowledge gaps:

_Tier 1 — Must research (Paul doesn't know):_
- Green Screen → Modern UI Patterns: 5250 terminal interaction mapping (F-keys, screen codes, keyboard-only nav) to web UI equivalents. 4 queries.
- CVS Health Brand/Design Language: CVS Health App UI, digital accessibility commitments, any public design system references. 4 queries.

_Tier 2 — Research to ground (Paul knows principles, needs pharmacy-specific application):_
- Pharmacy UX Best Practices: Pharmacy workflow patterns, clinical pharmacist UI, power-user keyboard patterns for PBM. 3 queries.
- Progressive Disclosure + Power User Patterns: Enterprise command palette patterns, green-screen-to-web power user migration. 2 queries.

_Tier 3 — Light verification (Paul has direct knowledge):_
- Accessibility: WCAG 2.2 updates (not 2.1), Section 508 healthcare-specific, ONC SED mandates. 2 queries.

Total: ~15 queries (focused on gaps, not fundamentals Paul already knows).

### Step 3: Define User Personas
Create 5 personas mapped to PBM workflows from Phase 0 research (reduced from "4-6" to a focused set that covers all PBM workflow types):
- **Claims Processor** — high-volume, speed-critical, keyboard-centric user
- **Pharmacist** — clinical decision-maker, needs quick data access
- **Benefits Analyst** — analytical, report-oriented, needs data visualization
- **IT Administrator** — system management, user provisioning, audit review
- **Business Analyst / Manager** — dashboards, KPIs, exception handling
- **New Hire / Trainee** — learning the system, needs guided workflows

For each persona: name, role, daily workflow, pain points with current green screen, goals, technical proficiency, accessibility needs.

### Step 4: Map Current-State Green Screen Workflows
Document representative green screen workflows (based on research, since we don't have access to actual screens):
- Claims adjudication flow
- Member eligibility lookup
- Pharmacy benefits verification
- Prior authorization processing
- Formulary management

For each workflow: current steps, screen count, keyboard commands, typical completion time, error-prone areas.

### Step 5: Design Future-State UX Patterns
For each workflow, design the modern UI equivalent:

**Design Principles** (grounded in Paul's Cognitive Science background):
1. **Cognitive Load Reduction** — progressive disclosure, sensible defaults, contextual help
2. **Efficiency Preservation** — keyboard shortcuts, command palette, quick actions (green screen users are FAST)
3. **Recognition Over Recall** — visual cues, status indicators, breadcrumbs replace memorized screen codes
4. **Error Prevention** — inline validation, confirmations for destructive actions, undo capability
5. **Dual-Mode Interface** — support both keyboard-power-user and mouse-discovery modes
6. **Consistent Mental Models** — map green screen concepts to modern equivalents predictably

**Pattern Library** (describe, not implement):
- Command palette (Ctrl+K style) for green screen-trained users
- Dashboard layouts with customizable widgets
- Split-pane views for comparison workflows
- Contextual side panels for related data
- Progressive form wizards for complex transactions
- Real-time validation and inline feedback
- Responsive design for tablet/mobile (future state)

### Step 6: Create Journey Maps
Create journey maps for 2-3 critical workflows showing:
- Stages: awareness → learning → daily use → mastery
- Touchpoints at each stage
- Emotional state / friction points
- Support needs
- Success metrics

### Step 7: Write UX Design Document
Write to: `outputs/cvs-legacy-transformation/ux-design-document.md`

Structure:
```markdown
# UX Design Document — CVS Legacy Transformation

## 1. Design Philosophy
[Grounded in Paul's Cognitive Science background — cite specific principles]

## 2. User Personas
[4-6 detailed personas]

## 3. Current-State Workflow Analysis
[Green screen workflow documentation]

## 4. Design Principles
[6 principles with cognitive science grounding]

## 5. Future-State UX Patterns
[Pattern library with rationale]

## 6. Journey Maps
[2-3 critical workflow journey maps]

## 7. Accessibility Strategy
[WCAG 2.2, Section 508, keyboard navigation]

## 8. Usability Testing Plan
[Methods: think-aloud, A/B testing, analytics-driven iteration]

## 9. Design System Recommendations
[Component library approach, CVS brand alignment]

## 10. Transition Design
[How to ease users from green screen to modern UI — bridges to Change Management]
```

### Step 8: Create Wireframe Descriptions
For 2-3 key screens, write detailed wireframe descriptions (textual, not graphical) that a designer could implement. Include:
- Layout structure (header, sidebar, main content, footer)
- Component placement and hierarchy
- Interaction patterns (click, keyboard, gesture)
- Data density and progressive disclosure approach
- Responsive breakpoints

## Honesty Rules

1. **Cognitive Science background** → Paul's genuine differentiator. Cite his degree and how it informs each design principle. This is a strength area.
2. **Green screen workflows** → researched, not firsthand. Label as: "Based on IBMi/AS/400 workflow research and industry patterns..."
3. **UX design experience** → map to Paul's actual projects from career-data.json
4. **CVS-specific design** → assumptions based on public information. Flag as: "Assumption A-1-NNN: CVS uses [pattern], based on [source]"
5. **Accessibility claims** → cite WCAG 2.2 and Section 508 standards directly
6. **Usability testing** → reference established methods (Nielsen, Krug), not invented approaches

## Quality Gate

- No formal `/review` for this phase (design document, not KB artifact)
- Self-review against these criteria:
  - [ ] Every design principle has cognitive science or established UX research grounding
  - [ ] Personas are realistic for PBM domain (validated against Phase 0 research)
  - [ ] Green screen workflow analysis is sourced, not invented
  - [ ] Accessibility strategy meets WCAG 2.2 AA minimum
  - [ ] Transition design bridges to Change Management (Phase 4)
  - [ ] Paul's voice is collaborative, solution-focused, empirical, and warm
  - [ ] Document score self-assessment >= 7.5/10
  - [ ] UX design document provides sufficient depth for a 45-minute HCD-focused interview

## Exit Criteria

Before proceeding to Phase 2:
- [ ] UX design document written with all 10 sections
- [ ] 4-6 personas defined with PBM-relevant workflows
- [ ] 2-3 wireframe descriptions detailed enough for a designer
- [ ] Accessibility strategy documented
- [ ] Design principles grounded in Cognitive Science
- [ ] Transition design section bridges to Change Management
- [ ] All assumptions numbered (A-1-NNN series)

## Context Handoff

After execution completes, save context for future phases:

1. **Write context summary** to `.claude/plans/cvs-engagement/context/phase-1-context.md` using the Context Summary Template (see master-plan.md)

2. **Update ALL remaining phase plan files** with:
   - Persona details that Phase 2 needs for architecture decisions (e.g., claims processor needs < 200ms response)
   - UX patterns that influence Phase 2's technology stack selection (e.g., command palette requires WebSocket)
   - Accessibility requirements that Phase 3 needs for IAM (e.g., screen reader compatible auth flows)
   - Transition design insights that Phase 4 needs for change management planning
   - Design principles and voice guidelines that Phase 6 needs for document assembly
   - Any new assumptions discovered during design

3. **Update master-plan.md** if any structural changes to the engagement

4. **Commit** all context and plan updates to git with message: `docs(plans): complete Phase 1 UX design, update future plans`

## Human Checkpoint

Paul: review the following before proceeding to Phase 2:
- UX design document: `outputs/cvs-legacy-transformation/ux-design-document.md`
  - Do the design principles authentically reflect your Cognitive Science training?
  - Are the personas realistic for the PBM domain?
  - Does the dual-mode interface (keyboard + mouse) approach resonate?
  - Is the transition design approach sound for resistant green screen users?
- Does the document voice feel like Paul's voice? (collaborative, empirical, warm)
- Any design patterns you want to add or remove?
- Updated future phase plans (review changes from this phase's learnings)
- Context summary accuracy
