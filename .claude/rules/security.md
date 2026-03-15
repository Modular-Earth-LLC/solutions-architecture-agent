---
paths:
  - "private/**/*"
  - "**/.env*"
  - "**/*credential*"
  - "**/*secret*"
---

# Security Rules

- Never commit API keys, tokens, credentials, or PII to this repository
- The `private/` directory is for local sensitive outputs — its contents are git-ignored
- Use environment variables or secret managers for all credentials
- Review all AI-generated outputs before sharing externally
- Secret scanning and push protection are enabled on the GitHub repository
