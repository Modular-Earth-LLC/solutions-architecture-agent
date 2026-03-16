#Requires -Version 5.1
<#
.SYNOPSIS
    Quick health check for the Solutions Architecture Agent setup.
.DESCRIPTION
    Read-only verification — checks plugin, venv, tests, and Desktop config.
.EXAMPLE
    .\scripts\verify.ps1
#>

$ErrorActionPreference = "Continue"
$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $repoRoot

Write-Host "`n=== Solutions Architecture Agent — Verify ===" -ForegroundColor Cyan

$checks = @()

# --- Plugin validation ---
Write-Host "`n[Plugin] Validating manifest..." -ForegroundColor Yellow
$result = & claude plugin validate $repoRoot 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "  PASS: $result" -ForegroundColor Green
    $checks += @{Name="Plugin manifest"; Status="PASS"}
} else {
    Write-Host "  FAIL: $result" -ForegroundColor Red
    $checks += @{Name="Plugin manifest"; Status="FAIL"}
}

# --- Python venv ---
Write-Host "`n[Venv] Checking Python virtual environment..." -ForegroundColor Yellow
$venvPython = Join-Path $repoRoot ".venv\Scripts\python.exe"
if (Test-Path $venvPython) {
    $ver = & $venvPython --version 2>&1
    Write-Host "  PASS: $ver" -ForegroundColor Green
    $checks += @{Name="Python venv"; Status="PASS"}

    # Check jsonschema is installed
    $hasJsonschema = & $venvPython -c "import jsonschema; print(jsonschema.__version__)" 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  PASS: jsonschema $hasJsonschema" -ForegroundColor Green
        $checks += @{Name="jsonschema installed"; Status="PASS"}
    } else {
        Write-Host "  FAIL: jsonschema not installed — run: .venv\Scripts\pip install -r requirements.txt" -ForegroundColor Red
        $checks += @{Name="jsonschema installed"; Status="FAIL"}
    }
} else {
    Write-Host "  FAIL: No venv at $venvPython — run: python -m venv .venv" -ForegroundColor Red
    $checks += @{Name="Python venv"; Status="FAIL"}
}

# --- Test scripts ---
Write-Host "`n[Tests] Running core validation..." -ForegroundColor Yellow
$coreTests = @(
    "tests/validate_knowledge_base.py",
    "tests/validate_consistency.py",
    "tests/test_plugin_structure.py"
)

if (Test-Path $venvPython) {
    foreach ($test in $coreTests) {
        $testPath = Join-Path $repoRoot $test
        & $venvPython $testPath 2>&1 | Out-Null
        $testName = Split-Path -Leaf $test
        if ($LASTEXITCODE -eq 0) {
            Write-Host "  PASS: $testName" -ForegroundColor Green
            $checks += @{Name=$testName; Status="PASS"}
        } else {
            Write-Host "  FAIL: $testName" -ForegroundColor Red
            $checks += @{Name=$testName; Status="FAIL"}
        }
    }
} else {
    Write-Host "  SKIP: No venv — cannot run tests" -ForegroundColor DarkYellow
}

# --- Claude Desktop config ---
Write-Host "`n[Desktop] Checking trusted folders..." -ForegroundColor Yellow
$desktopConfigPath = Join-Path $env:APPDATA "Claude\claude_desktop_config.json"
if (Test-Path $desktopConfigPath) {
    $config = Get-Content $desktopConfigPath -Raw | ConvertFrom-Json
    $trustedFolders = @()
    if ($config.PSObject.Properties["localAgentModeTrustedFolders"]) {
        $trustedFolders = @($config.localAgentModeTrustedFolders)
    }
    $normalizedRepo = $repoRoot.Replace("\", "/")
    $found = $trustedFolders | Where-Object { $_.Replace("\", "/") -eq $normalizedRepo }
    if ($found) {
        Write-Host "  PASS: Repo in trusted folders" -ForegroundColor Green
        $checks += @{Name="Desktop trusted folders"; Status="PASS"}
    } else {
        Write-Host "  FAIL: Repo not in trusted folders — run setup.ps1" -ForegroundColor Red
        $checks += @{Name="Desktop trusted folders"; Status="FAIL"}
    }
} else {
    Write-Host "  SKIP: Claude Desktop config not found" -ForegroundColor DarkYellow
    $checks += @{Name="Desktop trusted folders"; Status="SKIP"}
}

# --- Summary ---
$passCount = ($checks | Where-Object { $_.Status -eq "PASS" }).Count
$failCount = ($checks | Where-Object { $_.Status -eq "FAIL" }).Count
$skipCount = ($checks | Where-Object { $_.Status -eq "SKIP" }).Count

Write-Host "`n=== Results: $passCount PASS, $failCount FAIL, $skipCount SKIP ===" -ForegroundColor $(if ($failCount -eq 0) { "Green" } else { "Red" })
