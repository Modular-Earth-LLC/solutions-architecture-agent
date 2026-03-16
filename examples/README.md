# Example Engagements

Sample outputs from validated end-to-end skill runs. Use these to understand what each skill produces and how KB files accumulate through an engagement flow.

---

## Healthcare IBMi Migration

**Engagement**: `eng-2026-001`
**Type**: Migration (legacy modernization)
**Flow**: Full 9-skill lifecycle
**Domain**: Healthcare IBMi RPG system modernization for 500+ users, HIPAA-compliant

### Files

| File | Skill | Description |
|------|-------|-------------|
| `engagement.json` | All | Engagement envelope with lifecycle state tracking |
| `requirements.json` | `/requirements` | Comprehensive discovery: 15 stakeholder concerns, 18 functional reqs, HIPAA compliance |
| `architecture.json` | `/architecture` | Strangler fig pattern, NestJS + React + PostgreSQL, WA scores (7.3 overall) |
| `data_model.json` | `/data-model` | 12 entities, IBMi-to-PostgreSQL mapping, audit trail, HIPAA retention |
| `security_review.json` | `/security-review` | 18 STRIDE threats, HIPAA compliance matrix, defense-in-depth architecture |
| `integration_plan.json` | `/integration-plan` | 8 API contracts, IBMi ODBC bridge, strangler fig migration strategy |
| `estimate.json` | `/estimate` | 8-person team, 5-phase delivery, $680K-$850K range |
| `project_plan.json` | `/project-plan` | 36-week roadmap, 18 sprints, 6 milestones, critical path analysis |
| `reviews.json` | `/review` | 3-iteration review, 5 dimensions, 7.6/10 overall score |
| `proposal.md` | `/proposal` | Implementation SOW with all 12 sections |

### Validation

All KB files validate against their schemas:

```bash
python tests/validate_knowledge_base.py  # Expected: 11 PASS, 0 FAIL
```

### How to Explore

- Start with `engagement.json` for the engagement overview
- Read `requirements.json` → `architecture.json` to see how context flows downstream
- Compare `architecture.json` fields against `knowledge_base/schemas/architecture.schema.json`
- Read `proposal.md` for the final client-facing deliverable

**Key fields in every KB file**:
- `$depends_on` — lists which upstream KB files this skill read as input
- `engagement_id` — shared identifier linking all files in one engagement
- `version` — MAJOR.MINOR iteration count (increments on re-runs)
- `status` — `draft` → `in_progress` → `complete` → `approved`
- `lifecycle_state` (in `engagement.json`) — tracks the status of every skill's output
