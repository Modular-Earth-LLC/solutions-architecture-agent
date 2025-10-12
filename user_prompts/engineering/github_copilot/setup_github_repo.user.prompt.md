# Setup GitHub Repository for AI Project

**Agent:** GitHub & Cursor Integration Agent  
**Category:** DevOps & Tooling  
**Complexity:** Intermediate  
**Duration:** 1-2 hours

---

## Purpose

Initialize GitHub repository with proper .gitignore, CI/CD workflows, and development best practices for Python AI projects.

---

## Instructions

Setup repository with:

1. **Repository initialization**
2. **.gitignore for Python AI projects**
3. **GitHub Actions workflows** (test, lint, deploy)
4. **Branch protection rules**
5. **README and CONTRIBUTING.md**

---

## Expected Output

```bash
# Initialize repository
git init
git add .
git commit -m "Initial commit: AI project setup"
git branch -M main
git remote add origin https://github.com/username/repo.git
git push -u origin main

# .gitignore
```.gitignore
# Python
*.pyc
__pycache__/
.pytest_cache/
.coverage
*.egg-info/
dist/
build/

# Environment
.env
.env.local

# Streamlit
.streamlit/secrets.toml

# Data
*.db
*.sqlite
chroma_db/
.faiss/

# AWS
.aws/
cdk.out/

# IDE
.cursor/
.vscode/
```

# .github/workflows/ci.yml
```yaml
name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov black flake8
      - name: Lint
        run: flake8 src/ --max-line-length=100
      - name: Format check
        run: black --check src/
      - name: Test
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: pytest --cov=src --cov-report=term
```

# CONTRIBUTING.md
```markdown
# Contributing to AI Project

## Development Setup

1. Clone repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add API keys
4. Run tests: `pytest`

## Code Standards

- Follow PEP 8
- Use type hints
- Write docstrings
- Maintain >80% test coverage
- Run linters before committing

## Pull Request Process

1. Create feature branch
2. Make changes with tests
3. Run: `black src/ && flake8 src/ && pytest`
4. Push and create PR
5. Wait for CI to pass
6. Request review
```

---

## Success Criteria

✅ Repository initialized  
✅ .gitignore prevents sensitive files  
✅ CI/CD workflows functional  
✅ Branch protection configured  
✅ Contributing guidelines clear

---

## Commands

```bash
# Setup
git init
git add .
git commit -m "Initial commit"

# Configure remote
git remote add origin URL
git push -u origin main

# Enable pre-commit
pip install pre-commit
pre-commit install
```
