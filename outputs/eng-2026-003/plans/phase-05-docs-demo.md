# Phase 5: Docs and Demo

**Goal:** Write comprehensive README with embedded images, generate demo data with 4+ SKU briefs, publish the repo publicly with `v1.0.0` tag, and prepare the demo script.

**Minimum state after this phase:** `github.com/praeducer/pai-take-home-exercise` shows README with embedded images. CI/CD badge green. Demo rehearsable in ≤5 minutes. **G-005 passed.** The exercise is complete.

---

## Prerequisites Checklist

- [ ] `phase-04-complete.md` exists
- [ ] GitHub Actions `ci.yml` shows green on main (G-004 passed)
- [ ] All 3 aspect ratios working, 2+ products per run (G-003 passed)
- [ ] `git status` shows clean working tree

**Load prior context:** Read `phase-01-complete.md` through `phase-04-complete.md`. The README and demo data must use actual values: real S3 bucket names, actual model IDs, confirmed aspect ratio dimensions.

---

## Architecture Decisions for This Phase

| Decision | Value |
|---------|-------|
| Demo model tier | `final` (Nova Canvas $0.04/image) for showcase quality |
| Demo briefs | 4 SKU briefs in `inputs/demo_briefs/` covering distinct product types and regions |
| README images | Committed to `outputs/demo/` in repo (PNG files, ~1-5MB each) |
| Demo script | 5-step, ≤5 minutes total, in `docs/demo-script.md` |
| Version tag | `v1.0.0` on final commit after G-005 approval |
| BACKLOG | `BACKLOG.md` in repo root — honest about PoC limitations |

---

## Tasks

### Task 1: Write `README.md`

Required sections (in this order):

```markdown
# PAI Packaging Automation PoC

[![CI](https://github.com/praeducer/pai-take-home-exercise/actions/workflows/ci.yml/badge.svg)](...)

## Overview
What this does in 3 sentences: GenAI packaging image generation pipeline, Bedrock + Pillow,
Claude Code interface, 3 aspect ratios, S3 output.

## Architecture
Brief description + key components table (C-001 through C-008 at minimum, mention C-009/C-010/C-011/C-012).
Optional: Mermaid diagram of data flow.

## Quick Start (5-minute setup)
1. Prerequisites (Python 3.12, AWS CLI, Claude Code)
2. `pip install -r requirements.txt`
3. `aws configure --profile pai-exercise`
4. Enable Bedrock model access in AWS console (Nova Canvas, Titan V2, Claude Sonnet 4.6)
5. `aws cloudformation deploy --stack-name pai-exercise --template-file infra/cloudformation/stack.yaml --capabilities CAPABILITY_IAM --profile pai-exercise`
6. `/run-pipeline inputs/sample_sku_brief.json`

## Example Input
Show `inputs/sample_sku_brief.json` as code block.

## Example Output
Embed 3-6 generated images (from `outputs/demo/`):
![Trail Mix Front Label](outputs/demo/organic-trail-mix-us/front_label/original.png)
![Trail Mix Back Label](outputs/demo/organic-trail-mix-us/back_label/original.png)
etc.

## Claude Code Skills
Table of all 8 skills with invocation and purpose.

## Design Decisions
8-10 decisions with brief rationale (see design-decisions.md for deep-dive):
- Nova Canvas over SD3.5 Large (model availability: us-east-1)
- Flat JSON manifests over PostgreSQL (PoC scope; database is BACKLOG)
- Claude Code skills over argparse CLI (zero UI development, better developer experience)
- anthropic[bedrock] over boto3 InvokeModel (cleaner API, same IAM permissions)
- CloudFormation over Terraform/CDK (self-contained, no extra tooling for PoC)
- S3 only (no Lambda) — local execution sufficient for PoC scope
- Image caching via content hash (avoids re-generation cost during dev iterations)
- GitHub Actions (must-have CI/CD, not nice-to-have)

## Assumptions and Limitations
Be honest:
- Text overlay coordinates are tuned for English product names. Different languages/lengths may need adjustment.
- No real regulatory compliance database — uses synthesized placeholder text.
- PoC scope: single-user, local execution, no production auto-scaling.
- Image quality suitable for demonstration; not validated against real Adobe packaging standards.
- Bedrock model access requires manual console enablement — cannot be automated.

## Backlog
Link to BACKLOG.md.
```

