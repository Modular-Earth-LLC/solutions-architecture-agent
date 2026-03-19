# Phase 1: Foundation

**Goal:** Set up the complete development environment, repository, and AWS infrastructure so that the implementation agent can write pipeline code immediately. No application code in this phase — foundation only.

**Minimum state after this phase:** `aws cloudformation describe-stacks --stack-name pai-exercise` returns `CREATE_COMPLETE` and Bedrock model access is confirmed (G-001 passed).

---

## Prerequisites Checklist

Complete ALL of these before starting Phase 1:

- [ ] AWS account available (ID: `730007904340`)
- [ ] Bedrock model access enabled in AWS console — Request access for ALL of:
  - `amazon.nova-canvas-v1:0` (Nova Canvas)
  - `amazon.titan-image-generator-v2:0` (Titan Image Generator V2)
  - `anthropic.claude-sonnet-4-6` (Claude Sonnet 4.6)
- [ ] `aws configure --profile pai-exercise` complete → `aws sts get-caller-identity --profile pai-exercise` returns `730007904340`
- [ ] `gh auth status` shows authenticated as `praeducer` → if not: `gh auth login --web`
- [ ] Python 3.12 available: `python --version` returns `3.12.x`
- [ ] `uv` available for MCP server execution: `uv --version` → if not: `pip install uv` (Node.js is NOT required — AWS MCP servers use `uv tool run`)
- [ ] Git Bash or WSL available: `git --version` returns `2.x`
- [ ] `uv` available: `uv --version` → if not: `pip install uv`

---

## Architecture Decisions for This Phase

| Decision | Value |
|---------|-------|
| Region | `us-east-1` |
| Primary image model | `amazon.nova-canvas-v1:0` |
| Dev/fallback model | `amazon.titan-image-generator-v2:0` |
| Text reasoning model | `anthropic.claude-sonnet-4-6` |
| IaC | CloudFormation YAML (self-contained) |
| Interface | Claude Code custom skills (8 stubs in this phase) |
| Credentials | AWS CLI named profile `pai-exercise` |
| MCP transport | `uv tool run` (Python packages, NOT npm) |
| Repo | `praeducer/pai-take-home-exercise` (public) |
| Local path | `C:\dev\pai-take-home-exercise` |

---

## Tasks

### Task 1: Create GitHub Repository

```bash
gh repo create praeducer/pai-take-home-exercise --public --clone --gitignore Python
cd C:/dev/pai-take-home-exercise
```

**Acceptance:** `gh repo view praeducer/pai-take-home-exercise` shows public repo; `git remote -v` shows origin pointing to GitHub.

---

### Task 2: Create Directory Structure

```bash
mkdir -p src/pipeline src/schemas tests infra/cloudformation docs inputs outputs/.gitkeep
mkdir -p .claude/skills .github/workflows
```

Copy exercise spec from SA agent:
```bash
cp C:/dev/solutions-architecture-agent/inputs/PAI-Take_Home_Exercise.md inputs/
```

**Acceptance:** All directories exist. `ls inputs/` shows `PAI-Take_Home_Exercise.md`.

---

### Task 3: Python Virtual Environment and requirements.txt

```bash
python -m venv .venv
.venv/Scripts/activate   # Windows
pip install boto3 pillow anthropic pytest ruff jsonschema pip-audit
pip freeze > requirements.txt
```

Pin exact versions. Verify `requirements.txt` includes at minimum:
- `boto3>=1.35.0`
- `Pillow>=10.0.0`
- `anthropic[bedrock]>=0.40.0`
- `pytest>=8.0.0`
- `ruff>=0.3.0`
- `jsonschema>=4.23.0`
- `pip-audit>=2.7.0`

**Acceptance:** `pip list` shows all packages. `python -c "import boto3, PIL, anthropic, jsonschema; print('deps OK')"` exits 0.

---

### Task 4: CloudFormation Stack (`infra/cloudformation/stack.yaml`)

Write a CloudFormation YAML with these resources:

**S3 Input Bucket** (`PaiAssetsInputBucket`):
- `BlockPublicAcls: true`, `IgnorePublicAcls: true`, `BlockPublicPolicy: true`, `RestrictPublicBuckets: true`
- SSE-S3 encryption (`ServerSideEncryptionConfiguration`)
- 90-day lifecycle policy (noncurrent version expiration)

