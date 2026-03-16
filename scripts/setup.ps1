#Requires -Version 5.1
<#
.SYNOPSIS
    Automated setup for the Solutions Architecture Agent plugin.
.DESCRIPTION
    Idempotent setup script that:
    1. Checks prerequisites (claude, python, git)
    2. Creates/updates Python venv and installs dependencies
    3. Validates the plugin manifest
    4. Registers as a local marketplace and installs the plugin
    5. Optionally adds the repo to Claude Desktop trusted folders
    6. Runs all test scripts
.EXAMPLE
    .\scripts\setup.ps1
    .\scripts\setup.ps1 -SkipDesktop
#>
param(
    [switch]$SkipDesktop,
    [switch]$SkipTests
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $repoRoot

Write-Host "`n=== Solutions Architecture Agent — Setup ===" -ForegroundColor Cyan

# --- 1. Prerequisites ---
Write-Host "`n[1/7] Checking prerequisites..." -ForegroundColor Yellow

$missing = @()
foreach ($cmd in @("claude", "python", "git")) {
    if (-not (Get-Command $cmd -ErrorAction SilentlyContinue)) {
        $missing += $cmd
    }
}
if ($missing.Count -gt 0) {
    Write-Host "ERROR: Missing required commands: $($missing -join ', ')" -ForegroundColor Red
    Write-Host "Install them and re-run this script." -ForegroundColor Red
    exit 1
}

$claudeVersion = & claude --version 2>&1
$pythonVersion = & python --version 2>&1
$gitVersion = & git --version 2>&1
Write-Host "  claude: $claudeVersion"
Write-Host "  python: $pythonVersion"
Write-Host "  git:    $gitVersion"

# --- 2. Python venv + dependencies ---
Write-Host "`n[2/7] Setting up Python virtual environment..." -ForegroundColor Yellow

$venvPath = Join-Path $repoRoot ".venv"
if (-not (Test-Path (Join-Path $venvPath "Scripts\python.exe"))) {
    Write-Host "  Creating venv at $venvPath..."
    & python -m venv $venvPath
} else {
    Write-Host "  Venv already exists at $venvPath"
}

$venvPython = Join-Path $venvPath "Scripts\python.exe"
Write-Host "  Installing dependencies from requirements.txt..."
& $venvPython -m pip install -r (Join-Path $repoRoot "requirements.txt") --quiet

# --- 3. Plugin validation ---
Write-Host "`n[3/7] Validating plugin manifest..." -ForegroundColor Yellow

$validateResult = & claude plugin validate $repoRoot 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Plugin validation failed:" -ForegroundColor Red
    Write-Host $validateResult -ForegroundColor Red
    exit 1
}
Write-Host "  $validateResult" -ForegroundColor Green

# --- 4. Register marketplace + install plugin ---
Write-Host "`n[4/7] Registering local marketplace..." -ForegroundColor Yellow

& claude plugin marketplace add $repoRoot 2>&1 | ForEach-Object { Write-Host "  $_" }

Write-Host "`n[5/7] Installing plugin from marketplace..." -ForegroundColor Yellow

& claude plugin install "solutions-architecture-agent@solutions-architecture-agent" 2>&1 | ForEach-Object { Write-Host "  $_" }

# --- 5. Claude Desktop trusted folders ---
if (-not $SkipDesktop) {
    Write-Host "`n[6/7] Configuring Claude Desktop trusted folders..." -ForegroundColor Yellow

    $desktopConfigPath = Join-Path $env:APPDATA "Claude\claude_desktop_config.json"
    if (Test-Path $desktopConfigPath) {
        $config = Get-Content $desktopConfigPath -Raw | ConvertFrom-Json

        $trustedFolders = @()
        if ($config.PSObject.Properties["localAgentModeTrustedFolders"]) {
            $trustedFolders = @($config.localAgentModeTrustedFolders)
        }

        $normalizedRepo = $repoRoot.Replace("\", "/")
        $alreadyTrusted = $trustedFolders | Where-Object { $_.Replace("\", "/") -eq $normalizedRepo }

        if ($alreadyTrusted) {
            Write-Host "  Already in trusted folders" -ForegroundColor Green
        } else {
            # Backup before modifying
            $backupPath = "$desktopConfigPath.backup.$(Get-Date -Format 'yyyyMMdd-HHmmss')"
            Copy-Item $desktopConfigPath $backupPath
            Write-Host "  Backed up config to $backupPath"

            $trustedFolders += $repoRoot
            $config | Add-Member -NotePropertyName "localAgentModeTrustedFolders" -NotePropertyValue $trustedFolders -Force
            $config | ConvertTo-Json -Depth 10 | Set-Content $desktopConfigPath -Encoding UTF8
            Write-Host "  Added $repoRoot to localAgentModeTrustedFolders" -ForegroundColor Green
        }
    } else {
        Write-Host "  Claude Desktop config not found at $desktopConfigPath — skipping" -ForegroundColor DarkYellow
    }
} else {
    Write-Host "`n[6/7] Skipping Claude Desktop config (--SkipDesktop)" -ForegroundColor DarkYellow
}

# --- 6. Run tests ---
if (-not $SkipTests) {
    Write-Host "`n[7/7] Running validation tests..." -ForegroundColor Yellow

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

    Write-Host "`n  Tests: $passed passed, $failed failed" -ForegroundColor $(if ($failed -eq 0) { "Green" } else { "Red" })
} else {
    Write-Host "`n[7/7] Skipping tests (--SkipTests)" -ForegroundColor DarkYellow
}

# --- Summary ---
Write-Host "`n=== Setup Complete ===" -ForegroundColor Cyan
Write-Host @"

Verification commands:
  claude plugin validate .                              # Plugin manifest OK
  claude --plugin-dir . -p "What skills do you have?"   # Plugin loads in CLI
  .venv\Scripts\python.exe tests\validate_knowledge_base.py  # Tests pass

Environments:
  Claude Code CLI:  claude --plugin-dir $repoRoot
  VS Code:          Open $repoRoot in VS Code — auto-discovered
  Claude Desktop:   Code mode uses CLI; Cowork uses trusted folders
"@
