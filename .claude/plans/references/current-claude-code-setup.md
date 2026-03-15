# Current Claude Code CLI Setup Reference

## User Environment

- **OS**: Windows 11 Pro for Workstations
- **Shell**: bash (Git Bash / WSL)
- **Model**: Claude Opus 4.6 (1M context)
- **Working directories**: `C:\dev\`, `\\wsl.localhost\Ubuntu\home\praeducer\dev`, `D:\dev`
- **GitHub user**: @paulpham157 (Modular-Earth-LLC org)

## Active Plugins

| Plugin | Purpose |
|--------|---------|
| superpowers | Brainstorming, TDD, debugging, plans, verification |
| feature-dev | Feature architecture, exploration, review |
| commit-commands | Git commit, push, PR workflows |
| pr-review-toolkit | PR review with specialized agents |
| code-review | Code review |
| code-simplifier | Code simplification |
| claude-md-management | CLAUDE.md auditing and improvement |
| claude-code-setup | Automation recommendations |
| skill-creator | Skill creation and testing |
| agent-sdk-dev | Agent SDK application development |
| frontend-design | Frontend interface design |
| Notion | Task management and documentation |
| vercel | Deployment to Vercel |
| supabase | Database operations |
| security-guidance | Security best practices |
| github | GitHub operations |
| typescript-lsp | TypeScript language server |
| rust-analyzer-lsp | Rust language server |

## MCP Servers (from Claude.ai)

- Microsoft Learn — documentation search
- bioRxiv — preprint search
- Mermaid Chart — diagram rendering
- PubMed — article search
- Vercel — deployment management

## Key Integration Points

When building skills for this project, leverage:
1. **superpowers plugin** — brainstorming and planning workflows
2. **skill-creator plugin** — to build and test new skills
3. **agent-sdk-dev plugin** — for cloud deployment packaging
4. **Notion plugin** — task tracking integration
5. **commit-commands** — automated git workflows
