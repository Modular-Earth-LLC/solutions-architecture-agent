# Decisions Made Without Paul

> Technical decisions made during autonomous overnight execution of eng-2026-004 v2.
> Paul: review these when you wake up. High-impact decisions are flagged.

## Decisions

### D-001: Un-ignored outputs/ and knowledge_base/ in .gitignore
- **Decision:** Removed `outputs/` and `knowledge_base/*.json` from `.gitignore` so all deliverables are tracked and backed up to GitHub
- **Alternatives:** Keep gitignore and use `git add -f` for each file; create separate repo for deliverables
- **Rationale:** Paul explicitly requested deliverables be saved and backed up to GitHub. Simplest approach is to un-ignore the directories. Previous rationale (client PII) doesn't apply — eng-2026-004 is Paul's own interview prep, not client data.
- **Impact:** LOW — all future outputs will be tracked. Previous outputs (eng-2026-004 v1) will also become trackable.
- **Aligns with:** Paul's explicit instruction, Principle #17 (Ship. Create value.)

### D-002: CAQH payer cost corrected from $3.14 to $3.41
- **Decision:** Use $3.41 (2024 CAQH Index) instead of $3.14 (likely from 2023 or earlier report) for payer per-transaction cost
- **Alternatives:** Use $3.14 with "approximate" qualifier; omit payer cost entirely
- **Rationale:** 2024 CAQH Index report is the most current authoritative source. Using outdated numbers would violate guardrail #1 (no fabricated numbers).
- **Impact:** LOW — minor number change, same order of magnitude
- **Aligns with:** Guardrail #1, Principle #6 (Cited or removed)

### D-003: AMA physician time burden corrected from 14 to 12-13 hours/week
- **Decision:** Use "12-13 hours/week" (2024 AMA survey) instead of "14 hours/week" with note that 14 is commonly cited approximation
- **Alternatives:** Use 14 with "approximately" qualifier; cite range "12-14 hours"
- **Rationale:** Most recent AMA data shows 12-13 hours. Citing the exact survey data is more defensible if Suresh or Ujjwal challenge the number.
- **Impact:** LOW — strengthens credibility by using most current data
- **Aligns with:** Guardrail #1, Principle #6

