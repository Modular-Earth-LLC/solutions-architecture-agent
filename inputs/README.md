# Inputs

Drop engagement source materials here. This directory is **gitignored** — contents stay local and are never committed.

## What Goes Here

- Assignment briefs and case studies (PDF, DOCX, MD)
- Client-provided documentation (system specs, API docs, org charts)
- Job descriptions or interview context
- Reference architectures from clients
- Meeting notes or transcripts
- Personal career/profile data for voice calibration

## How the Agent Uses Inputs

During **scope negotiation**, the agent asks:
> "Do you have a personal profile or career context to load?"

Point it to files in this directory:
```
/architecture --depth QUICK
> Load inputs/case-study.pdf as the assignment brief
```

For the **Direct Delivery** flow, inputs are the primary context source (no KB files needed).

## Marketplace vs CLI

| Environment | How inputs are provided |
|-------------|----------------------|
| **Claude Code CLI** | File paths in `inputs/` or anywhere on disk |
| **Claude Desktop** | Paste content or attach files in the conversation |
| **Marketplace plugin** | Via `$ARGUMENTS` or pasted inline |

## Parallel to outputs/

| Directory | Purpose | Gitignored |
|-----------|---------|------------|
| `inputs/` | Source materials (client data, assignments) | Yes |
| `outputs/` | Generated deliverables (proposals, docs) | Partially (engagement-specific) |
| `knowledge_base/` | Intermediate KB files (JSON) | Yes (except system_config.json) |
