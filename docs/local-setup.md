# Local Development Setup

Set up the Solutions Architecture Agent plugin across Claude Code CLI, Claude Desktop, and VS Code.

---

## Quick Setup (Automated)

```powershell
# Windows PowerShell
.\scripts\setup.ps1
```

```bash
# WSL / Linux / macOS
bash scripts/setup.sh
```

The setup script checks prerequisites, creates a Python venv, validates the plugin, registers it as a local marketplace, installs it persistently, and runs all tests.

---

## Environment 1: Claude Code CLI

### Development Mode (recommended while developing)

Loads the plugin directly from the repo — changes take effect immediately:

```bash
cd C:\dev\solutions-architecture-agent
claude --plugin-dir .
```

### Persistent Installation

Register the repo as a local marketplace and install:

```bash
claude plugin marketplace add C:\dev\solutions-architecture-agent
claude plugin install solutions-architecture-agent@solutions-architecture-agent
```

After persistent installation, the plugin loads automatically in every `claude` session without `--plugin-dir`.

### Verification

```bash
claude plugin validate .
claude --plugin-dir . -p "List available skills"
```

---

## Environment 2: Claude Desktop

### Code Mode

Code mode runs the Claude Code CLI as a subprocess. Persistent plugin registration (above) carries over automatically.

### Cowork (Local Agent Mode)

Cowork discovers plugins in trusted folders. Add this repo:

1. Open `%APPDATA%\Claude\claude_desktop_config.json`
2. Add to (or create) `localAgentModeTrustedFolders`:

```json
{
  "localAgentModeTrustedFolders": [
    "C:\\dev\\solutions-architecture-agent"
  ]
}
```

The `setup.ps1` script does this automatically (with backup).

### Verification

Open Claude Desktop → Code mode → type `/requirements`

---

## Environment 3: VS Code

### Claude Code Panel

The Claude Code extension auto-discovers `.claude-plugin/plugin.json` in workspace roots. Open the repo folder in VS Code — no registration needed.

### GitHub Copilot

`.github/copilot-instructions.md` provides project context automatically when Copilot is active.

### Verification

Open Claude Code panel in VS Code → type `/requirements`

---

## Python Test Environment

### Setup

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
```

### Run All Tests

```bash
python tests/validate_knowledge_base.py
python tests/validate_consistency.py
python tests/test_plugin_structure.py
python tests/test_engagement_flow.py
python tests/test_skill_independence.py
python tests/validate_well_architected.py
python tests/test_end_to_end_example.py
python tests/validate_urls.py
```

Or use the VS Code task runner: **Terminal → Run Task → Validate: All**

### Quick Health Check

```powershell
.\scripts\verify.ps1
```

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `claude: command not found` | Install Claude Code CLI: `npm install -g @anthropic-ai/claude-code` |
| `No module named 'jsonschema'` | Activate venv and install: `pip install -r requirements.txt` |
| Plugin not loading in CLI | Check `claude plugin validate .` passes |
| Skills not in Claude Desktop Cowork | Verify `localAgentModeTrustedFolders` in Desktop config |
| VS Code doesn't see plugin | Ensure `.claude-plugin/plugin.json` exists and folder is workspace root |
