# Risk Assessment — Interview Outcome
## eng-2026-004 v2 | March 24, 2026

> **For Paul:** Review this before presenting. These are risks to the INTERVIEW outcome, not project delivery risks.

---

## Content Accuracy Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Altais metrics (45%/54%/50%) challenged by panel | Low | Medium | Source verified: BusinessWire Feb 2026. Have URL ready. |
| CAQH cost numbers questioned | Low | Low | Source verified: 2024 CAQH Index PDF. Note: payer cost is $3.41 (not $3.14 from earlier reports). |
| CMS-0057-F timeline questioned | Low | Medium | Phase 1 live Jan 2026, Phase 2 Jan 2027. CMS fact sheet URL ready. |
| Autonomize platform claims challenged | Medium | High | Only cite publicly verified facts (Pegasus Program, Azure Marketplace, ServiceNow partnership, SOC 2, 3 of top 5 plans). No internal platform claims. |
| Claude healthcare connectors availability via API unclear | Medium | Low | Frame as "Claude platform capability" — demo uses Anthropic SDK tool-use pattern regardless. |

## Presentation Readiness Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Paul goes over time (known tendency) | High | Medium | Priority-tiered slides. 3-minute rule per slide. Coaching doc has time awareness tips. |
| Paul tells stories instead of answering directly | High | Medium | "Don't elaborate" flags on each slide. Pivot phrases in coaching doc. |
| Panel asks about FHIR Da Vinci / SMART on FHIR details | Medium | Medium | Redirect: "That's a discovery-phase activity with clinical informaticists." Don't fabricate depth. |
| Panel asks about EDI X12 parsing | Low | Low | Redirect: "Integration-build detail for discovery phase." Not in Paul's depth. |
| Panel asks about traditional ML metrics (KS, PSI) | Medium | Medium | Bridge: "Those apply if we add a triage classifier. The LLM monitoring is eval-driven, not distribution-driven." |

## Demo Readiness Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Anthropic PA review skill doesn't install or work | Medium | High | Test BEFORE the interview. Have mock data fallback. |
| Azure deployment fails | Medium | Low | Local demo is perfectly acceptable. Don't force Azure. |
| Demo doesn't match slide architecture | Low | High | Demo prompt explicitly aligned to slide narrative. Demo walkthrough script in proposal.md. |
| Panel wants to try unusual PA cases | Medium | Low | Have 3-5 mock cases covering different outcomes. Acknowledge demo uses mock data. |

## Knowledge Gap Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Suresh probes payer-specific LOB terminology | Medium | Medium | Be honest: "My payer experience is at the integration level — I'd want to work with your clinical operations team on LOB-specific rules." |
| Ujjwal asks about TOGAF or enterprise architecture frameworks | Low | Low | Paul doesn't claim TOGAF. Redirect to practical experience: "I focus on iterative architecture — design, validate, iterate." |
| Panel asks about Snowflake/dbt details | Low | Low | Paul has ~6 months. Mention Arine experience briefly, don't deep-dive. |
| Questions about Autonomize platform internals | High | Medium | "No public API documentation available. These are discovery questions I'd explore during onboarding." |

## Items Paul MUST Verify Before Presenting

1. **Read all speaker notes aloud** — every slide. Time yourself. Flag anything that sounds unnatural.
2. **Check diagram rendering** at presentation display size — text readability at projector resolution.
3. **Test the demo** — PA review skill installs, mock data produces reasonable output.
4. **Review Azure↔AWS mapping** in interview-prep/azure-aws-mapping.md — be ready for Ujjwal's questions.
5. **Review assumptions-and-questions.md** — these show depth and honesty.
6. **Verify all cited URLs work** — spot-check 5 random source links from the appendix.
7. **Practice the 60-second opening thesis** from presentation-coaching.md.
8. **Practice the 30-second closing summary** — this is your landing point no matter what.

## Overnight Decisions Requiring Review

See `outputs/eng-2026-004-v2/plans/decisions-made-without-paul.md` for 3 decisions made during autonomous execution:
- D-001: Un-ignored outputs/ in .gitignore (your explicit request)
- D-002: CAQH payer cost corrected $3.14 → $3.41
- D-003: AMA physician burden corrected 14 → 12-13 hours/week