**S3 Output Bucket** (`PaiPackagingOutputBucket`):
- Same Block Public Access settings as above
- SSE-S3 encryption
- Versioning enabled
- 90-day lifecycle policy

**IAM Role** (`PaiPipelineRole`):
- `s3:GetObject, s3:ListBucket, s3:HeadObject` on input bucket ARN
- `s3:PutObject, s3:GetObject, s3:ListBucket` on output bucket ARN
- `bedrock:InvokeModel` on:
  - `arn:aws:bedrock:us-east-1::foundation-model/amazon.nova-canvas-v1:0`
  - `arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-image-generator-v2:0`
  - `arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-sonnet-4-6`
- Explicit denies: `s3:DeleteObject, s3:DeleteBucket, s3:PutBucketPolicy, iam:*`

**AWS Budget** (`PaiBudgetAlarm`):
- Limit: $25 (USD), monthly
- Email notification at 80% ($20) and 100% ($25) thresholds
- Use `AWS::Budgets::Budget`

**Outputs:** `InputBucketName`, `OutputBucketName`, `PipelineRoleArn`

```bash
aws cloudformation validate-template --template-body file://infra/cloudformation/stack.yaml --profile pai-exercise
```

**Acceptance:** `validate-template` exits 0 with no errors.

---

### Task 5: Deploy CloudFormation Stack

```bash
aws cloudformation deploy \
  --stack-name pai-exercise \
  --template-file infra/cloudformation/stack.yaml \
  --capabilities CAPABILITY_IAM \
  --profile pai-exercise \
  --region us-east-1
```

**Acceptance:** `aws cloudformation describe-stacks --stack-name pai-exercise --profile pai-exercise --query 'Stacks[0].StackStatus'` returns `"CREATE_COMPLETE"`.

Extract outputs for use in future phases:
```bash
aws cloudformation describe-stacks --stack-name pai-exercise --profile pai-exercise \
  --query 'Stacks[0].Outputs' --output table
```

Save these values to `phase-01-complete.md` (see Exit Protocol).

---

### Task 6: DECISION GATE G-001 — Verify Bedrock Access

```bash
aws bedrock list-foundation-models --profile pai-exercise --region us-east-1 \
  --query 'modelSummaries[?modelId==`amazon.nova-canvas-v1:0`]'

aws bedrock list-foundation-models --profile pai-exercise --region us-east-1 \
  --query 'modelSummaries[?modelId==`anthropic.claude-sonnet-4-6`]'
```

Both commands must return non-empty results. If empty, Bedrock access has not been granted yet — wait for AWS console approval (can take minutes to hours for first-time request).

**Acceptance:** Both model IDs visible in list-foundation-models output. **G-001 PASSED.**

---

### Task 7: Create CLAUDE.md

Write `CLAUDE.md` in the repo root with:
- Project purpose: PAI Packaging Automation PoC (Adobe take-home exercise)
- Architecture summary: Nova Canvas primary model, Titan V2 dev/fallback, Claude Sonnet 4.6 text reasoning, flat JSON manifests, S3 storage, CloudFormation IaC
- Skills index: table of all 8 skills with invocation and purpose
- Workflow: typical session starts with `/health-check`, then `/run-pipeline`
- Key decisions: region (us-east-1), no argparse, no database, AI-assisted development
- AWS profile: `pai-exercise`

**Acceptance:** CLAUDE.md exists with all sections.

---

### Task 8: Scaffold 8 Claude Code Skills in `.claude/skills/`

Create one markdown file per skill with YAML frontmatter:

```markdown
---
name: run-pipeline
description: Run the PAI packaging image generation pipeline with a given SKU brief JSON file
---

# /run-pipeline

[stub — will be implemented in Phase 2]
```

