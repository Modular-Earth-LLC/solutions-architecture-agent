#Requires -Version 5.1
<#
.SYNOPSIS
    Install the SA Agent as a Claude Code CLI plugin (persistent).
.DESCRIPTION
    Validates the plugin manifest, registers as a local marketplace, and installs.
    After this, the plugin loads automatically in every `claude` session.
    Idempotent — safe to re-run.
.EXAMPLE
    .\scripts\install-cli.ps1
#>

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)

Write-Host "`n=== Install Claude Code CLI Plugin ===" -ForegroundColor Cyan

# Check claude
if (-not (Get-Command claude -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: claude not found. Install Claude Code CLI and re-run." -ForegroundColor Red
    Write-Host "  npm install -g @anthropic-ai/claude-code" -ForegroundColor Yellow
    exit 1
}
Write-Host "  claude: $(claude --version 2>&1)"

# Validate
Write-Host "`n  Validating plugin manifest..."
$validateResult = & claude plugin validate $repoRoot 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Plugin validation failed:" -ForegroundColor Red
    Write-Host $validateResult -ForegroundColor Red
    exit 1
}
Write-Host "  $validateResult" -ForegroundColor Green

# Register marketplace
Write-Host "`n  Registering local marketplace..."
& claude plugin marketplace add $repoRoot 2>&1 | ForEach-Object { Write-Host "  $_" }

# Install plugin
Write-Host "`n  Installing plugin..."
& claude plugin install "solutions-architecture-agent@solutions-architecture-agent" 2>&1 | ForEach-Object { Write-Host "  $_" }

Write-Host "`nDone. Plugin loads automatically in all future claude sessions." -ForegroundColor Cyan
Write-Host "  Verify: claude -p 'List available skills'" -ForegroundColor Cyan