**Acceptance:** README renders correctly at `github.com/praeducer/pai-take-home-exercise`. All sections present. Images visible in browser.

---

### Task 2: Write `BACKLOG.md`

```markdown
# BACKLOG — PAI Packaging Automation

Items explicitly deferred from the PoC scope. Prioritized for production evolution.

## High Priority (Phase 2 — Production MVP)
- **PostgreSQL on RDS** — structured run history, approval tracking, audit trail
- **Regulatory compliance database** — real regulatory requirements by region (not synthesized JSON)
- **stability.sd3-5-large-v1:0** — SD3.5 Large when us-east-1 availability confirmed; benchmark vs Nova Canvas
- **Content moderation** — Amazon Rekognition DetectModerationLabels on generated images before S3 storage
- **CloudTrail audit logging** — S3 and Bedrock API call audit trail

## Medium Priority (Phase 3 — Quality and Scale)
- **Amazon QuickSight dashboard** — analytics on generated images, approval rates, cost per run
- **Multi-language localization** — Japanese, Spanish, French beyond English text overlay
- **Fine-tuned image models** — brand-specific style consistency (requires training data)
- **A/B testing pipeline** — variant comparison framework for packaging decisions

## Low Priority (Phase 4 — Production Operations)
- **Lambda + API Gateway** — serverless execution for production auto-scaling
- **Web dashboard UI** — non-technical marketing stakeholder interface
- **Brand asset library integration** — DAM (Digital Asset Management) connector
- **Real-time WebSocket progress** — live generation status for long-running jobs
```

**Acceptance:** BACKLOG.md present with at least 10 items organized by priority.

---

### Task 3: Write `docs/design-decisions.md`

Deep-dive technical decisions for interviewers who want to go deeper:

```markdown
# Design Decisions — PAI Packaging Automation PoC

## Model Selection: Nova Canvas over SD3.5 Large

**Decision:** Primary model is `amazon.nova-canvas-v1:0` (Nova Canvas).
**Why not SD3.5 Large:** `stability.sd3-5-large-v1:0` is only available in us-west-2.
Nova Canvas is available in us-east-1. No cross-region inference profile exists for SD3.5 Large as of 2026-03.

**Nova Canvas benchmark evidence:**
- TIFA score: 0.897 (text-image fidelity alignment)
- ImageReward: 1.250 (human preference alignment)
- Source: Amazon Nova Technical Report (arxiv 2506.12103v1, 2025)
- Built-in inpainting/outpainting for future enhancements

## Interface: Claude Code Skills over argparse

**Decision:** 8 Claude Code custom skills replace all CLI/argparse interaction.
**Why:** Zero UI development time. Better developer experience (natural language invocations).
Positions AI-native tooling as the primary interface pattern. Hooks enforce code quality automatically.

## Storage: Flat JSON over PostgreSQL

**Decision:** Pipeline manifests stored as flat JSON files (S3 + local `outputs/runs/`). No database.
**Why for PoC:** PostgreSQL adds setup complexity (RDS, schema migrations, connection pooling)
disproportionate to PoC requirements. Flat JSON is sufficient for 10-100 runs per session.
**Production path:** PostgreSQL on RDS documented in BACKLOG.md Phase 2.

## Text Reasoning: anthropic[bedrock] over boto3 InvokeModel

**Decision:** `AnthropicBedrock(aws_region='us-east-1')` for Claude Sonnet 4.6 calls.
**Why:** Cleaner messages API vs raw JSON body serialization in boto3. Same IAM `bedrock:InvokeModel`
permission. No additional credentials required.
**Caveat:** Does NOT auto-read `~/.aws/config` for region — `aws_region` must be explicit.

## IaC: CloudFormation over Terraform/CDK

**Decision:** CloudFormation YAML (`infra/cloudformation/stack.yaml`).
**Why:** Self-contained, no additional tooling (no npm, no Terraform binary).
Native AWS service. Sufficient for 3 resources (S3×2, IAM). CDK adds Node.js dependency complexity
for a PoC that has 1 stack with 3 resources.

## CI/CD: Must-Have, Not Nice-To-Have

**Decision:** GitHub Actions ci.yml + deploy.yml are must-have (FR-009 v2.0), not bonus.
**Why:** Demonstrates production engineering maturity. Auto-lint hook catches regressions.
pip-audit in CI closes security finding F-003. SHA-pinned actions close T-015 supply chain risk.

## Text Overlay: Pillow over Server-Side Rendering

**Decision:** Pillow (PIL) for all text compositing.
**Why:** Zero additional services. Runs locally and in CI. Sufficient precision for PoC
(coordinate tuning documented in `phase-03-complete.md`). Production alternative:
ImageMagick + font subsetting or canvas-based web rendering.
```

