# Pre-Show Checklist -- 1 Hour Before
## AI-Driven Prior Authorization — Autonomize AI Interview

> Work through this checklist before sending the email and before presenting.
> For study material, see [study-guide.md](study-guide.md). For speaking notes, see [speaker-script.md](../speaker-script.md).

---

## Overnight Decisions (Review Required)

See [decisions-made-without-paul.md](../plans/decisions-made-without-paul.md):
- [x] D-001: outputs/ un-ignored in .gitignore -- Paul requested this
- [x] D-002: CAQH payer cost $3.52 -- verified against 2024 CAQH Index
- [ ] D-003: AMA physician burden 14 to 12-13 hr/week -- verify you're comfortable

---

## Before Sending Email

- [ ] Read `email-draft.md` -- personalize tone, check formality level
- [ ] Verify demo link placeholder is updated (or remove if demo not deployed)
- [ ] Confirm attachment includes slide deck (PowerPoint or PDF)
- [ ] Confirm diagram PNGs render at readable size
- [ ] Spell-check: Paul Prae, www.paulprae.com (never misspelled)
- [ ] Check panel names spelled correctly: Kris Nair, Suresh Gopalakrishnan, Ujjwal Rajbhandari
- [ ] Verify email tone and content match your voice

---

## Before Presenting -- Content Accuracy

- [ ] Verify Altais metrics: 45% review time reduction, 54% error reduction, 50% auto-approval
- [ ] Verify CAQH numbers: $10.97 provider, $3.52 payer, ~$0.05 automated (2024 Index)
- [ ] Verify CMS-0057-F: Phase 1 live Jan 2026, Phase 2 Jan 2027
- [ ] Verify Autonomize: Pegasus Program (Nov 2025), Azure Marketplace, ServiceNow partnership (Mar 2026)
- [ ] Spot-check 5 source URLs from appendix -- all should load

---

## Before Presenting -- Azure Service Names

- [ ] Azure AI Foundry (not "Azure OpenAI Service" -- rebranded)
- [ ] Azure AI Document Intelligence (not "Form Recognizer" -- rebranded)
- [ ] Microsoft Entra ID (not "Azure AD" -- rebranded)
- [ ] Azure Health Data Services (not "Azure API for FHIR" -- evolved)
- [ ] Azure Container Apps (confirm still GA, not deprecated)

---

## Before Presenting -- Rehearsal

- [ ] Read [speaker-script.md](../speaker-script.md) opening thesis aloud
- [ ] Read closing summary aloud
- [ ] Time yourself on slides 1-6 (target: 15 min)
- [ ] Review "don't elaborate" topics in speaker-script.md

---

## Before Presenting -- Diagrams

- [ ] All 6 diagrams render in PowerPoint at readable size
- [ ] Diagram labels match component names in speaker notes
- [ ] No diagram has more text than fits comfortably on a slide

---

## Before Presenting -- Demo

- [ ] Anthropic PA review skill installs successfully
- [ ] `pip install anthropic` works
- [ ] Mock data produces reasonable AI determinations
- [ ] Demo walkthrough script practiced at least once
- [ ] If Azure deployment: test the URL, confirm it responds
- [ ] If local only: confirm laptop display setup for screen sharing
- [ ] Run all mock cases -- verify 4 outcomes (approve, deny, pend, complex)
- [ ] Check response times -- should be under 30 seconds per case
- [ ] Verify confidence scores are in reasonable range (0.0-1.0)
- [ ] Verify reasoning includes evidence citations
- [ ] Have backup plan if demo fails: "Let me walk you through the architecture using the diagrams instead"

---

## Risk Awareness

### Content Accuracy Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Altais metrics (45%/54%/50%) challenged by panel | Low | Medium | Source verified: BusinessWire Feb 2026. Have URL ready. |
| CAQH cost numbers questioned | Low | Low | Source verified: 2024 CAQH Index PDF. Payer cost is $3.52 per transaction. |
| CMS-0057-F timeline questioned | Low | Medium | Phase 1 live Jan 2026, Phase 2 Jan 2027. CMS fact sheet URL ready. |
| Autonomize platform claims challenged | Medium | High | Only cite publicly verified facts (Pegasus Program, Azure Marketplace, ServiceNow partnership, SOC 2, 3 of top 5 plans). No internal platform claims. |
| Claude healthcare connectors availability via API unclear | Medium | Low | Frame as "Claude platform capability" -- demo uses Anthropic SDK tool-use pattern regardless. |

### Presentation Readiness Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Paul goes over time (known tendency) | High | Medium | Priority-tiered slides. 3-minute rule per slide. Coaching doc has time awareness tips. |
| Paul tells stories instead of answering directly | High | Medium | "Don't elaborate" flags on each slide. Pivot phrases in speaker-script.md. |
| Panel asks about FHIR Da Vinci / SMART on FHIR details | Medium | Medium | Redirect: "That's a discovery-phase activity with clinical informaticists." Don't fabricate depth. |
| Panel asks about EDI X12 parsing | Low | Low | Redirect: "Integration-build detail for discovery phase." Not in Paul's depth. |
| Panel asks about traditional ML metrics (KS, PSI) | Medium | Medium | Bridge: "Those apply if we add a triage classifier. The LLM monitoring is eval-driven, not distribution-driven." |

### Demo Readiness Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Anthropic PA review skill doesn't install or work | Medium | High | Test BEFORE the interview. Have mock data fallback. |
| Azure deployment fails | Medium | Low | Local demo is perfectly acceptable. Don't force Azure. |
| Demo doesn't match slide architecture | Low | High | Demo prompt explicitly aligned to slide narrative. Demo walkthrough script in presentation.md. |
| Panel wants to try unusual PA cases | Medium | Low | Have 3-5 mock cases covering different outcomes. Acknowledge demo uses mock data. |

### Knowledge Gap Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Suresh probes payer-specific LOB terminology | Medium | Medium | Be honest: "My payer experience is at the integration level -- I'd want to work with your clinical operations team on LOB-specific rules." |
| Ujjwal asks about TOGAF or enterprise architecture frameworks | Low | Low | Paul doesn't claim TOGAF. Redirect to practical experience: "I focus on iterative architecture -- design, validate, iterate." |
| Panel asks about Snowflake/dbt details | Low | Low | Paul has ~6 months. Mention Arine experience briefly, don't deep-dive. |
| Questions about Autonomize platform internals | High | Medium | "No public API documentation available. These are discovery questions I'd explore during onboarding." |

---

## Items Paul MUST Verify Before Presenting

1. **Read all speaker notes aloud** -- every slide. Time yourself. Flag anything that sounds unnatural.
2. **Check diagram rendering** at presentation display size -- text readability at projector resolution.
3. **Test the demo** -- PA review skill installs, mock data produces reasonable output.
4. **Review Azure-to-AWS mapping** in [study-guide.md](study-guide.md) -- be ready for Ujjwal's questions.
5. **Review assumptions and discovery questions** in [study-guide.md](study-guide.md) -- these show depth and honesty.
6. **Verify all cited URLs work** -- spot-check 5 random source links from the appendix.
7. **Practice the 60-second opening thesis** from [speaker-script.md](../speaker-script.md).
8. **Practice the 30-second closing summary** -- this is your landing point no matter what.

---

## Sign-Off

| Reviewer | Date | Status | Notes |
|----------|------|--------|-------|
| Paul Prae | | | |
