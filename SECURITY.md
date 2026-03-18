# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.1.0   | :white_check_mark: |

Previously supported: 0.2.x, 0.1.x (no longer receiving security updates).

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it responsibly.

**Do NOT open a public GitHub issue for security vulnerabilities.**

Instead, please email: **paul@modularearth.com**

You should receive a response within 48 hours. We will work with you to understand the issue and coordinate a fix before any public disclosure.

## Security Considerations

This repository contains AI agent system prompts and configuration files. Key security notes:

- **Never commit secrets** (API keys, credentials, tokens) to this repository
- Agent prompts may reference external services (AWS, Anthropic, etc.) — ensure credentials are managed via environment variables or secret managers
- Review all AI-generated outputs before deploying to production
- Secret scanning and push protection are enabled on this repository

### Rate Limiting

The SA agent makes no outbound API calls itself — all API calls are made by the Claude Code runtime. Rate limiting should be applied at the host level (Claude Code CLI or Claude API settings). Consult Anthropic's rate limit documentation for current limits.

### PII in Knowledge Base Files

KB files (`knowledge_base/*.json`) and assembled outputs (`outputs/`) may contain client names, system details, and proprietary architecture decisions. Per-engagement handling:

- Add `knowledge_base/*.json` and `outputs/` to `.gitignore` when working on client engagements
- Mark these directories as private in your repository settings
- Never commit client-identifying information to public repositories

### Prompt Injection

For cloud deployments where end-users provide input text that is passed to skills, sanitize client-provided input before passing to skill invocations. Untrusted input should be validated and escaped to prevent prompt injection attacks that could alter agent behavior or exfiltrate KB data.
