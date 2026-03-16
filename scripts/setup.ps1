#Requires -Version 5.1
<#
.SYNOPSIS
    Full automated setup — orchestrates all per-platform install scripts.
.DESCRIPTION
    Runs install-deps, install-cli, install-desktop, and run-tests in sequence.
    Each script is independently runnable. Use this for one-command setup,
    or run individual scripts for targeted installation.
.EXAMPLE
    .\scripts\setup.ps1
    .\scripts\setup.ps1 -SkipDesktop
    .\scripts\setup.ps1 -SkipTests
#>
param(
    [switch]$SkipDesktop,
    [switch]$SkipTests
)

$ErrorActionPreference = "Stop"
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "`n=== Solutions Architecture Agent — Full Setup ===" -ForegroundColor Cyan
Write-Host "  Running individual scripts. Each can also be run standalone.`n"

# 1. Python dependencies
& "$scriptDir\install-deps.ps1"

# 2. Claude Code CLI plugin
& "$scriptDir\install-cli.ps1"

# 3. Claude Desktop trusted folders
if (-not $SkipDesktop) {
    & "$scriptDir\install-desktop.ps1"
} else {
    Write-Host "`n  Skipping Claude Desktop config (-SkipDesktop)" -ForegroundColor DarkYellow
}

# 4. Run tests
if (-not $SkipTests) {
    & "$scriptDir\run-tests.ps1"
} else {
    Write-Host "`n  Skipping tests (-SkipTests)" -ForegroundColor DarkYellow
}

Write-Host "`n=== Full Setup Complete ===" -ForegroundColor Cyan
Write-Host @"

Individual scripts (run any standalone):
  .\scripts\install-deps.ps1      # Python venv + requirements.txt
  .\scripts\install-cli.ps1       # Claude Code CLI plugin (persistent)
  .\scripts\install-desktop.ps1   # Claude Desktop trusted folders
  .\scripts\run-tests.ps1         # All 8 validation tests
  .\scripts\verify.ps1            # Quick health check (read-only)
"@
