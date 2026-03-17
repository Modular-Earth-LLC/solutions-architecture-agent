# Phase 1 Context Summary — UX & Workflow Design

> **Completed**: 2026-03-16
> **Status**: complete

## Key Findings

- **CVS Health accessibility maturity is higher than expected**: 120+ accessibility professionals, W3C member, open-source Accessibility Annotations Kit on GitHub (150,000+ annotations, 22% decrease in defects). The modernized UI should build on their existing standards, not reinvent.
- **Command palette (Ctrl+K) is the ideal bridge pattern**: Maps directly to green screen "type a code → get a result" mental model. Validated by industry examples (VS Code, Figma, Linear, Notion, Superhuman).
- **Dual-mode interface is necessary, not optional**: Dreyfus skill acquisition model requires simultaneous support for novice (mouse-discovery) and expert (keyboard-power) users. No mode toggle — both active always.
- **Five personas cover the PBM workflow space**: Claims Processor (highest risk), Clinical Pharmacist (GenAI target), Benefits Analyst (lowest resistance), IT Administrator (IAM bridge), New Hire/Trainee (change management bridge).
- **Three workflows prioritized for depth**: Claims adjudication (flagship), Prior Authorization (GenAI demonstration), Member Eligibility Lookup (first strangler fig candidate).
- **WCAG 2.2 AA is the target** (not 2.1): CVS is already working toward 2.2 conformance. Nine new success criteria include focus management, target size, accessible authentication — all relevant to this modernization.
- **ONC Safety-Enhanced Design is recommended as voluntary standard**: Even though internal PBM tools may not require ONC certification, following SED methodology (UCD process + summative usability testing with 10+ participants per capability) demonstrates due diligence.
- **Green screen escape hatch is critical for adoption**: 85% digital transformation failure rate for people/process issues justifies temporary dual-UI cost. Track escape hatch usage as adoption proxy.
- **CVS uses generative agent simulations for UX decisions**: 2.9M consented responses from 400K+ participants across 200+ behavioral scenarios. Evidence-based UX testing aligns with this approach.

## Artifacts Produced

| File | Description |
|------|-------------|
| `outputs/cvs-legacy-transformation/ux-design-document.md` | Complete UX design document (10 sections, 2 wireframes, 7 assumptions) |
| `outputs/cvs-legacy-transformation/phase-1-ux-research.md` | Web research findings (8 queries across Tiers 1-3) |

## Decisions Made

- **5 personas (not 4-6)**: Dropped "Business Analyst / Manager" — overlaps with Benefits Analyst. Added New Hire/Trainee as explicit change management bridge persona.
- **3 workflows (not 5)**: Focused on Claims Adjudication, Prior Authorization, and Member Eligibility Lookup for depth over breadth. Formulary Management and Benefits Verification deferred as extensions of the same patterns.
- **WCAG 2.2 AA (not 2.1)**: CVS is already targeting 2.2 through their design system. Phase 0 requirements.json references 2.1 — updated target to 2.2.
- **ONC SED as voluntary standard**: Not legally required for internal tools, but provides gold-standard testing methodology.
- **Command palette as primary bridge pattern**: Chosen over alternative approaches (toolbar-based, menu-based) due to direct mapping to green screen mental model.

## Surprises and Pivots

- **CVS accessibility depth**: Was prepared for standard enterprise accessibility. CVS's 120+ accessibility professionals, W3C membership, and open-source annotation kit indicate design system maturity far beyond typical healthcare enterprises. This is a strength to build on.
- **myPBM already exists as modern PBM interface**: CVS's Azure-hosted myPBM client portal represents their target state for modern PBM UX. Internal tool modernization should echo this design language for consistency.
- **CVS moved from "digital transformation" to "digital optimization"**: Indicates maturity — they are past initial transformation. Position this engagement as the next optimization frontier for internal tools.

## Assumptions

### Confirmed
- A-0-007 (React is likely frontend framework): CVS job postings confirm React and Angular usage
- A-0-010 (Sub-second claims adjudication non-negotiable): Validated across all PBM research — P95 ≤ 500ms

### New
- A-1-001: CVS Health will provide access to representative pharmacy staff for usability testing
- A-1-002: CVS Health has internal brand guidelines for enterprise applications
- A-1-003: Green screen escape hatch during transition justifies temporary dual-UI cost
- A-1-004: Claims processors' primary pain point is context-switching between screens
- A-1-005: Command palette will be accepted by green screen power users as a bridge pattern
- A-1-006: React is the frontend framework for implementation
- A-1-007: Dual-mode interface is preferable to separate expert/normal modes

## Insights for Future Phases

- **Phase 2 (Architecture)**: The command palette requires WebSocket or server-sent events for real-time fuzzy search across green screen codes, member IDs, and workflow actions. Split-pane views require efficient API design — member info and claim details loaded in parallel, not sequentially. Performance budget: 200ms UI render + 300ms API response = 500ms total for claims adjudication.
- **Phase 2 (Architecture)**: myPBM on Azure and the new internal UI on GCP create a multi-cloud UX challenge — design for visual consistency across platforms.
- **Phase 3 (Security & IAM)**: Accessible authentication is a WCAG 2.2 AA requirement (3.3.8) — login flow must not require cognitive function tests (CAPTCHAs). IT Administrator persona (Raj Patel) needs unified IAM dashboard showing both IBMi + cloud user profiles.
- **Phase 4 (Estimation)**: Change management cost must include: F-key mapping laminated cards, training sandbox environment, champion network setup, monthly NPS surveys, and dual-UI maintenance during transition period.
- **Phase 4 (Change Management)**: Five personas with mapped change resistance levels (HIGH → NONE) provide the basis for targeted change management strategies. Maria Torres (Claims Processor, HIGH resistance) requires speed parity demonstration; Sofia Martinez (Trainee, NO resistance) validates onboarding time reduction.
- **Phase 5 (Methodology)**: AI-assisted UX design is a strong "show, don't tell" example — the GenAI recommendation panel wireframe demonstrates exactly the kind of human-AI workflow Paul would build as GenAI team leader.
- **Phase 6 (Assembly)**: Design principles should be presented as a strength section — Paul's Cognitive Science degree is a genuine differentiator. Six principles with cited theories (Hick's Law, Fitts's Law, Dreyfus model, etc.) provide depth for the 45-minute HCD interview.
- **Phase 7 (Interview Prep)**: HCD interview is Paul's strongest interview of the three. Prepare detailed answers for: "How does your Cognitive Science background inform your design approach?" and "How do you handle resistance from expert users who are faster on the old system?"

## Paul's Feedback

- [Pending — Paul has not yet reviewed Phase 1 outputs]
