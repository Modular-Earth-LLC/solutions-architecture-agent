# Local Development Setup

Set up the Solutions Architecture Agent plugin across Claude Code CLI, Claude Desktop, and VS Code.

Each installation path is **fully decoupled** — install only what you need.

---

## Quick Setup (All Environments)

Install the Claude Code CLI if you haven't already:

```bash
npm install -g @anthropic-ai/claude-code
```

Then activate the plugin in development mode (loads from working directory):

```bash
claude --plugin-dir .
```

---

## Environment 1: Claude Code CLI

**What**: Development mode — skills load from the working directory for the current session.

```bash
claude --plugin-dir /path/to/solutions-architecture-agent
```

**Persistent installation** — register as a local marketplace plugin:

```bash
claude plugin install .
```

**Verify**:

```bash
claude plugin validate .
claude -p "List available skills"
```

---

## Environment 2: Claude Desktop

### Code Mode

Code mode runs the Claude Code CLI as a subprocess. Persistent plugin registration (above) carries over automatically — run `claude plugin install .` first.

### Cowork (Local Agent Mode)

Cowork discovers plugins in trusted folders. Add the repo to trusted folders by editing `%APPDATA%\Claude\claude_desktop_config.json`:

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

**Verify**: Open Claude Code panel → type `/requirements`

---

## Python Test Dependencies

Required for running the validation test scripts. Not needed for plugin usage.

```bash
uv sync
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
python tests/test_workflow_validation.py
python tests/test_output_quality.py
```

### Quick Health Check (read-only)

```bash
python tests/validate_consistency.py
```

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `claude: command not found` | Install Claude Code CLI: `npm install -g @anthropic-ai/claude-code` |
| `python: command not found` | Install [uv](https://docs.astral.sh/uv/) which manages Python automatically |
| `No module named 'jsonschema'` | Run: `uv sync` |
| Plugin not loading in CLI | Check `claude plugin validate .` passes |
| Skills not in Claude Desktop Cowork | Manually edit Desktop config per Environment 2 above |
| VS Code doesn't see plugin | Ensure `.claude-plugin/plugin.json` exists and folder is workspace root |
