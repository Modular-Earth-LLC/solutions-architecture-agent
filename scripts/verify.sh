#!/usr/bin/env bash
# Quick health check for the Solutions Architecture Agent setup.
# Read-only — does not modify anything.
#
# Usage: bash scripts/verify.sh

set -uo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

echo ""
echo "=== Solutions Architecture Agent — Verify ==="

pass=0
fail=0
skip=0

check() {
    local name="$1" status="$2"
    case "$status" in
        PASS) echo "  PASS: $name"; ((pass++)) ;;
        FAIL) echo "  FAIL: $name"; ((fail++)) ;;
        SKIP) echo "  SKIP: $name"; ((skip++)) ;;
    esac
}

# --- Plugin validation ---
echo ""
echo "[Plugin] Validating manifest..."
if command -v claude &>/dev/null; then
    if claude plugin validate "$REPO_ROOT" &>/dev/null; then
        check "Plugin manifest" "PASS"
    else
        check "Plugin manifest" "FAIL"
    fi
else
    check "Plugin manifest (claude not installed)" "SKIP"
fi

# --- Python venv ---
echo ""
echo "[Venv] Checking Python virtual environment..."
VENV_PYTHON="$REPO_ROOT/.venv/bin/python"
if [ -f "$VENV_PYTHON" ]; then
    check "Python venv ($($VENV_PYTHON --version 2>&1))" "PASS"
    if "$VENV_PYTHON" -c "import jsonschema" &>/dev/null; then
        JS_VER=$("$VENV_PYTHON" -c "import jsonschema; print(jsonschema.__version__)" 2>&1)
        check "jsonschema $JS_VER" "PASS"
    else
        check "jsonschema not installed" "FAIL"
    fi
else
    check "Python venv (.venv not found)" "FAIL"
fi

# --- Core tests ---
echo ""
echo "[Tests] Running core validation..."
if [ -f "$VENV_PYTHON" ]; then
    for test in tests/validate_knowledge_base.py tests/validate_consistency.py tests/test_plugin_structure.py; do
        name=$(basename "$test")
        if "$VENV_PYTHON" "$REPO_ROOT/$test" &>/dev/null; then
            check "$name" "PASS"
        else
            check "$name" "FAIL"
        fi
    done
else
    check "Tests (no venv)" "SKIP"
fi

# --- Summary ---
echo ""
echo "=== Results: $pass PASS, $fail FAIL, $skip SKIP ==="
