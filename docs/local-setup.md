# Local Development Setup

Set up the Solutions Architecture Agent plugin across Claude Code CLI, Claude Desktop, and VS Code.

Each installation path is **fully decoupled** — install only what you need. Scripts are in `scripts/` with PowerShell (`.ps1`) and Bash (`.sh`) variants.

---

## Quick Setup (All Environments)

One command to install everything:

```powershell
# Windows PowerShell
.\scripts\setup.ps1
```

```bash
# Linux / macOS / WSL
bash scripts/setup.sh
```

Or install each target individually using the scripts below.

---

## Environment 1: Claude Code CLI

**What**: Persistent plugin installation — skills load in every `claude` session.

```powershell
# Windows PowerShell
.\scripts\install-cli.ps1
```

```bash
# Linux / macOS / WSL
bash scripts/install-cli.sh
```

This validates the plugin manifest, registers it as a local marketplace, and installs it.

**Alternative — development mode** (loads from working directory, no persistent install):

```bash
claude --plugin-dir /path/to/solutions-architecture-agent
```

**Verify**:

```bash
claude plugin validate .
claude -p "List available skills"
```

---

## Environment 2: Claude Desktop

### Code Mode

Code mode runs the Claude Code CLI as a subprocess. Persistent plugin registration (above) carries over automatically — run `install-cli` first.

### Cowork (Local Agent Mode)

Cowork discovers plugins in trusted folders. Windows only:

```powershell
.\scripts\install-desktop.ps1
```

This adds the repo to `localAgentModeTrustedFolders` in `%APPDATA%\Claude\claude_desktop_config.json` (with timestamped backup).

**Manual alternative** — edit the config directly:

```json
{
  "localAgentModeTrustedFolders": [
    "C:\\path\\to\\solutions-architecture-agent"
  ]
}
```

**Verify**: Open Claude Desktop → Code mode → type `/requirements`

---

## Environment 3: VS Code

**No installation needed.** The Claude Code extension auto-discovers `.claude-plugin/plugin.json` in workspace roots. Open the repo folder in VS Code and skills appear in the Claude Code panel.

GitHub Copilot also picks up `.github/copilot-instructions.md` automatically.

**Verify**: Open Claude Code panel → type `/requirements`

---

## Python Test Dependencies

Required for running the 8 validation test scripts. Not needed for plugin usage.

```powershell
# Windows PowerShell
.\scripts\install-deps.ps1
```

```bash
# Linux / macOS / WSL
bash scripts/install-deps.sh
```

### Run All Tests

```powershell
# Windows PowerShell
.\scripts\run-tests.ps1
```

```bash
# Linux / macOS / WSL
bash scripts/run-tests.sh
```

Or use VS Code: **Terminal → Run Task → Validate: All**

### Quick Health Check (read-only)

```powershell
.\scripts\verify.ps1       # Windows
```

```bash
bash scripts/verify.sh     # Linux / macOS / WSL
```

---

## Script Reference

| Script | Purpose | Platform |
|--------|---------|----------|
| `scripts/setup.ps1` / `setup.sh` | Full setup (calls all scripts below) | Windows / Unix |
| `scripts/install-deps.ps1` / `install-deps.sh` | Python venv + requirements.txt | Windows / Unix |
| `scripts/install-cli.ps1` / `install-cli.sh` | Claude Code CLI plugin (persistent) | Windows / Unix |
| `scripts/install-desktop.ps1` | Claude Desktop trusted folders | Windows only |
| `scripts/run-tests.ps1` / `run-tests.sh` | All 8 validation test scripts | Windows / Unix |
| `scripts/verify.ps1` / `verify.sh` | Quick health check (read-only) | Windows / Unix |

All scripts are idempotent — safe to re-run.

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `claude: command not found` | Install Claude Code CLI: `npm install -g @anthropic-ai/claude-code` |
| `python: command not found` | Install Python 3.10+: [python.org](https://www.python.org/downloads/) |
| `No module named 'jsonschema'` | Run `install-deps` script or: `pip install -r requirements.txt` |
| Plugin not loading in CLI | Check `claude plugin validate .` passes |
| Skills not in Claude Desktop Cowork | Run `install-desktop.ps1` or manually edit Desktop config |
| VS Code doesn't see plugin | Ensure `.claude-plugin/plugin.json` exists and folder is workspace root |
