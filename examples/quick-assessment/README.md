# Quick Assessment Example

This example demonstrates the **Direct Delivery** flow with QUICK depth — the fastest path for single-document deliverables.

## Scenario

A Solutions Architect needs to produce a ~10-page solution architecture document for an interview case study. The assignment is to propose a modernization approach for a legacy system.

## How It Was Produced

```
User: "Write a 10-page solution architecture for modernizing a legacy healthcare claims system.
       Target audience: interview panel. --depth QUICK"

Agent: [scope negotiation → Direct Delivery flow → single /architecture QUICK pass → output]
```

## Key Differences from STANDARD

| Aspect | QUICK | STANDARD |
|--------|-------|----------|
| KB files produced | 0 | 8-10 JSON files |
| Sub-agents invoked | 0 | 12-18 (WA + STRIDE) |
| Output | Single markdown document | KB files + assembled proposal |
| Target time | <30 minutes | 2-8 hours |
| Depth | Executive + 1 diagram + tech stack | Full WA scoring, STRIDE, data models |

## Files

- `engagement.json` — Minimal engagement envelope (QUICK depth)
- `output.md` — The final deliverable (single document)

## Validation

This example is used by `tests/test_output_quality.py` to verify QUICK-depth output stays within length constraints.
