# UAT Checklist — v2
## eng-2026-004 v2 | March 24, 2026

> **For Paul:** Work through this checklist before sending the email and before presenting.

---

## Phase 0 Technical Decisions — All Resolved

| ID | Decision | Chosen Option | Status |
|----|----------|---------------|--------|
| TD-1 | Cloud platform | Azure-primary, generic-first | RESOLVED |
| TD-2 | AI platform | Integrate Autonomize PA Copilot | RESOLVED |
| TD-3 | Message queue | Azure Service Bus (Kafka as future) | RESOLVED |
| TD-4 | FHIR depth | R4 label only, limited depth | RESOLVED |
| TD-5 | AI monitoring | LLM evals + guardrails + human feedback | RESOLVED |
| TD-6 | Auto-determination | Altais benchmark, configurable threshold | RESOLVED |
| TD-7 | Estimates | No dollar amounts, no FTE counts | RESOLVED |

---

## Review Before Sending Email

- [ ] Read `email-draft.md` — personalize tone, check formality level
- [ ] Verify demo link placeholder is updated (or remove if demo not deployed)
- [ ] Confirm attachment includes slide deck (PowerPoint or PDF)
- [ ] Confirm diagram PNGs render at readable size
- [ ] Spell-check: Paul Prae, www.paulprae.com (never misspelled)
- [ ] Check panel names spelled correctly: Kris Nair, Suresh Gopalakrishnan, Ujjwal Rajbhandari
- [ ] Mention Solutions Architecture Agent in email (already in draft)

## Review Before Presenting

### Content Accuracy
- [ ] Verify Altais metrics: 45% review time reduction, 54% error reduction, 50% auto-approval
- [ ] Verify CAQH numbers: $10.97 provider, $3.41 payer, ~$0.05 automated (2024 Index)
- [ ] Verify CMS-0057-F: Phase 1 live Jan 2026, Phase 2 Jan 2027
- [ ] Verify Autonomize: Pegasus Program (Nov 2025), Azure Marketplace, ServiceNow partnership (Mar 2026)
- [ ] Spot-check 5 source URLs from appendix — all should load

### Azure Services (verify names are current)
- [ ] Azure AI Foundry (not "Azure OpenAI Service" — rebranded)
- [ ] Azure AI Document Intelligence (not "Form Recognizer" — rebranded)
- [ ] Microsoft Entra ID (not "Azure AD" — rebranded)
- [ ] Azure Health Data Services (not "Azure API for FHIR" — evolved)
- [ ] Azure Container Apps (confirm still GA, not deprecated)

### Speaker Notes
- [ ] Read every speaker note aloud — flag unnatural phrasing
- [ ] Time yourself on Tier A slides (target: 15 minutes total for 6 slides)
- [ ] Practice 60-second opening thesis from coaching doc
- [ ] Practice 30-second closing summary
- [ ] Review "don't elaborate" flags — know your stop points

### Diagrams
- [ ] All 6 diagrams render in PowerPoint at readable size
- [ ] Diagram labels match component names in speaker notes
- [ ] No diagram has more text than fits comfortably on a slide

### Demo Readiness
- [ ] Anthropic PA review skill installs successfully
- [ ] `pip install anthropic` works
- [ ] Mock data produces reasonable AI determinations
- [ ] Demo walkthrough script practiced at least once
- [ ] If Azure deployment: test the URL, confirm it responds
- [ ] If local only: confirm laptop display setup for screen sharing

## Review Before Demo (if time permits)

- [ ] Run all mock cases — verify 4 outcomes (approve, deny, pend, complex)
- [ ] Check response times — should be under 30 seconds per case
- [ ] Verify confidence scores are in reasonable range (0.0-1.0)
- [ ] Verify reasoning includes evidence citations
- [ ] Have backup plan if demo fails: "Let me walk you through the architecture using the diagrams instead"

---

## Sign-Off

| Reviewer | Date | Status | Notes |
|----------|------|--------|-------|
| Paul Prae | | | |

---

## Decisions Made Overnight (Review Required)

See `plans/decisions-made-without-paul.md`:
- [x] D-001: outputs/ un-ignored in .gitignore — Paul requested this
- [ ] D-002: CAQH payer cost $3.14 → $3.41 — verify you're comfortable with this change
- [ ] D-003: AMA physician burden 14 → 12-13 hr/week — verify you're comfortable with this change
