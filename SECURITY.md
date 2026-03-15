# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.2.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it responsibly.

**Do NOT open a public GitHub issue for security vulnerabilities.**

Instead, please email: **security@modular-earth.com**

You should receive a response within 48 hours. We will work with you to understand the issue and coordinate a fix before any public disclosure.

## Security Considerations

This repository contains AI agent system prompts and configuration files. Key security notes:

- **Never commit secrets** (API keys, credentials, tokens) to this repository
- The `private/` directory is git-ignored for sensitive outputs — see `private/README.md`
- Agent prompts may reference external services (AWS, Anthropic, etc.) — ensure credentials are managed via environment variables or secret managers
- Review all AI-generated outputs before deploying to production
- Secret scanning and push protection are enabled on this repository
