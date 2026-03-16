#!/usr/bin/env bash
# Full automated setup — orchestrates all per-platform install scripts.
# Each script is independently runnable. Use this for one-command setup,
# or run individual scripts for targeted installation.
#
# Usage:
#   bash scripts/setup.sh
#   bash scripts/setup.sh --skip-tests

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

SKIP_TESTS=false
for arg in "$@"; do
    case "$arg" in
        --skip-tests) SKIP_TESTS=true ;;
    esac
done

echo ""
echo "=== Solutions Architecture Agent — Full Setup ==="
echo "  Running individual scripts. Each can also be run standalone."

# 1. Python dependencies
bash "$SCRIPT_DIR/install-deps.sh"

# 2. Claude Code CLI plugin
bash "$SCRIPT_DIR/install-cli.sh"

# 3. Claude Desktop — Windows-only, skip on Linux/macOS
if grep -qi microsoft /proc/version 2>/dev/null; then
    echo ""
    echo "NOTE (WSL): Claude Desktop config is on the Windows side."
    echo "  Run scripts\\install-desktop.ps1 from PowerShell to configure trusted folders."
else
    echo ""
    echo "  Skipping Claude Desktop config (not on Windows)"
fi

# 4. Run tests
if [ "$SKIP_TESTS" = false ]; then
    bash "$SCRIPT_DIR/run-tests.sh"
else
    echo ""
    echo "  Skipping tests (--skip-tests)"
fi

echo ""
echo "=== Full Setup Complete ==="
echo ""
echo "Individual scripts (run any standalone):"
echo "  bash scripts/install-deps.sh      # Python venv + requirements.txt"
echo "  bash scripts/install-cli.sh       # Claude Code CLI plugin (persistent)"
echo "  bash scripts/run-tests.sh         # All 8 validation tests"
echo "  bash scripts/verify.sh            # Quick health check (read-only)"
