# GitHub Copilot Optimization Guide

This repository is optimized for Claude Code CLI as primary and GitHub Copilot as a strong secondary copilot for implementation, CI/CD, and repository operations.

## What Is Configured In-Repo

- `.github/copilot-instructions.md`: Repository-specific Copilot behavior and safety constraints
- `.vscode/settings.json`: Workspace defaults tuned for Copilot-assisted editing
- `.vscode/extensions.json`: Recommended extension set for this codebase
- `.vscode/tasks.json`: One-click validation tasks for consistency, knowledge base, and URL checks

## One-Time Local Setup (VS Code)

1. Install recommended extensions from `.vscode/extensions.json`.
2. Sign in to GitHub and ensure Copilot + Copilot Chat are active.
3. Open this repository root as the workspace folder.
4. Confirm Copilot chat can read workspace context (`@workspace`).

## Recommended Personal User Settings

Add these to your VS Code user settings (not committed) to specialize your personal workflow:

```json
{
  "chat.agent.enabled": true,
  "chat.tools.autoApprove": false,
  "github.copilot.nextEditSuggestions.enabled": true,
  "editor.inlineSuggest.suppressSuggestions": false
}
```

If a setting is unavailable in your VS Code version, remove it and keep the rest.

## Best Prompting Pattern For This Repo

Use this structure in Copilot Chat for highest-quality outputs:

1. Goal: One sentence with business outcome.
2. Scope: Exact files/directories to touch.
3. Constraints: Security, architecture, and validation requirements.
4. Done criteria: Tests or validation commands to pass.

Example:

```text
Goal: Migrate one legacy agent capability into a skill.
Scope: .claude/skills/, docs/, no ai_agents changes.
Constraints: Keep system_config read-only; no secrets; small reversible diff.
Done criteria: update docs and pass python tests/validate_consistency.py.
```

## Validation Commands

Run after relevant edits:

```bash
python tests/validate_consistency.py
python tests/validate_knowledge_base.py
python tests/validate_urls.py
```

Or run VS Code task `Validate: All` from Run Task.

## Guardrails To Keep Enabled

- Never commit secrets or sensitive data.
- Keep `knowledge_base/system_config.json` unchanged.
- Prefer adding skills under `.claude/skills/` over adding new agents.
- Keep changes minimal and easy to review.

## Troubleshooting

- Copilot gives generic answers: mention exact file paths and ask for a minimal diff.
- Suggestions ignore repo conventions: reference `.github/copilot-instructions.md` in your prompt.
- Too much noise: narrow scope to a single directory and single validation command.
