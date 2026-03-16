#Requires -Version 5.1
<#
.SYNOPSIS
    Add this repo to Claude Desktop's trusted folders for Cowork (Local Agent Mode).
.DESCRIPTION
    Reads claude_desktop_config.json, adds the repo path to localAgentModeTrustedFolders
    if not already present, and writes back with a timestamped backup.
    Windows-only — Claude Desktop config lives on the Windows filesystem.
    Idempotent — safe to re-run.
.EXAMPLE
    .\scripts\install-desktop.ps1
#>

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)

Write-Host "`n=== Configure Claude Desktop Trusted Folders ===" -ForegroundColor Cyan

$desktopConfigPath = Join-Path $env:APPDATA "Claude\claude_desktop_config.json"

if (-not (Test-Path $desktopConfigPath)) {
    Write-Host "  Claude Desktop config not found at:" -ForegroundColor DarkYellow
    Write-Host "    $desktopConfigPath" -ForegroundColor DarkYellow
    Write-Host "  Install Claude Desktop first, or create the config manually." -ForegroundColor DarkYellow
    exit 0
}

$config = Get-Content $desktopConfigPath -Raw | ConvertFrom-Json

$trustedFolders = @()
if ($config.PSObject.Properties["localAgentModeTrustedFolders"]) {
    $trustedFolders = @($config.localAgentModeTrustedFolders)
}

$normalizedRepo = $repoRoot.Replace("\", "/")
$alreadyTrusted = $trustedFolders | Where-Object { $_.Replace("\", "/") -eq $normalizedRepo }

if ($alreadyTrusted) {
    Write-Host "  Already in trusted folders — no changes needed." -ForegroundColor Green
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

Write-Host "`nDone. Restart Claude Desktop for changes to take effect." -ForegroundColor Cyan
Write-Host "  Verify: Open Claude Desktop -> Code mode -> type /requirements" -ForegroundColor Cyan
