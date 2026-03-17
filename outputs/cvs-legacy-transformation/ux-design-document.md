# UX Design Document — CVS Health Legacy System Transformation

> **Engagement**: eng-2026-001 | CVS Health IBMi Green Screen UI/UX Modernization
> **Phase**: 1 — Business Workflow and UX Design
> **Author**: Paul Prae (Modular Earth LLC)
> **Date**: 2026-03-16
> **Status**: COMPLETE

---

## 1. Design Philosophy

This design approach is grounded in my academic training in **Cognitive Science with a focused foundation in Artificial Intelligence** (University of Georgia) and formal **Human-Computer Interaction (HCI) coursework**, combined with 6+ UX projects spanning healthcare, conversational AI, and enterprise applications.

The central insight from cognitive science that drives this design: **users don't adapt to interfaces — interfaces must adapt to users' existing mental models**. For CVS Health's green screen transformation, this means we cannot simply replace 5250 terminal screens with web forms. We must understand how pharmacy benefits staff have built expertise around the green screen paradigm — memorized screen codes, F-key sequences, spatial memory of data layouts — and create a modern UI that **preserves their expertise while eliminating their pain points**.

This is not an interface replacement. It is a **cognitive bridge** — a system that meets expert users where they are while opening the door to modern interaction patterns for new hires.

### Design Values

