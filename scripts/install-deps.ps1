#Requires -Version 5.1
<#
.SYNOPSIS
    Set up Python virtual environment and install test dependencies.
.DESCRIPTION
    Creates a .venv in the repo root (if missing) and installs requirements.txt.
    Idempotent — safe to re-run.
.EXAMPLE
    .\scripts\install-deps.ps1
#>

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)

Write-Host "`n=== Install Python Dependencies ===" -ForegroundColor Cyan

# Check python
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: python not found. Install Python 3.10+ and re-run." -ForegroundColor Red
    exit 1
}
Write-Host "  python: $(python --version 2>&1)"

# Create or reuse venv
$venvPath = Join-Path $repoRoot ".venv"
if (-not (Test-Path (Join-Path $venvPath "Scripts\python.exe"))) {
    Write-Host "  Creating venv at $venvPath..."
    & python -m venv $venvPath
} else {
    Write-Host "  Venv already exists at $venvPath"
}

# Install deps
$venvPython = Join-Path $venvPath "Scripts\python.exe"
Write-Host "  Installing dependencies from requirements.txt..."
& $venvPython -m pip install -r (Join-Path $repoRoot "requirements.txt") --quiet
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: pip install failed" -ForegroundColor Red
    exit 1
}

# Verify
$jsVer = & $venvPython -c "import jsonschema; print(jsonschema.__version__)" 2>&1
Write-Host "  jsonschema $jsVer installed" -ForegroundColor Green
Write-Host "`nDone. Activate with: .venv\Scripts\activate" -ForegroundColor Cyan
