#!/usr/bin/env bash
# Set up Python virtual environment and install test dependencies.
# Idempotent — safe to re-run.
#
# Usage: bash scripts/install-deps.sh

set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo ""
echo "=== Install Python Dependencies ==="

# Check python
if ! command -v python3 &>/dev/null; then
    echo "ERROR: python3 not found. Install Python 3.10+ and re-run."
    exit 1
fi
echo "  python: $(python3 --version 2>&1)"

# Create or reuse venv
VENV_PATH="$REPO_ROOT/.venv"
if [ ! -f "$VENV_PATH/bin/python" ]; then
    echo "  Creating venv at $VENV_PATH..."
    python3 -m venv "$VENV_PATH"
else
    echo "  Venv already exists at $VENV_PATH"
fi

# Install deps
VENV_PYTHON="$VENV_PATH/bin/python"
echo "  Installing dependencies from requirements.txt..."
"$VENV_PYTHON" -m pip install -r "$REPO_ROOT/requirements.txt" --quiet

# Verify
JS_VER=$("$VENV_PYTHON" -c "import jsonschema; print(jsonschema.__version__)" 2>&1)
echo "  jsonschema $JS_VER installed"
echo ""
echo "Done. Activate with: source .venv/bin/activate"
