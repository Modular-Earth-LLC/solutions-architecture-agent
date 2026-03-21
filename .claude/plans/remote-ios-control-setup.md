# Remote Desktop ↔ iOS Control Setup

## Overview
This document captures the configuration for controlling a Claude Code desktop session remotely from an iOS device using the Claude mobile app.

## Prerequisites
- Claude Code >= v2.1.51 (current: v2.1.80)
- Pro, Max, Team, or Enterprise plan
- Authentication via `/login` to claude.ai (not API key)
- Claude iOS app installed: https://apps.apple.com/us/app/claude-by-anthropic/id6473753684

## What Was Configured

### 1. Project Settings (`.claude/settings.json`)
- Added `Bash(claude *)` permission for CLI management commands
- Added `SessionStart` hook → `hooks/session-remote-ready.sh`
  - Verifies Claude Code version supports remote control
  - Checks no environment variables block remote connectivity
  - Logs branch and readiness status on each session start

### 2. Session Readiness Hook (`hooks/session-remote-ready.sh`)
- Validates version >= 2.1.51
- Warns if `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` or `DISABLE_TELEMETRY` are set
- Reports current git branch on session start
- Non-blocking (warnings only, never blocks session start)

### 3. User-Level Settings (`~/.claude/settings.json`)
- `Stop` hook ensures all changes are committed and pushed before session ends
- `Skill` permission allowed globally

## How to Connect from iOS

### On Desktop (already running)
1. In the active Claude Code session, run: `/remote-control`
   - Or start with: `claude --remote-control "SA Agent"`
2. A QR code and URL will be displayed

### On iOS
1. Open the Claude iOS app
2. Either:
   - Scan the QR code shown in the desktop terminal
   - Navigate to your session list at claude.ai/code
   - Open the session URL directly in Safari
3. You now have full remote control of the desktop session

### Server Mode (for persistent background sessions)
```bash
claude remote-control --name "SA Agent" --spawn worktree --capacity 4
```

## Security Model
- All traffic over TLS through Anthropic API
- No inbound ports opened on desktop
- Short-lived, purpose-scoped credentials
- Local files never leave the machine
- Same permission model as local sessions

## Troubleshooting
| Issue | Fix |
|-------|-----|
| "Remote Control is not yet enabled" | Unset `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` and `DISABLE_TELEMETRY` |
| "Disabled by organization policy" | Admin must enable at claude.ai/admin-settings/claude-code |
| Session disconnects | Terminal must stay open; extended outage >10min causes timeout |
| Can't find session on iOS | Ensure same claude.ai account on both devices |

## Multi-Device Sync
- Messages sync across terminal, browser, and phone
- One session, multiple viewers
- Desktop remains the execution environment
- Full access to local filesystem, MCP servers, and project config from all surfaces
