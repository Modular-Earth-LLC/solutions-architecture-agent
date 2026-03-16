#!/usr/bin/env bash
# Automated setup for the Solutions Architecture Agent plugin.
#
# Idempotent — safe to re-run.
#
# Usage:
#   bash scripts/setup.sh
#   bash scripts/setup.sh --skip-tests

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

SKIP_TESTS=false
for arg in "$@"; do
    case "$arg" in
        --skip-tests) SKIP_TESTS=true ;;
    esac
done

echo ""
echo "=== Solutions Architecture Agent — Setup ==="

# --- 1. Prerequisites ---
echo ""
echo "[1/6] Checking prerequisites..."

missing=()
for cmd in claude python3 git; do
    if ! command -v "$cmd" &>/dev/null; then
        missing+=("$cmd")
    fi
done

if [ ${#missing[@]} -gt 0 ]; then
    echo "ERROR: Missing required commands: ${missing[*]}"
    exit 1
fi

echo "  claude: $(claude --version 2>&1)"
echo "  python: $(python3 --version 2>&1)"
echo "  git:    $(git --version 2>&1)"

# --- 2. Python venv + dependencies ---
echo ""
echo "[2/6] Setting up Python virtual environment..."

VENV_PATH="$REPO_ROOT/.venv"
if [ ! -f "$VENV_PATH/bin/python" ]; then
    echo "  Creating venv at $VENV_PATH..."
    python3 -m venv "$VENV_PATH"
else
    echo "  Venv already exists at $VENV_PATH"
fi

VENV_PYTHON="$VENV_PATH/bin/python"
echo "  Installing dependencies from requirements.txt..."
"$VENV_PYTHON" -m pip install -r "$REPO_ROOT/requirements.txt" --quiet

# --- 3. Plugin validation ---
echo ""
echo "[3/6] Validating plugin manifest..."

validate_result=$(claude plugin validate "$REPO_ROOT" 2>&1) || {
    echo "ERROR: Plugin validation failed:"
    echo "$validate_result"
    exit 1
}
echo "  $validate_result"

# --- 4. Register marketplace + install plugin ---
echo ""
echo "[4/6] Registering local marketplace..."
claude plugin marketplace add "$REPO_ROOT" 2>&1 | sed 's/^/  /'

echo ""
echo "[5/6] Installing plugin from marketplace..."
claude plugin install "solutions-architecture-agent@solutions-architecture-agent" 2>&1 | sed 's/^/  /'

# --- 5. Run tests ---
if [ "$SKIP_TESTS" = false ]; then
    echo ""
    echo "[6/6] Running validation tests..."

    test_scripts=(
        "tests/validate_knowledge_base.py"
        "tests/validate_consistency.py"
        "tests/test_plugin_structure.py"
        "tests/test_engagement_flow.py"
        "tests/test_skill_independence.py"
        "tests/validate_well_architected.py"
        "tests/test_end_to_end_example.py"
        "tests/validate_urls.py"
    )

    passed=0
    failed=0
    for script in "${test_scripts[@]}"; do
        echo ""
        echo "  Running $script..."
        if "$VENV_PYTHON" "$REPO_ROOT/$script" 2>&1 | sed 's/^/    /'; then
            ((passed++))
        else
            ((failed++))
        fi
    done

    echo ""
    echo "  Tests: $passed passed, $failed failed"
else
    echo ""
    echo "[6/6] Skipping tests (--skip-tests)"
fi

# --- WSL note ---
if grep -qi microsoft /proc/version 2>/dev/null; then
    echo ""
    echo "NOTE (WSL): Claude Desktop config is on the Windows side."
    echo "  To add this repo to trusted folders, run setup.ps1 from PowerShell,"
    echo "  or manually edit %APPDATA%\\Claude\\claude_desktop_config.json"
fi

# --- Summary ---
echo ""
echo "=== Setup Complete ==="
echo ""
echo "Verification commands:"
echo "  claude plugin validate .                              # Plugin manifest OK"
echo "  claude --plugin-dir . -p \"What skills do you have?\"   # Plugin loads in CLI"
echo "  .venv/bin/python tests/validate_knowledge_base.py     # Tests pass"
echo ""
echo "Environments:"
echo "  Claude Code CLI:  claude --plugin-dir $REPO_ROOT"
echo "  VS Code:          Open $REPO_ROOT in VS Code — auto-discovered"
echo "  Claude Desktop:   Run setup.ps1 on Windows for trusted folder config"