**Acceptance:** docs/design-decisions.md present with at least 6 decisions explained with rationale and evidence.

---

### Task 4: Generate Demo Data (4+ SKU Briefs)

Create `inputs/demo_briefs/` with 4 distinct brief files:

**`inputs/demo_briefs/trail-mix-us.json`:** Organic Trail Mix, US market, 2 flavors (Original, Dark Chocolate). Attributes: organic, non-gmo, high-protein.

**`inputs/demo_briefs/granola-bar-latam.json`:** Granola Energy Bar, LATAM market, 2 flavors (Honey Oat, Tropical Fruit). Attributes: whole-grain, natural-flavors, no-preservatives.

**`inputs/demo_briefs/energy-drink-apac.json`:** Natural Energy Drink, APAC market, 2 variants (Original Citrus, Green Tea). Attributes: natural-caffeine, vitamin-b, sugar-free.

**`inputs/demo_briefs/protein-bar-eu.json`:** Plant Protein Bar, EU market, 2 variants (Vanilla Almond, Cocoa Hazelnut). Attributes: vegan, 20g-protein, gluten-free.

Then run:
```bash
for brief in inputs/demo_briefs/*.json; do
    PAI_OUTPUT_BUCKET={output-bucket} \
    python -m src.pipeline.run_pipeline "$brief" --model-tier final --profile pai-exercise
done
```

Expected: 4 briefs × 2 products × 3 ratios = **24 images** in S3.

**Acceptance:** `aws s3 ls s3://{output-bucket}/ --recursive --profile pai-exercise | wc -l` shows ≥24 image files.

---

### Task 5: Download Demo Images to `outputs/demo/`

```bash
mkdir -p outputs/demo
aws s3 cp s3://{output-bucket}/ outputs/demo/ --recursive \
  --exclude "*manifest.json" \
  --profile pai-exercise
```

Select the best 3-6 images (varied products and ratios) to embed in README:
- `outputs/demo/organic-trail-mix-us/us-west/front_label/original.png`
- `outputs/demo/organic-trail-mix-us/us-west/back_label/original.png`
- `outputs/demo/granola-bar-latam/{region}/front_label/honey-oat.png`

Add to README.md:
```markdown
## Example Output

### Organic Trail Mix — Front Label (1:1)
![Front Label](outputs/demo/organic-trail-mix-us/us-west/front_label/original.png)

### Organic Trail Mix — Back Label (9:16)
![Back Label](outputs/demo/organic-trail-mix-us/us-west/back_label/original.png)
```

**Acceptance:** Images render in GitHub README preview (`gh browse` or visit GitHub URL).

---

### Task 6: Update `/generate-demo` Skill

Update `.claude/skills/generate-demo.md` to be functional:

```markdown
---
name: generate-demo
description: Run the PAI pipeline for all demo SKU briefs with final-tier quality images
---

# /generate-demo

Generates a full demo dataset using all 4 demo SKU briefs at final-tier quality (Nova Canvas).

## What it does

Runs `/run-pipeline` for each brief in `inputs/demo_briefs/`:
1. trail-mix-us.json
2. granola-bar-latam.json
3. energy-drink-apac.json
4. protein-bar-eu.json

Expected output: 24 images (4 SKUs × 2 products × 3 ratios) in S3.
Expected cost: ~$1.92 (24 images × $0.04 each at Nova Canvas standard quality).

## Usage

`/generate-demo`

No arguments required. Uses `--model-tier final` automatically.
```