Skills to create:
1. `run-pipeline.md` — `disable-model-invocation: false` (reads sku-brief-path argument)
2. `pipeline-status.md` — read-only, shows recent runs from outputs/runs/*.json
3. `view-results.md` — lists S3 objects under {sku_id}/{region}/, optionally opens images
4. `deploy.md` — CloudFormation deploy; add `disable-model-invocation: true`
5. `teardown.md` — CloudFormation destroy; add `disable-model-invocation: true`
6. `health-check.md` — verify AWS resources and Bedrock access
7. `run-tests.md` — execute full test suite via pytest
8. `generate-demo.md` — run pipeline with all inputs/demo_briefs/ SKU briefs

**Acceptance:** `ls .claude/skills/` shows 8 markdown files.

---

### Task 9: Create `.claude/settings.json` with Hooks

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "ruff check ${CLAUDE_TOOL_INPUT_FILE_PATH} --fix --quiet 2>/dev/null || true"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "cd C:/dev/pai-take-home-exercise && python -m pytest tests/ -v -m 'not integration' -q 2>&1 | tail -5"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "echo '⚠️  Bash command requires review. Destructive AWS commands (cloudformation delete-stack, s3 rb --force) require explicit confirmation.'"
          }
        ]
      }
    ]
  }
}
```

**Acceptance:** `.claude/settings.json` exists and is valid JSON.

---

### Task 10: Create `.mcp.json` with AWS MCP Servers

```json
{
  "mcpServers": {
    "aws-iac": {
      "command": "uv",
      "args": ["tool", "run", "awslabs.aws-iac-mcp-server@latest"],
      "env": {
        "AWS_PROFILE": "pai-exercise",
        "AWS_REGION": "us-east-1"
      }
    },
    "aws-knowledge": {
      "url": "https://mcp.awslabs.amazon.com",
      "transport": "http"
    }
  }
}
```

**Note:** `awslabs.aws-iac-mcp-server@latest` uses `uv tool run` (Python package), NOT `npx`. The AWS Knowledge MCP server uses remote HTTP transport via fastmcp proxy — no local installation required.

**Acceptance:** `.mcp.json` exists and is valid JSON.

---

### Task 11: Initial Commit and Push

```bash
git add .
git commit -m "feat(phase-01): foundation complete — AWS stack deployed, Claude Code scaffolding done"
git push origin main
```

**Acceptance:** GitHub shows repo with all directory structure, CLAUDE.md, 8 skills, .claude/settings.json, .mcp.json, requirements.txt, and CloudFormation template.

---

## Automated Verification

Run all of these before calling Phase 1 complete:

```bash
# AWS auth
aws sts get-caller-identity --profile pai-exercise

# CloudFormation stack
aws cloudformation describe-stacks --stack-name pai-exercise --profile pai-exercise \
  --query 'Stacks[0].StackStatus'
# Expected: "CREATE_COMPLETE"

# Bedrock access (G-001)
aws bedrock list-foundation-models --profile pai-exercise --region us-east-1 \
  --query 'modelSummaries[?contains(modelId, `nova-canvas`)].modelId'
# Expected: ["amazon.nova-canvas-v1:0"]

# Python dependencies
python -c "import boto3, PIL, anthropic, jsonschema; print('deps OK')"
# Expected: "deps OK"

# Skills scaffolded
ls .claude/skills/ | wc -l
# Expected: 8

# Git clean
git status
# Expected: working tree clean after push
```

---

## Human Gate

After all automated verifications pass, present to Paul:

- CloudFormation stack outputs: input bucket name, output bucket name, IAM role ARN
- Bedrock model access confirmation (both nova-canvas-v1:0 and claude-sonnet-4-6 visible)
- GitHub repo URL: `github.com/praeducer/pai-take-home-exercise`

**Gate question:** "Bedrock access confirmed for all 3 required models? Stack outputs look correct?"

Paul approves → proceed to Phase 2. Paul needs to wait for Bedrock access → pause here.

---

## Exit Protocol

1. **Save context snapshot:** Write `phase-01-complete.md` in repo root with:
   ```markdown
   # Phase 1 Complete

   **Date:** [actual date]
   **Stack name:** pai-exercise
   **Input bucket name:** [from CF outputs]
   **Output bucket name:** [from CF outputs]
   **IAM role ARN:** [from CF outputs]
   **Region:** us-east-1
   **Models confirmed accessible:**
   - amazon.nova-canvas-v1:0 ✓
   - amazon.titan-image-generator-v2:0 ✓
   - anthropic.claude-sonnet-4-6 ✓
   **AWS profile:** pai-exercise
   **Deviations from plan:** [none / list any]
   ```

2. **Update future phases:** Replace `{output-bucket}` and `{input-bucket}` placeholders in phases 2-6 with actual bucket names from CloudFormation outputs.

3. **Commit:** `git commit -m "feat(phase-01): phase complete — context snapshot saved"`

4. **Push:** `git push origin main`

5. **Signal Phase 2 ready:** "Phase 1 complete — G-001 passed. Ready for Phase 2: Core Pipeline."
