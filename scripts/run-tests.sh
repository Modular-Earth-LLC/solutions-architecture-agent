#!/usr/bin/env bash
# Run all 8 validation test scripts.
# Run install-deps.sh first if .venv does not exist.
#
# Usage: bash scripts/run-tests.sh

set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

echo ""
echo "=== Run Validation Tests ==="

VENV_PYTHON="$REPO_ROOT/.venv/bin/python"
if [ ! -f "$VENV_PYTHON" ]; then
    echo "ERROR: .venv not found. Run install-deps.sh first."
    exit 1
fi

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
echo "=== Tests: $passed passed, $failed failed ==="

if [ "$failed" -gt 0 ]; then exit 1; fi
