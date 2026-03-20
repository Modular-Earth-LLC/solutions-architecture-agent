#!/bin/bash
# SessionStart hook: Verify remote session readiness
# Checks that the environment is configured for remote iOS control

set -euo pipefail

LOG_PREFIX="[session-remote-ready]"

# Verify Claude Code version supports remote control (>= 2.1.51)
CLAUDE_VERSION=$(claude --version 2>/dev/null | grep -oP '[\d.]+' | head -1 || echo "0.0.0")
MAJOR=$(echo "$CLAUDE_VERSION" | cut -d. -f1)
MINOR=$(echo "$CLAUDE_VERSION" | cut -d. -f2)
PATCH=$(echo "$CLAUDE_VERSION" | cut -d. -f3)

if [[ "$MAJOR" -lt 2 ]] || { [[ "$MAJOR" -eq 2 ]] && [[ "$MINOR" -lt 1 ]]; } || { [[ "$MAJOR" -eq 2 ]] && [[ "$MINOR" -eq 1 ]] && [[ "$PATCH" -lt 51 ]]; }; then
  echo "$LOG_PREFIX WARNING: Claude Code version $CLAUDE_VERSION may not support remote control. Requires >= 2.1.51" >&2
fi

# Check that telemetry/traffic is not disabled (required for remote control)
if [[ -n "${CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC:-}" ]]; then
  echo "$LOG_PREFIX WARNING: CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC is set. Remote control requires this to be unset." >&2
fi

if [[ -n "${DISABLE_TELEMETRY:-}" ]]; then
  echo "$LOG_PREFIX WARNING: DISABLE_TELEMETRY is set. Remote control requires this to be unset." >&2
fi

# Verify git repo is clean enough for session work
if git rev-parse --git-dir >/dev/null 2>&1; then
  BRANCH=$(git branch --show-current 2>/dev/null || echo "detached")
  echo "$LOG_PREFIX Session started on branch: $BRANCH"
  echo "$LOG_PREFIX Remote iOS control ready. Connect via Claude mobile app or claude.ai/code"
else
  echo "$LOG_PREFIX WARNING: Not in a git repository. Some features may be limited." >&2
fi

exit 0
