#!/usr/bin/env bash
# Install the SA Agent as a Claude Code CLI plugin (persistent).
# Validates, registers as local marketplace, and installs.
# Idempotent — safe to re-run.
#
# Usage: bash scripts/install-cli.sh

set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo ""
echo "=== Install Claude Code CLI Plugin ==="

# Check claude
if ! command -v claude &>/dev/null; then
    echo "ERROR: claude not found. Install Claude Code CLI and re-run."
    echo "  npm install -g @anthropic-ai/claude-code"
    exit 1
fi
echo "  claude: $(claude --version 2>&1)"

# Validate
echo ""
echo "  Validating plugin manifest..."
validate_result=$(claude plugin validate "$REPO_ROOT" 2>&1) || {
    echo "ERROR: Plugin validation failed:"
    echo "$validate_result"
    exit 1
}
echo "  $validate_result"

# Register marketplace
echo ""
echo "  Registering local marketplace..."
claude plugin marketplace add "$REPO_ROOT" 2>&1 | sed 's/^/  /'

# Install plugin
echo ""
echo "  Installing plugin..."
claude plugin install "solutions-architecture-agent@solutions-architecture-agent" 2>&1 | sed 's/^/  /'

echo ""
echo "Done. Plugin loads automatically in all future claude sessions."
echo "  Verify: claude -p 'List available skills'"