**Acceptance:** Skill file clear and accurate.

---

### Task 7: Write `docs/demo-script.md`

```markdown
# Demo Script — 5-Minute Flow

## Step 1: Architecture Overview (1 minute)
- Open README on github.com — point to embedded images
- "This is an AI packaging design pipeline: JSON brief in, packaging images out."
- Point to key decisions: Nova Canvas model, Claude Code interface, flat JSON, CloudFormation

## Step 2: Show the Code (1 minute)
- Open `src/pipeline/run_pipeline.py` — "This is the orchestrator, 60 lines"
- Open `.claude/skills/run-pipeline.md` — "This is the interface layer, replaces argparse"
- Open `infra/cloudformation/stack.yaml` — "This deploys everything: S3 × 2, IAM, Budget alarm"

## Step 3: Run the Pipeline (2 minutes)
```
/run-pipeline inputs/sample_sku_brief.json --model-tier dev
```
While it runs: "Titan V2 dev tier, $0.12 for 6 images. Switch to final tier for Nova Canvas quality."
After completion: "6 images in S3, organized by product and aspect ratio."

## Step 4: View Results (30 seconds)
```
/view-results organic-trail-mix-us
```
Open front_label and back_label images — show text overlay.

## Step 5: Show CI/CD (30 seconds)
- Open GitHub Actions tab: "Green on every push. Lint + tests + pip-audit. CloudFormation deploy on main."
- "This is how I would run it in production too — same pipeline, same confidence."
```

**Acceptance:** Demo script readable in <60 seconds and each step is executable.

---

### Task 8: Final Commit and Tag

```bash
git add .
git commit -m "feat(phase-05): docs, demo data, demo script — exercise complete"
git push origin main

git tag v1.0.0 -m "PoC complete — all PAI exercise requirements met"
git push origin v1.0.0
```

**Acceptance:** `github.com/praeducer/pai-take-home-exercise/releases/tag/v1.0.0` exists.

---

## Automated Verification

```bash
# Lint still passing with new files
ruff check src/ tests/

# Tests still passing
pytest tests/ -v -m "not integration"

# Demo briefs generate without error
PAI_DRY_RUN=1 python -m src.pipeline.run_pipeline inputs/demo_briefs/trail-mix-us.json --dry-run
PAI_DRY_RUN=1 python -m src.pipeline.run_pipeline inputs/demo_briefs/granola-bar-latam.json --dry-run

# Tag exists
git tag -l "v1.0.0"
# Expected: v1.0.0
```

---

## Human Gate

Paul reviews:

1. **Visit `github.com/praeducer/pai-take-home-exercise`** — README loads with embedded product images
2. **Check CI/CD badge** in README — shows green
3. **Verify README completeness:**
   - [ ] Setup instructions are accurate and runnable
   - [ ] Design decisions are explained (not just listed)
   - [ ] Assumptions/limitations are honest
   - [ ] BACKLOG.md linked
4. **Rehearse demo script** — 5-step flow executes in ≤5 minutes

**Gate question:** "Is this repo something you'd be proud to show an interview panel?"

**THIS IS THE END OF THE REQUIRED EXERCISE.** G-005 passed. Phase 6 (Enhancements) is optional bonus only.

---

## Exit Protocol

1. **Save context snapshot:** Write `phase-05-complete.md`:
   ```markdown
   # Phase 5 Complete — Exercise Requirements Met

   **Repo URL:** https://github.com/praeducer/pai-take-home-exercise
   **Release tag:** https://github.com/praeducer/pai-take-home-exercise/releases/tag/v1.0.0
   **Demo images generated:** 24 (4 briefs × 2 products × 3 ratios)
   **Demo script location:** docs/demo-script.md
   **CI badge:** green
   **Deviations:** [none / list any]
   ```

2. **Final push is already done** (in Task 8 above)

3. **Signal complete:** "Phase 5 complete — G-005 passed. All exercise requirements met. Repo submitted. Phase 6 available if time allows."