| Value | Meaning | Cognitive Science Basis |
|-------|---------|------------------------|
| **Preserve expertise** | Expert users should feel faster on day one, not slower | Skill acquisition theory — experts have automated schemas that must be respected |
| **Eliminate memorization** | Screen codes, F-key combinations, and cryptic commands become discoverable | Recognition over recall (Nielsen's heuristic #6) |
| **Reduce errors, not speed** | Target the 40% error reduction; don't compromise sub-second workflows | Error prevention via inline validation vs. submit-and-get-error-code pattern |
| **Dual-mode always** | Keyboard-first for experts, mouse-discoverable for learners | Dreyfus model — novice and expert need different interaction patterns simultaneously |
| **Evidence-based iteration** | Every design decision testable; usability testing is mandatory, not optional | ONC Safety-Enhanced Design mandates summative usability testing |

---

## 2. User Personas

Five personas mapped to PBM workflows identified in Phase 0 research. Each persona represents a distinct interaction pattern with the modernized system.

### Persona 1: Maria Torres — Claims Processor

| Attribute | Detail |
|-----------|--------|
| **Role** | Senior Claims Processor, CVS Caremark |
| **Experience** | 12 years on green screen; processes 200+ claims per shift |
| **Workflow** | Real-time claims adjudication via NCPDP B1 transactions |
| **Technical Proficiency** | Expert green screen user — memorized 40+ screen codes, uses F-keys without looking |
| **Performance Requirement** | Sub-second response (P95 ≤ 500ms); any latency increase is unacceptable (A-0-010) |
| **Pain Points** | Cannot see member history and current claim simultaneously (requires screen-switching); cryptic error codes require lookup; new hires slow the team for 6-8 weeks |
| **Goals** | Maintain or improve speed; fewer errors; help train new staff faster |
| **Accessibility Needs** | Keyboard-only navigation is a requirement (RSI from years of keyboard use); high-contrast display for extended screen time |
| **Change Resistance** | **HIGH** — "I'm faster on the green screen." Must demonstrate speed parity on day one. |

**Design Implications**: Split-pane views for member + claim context. Command palette (Ctrl+K) mapping to memorized screen codes. Keyboard shortcuts for every action. Zero mouse dependency for core workflows. Performance budget: 200ms UI render + 300ms API response = 500ms total.

### Persona 2: Dr. James Chen — Clinical Pharmacist

| Attribute | Detail |
|-----------|--------|
| **Role** | Clinical Pharmacist, Formulary and DUR Review |
| **Experience** | 8 years; splits time between green screen and clinical reference tools |
| **Workflow** | Drug Utilization Review (DUR), formulary management, Prior Authorization review |
| **Technical Proficiency** | Moderate green screen proficiency; strong with clinical databases and reference tools |
| **Performance Requirement** | Clinical data must load within 2 seconds; DUR alerts must be real-time |
| **Pain Points** | Context-switching between green screen and external clinical references; PA reviews require manual comparison of medical history against policy guidelines; DUR alerts are text-only with no severity hierarchy |
| **Goals** | Inline clinical data during DUR review; GenAI-assisted PA recommendations; severity-coded DUR alerts |
| **Accessibility Needs** | Color-coded clinical alerts must also have text/icon differentiation (color blindness consideration) |
| **Change Resistance** | **MODERATE** — Open to better tools if they don't slow clinical workflow. |

**Design Implications**: Contextual side panels for drug monographs and interaction data. GenAI recommendation panel for PA workflows (FR-006). Severity-coded DUR alerts with both color AND icon/text indicators. Progressive disclosure: summary view → full clinical detail on demand.

### Persona 3: Angela Washington — Benefits Analyst

| Attribute | Detail |
|-----------|--------|
| **Role** | Benefits Analyst, PBM Client Services |
| **Experience** | 5 years; works across green screen and myPBM portal |
| **Workflow** | Plan configuration, benefits verification, reporting, client support |
| **Technical Proficiency** | Moderate; comfortable with both green screen and modern web tools (myPBM) |
| **Performance Requirement** | Report generation acceptable within 5-10 seconds; plan lookups within 2 seconds |
| **Pain Points** | Green screen reports are text-only with no data visualization; plan configuration requires navigating 8-12 screens sequentially; cannot compare plan configurations side by side |
| **Goals** | Visual data dashboards; streamlined plan configuration wizard; side-by-side plan comparison |
| **Accessibility Needs** | Standard WCAG AA compliance |
| **Change Resistance** | **LOW** — Already uses myPBM; would welcome consistent UX across tools. |

**Design Implications**: Dashboard with data visualization widgets. Progressive form wizard for plan configuration (replacing 8-12 screen navigation). Split-pane comparison views. Design language consistent with myPBM (Azure-hosted client portal) to reduce cognitive switching.

### Persona 4: Raj Patel — IT Administrator

| Attribute | Detail |
|-----------|--------|
| **Role** | IT Systems Administrator, PBM Operations |
| **Experience** | 7 years; manages IBMi user profiles and system access |
| **Workflow** | User provisioning, access reviews, audit log review, system monitoring |
| **Technical Proficiency** | High; works in both IBMi and modern cloud environments |
| **Performance Requirement** | Provisioning completion within minutes (current: manual, takes hours) |
| **Pain Points** | IBMi user profile management is manual and slow; audit log review is text-based grep on green screen; no centralized IAM dashboard across IBMi + modern systems |
| **Goals** | Unified IAM dashboard; automated provisioning; visual audit log review with search and filtering |
| **Accessibility Needs** | Standard WCAG AA compliance |
| **Change Resistance** | **LOW** — Actively wants modernization; frustrated by manual processes. |

**Design Implications**: IAM bridge persona — this persona's needs directly inform Phase 3 (Security & IAM). Unified dashboard showing IBMi + cloud user profiles during transition. Self-service provisioning with approval workflows. Audit log viewer with search, filter, and export capabilities. This persona validates whether auth flows are accessible and efficient.

### Persona 5: Sofia Martinez — New Hire / Trainee

| Attribute | Detail |
|-----------|--------|
| **Role** | Claims Processing Trainee (first 90 days) |
| **Experience** | Recent college graduate; no green screen experience; familiar with modern web applications |
| **Workflow** | Learning claims adjudication, eligibility verification, basic member lookup |
| **Technical Proficiency** | High with modern web applications; zero terminal experience |
| **Performance Requirement** | Achieve independent task completion within 10 days (current: 6-8 weeks on green screen) |
| **Pain Points** | On current system: must memorize screen codes, F-key sequences, and cryptic abbreviations before processing a single claim; no inline help; errors are cryptic codes requiring senior staff to decode |
| **Goals** | Guided workflows with contextual help; learn by doing, not memorizing; self-serve error resolution |
| **Accessibility Needs** | Standard WCAG AA compliance; may need internationalization (i18n) support |
| **Change Resistance** | **NONE** — Has never used the green screen; represents the future workforce. |

**Design Implications**: Change management bridge persona — this persona validates onboarding time reduction (SC-001: 42 days → 10 days). Guided workflows with step indicators. Contextual tooltips and inline documentation. Error messages in plain language with suggested resolution. Dual-mode interface: Sofia uses mouse-discovery mode initially, transitions to keyboard shortcuts as expertise grows. Training analytics: track time-to-competency to validate SC-001.

---

## 3. Current-State Workflow Analysis

Based on IBMi/AS/400 workflow research and industry patterns for PBM green screen applications. All workflow descriptions are researched, not firsthand — Paul has no direct green screen experience (Honesty Map: IBMi 2/5).

### Workflow 1: Claims Adjudication (Flagship — FR-004)

**Criticality**: Highest. Sub-second latency non-negotiable (A-0-010). 99%+ claims adjudicated electronically at POS.

| Step | Green Screen Action | Estimated Screens | Keyboard Commands |
|------|-------------------|-------------------|-------------------|
| 1. Receive claim | NCPDP B1 transaction arrives; claim populates adjudication screen | 1 | Auto-populated |
| 2. Member verification | Enter member ID; system returns eligibility and plan details | 1-2 | Tab, Enter, F-key to navigate |
| 3. Drug lookup | Enter NDC (National Drug Code); system returns formulary status | 1 | Tab, Enter |
| 4. DUR screening | System performs automated drug utilization review; alerts display as text codes | 1 | Review text alerts; F-key to override or accept |
| 5. UM check | Prior authorization, step therapy, quantity limit checks | 1-2 | F-key to proceed or pend |
| 6. Pricing | System calculates copay/coinsurance based on network contracts | 1 | Auto-calculated |
| 7. Adjudication decision | Approve/deny/pend with reason codes | 1 | F-key to submit |
| 8. Response | Result transmitted back to pharmacy POS | 0 | Auto-transmitted |

**Estimated Total**: 6-8 screens, 15-25 keystrokes, 3-8 seconds per claim (expert user)

**Pain Points** (labeled as RESEARCHED):
- **No contextual view**: Member history and current claim cannot be viewed simultaneously — requires F-key screen-switching
- **Cryptic DUR alerts**: Drug interaction alerts are text codes (e.g., "DD 03") requiring lookup in a separate reference
- **Error codes**: Rejection reasons are numeric codes (e.g., "70" = Product/Service Not Covered) — no plain-language explanation
- **No undo**: Incorrect adjudication requires a reversal claim (separate process), not a simple undo
- **Training burden**: New processors memorize 40+ screen codes and 24 F-key functions before processing independently

**Performance Baseline**: Sub-second for routine claims (A-0-010). Complex claims with DUR alerts may take 5-15 seconds of human review time.

### Workflow 2: Prior Authorization (High Complexity — FR-006)

**Criticality**: High. Multiple decision points. GenAI dual-competency demonstration target.

| Step | Green Screen Action | Estimated Screens | Keyboard Commands |
|------|-------------------|-------------------|-------------------|
| 1. PA request intake | Provider submits PA via fax, phone, or portal | 1 | Manual entry or auto-populated |
| 2. Member lookup | Verify member eligibility and benefits for requested medication | 2-3 | Tab, Enter, F-keys |
| 3. Clinical review | Pharmacist reviews medical history, diagnosis codes, prior medications | 3-5 | F-key navigation between history screens |
| 4. Policy lookup | Check formulary status, step therapy requirements, PA criteria | 2-3 | F-key to reference screens |
| 5. Decision | Approve, deny, or request more information | 1 | F-key to submit decision |
| 6. Notification | Generate approval/denial letter with rationale | 1 | Auto-generated text template |

**Estimated Total**: 10-15 screens, 30-50 keystrokes, 5-20 minutes per PA (depending on complexity)

**Pain Points** (labeled as RESEARCHED):
- **Massive context-switching**: Pharmacist navigates 10-15 screens of member history, diagnosis codes, medication records, and policy documents across multiple green screen views
- **No intelligent pre-screening**: Every PA gets the same manual review process regardless of straightforward vs. complex cases
- **Manual document comparison**: Pharmacist manually cross-references medical history against policy guidelines — the exact use case for GenAI assistance (FR-006)
- **Processing time**: Standard PA cases take days due to manual review queue — GenAI target is minutes for straightforward cases

**GenAI Opportunity**: This workflow is the primary target for AI-assisted decision support. An LLM can analyze medical history, policy guidelines, and clinical evidence to generate PA recommendations for pharmacist review — human-in-the-loop required (FR-006 acceptance criteria).

### Workflow 3: Member Eligibility Lookup (High Frequency — First Strangler Fig Candidate)

**Criticality**: Moderate (not safety-critical). But highest frequency and simplest workflow — ideal first migration candidate.

| Step | Green Screen Action | Estimated Screens | Keyboard Commands |
|------|-------------------|-------------------|-------------------|
| 1. Search | Enter member ID, name, or SSN | 1 | Tab, Enter |
| 2. Results | System returns member details: plan, group, coverage dates, copay structure | 1-2 | F-key to navigate detail screens |
| 3. Coverage check | View covered medications, excluded drugs, PA requirements | 1-2 | F-key to formulary reference |
| 4. History | View claims history, PA history, coverage changes | 1-2 | F-key navigation |

**Estimated Total**: 3-6 screens, 10-15 keystrokes, 15-30 seconds

**Pain Points** (labeled as RESEARCHED):
- **Multiple screens for one member**: Member demographics, coverage details, and claims history are on separate green screens requiring F-key navigation
- **No search flexibility**: Member lookup requires exact ID match — no partial name search, no fuzzy matching
- **No visual summary**: All data is text-only; no visual timeline of coverage or claims

**Why First Strangler Fig Candidate**: Low risk (read-only operations, no adjudication), high visibility (used by all personas), simple API surface (member lookup maps cleanly to REST endpoints), fast validation (easy to compare green screen output with API output via GCP Dual Run).

---

## 4. Design Principles

Six design principles grounded in cognitive science theory. Each principle draws from Paul's Cognitive Science academic training and UX project experience.

### Principle 1: Cognitive Load Reduction

**Cognitive Science Grounding**: Hick's Law states that decision time increases logarithmically with the number of options. Miller's Law (7±2) establishes working memory capacity limits. Green screen users face both: dozens of F-key options and screens packed with 1,920 characters (80 columns × 24 rows) of undifferentiated text.

**Application to CVS Modernization**:
- **Progressive disclosure**: Replace 80×24 character screens with layered information architecture — summary view first, detail on demand
- **Sensible defaults**: Pre-populate fields based on claim context (member plan, common medications) to reduce keystrokes
- **Visual hierarchy**: Use typography, spacing, and color to create information hierarchy that green screens cannot provide
- **Contextual help**: Inline tooltips replace the "look up the error code in the manual" pattern

**Measurable Target**: 40% reduction in data entry errors (SC-002); training time from 42 days to 10 days (SC-001)

**Sources**: Hick, W.E. (1952). On the rate of gain of information. *Quarterly Journal of Experimental Psychology*, 4(1), 11-26. Miller, G.A. (1956). The magical number seven, plus or minus two. *Psychological Review*, 63(2), 81-97.

### Principle 2: Efficiency Preservation

**Cognitive Science Grounding**: Fitts's Law predicts that the time to move to a target is a function of target size and distance. For keyboard users, this means keyboard shortcuts (zero distance) will always outperform mouse targets. Green screen power users like Maria Torres have optimized their workflows to near-zero cognitive overhead through muscle memory — we must not destroy this.

**Application to CVS Modernization**:
- **Keyboard shortcuts for every action**: No action should require mouse-only interaction
- **Command palette (Ctrl+K)**: Maps directly to the green screen mental model — type a code, get a result. Instead of memorizing "SC04" for member lookup, type "member" and fuzzy-match
- **Tab-order optimization**: Form tab order mirrors the claims adjudication workflow sequence
- **Shortcut discovery**: Keyboard shortcuts displayed alongside menu items (like VS Code, Figma) — power users see them, learners discover them

**Measurable Target**: Expert users achieve speed parity within 1 week of transition; no degradation in claims-per-hour metrics

### Principle 3: Recognition Over Recall

**Cognitive Science Grounding**: Nielsen's usability heuristic #6 and schema theory from cognitive psychology. Recognition memory is fundamentally stronger than recall memory — humans can recognize thousands of items they cannot freely recall. Green screens demand recall: memorize 40+ screen codes, 24 F-key functions, and hundreds of error codes.

**Application to CVS Modernization**:
- **Visual navigation**: Breadcrumbs, sidebar navigation, and search replace memorized screen codes
- **Status indicators**: Visual badges for claim status (approved = green, denied = red, pended = yellow) replace numeric status codes
- **Autocomplete**: Medication search with autocomplete replaces typing exact NDC codes from memory
- **Contextual menus**: Right-click or action menus show available operations for the current context — no need to remember which F-key does what on which screen

**Measurable Target**: New hire onboarding time reduced by 80% (SC-001: 42 days → 10 days) — the biggest single metric demonstrating recognition-over-recall effectiveness.

### Principle 4: Error Prevention

**Cognitive Science Grounding**: Reason's taxonomy of human error distinguishes between slips (execution errors in routine tasks) and mistakes (planning errors from misunderstanding). Green screens are slip-prone: one wrong keystroke in a 15-keystroke sequence can adjudicate a claim incorrectly. They are also mistake-prone: cryptic codes provide no feedback about what went wrong or why.

**Application to CVS Modernization**:
- **Real-time inline validation**: Validate NDC codes, member IDs, and coverage dates as entered — not after submission (replacing the "submit and get error code" pattern)
- **Confirmation for high-impact actions**: Claims adjudication denial requires explicit confirmation with plain-language summary of what will happen
- **Undo capability**: Reversible actions can be undone within a grace period (claim reversal becomes "undo" within 30 seconds, not a separate multi-step process)
- **Plain-language errors**: "This medication is not covered under the member's current plan (Formulary Tier: Excluded). Alternatives: [list]" replaces "Rejection Code: 70"

**Measurable Target**: 40% reduction in data entry errors (SC-002)

**Sources**: Reason, J. (1990). *Human Error*. Cambridge University Press.

### Principle 5: Dual-Mode Interface

**Cognitive Science Grounding**: The Dreyfus model of skill acquisition describes five stages: novice, advanced beginner, competent, proficient, and expert. A single interface must serve users at all stages simultaneously. Green screens serve only experts. Typical modern UIs serve only novices. The dual-mode interface serves both.

**Application to CVS Modernization**:
- **Mouse-discovery mode** (default for new users): Visible buttons, menus, and tooltips guide the user through workflows
- **Keyboard-power mode** (for expert users): Command palette, keyboard shortcuts, and tab-order navigation enable green-screen-speed workflows
- **Progressive transition**: As users gain expertise, they naturally discover keyboard shortcuts (shown alongside UI elements) and shift from mouse to keyboard
- **No mode switching**: Both modes are always active — an expert can use keyboard shortcuts while a trainee sitting beside them uses the mouse. No toggle, no configuration.

**Measurable Target**: Claims processor journey from mouse-discovery (week 1) to keyboard-power (month 3) to full proficiency (month 6+) — see Journey Maps in Section 6.

**Sources**: Dreyfus, S.E. & Dreyfus, H.L. (1980). A five-stage model of the mental activities involved in directed skill acquisition. *Operations Research Center, University of California, Berkeley*.

### Principle 6: Consistent Mental Models

**Cognitive Science Grounding**: Mental model theory (Johnson-Laird, 1983) and schema theory explain how humans construct internal representations of how systems work. Green screen users have deeply embedded mental models: "screen SC04 shows member details," "F3 goes back," "F12 cancels." The modernized UI must map these mental models to new interaction patterns predictably — not randomly.

**Application to CVS Modernization**:
- **Screen code → URL mapping**: SC04 (member lookup) maps to `/members/{id}` — bookmarkable, shareable, consistent
- **F-key → shortcut mapping**: F3 (back) → Escape or Backspace; F12 (cancel) → Escape; F5 (refresh) → F5 (same!)
- **Consistent information layout**: Member ID always appears in the same position across all screens — preserving the spatial consistency green screen users rely on
- **Terminology preservation**: Use the same field names and abbreviations that green screen users already know — relabel only where truly ambiguous

**Measurable Target**: User satisfaction (NPS ≥ 7/10 within 6 months — SC-008); adoption rate ≥ 80% within 6 months (SC-004)

**Sources**: Johnson-Laird, P.N. (1983). *Mental Models: Towards a Cognitive Science of Language, Inference, and Consciousness*. Harvard University Press.

---

## 5. Future-State UX Patterns

### Pattern Library

Patterns described conceptually for the solution architecture document. Implementation details deferred to engineering.

#### 5.1 Command Palette (Ctrl+K)

**Purpose**: Bridge pattern between green screen screen codes and modern navigation.

**How It Works**:
- User presses Ctrl+K (or Cmd+K on Mac) — a search overlay appears center-screen
- Type any of: screen code ("SC04"), action ("lookup member"), member ID ("M1234567"), NDC code, or natural language query
- Fuzzy matching returns results instantly — "mem" matches "Member Lookup," "Member History," "Member Eligibility"
- Results grouped by type: Navigation, Actions, Recent, Bookmarks
- Each result shows the keyboard shortcut alongside it (progressive discovery)

**Why This Pattern**:
- Green screen users already think in "type a code → get a result" terms. The command palette is this exact mental model in modern form.
- Research shows command palettes are ideal for "products with a large number of features, complex navigation structures, and power users who rely on keyboard shortcuts" ([Mobbin — Command Palette Design](https://mobbin.com/glossary/command-palette)).
- Used successfully in VS Code (Ctrl+Shift+P), Figma (Ctrl+/), Notion (Ctrl+K), Linear, GitHub, and Superhuman.

**Green Screen Mapping Example**:

| Green Screen Command | Command Palette Equivalent |
|---------------------|---------------------------|
| `SC04` | Type "SC04" or "member" or "eligibility" |
| `F5` (refresh) | Type "refresh" or press F5 |
| `F3` (exit) | Press Escape or type "back" |
| `WRKACTJOB` | Type "active jobs" or "system status" |

#### 5.2 Split-Pane Views

**Purpose**: Eliminate context-switching between green screen pages.

**How It Works**:
- Claims adjudication screen splits into two (or three) resizable panes
- Left pane: member information (demographics, plan, coverage)
- Right pane: current claim details (medication, pricing, DUR alerts)
- Optional bottom pane: claims history timeline

**Why This Pattern**: Green screen users' #1 pain point is navigating between screens to see related data. Maria Torres (Persona 1) currently presses F-keys 8-12 times per claim to view member details and claim data on separate screens. Split-pane eliminates this entirely.

**Responsive Behavior**: On smaller screens, panes stack vertically. On mobile (future state), panes become swipeable tabs.

#### 5.3 Contextual Side Panels

**Purpose**: Progressive disclosure without losing list context.

**How It Works**:
- Viewing a list of claims, PA requests, or formulary entries
- Click/select a row → a side panel slides in from the right showing full details
- The list remains visible on the left — no full-page navigation
- Side panel supports inline editing, status changes, and notes

**Why This Pattern**: Preserves the "list → detail" workflow that power users expect, while keeping the list visible for rapid sequential processing. Dr. Chen (Persona 2) can review PA requests sequentially without navigating away from the queue.

#### 5.4 Real-Time Inline Validation

**Purpose**: Replace the "submit and get error code" pattern.

**How It Works**:
- As users type in form fields, validation occurs in real-time:
  - Member ID: validated against eligibility database as typed (debounced 300ms)
  - NDC code: validated against formulary with autocomplete suggestions
  - Date fields: calendar picker with valid range enforcement
  - Coverage: real-time coverage check as medication is entered
- Validation messages appear inline (below the field), not as modal error dialogs
- Suggestions are offered for common errors: "Did you mean NDC 12345-6789-01?"

**Why This Pattern**: Green screen error handling is batch — submit the form, get an error code, decode the code, fix the field, resubmit. This pattern eliminates an entire cycle of error-submit-decode-fix by catching errors before submission.

#### 5.5 Severity-Coded Clinical Alerts

**Purpose**: Replace undifferentiated text-code DUR alerts with visually prioritized clinical alerts.

**How It Works**:

| Severity | Visual Treatment | Action Required | Example |
|----------|-----------------|-----------------|---------|
| **Critical** | Red banner, icon, sound | Must resolve before proceeding | Severe drug-drug interaction |
| **Warning** | Orange badge, icon | Review recommended; can override with reason | Duplicate therapy detected |
| **Info** | Blue badge, icon | Informational only | Formulary alternative available |

- Each alert shows: severity icon + color (for sighted users), text label (for screen readers), plain-language description, and evidence source
- Critical alerts require explicit acknowledgment before proceeding
- Overrides require reason selection (for audit trail — HIPAA compliance)

**Accessibility Note**: Severity coding uses BOTH color AND icon/text differentiation to accommodate color blindness (WCAG 1.4.1: Use of Color). Sound alerts have visual equivalents.

#### 5.6 Guided Workflow Wizards

**Purpose**: Replace multi-screen sequential navigation with structured step flows.

**How It Works**:
- Complex workflows (PA submission, plan configuration) presented as step-by-step wizards
- Step indicator shows progress: Step 2 of 5 — Clinical Review
- Each step validates before allowing progression
- "Back" and "Save Draft" always available
- Summary screen before final submission

**Why This Pattern**: Reduces Angela Washington's (Persona 3) plan configuration from navigating 8-12 green screens to completing 4-5 wizard steps with clear progress indication. Sofia Martinez (Persona 5) can follow guided workflows from day one without memorizing screen sequences.

---

## 6. Journey Maps

### Journey Map 1: Claims Adjudication — Maria Torres (Claims Processor)

Four stages aligned with the Dreyfus skill acquisition model: Learning → Competence → Proficiency → Mastery.

#### Stage 1: Learning (Week 1-2)

| Dimension | Detail |
|-----------|--------|
| **Activities** | Guided claims processing with training mode enabled; contextual tooltips active; processes 20-30 claims/day |
| **Touchpoints** | Training sandbox environment; side-by-side with senior processor; LMS training modules |
| **Interaction Mode** | Mouse-discovery mode — clicks buttons, uses menus, follows guided workflows |
| **Emotional State** | Cautious but optimistic — "This is more intuitive than the green screen training I heard about" |
| **Friction Points** | Unfamiliar with PBM terminology (not a UI problem); some lookup workflows feel slower than described by veterans |
| **Support Needs** | Inline help tooltips; "What does this field mean?" links to glossary; senior processor available for questions |
| **Success Metrics** | Completes first independent claim within 3 days; error rate < 15% |

#### Stage 2: Competence (Week 3 — Month 1)

| Dimension | Detail |
|-----------|--------|
| **Activities** | Independent claims processing; 50-80 claims/day; begins discovering keyboard shortcuts |
| **Touchpoints** | Production environment with training guardrails; weekly check-ins with supervisor |
| **Interaction Mode** | Hybrid — primarily mouse with increasing keyboard shortcut usage; begins using Tab-order navigation |
| **Emotional State** | Growing confidence — "I'm starting to get the rhythm" |
| **Friction Points** | Wants to go faster but hasn't internalized keyboard shortcuts; some complex claims still require help |
| **Support Needs** | Keyboard shortcut cheat sheet visible on desk; "Show me the keyboard shortcut" option in UI |
| **Success Metrics** | Processing 50+ claims/day independently; error rate < 10%; begins using command palette |

#### Stage 3: Proficiency (Month 1-3)

| Dimension | Detail |
|-----------|--------|
| **Activities** | Full-speed claims processing; 100-150 claims/day; handles complex claims with DUR alerts independently |
| **Touchpoints** | Full production; participates in team metrics review; begins mentoring newer hires |
| **Interaction Mode** | Keyboard-power mode — uses command palette, keyboard shortcuts, and Tab-order for 80%+ of interactions |
| **Emotional State** | Confident and efficient — "The split-pane view is a game-changer. I can see everything at once." |
| **Friction Points** | Occasional desire for green-screen-specific shortcuts that weren't mapped; suggests new shortcuts |
| **Support Needs** | Minimal — customization options (keyboard shortcut remapping, layout preferences) |
| **Success Metrics** | Processing 100+ claims/day; error rate < 5%; NPS ≥ 7; no green screen fallback usage |

#### Stage 4: Mastery (Month 3-6+)

| Dimension | Detail |
|-----------|--------|
| **Activities** | Peak performance; 200+ claims/day; handles exceptions and edge cases; trains new hires |
| **Touchpoints** | Full production; champion network member; provides feedback on UI improvements |
| **Interaction Mode** | Full keyboard-power mode — command palette is primary navigation; mouse used only for data visualization interactions |
| **Emotional State** | Ownership — "I helped a new hire get up to speed in a week. On the old system, that took two months." |
| **Friction Points** | Wants advanced customization; suggests workflow improvements based on expertise |
| **Support Needs** | Feature request channel; advanced customization options |
| **Success Metrics** | At or above pre-transition productivity; error rate < 3%; actively helps adopt new users (champion) |

### Journey Map 2: Prior Authorization — Dr. James Chen (Clinical Pharmacist)

Includes GenAI-assisted decision support touchpoints (FR-006 demonstration).

#### Stage 1: PA Request Intake

| Dimension | Detail |
|-----------|--------|
| **Activities** | Receives PA request; reviews member eligibility and requested medication |
| **Touchpoints** | PA queue (list view with priority sorting); member profile (side panel); formulary reference (inline) |
| **GenAI Touchpoint** | **AI Pre-Screen**: System automatically classifies PA as "straightforward" or "complex" based on medical history and policy criteria. Straightforward cases get pre-populated recommendation. |
| **Emotional State** | Focused — "Let me see what we're working with" |

#### Stage 2: Clinical Evidence Review

| Dimension | Detail |
|-----------|--------|
| **Activities** | Reviews medical history, diagnosis codes, prior medications, lab results |
| **Touchpoints** | Clinical data panel (contextual side panel); medication timeline (visual); diagnosis codes (searchable) |
| **GenAI Touchpoint** | **AI Evidence Summary**: GenAI surfaces relevant clinical evidence, prior PA decisions for similar cases, and policy citations — displayed in a recommendation panel alongside the clinical data. All AI-generated content clearly labeled with confidence scores. |
| **Emotional State** | Analytical — "The AI summary saves me from reading 15 screens of history" |
| **Friction Points** | Must verify AI summary against source data; AI confidence scores help prioritize what to verify |

#### Stage 3: Decision Making

| Dimension | Detail |
|-----------|--------|
| **Activities** | Makes PA decision: approve, deny, or request additional information |
| **Touchpoints** | Decision form with structured rationale; AI recommendation with supporting evidence; override reason selector |
| **GenAI Touchpoint** | **AI Recommendation**: GenAI presents recommendation (approve/deny) with supporting evidence citations, policy references, and confidence score. **Human-in-the-loop required**: pharmacist must explicitly approve or override the AI recommendation (FR-006 acceptance criteria). |
| **Emotional State** | Confident — "I agree with the AI recommendation, and I can see exactly why it reached this conclusion" or "The AI missed this contraindication — good thing human review is mandatory" |

#### Stage 4: Documentation and Notification

| Dimension | Detail |
|-----------|--------|
| **Activities** | Generates approval/denial letter; documents clinical rationale; updates member record |
| **Touchpoints** | Auto-generated letter (editable); audit trail (automatic); member notification trigger |
| **GenAI Touchpoint** | **AI Draft Letter**: GenAI drafts the approval/denial letter incorporating the decision rationale, policy citations, and next steps. Pharmacist reviews and edits before sending. |
| **Emotional State** | Satisfied — "What used to take 20 minutes of documentation now takes 3 minutes of review" |

**Overall PA Workflow Improvement Target**: Standard PA cases from days to minutes; complex cases from hours to minutes. All improvements measured against FR-006 acceptance criteria.

---

## 7. Accessibility Strategy

CVS Health has a demonstrated commitment to accessibility: 120+ accessibility professionals hired, W3C membership, and the open-source [Accessibility Annotations Kit](https://github.com/cvs-health/annotations) with 150,000+ annotations across 1,100+ design files, contributing to a 22% decrease in accessibility defects. The modernized PBM interface must build on this foundation.

### 7.1 WCAG 2.2 AA Compliance

The modernized interface targets **WCAG 2.2 AA** conformance (CVS Health is already working toward WCAG 2.2 through their design system — [CVS Health Tech Blog](https://medium.com/cvs-health-tech-blog/the-path-to-wcag-2-2-conformance-through-our-design-system-59913a8bf876)).

Key WCAG 2.2 success criteria relevant to this modernization:

| Criterion | Level | Relevance to PBM Modernization |
|-----------|-------|-------------------------------|
| **2.4.11 Focus Not Obscured (Minimum)** | AA | Critical — modals, side panels, and contextual overlays must not obscure the focused element |
| **2.5.7 Dragging Movements** | AA | Split-pane resizing must have a non-drag alternative (e.g., keyboard-based resize) |
| **2.5.8 Target Size (Minimum)** | AA | All interactive targets ≥ 24×24 CSS pixels — important for toolbar buttons replacing F-keys |
| **3.2.6 Consistent Help** | A | Help mechanisms (tooltips, chat, documentation links) in consistent location across all screens |
| **3.3.7 Redundant Entry** | A | Auto-populate previously entered data (member ID, plan details) — don't force re-entry |
| **3.3.8 Accessible Authentication (Minimum)** | AA | Login flow must not require cognitive function tests (CAPTCHAs) — aligns with Phase 3 IAM strategy |

### 7.2 Section 508 and ONC Safety-Enhanced Design

**Section 508**: Federal accessibility standard applicable to CVS Health as a healthcare organization receiving federal funding (Medicare Part D). All modernized interfaces must comply with the Revised Section 508 Standards (2017), which incorporate WCAG 2.0 Level AA.

**ONC Safety-Enhanced Design (SED)**: Although CVS's internal PBM tools may not require ONC certification directly, the SED framework provides the gold standard for healthcare UX:
- Requires formal **User-Centered Design (UCD) process** (ISO 9241-210 or equivalent)
- Mandates **summative usability testing** with minimum 10 test participants per capability
- Requires documentation per NISTIR 7742: task success rate, task failures, task performance time, and user satisfaction
- Purpose: increasing patient safety by designing to prevent human errors in healthcare IT

**Recommendation**: Follow ONC SED requirements voluntarily as a quality standard, even if not legally required for internal tools. This demonstrates due diligence and aligns with NIST health IT usability best practices.

Sources:
- [HealthIT.gov — Safety-Enhanced Design](https://www.healthit.gov/test-method/safety-enhanced-design)
- [Healthcare Usability — §170.315(g)(3)](https://www.healthcareusability.com/article/170315g3-safety-enhanced-design-and-onc-2015-certification)

### 7.3 Keyboard Navigation

Green screen modernization has a unique accessibility advantage: **the existing system is already keyboard-only**. The modernized interface inherits this strength by design.

| Requirement | Implementation |
|-------------|----------------|
| **Full keyboard operability** | Every action achievable via keyboard — no mouse-only interactions |
| **Visible focus indicator** | 2px+ border with 3:1 contrast ratio (WCAG 2.4.13 Focus Appearance) |
| **Logical tab order** | Tab order follows the workflow sequence (claim intake → validation → decision) |
| **Skip navigation** | Skip links for long page structures |
| **Keyboard shortcut documentation** | Accessible shortcut reference via `?` key |
| **No keyboard traps** | All modals, side panels, and overlays are escapable via Escape key |

### 7.4 Color and Contrast for Clinical Alerts

Clinical alerts (DUR screening, drug interactions) use color-coding for severity. WCAG 1.4.1 (Use of Color) prohibits conveying information solely through color.

**Implementation**: Every color-coded alert includes:
- Icon differentiation (critical = octagon, warning = triangle, info = circle)
- Text label ("Critical," "Warning," "Info")
- Aria-label for screen readers
- Minimum 4.5:1 contrast ratio for text, 3:1 for large text and graphical elements

### 7.5 Screen Reader Compatibility

| Element | Screen Reader Implementation |
|---------|------------------------------|
| **Dynamic content updates** | ARIA live regions for real-time claim status, DUR alert popups |
| **Data tables** | Proper `<th>`, `scope`, and `<caption>` elements for claims lists and formulary tables |
| **Form validation** | `aria-invalid`, `aria-describedby` linking error messages to form fields |
| **Command palette** | `role="combobox"` with `aria-expanded`, `aria-activedescendant` for results navigation |
| **Split-pane views** | `role="region"` with `aria-label` for each pane; keyboard-navigable pane switching |

### 7.6 Focus Management

Critical for single-page application architecture where context changes don't trigger full page loads:
- When a side panel opens, focus moves to the panel header
- When a modal closes, focus returns to the triggering element
- When a form submits successfully, focus moves to the success message
- When navigating between claims in a list, focus stays in the list for rapid sequential processing

---

## 8. Usability Testing Plan

Following ONC Safety-Enhanced Design testing methodology and NISTIR 7742 documentation requirements.

### 8.1 Testing Methods

| Method | When | Participants | What We Measure |
|--------|------|-------------|-----------------|
| **Think-Aloud Protocol** | During prototype phase | 10+ per persona type | Cognitive load, confusion points, task flow understanding |
| **Task Completion Testing** | Before each release | 10+ per workflow | Task success rate, error rate, time-on-task (NISTIR 7742) |
| **A/B Testing** | Post-launch | Production users (10% sample) | Completion rates, error rates, time metrics for design variants |
| **Heuristic Evaluation** | Before usability testing | 3-5 UX experts | Nielsen's 10 heuristics compliance |
| **Accessibility Audit** | Before each release | Automated (axe-core) + manual (VPAT) | WCAG 2.2 AA compliance score (SC-005) |

### 8.2 Testing Cadence

| Phase | Testing Activity | Frequency |
|-------|-----------------|-----------|
| **Design** | Paper prototype testing with pharmacy staff | Per major workflow design |
| **Development** | Automated accessibility scanning (CI/CD integration) | Every build |
| **Pre-release** | Summative usability testing (NISTIR 7742 format) | Per screen release |
| **Post-launch** | User satisfaction survey (NPS — SC-008) | Monthly |
| **Ongoing** | Analytics-driven iteration (heatmaps, click tracking, error rates) | Continuous |

### 8.3 Participant Recruitment

Testing participants must represent the actual user base per ONC SED requirements:
- **Claims Processors** (like Maria Torres): 10+ participants across experience levels (1-15 years)
- **Clinical Pharmacists** (like Dr. Chen): 10+ participants with clinical workflow experience
- **Benefits Analysts** (like Angela Washington): 5+ participants
- **New Hires** (like Sofia Martinez): 5+ participants with zero green screen experience

**Assumption A-1-001**: CVS Health will provide access to representative pharmacy staff for usability testing. If not, proxy testing with pharmacy professionals from partner organizations is an alternative.

---

## 9. Design System Recommendations

### 9.1 Component Library Approach

**Recommendation**: Build a component library using React (A-0-007) that extends or aligns with CVS Health's existing design system standards.

CVS Health has demonstrated design system maturity through their open-source [Accessibility Annotations Kit](https://github.com/cvs-health/annotations). The PBM modernization should:

1. **Adopt CVS Health's existing accessibility standards** — 150,000+ annotations across 1,100+ design files represent battle-tested patterns
2. **Build PBM-specific components** on top of the core design system:
   - Claims adjudication dashboard layout
   - DUR alert component (severity-coded with accessibility)
   - Member profile card (reusable across all screens)
   - Command palette overlay
   - Split-pane layout container
3. **Maintain visual consistency with myPBM** — the Azure-hosted client portal uses modern web patterns that internal PBM tools should echo

### 9.2 Core Component Set

| Component | Purpose | Accessibility Requirements |
|-----------|---------|---------------------------|
| **DataTable** | Claims lists, formulary tables, audit logs | Sortable columns, keyboard-navigable rows, screen reader captions |
| **SplitPane** | Claims adjudication, side-by-side comparison | Keyboard-resizable, ARIA landmarks, responsive stacking |
| **CommandPalette** | Primary navigation for power users | Combobox ARIA pattern, keyboard-navigable results, fuzzy search |
| **AlertBanner** | DUR alerts, system notifications | ARIA live region, icon + color + text severity coding |
| **FormWizard** | PA submission, plan configuration | Step indicator, progress announcement, save-draft capability |
| **SidePanel** | Detail views, clinical references | Focus management, escape-to-close, return-focus-on-close |
| **MemberCard** | Reusable member information display | Consistent layout, expandable sections, keyboard-accessible |

### 9.3 CVS Brand Alignment

**Assumption A-1-002**: CVS Health has internal brand guidelines for enterprise applications that will be provided during the engagement. Public-facing CVS brand elements (red/white color scheme, CVS Health logo) provide directional guidance, but internal PBM tools may have different brand treatment.

Design recommendations until brand guidelines are available:
- **Typography**: System font stack (Inter, Segoe UI, or similar) for readability in data-dense views
- **Color palette**: Neutral base (gray scale) with brand accent colors for interactive elements and status indicators
- **Spacing**: 8px grid system for consistent spacing and density control
- **Density modes**: Comfortable (default) and compact (for power users who want more data on screen)

---

## 10. Transition Design

Bridge between current green screen workflows and the modernized interface. Connects to Change Management (Phase 4) and the Strangler Fig migration pattern (Phase 2).

### 10.1 Dual-Mode Coexistence

During migration, green screen and web UI must operate simultaneously. Users choose their interface per-workflow based on migration status.

```
┌─────────────────────────────────────────────────────┐
│                   API Gateway (Apigee)               │
├─────────────────┬───────────────────────────────────┤
│  Modern Web UI  │  Green Screen Terminal             │
│  (React)        │  (5250 emulator)                   │
│                 │                                    │
│  ● Migrated     │  ● Not-yet-migrated               │
│    workflows    │    workflows                       │
│  ● New features │  ● Fallback for migrated           │
│                 │    workflows (escape hatch)         │
├─────────────────┴───────────────────────────────────┤
│              IBM i Backend (unchanged)               │
└─────────────────────────────────────────────────────┘
```

### 10.2 Green Screen "Escape Hatch"

During the transition period, every migrated workflow retains a "Return to Green Screen" option. This is critical for change management:

- **Psychological safety**: Users know they can always fall back to the familiar interface
- **Risk mitigation**: If the modern UI has a bug or performance issue, work continues uninterrupted
- **Adoption measurement**: Track escape hatch usage as a proxy for adoption confidence — decreasing usage = increasing trust
- **Sunset trigger**: When escape hatch usage drops below 5% for a workflow, begin decommission planning for that green screen

**Assumption A-1-003**: The green screen escape hatch adds development cost (maintaining two UIs temporarily) but significantly reduces change management risk. The 85% digital transformation failure rate for people/process issues justifies this investment.

### 10.3 Progressive Rollout by Workflow (Strangler Fig Alignment)

Rollout order optimized for risk-reward:

| Order | Workflow | Risk | Visibility | Rationale |
|-------|----------|------|------------|-----------|
| 1 | Member Eligibility Lookup | Low (read-only) | High (used by all) | Low-risk validation of the full stack; GCP Dual Run validates output equivalence |
| 2 | Benefits Verification | Low-Medium | High | Extends member lookup; adds plan detail views |
| 3 | Claims Adjudication | High (sub-second latency) | Highest | Flagship workflow; requires extensive performance validation |
| 4 | Prior Authorization | Medium-High | Medium | GenAI integration; most complex UX changes |
| 5 | Formulary Management | Medium | Medium | Clinical workflow; pharmacist-specific UX |

### 10.4 F-Key to Modern Shortcut Mapping Guide

Published to all users before transition begins. Posted as laminated cards at workstations (per change management plan).

| F-Key | Green Screen Function | Modern UI Equivalent | Keyboard Shortcut |
|-------|----------------------|---------------------|--------------------|
| F1 | Help | Contextual help panel | F1 (unchanged) |
| F3 | Exit/Return | Back / Close panel | Escape |
| F4 | Prompt/List | Dropdown / Autocomplete | Down Arrow (in field) |
| F5 | Refresh | Refresh data | F5 (unchanged) |
| F6 | Create/Add | Create new record | Ctrl+N |
| F7 | Page Up (scroll) | Scroll up | Page Up (unchanged) |
| F8 | Page Down (scroll) | Scroll down | Page Down (unchanged) |
| F9 | Retrieve last command | Command palette history | Ctrl+K, then Up Arrow |
| F10 | Actions menu | Context menu / Action menu | Shift+F10 or Right-click |
| F12 | Cancel | Cancel / Discard | Escape |
| Screen codes | Navigate to specific screen | Command palette | Ctrl+K, type code/name |

### 10.5 Training Integration

Transition design connects directly to the Change Management strategy (Phase 4):

- **Pre-transition**: Awareness campaign showing side-by-side green screen vs. modern UI for the same workflow
- **Launch week**: Guided walkthroughs in the modern UI with "tour" overlay (showing where F-key equivalents are)
- **First 30 days**: Training mode with extended tooltips and "Did you know?" tips for keyboard shortcuts
- **Ongoing**: Keyboard shortcut of the day in the system's notification area
- **Champion network**: Green screen power users trained first to become change champions for their teams

---

## Appendix A: Wireframe Descriptions

### Wireframe 1: Claims Adjudication Dashboard

**Screen**: Primary claims processing view — Maria Torres's daily workspace

**Layout** (Desktop, 1920×1080 minimum):

```
┌─────────────────────────────────────────────────────────────┐
│  Header: CVS Caremark | Claims Processing | [User] | [?]   │
│  Command Palette Trigger: Ctrl+K ───────────────────────────│
├────────────┬────────────────────────────────────────────────┤
│            │                                                │
│  Left Pane │  Center Pane: Current Claim                   │
│  (300px)   │  (flexible width)                             │
│            │                                                │
│  Member    │  ┌──────────────────────────────────────────┐  │
│  Info      │  │ Claim #: CLM-2026-0847291                │  │
│            │  │ Rx: Lisinopril 10mg (NDC: 00093-7339-01) │  │
│  ● Name    │  │ Pharmacy: CVS #4521 — Atlanta, GA        │  │
│  ● ID      │  │ Status: ● Pending Adjudication           │  │
│  ● Plan    │  ├──────────────────────────────────────────┤  │
│  ● Group   │  │ DUR Alerts:                              │  │
│  ● Elig.   │  │ ⓘ  Duplicate therapy detected (Tier: Low)│  │
│    Dates   │  │ ⚠  Dosage outside typical range (Medium) │  │
│  ● Copay   │  ├──────────────────────────────────────────┤  │
│    Struct.  │  │ Pricing:                                 │  │
│            │  │ Cost: $12.47 | Copay: $5.00 | Plan: $7.47│  │
│  [Expand   │  ├──────────────────────────────────────────┤  │
│   History] │  │ [Approve] [Deny ▾] [Pend] [Override DUR] │  │
│            │  │  Keyboard: A      D       P     O        │  │
│            │  └──────────────────────────────────────────┘  │
├────────────┴────────────────────────────────────────────────┤
│  Bottom Bar: Claims Queue (15 pending) | Processed Today: 47│
│  [◄ Previous] [Next ►]  |  Shortcuts: ? | Palette: Ctrl+K  │
└─────────────────────────────────────────────────────────────┘
```

**Key Interaction Patterns**:
- **Split-pane**: Member info (left) and claim details (center) visible simultaneously — eliminates F-key screen-switching
- **Keyboard shortcuts**: Single-letter keys for primary actions (A=Approve, D=Deny, P=Pend, O=Override)
- **DUR alerts**: Severity-coded with icon + color + text; expandable for clinical detail
- **Command palette**: Ctrl+K opens overlay for navigation, member lookup, or action search
- **Queue navigation**: Arrow keys or Next/Previous buttons for sequential claim processing
- **Responsive**: On smaller screens, left pane collapses to a "Member Info" tab at the top

**Accessibility Features**:
- Tab order: Member info → Claim details → DUR alerts → Actions → Queue navigation
- ARIA landmarks for each pane region
- Live region for DUR alert count updates
- Focus returns to action buttons after DUR alert review
- All keyboard shortcuts documented in `?` help overlay

### Wireframe 2: Prior Authorization Workflow (GenAI-Assisted)

**Screen**: PA review workflow — Dr. James Chen's clinical workspace

**Layout** (Desktop, progressive wizard + recommendation panel):

```
┌─────────────────────────────────────────────────────────────┐
│  Header: CVS Caremark | Prior Authorization | [User] | [?] │
│  PA Queue (3 pending) ─────── Step 2 of 4: Clinical Review  │
├─────────────────────────────────────┬───────────────────────┤
│                                     │                       │
│  Main Content: Clinical Review      │  AI Recommendation    │
│  (flexible width)                   │  Panel (350px)        │
│                                     │                       │
│  Patient: John Smith (M-4829103)    │  ┌─────────────────┐  │
│  Requested: Ozempic 1mg weekly      │  │ 🤖 AI Analysis  │  │
│  Prescriber: Dr. Sarah Johnson      │  │                 │  │
│                                     │  │ Recommendation: │  │
│  ┌─ Medical History ──────────────┐ │  │ ✅ APPROVE      │  │
│  │ ● Type 2 Diabetes (E11.9)     │ │  │ Confidence: 92% │  │
│  │   Diagnosed: 2019-03-14       │ │  │                 │  │
│  │ ● Metformin 1000mg (current)  │ │  │ Evidence:       │  │
│  │ ● HbA1c: 8.2% (2026-01-15)   │ │  │ • Step therapy  │  │
│  │ ● BMI: 34.2                   │ │  │   met (Metformin │  │
│  │ ● Prior PA: Trulicity (denied │ │  │   >6mo at max   │  │
│  │   2025-06 — step therapy)     │ │  │   dose)         │  │
│  └────────────────────────────────┘ │  │ • HbA1c >7%    │  │
│                                     │  │   (target met)  │  │
│  ┌─ Policy Criteria ──────────────┐ │  │ • BMI >30      │  │
│  │ CVS Formulary: Tier 3 (PA Req) │ │  │   (qualifier)  │  │
│  │ Step Therapy: Must try         │ │  │                 │  │
│  │   Metformin ≥6mo first ✅      │ │  │ Policy Ref:     │  │
│  │ Clinical Criteria:             │ │  │ PA-GLP1-2026-v3 │  │
│  │   HbA1c >7% ✅                 │ │  │ §4.2.1          │  │
│  │   BMI >30 ✅                    │ │  │                 │  │
│  └────────────────────────────────┘ │  │ [Accept AI Rec] │  │
│                                     │  │ [Override ▾]    │  │
│  [◄ Back] [Save Draft]    [Next ►]  │  │ [Request Info]  │  │
│                                     │  └─────────────────┘  │
├─────────────────────────────────────┴───────────────────────┤
│  Step Progress: ① Intake ② Clinical Review ③ Decision ④ Doc │
└─────────────────────────────────────────────────────────────┘
```

**Key Interaction Patterns**:
- **Progressive wizard**: 4-step flow replaces 10-15 green screen navigations
- **GenAI recommendation panel**: AI analysis with confidence score, evidence citations, and policy references — always visible alongside the clinical data for cross-reference
- **Human-in-the-loop**: "Accept AI Rec" and "Override" buttons require explicit pharmacist action — AI never auto-decides
- **Expandable sections**: Medical history and policy criteria sections expand/collapse for progressive disclosure
- **Step navigation**: Back and Next with save-draft at every step
- **Checkmarks**: Visual indicators showing which policy criteria are met (✅) — recognition over recall

**GenAI Design Principles**:
- AI recommendations are clearly labeled as AI-generated (🤖 icon + "AI Analysis" label)
- Confidence score displayed prominently — pharmacist knows when to scrutinize more carefully
- Evidence is cited with specific policy references (not just "approved based on criteria")
- Override requires reason selection (for audit trail and model improvement)
- All AI interactions logged for evaluation framework (FR-006 acceptance criteria)

**Accessibility Features**:
- Wizard step indicator announced to screen readers ("Step 2 of 4: Clinical Review")
- AI panel uses `role="complementary"` with `aria-label="AI Recommendation"`
- Expandable sections use `aria-expanded` and are keyboard-operable
- Checkmark indicators have text alternatives ("Met" / "Not Met")
- Focus management: on step transition, focus moves to the first interactive element of the new step

---

## Appendix B: Assumption Register (Phase 1)

| ID | Assumption | Basis | Risk if Wrong | Validation Strategy |
|----|-----------|-------|---------------|-------------------|
| **A-1-001** | CVS Health will provide access to representative pharmacy staff for usability testing | Standard practice for enterprise UX modernization | Usability testing would use proxy participants, reducing validity | Ask during engagement: "Can we include pharmacy staff in usability testing?" |
| **A-1-002** | CVS Health has internal brand guidelines for enterprise applications | Large enterprise with 120+ accessibility professionals has design system maturity | Design system alignment may require rework once guidelines are available | Ask: "Are there brand guidelines for internal tools?" |
| **A-1-003** | Green screen escape hatch during transition justifies temporary dual-UI cost | 85% digital transformation failure rate for people/process issues | If users never adopt the modern UI, the escape hatch becomes a permanent crutch | Track escape hatch usage; sunset when <5% per workflow |
| **A-1-004** | Claims processors' primary pain point is context-switching between screens | Consistent across IBMi modernization literature and PBM domain research | If pain point is actually performance latency, split-pane views may not be the right focus | Validate in user research: "What slows you down most?" |
| **A-1-005** | Command palette will be accepted by green screen power users as a bridge pattern | Command palette maps directly to the "type a code → get a result" mental model | Power users may reject any change regardless of familiarity mapping | Pilot test command palette with 5 expert users before full rollout |
| **A-1-006** | React is the frontend framework for implementation | CVS uses React and Angular per job postings (A-0-007) | Angular or another framework may be mandated | Present framework-agnostic component architecture |
| **A-1-007** | Dual-mode interface (keyboard + mouse) is preferable to separate "power user" and "normal" modes | Dreyfus model supports continuous skill progression, not discrete modes | Some organizations prefer explicit "expert mode" toggles | Test both approaches in prototype phase |

---

## Self-Review Assessment

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| Design principles grounded in cognitive science | 9/10 | Each principle cites specific theories (Hick's Law, Fitts's Law, Dreyfus model, Johnson-Laird, Reason's taxonomy, Miller's Law) |
| Personas realistic for PBM domain | 8/10 | 5 personas cover all major PBM roles; workflows based on Phase 0 research; would benefit from validation with actual CVS staff |
| Green screen workflow analysis is sourced | 8/10 | All workflow descriptions labeled as RESEARCHED; based on Phase 0 research + Tier 1 web research; no unsourced claims |
| Accessibility strategy meets WCAG 2.2 AA | 9/10 | Covers WCAG 2.2 new criteria, Section 508, ONC SED, keyboard navigation, screen reader, focus management, color contrast |
| Transition design bridges to Change Management | 8/10 | Escape hatch, progressive rollout, F-key mapping guide, training integration; connects to ADKAR model in Phase 4 |
| Interview depth for 45-minute HCD deep dive | 8/10 | Design philosophy, 6 grounded principles, 5 personas, 3 workflows, 2 journey maps, comprehensive accessibility strategy — sufficient for sustained questioning |
| Paul's voice (collaborative, empirical, warm) | 8/10 | First-person framing where appropriate; evidence-based claims; honest about researched vs. direct knowledge |
| **Overall** | **8.3/10** | Strong design document that leverages Cognitive Science differentiator effectively; would benefit from real user validation |

---

*Document produced by Paul Prae with AI assistance. Green screen workflow analysis based on IBMi modernization research (11 sources) and PBM domain research (5 sources). Design principles grounded in Paul's Cognitive Science training (University of Georgia) and 6+ UX projects. CVS Health brand alignment informed by publicly available design system information and the CVS Health Accessibility Annotations Kit.*
