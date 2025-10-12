# CI/CD Examples (Optional)

This directory contains **optional** CI/CD configuration examples for different platforms.

**The framework itself is platform-agnostic** - these are just examples you can use if you want automated validation.

## Available Examples

### GitHub Actions
- **File**: `github-actions-example.yml`
- **Usage**: Copy to `.github/workflows/validate-knowledge-base.yml` to enable
- **Purpose**: Validates knowledge base JSON files against schemas on commits
- **Status**: Disabled by default (manual trigger only)

### Other Platforms

You can adapt the validation script (`tests/validate_knowledge_base.py` or `tests/validate_consistency.py`) for any CI/CD platform:

- **GitLab CI**: Create `.gitlab-ci.yml`
- **Azure Pipelines**: Create `azure-pipelines.yml`
- **Jenkins**: Create `Jenkinsfile`
- **CircleCI**: Create `.circleci/config.yml`
- **Self-hosted**: Run validation scripts manually or via cron

## Platform-Agnostic Validation

The validation scripts themselves work anywhere:

```bash
# Run locally
python tests/validate_knowledge_base.py
python tests/validate_consistency.py
```

## Key Principle

**This AI Development Framework is NOT tied to any platform**. Use it with:
- GitHub (with GitHub Actions automation)
- GitLab (with GitLab CI automation)
- Bitbucket (with Pipelines automation)
- Local repositories (manual validation)
- Any version control system

The CI examples are just conveniences, not requirements.
