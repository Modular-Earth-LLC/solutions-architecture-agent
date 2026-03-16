#Requires -Version 5.1
<#
.SYNOPSIS
    Run all 8 validation test scripts.
.DESCRIPTION
    Runs test scripts using the .venv Python interpreter.
    Run install-deps.ps1 first if .venv does not exist.
.EXAMPLE
    .\scripts\run-tests.ps1
#>

$ErrorActionPreference = "Continue"
$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $repoRoot

Write-Host "`n=== Run Validation Tests ===" -ForegroundColor Cyan

$venvPython = Join-Path $repoRoot ".venv\Scripts\python.exe"
if (-not (Test-Path $venvPython)) {
    Write-Host "ERROR: .venv not found. Run install-deps.ps1 first." -ForegroundColor Red
    exit 1
}

$testScripts = @(
    "tests/validate_knowledge_base.py",
    "tests/validate_consistency.py",
    "tests/test_plugin_structure.py",
    "tests/test_engagement_flow.py",
    "tests/test_skill_independence.py",
    "tests/validate_well_architected.py",
    "tests/test_end_to_end_example.py",
    "tests/validate_urls.py"
)

$passed = 0
$failed = 0
foreach ($script in $testScripts) {
    $scriptPath = Join-Path $repoRoot $script
    Write-Host "`n  Running $script..." -ForegroundColor DarkCyan
    & $venvPython $scriptPath 2>&1 | ForEach-Object { Write-Host "    $_" }
    if ($LASTEXITCODE -eq 0) { $passed++ } else { $failed++ }
}

Write-Host "`n=== Tests: $passed passed, $failed failed ===" -ForegroundColor $(if ($failed -eq 0) { "Green" } else { "Red" })

if ($failed -gt 0) { exit 1 }
