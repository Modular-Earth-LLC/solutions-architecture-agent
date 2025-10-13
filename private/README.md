## Secure Private Directory for Sensitive Content

This directory provides a **privacy-preserving workspace** for sensitive files, proprietary designs, and confidential data that must **never** be committed to Git, pushed to GitHub, or exposed through any version control system.

## How It Works

The `private/` directory uses a carefully configured `.gitignore` file that:

- ✅ **Tracks** the directory structure and this README (for other engineers to use)
- ❌ **Blocks** all file contents from being committed to Git
- 🔒 **Protects** your sensitive data from accidental exposure

### What You Can Safely Store Here

- Proprietary technical design documents
- Data architectures and models containing sensitive information
- API keys, credentials, and configuration files with secrets
- Private business strategy documents
- Customer data or PII used for development/testing
- Internal system documentation not meant for public release
- AI-generated content with proprietary information

## Step-by-Step: Adding Sensitive Content

### 1. Place Your File in the Private Directory

```bash
# Copy a sensitive file
cp /path/to/sensitive-document.md private/

# Or create a new file directly
echo "Proprietary design details..." > private/my-secret-design.md
```

### 2. Verify It's Being Ignored

**CRITICAL**: Always verify before committing anything.

```bash
# Check git status - your file should NOT appear
git status

# Explicitly check if the file is ignored
git check-ignore -v private/my-secret-design.md

# Expected output should show it's ignored by .gitignore
```

### 3. What You Should See

✅ **Correct** - File is protected:
```
On branch main
nothing to commit, working tree clean
```

❌ **DANGER** - File is NOT protected:
```
Untracked files:
  private/my-secret-design.md
```

**If you see your file in `git status`, STOP. Review the .gitignore configuration.**

### 4. Using Subdirectories

You can create subdirectories for organization:

```bash
# Create a subdirectory
mkdir -p private/my-project-designs

# Add a .gitignore to that subdirectory
cp private/sensitive-ai-agent-outputs/.gitignore private/my-project-designs/

# Add your files
cp design.md private/my-project-designs/
```

## Using with AI Agents

### Instructing AI to Use This Directory

When working with AI coding assistants (Claude, Cursor, GitHub Copilot, etc.), explicitly specify this directory:

**Examples:**

- *"Generate a technical architecture document and save it to `private/sensitive-ai-agent-outputs/`"*
- *"Create a data model for our customer database and place it in the private folder"*
- *"Save all outputs containing API endpoints to `private/sensitive-ai-agent-outputs/`"*

### AI Agent Security Considerations

**⚠️ CRITICAL AWARENESS:**

1. **Cloud-Based AI Models**: When you use cloud-based AI services (Claude, ChatGPT, GitHub Copilot), the content you share with them is sent to remote servers. The `private/` directory only protects against Git exposure, not AI exposure.

2. **Data Minimization**: Only share the minimum necessary information with AI agents. Avoid pasting entire sensitive documents into AI chat interfaces.

3. **Local vs. Cloud**: Consider using local AI models for highly sensitive work when possible.

4. **Context Windows**: Be aware that AI agents retain conversation history. Sensitive data shared earlier in a conversation may be referenced later.

### Safe AI Workflows

**✅ DO:**
- Use AI to generate templates, then fill in sensitive details manually in the private directory
- Ask AI to create file structures in `private/` without sensitive content
- Request code scaffolding, then add proprietary logic yourself

**❌ DON'T:**
- Paste entire proprietary documents into AI chat
- Ask AI to process real customer data or PII
- Share actual API keys or credentials with AI (use placeholders)

## Security Best Practices

### 1. Defense in Depth

**Multiple Layers of Protection:**

- ✅ `.gitignore` prevents Git commits
- ✅ `.gitignore` is committed so it protects all team members
- ✅ Pre-commit hooks can add additional checks (optional)
- ✅ Code review process should catch any accidental exposure

### 2. Human Behavior Risks

**Common Mistakes to Avoid:**

| Risk | Mitigation |
|------|------------|
| **Accidental `git add -f`** (force add) | Never use `-f` flag in this directory |
| **Copy-paste sensitive data to public files** | Always verify file location before pasting |
| **Screen sharing during demos** | Close or hide sensitive files before sharing |
| **Terminal history exposure** | Avoid typing secrets in commands; use files instead |
| **IDE cloud sync** (VS Code Settings Sync, etc.) | Verify sync settings exclude `private/` |
| **Cloud backup services** | Check if OneDrive/Dropbox backs up workspace |

### 3. Team Collaboration

**When Working with Others:**

- ✅ Each engineer maintains their own `private/` contents locally
- ✅ Use secure channels (encrypted messaging) to share if needed
- ✅ Never commit someone else's file from `private/` to Git
- ❌ Don't rely on GitHub/GitLab issues to discuss private file contents

### 4. OneDrive / Cloud Storage Warning

**🚨 IMPORTANT**: This repository appears to be in OneDrive:
```
C:\Users\paulp\OneDrive\Documents\GitHub\
```

**Implications:**
- OneDrive **will sync** the contents of `private/` to Microsoft's cloud
- `.gitignore` only affects Git, not OneDrive
- Your private files may be accessible to your Microsoft account and anyone with shared access

**Recommendations:**
- Consider moving truly sensitive files outside the OneDrive folder
- Or exclude `private/` from OneDrive sync (right-click → Free up space)
- Review your OneDrive sharing settings regularly

## Emergency Procedures

### If You Accidentally Commit Sensitive Data

**⚠️ CRITICAL**: Simply removing a file in a new commit does NOT remove it from Git history.

#### Option 1: Before Pushing to Remote (Safest)

```bash
# Reset to before the commit
git reset HEAD~1

# Verify the sensitive file is gone from staging
git status

# The file should still exist locally in private/
```

#### Option 2: After Pushing to Remote (More Complex)

**🚨 DANGER ZONE**: This requires force-pushing and coordinating with your team.

```bash
# Remove file from Git history entirely
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch private/sensitive-file.md" \
  --prune-empty --tag-name-filter cat -- --all

# Force push (ONLY if no one else has pulled the changes)
git push origin --force --all
```

**⚠️ For GitHub repositories**, you must also:
1. Contact GitHub Support to purge cached copies
2. Consider the data compromised if public repo
3. Rotate any exposed credentials immediately

#### Option 3: Use BFG Repo-Cleaner (Recommended for Large Cleanups)

```bash
# Install BFG: https://rtyley.github.io/bfg-repo-cleaner/
# Then run:
bfg --delete-files sensitive-file.md
git reflog expire --expire=now --all && git gc --prune=now --aggressive
```

### If Credentials Are Exposed

**Immediate Actions:**
1. ✅ Rotate/revoke the exposed credentials immediately
2. ✅ Notify your security team
3. ✅ Review access logs for unauthorized usage
4. ✅ Follow your organization's incident response procedures

## Verification Checklist

Before committing any changes to this repository, verify:

- [ ] Run `git status` and confirm no `private/` files appear
- [ ] Run `git diff --cached` and visually confirm no sensitive content
- [ ] Check that only `.gitignore` and `README.md` are in the private directory
- [ ] Review any AI-generated code for embedded secrets or proprietary details
- [ ] Verify subdirectories have their own `.gitignore` files

## Advanced: Pre-Commit Hook (Optional)

For additional safety, create a pre-commit hook:

```bash
# Create the hook file
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/sh

# Check if any private files (except .gitignore and README.md) are staged
if git diff --cached --name-only | grep -E '^private/.*' | grep -v -E '(\.gitignore|README\.md)$'; then
    echo "ERROR: Attempting to commit files from private/ directory!"
    echo "Only .gitignore and README.md should be committed."
    exit 1
fi
EOF

# Make it executable
chmod +x .git/hooks/pre-commit
```

## Threat Model

### What This Protects Against

✅ Accidental `git commit` of sensitive files  
✅ Accidental `git push` to public/private GitHub repos  
✅ Team members inadvertently committing your private files  
✅ Git history exposure in forks and clones

### What This Does NOT Protect Against

❌ Malicious actors with physical access to your machine  
❌ Malware/keyloggers capturing sensitive data  
❌ Cloud sync services (OneDrive, Dropbox, Google Drive)  
❌ AI services that receive your data (Claude, ChatGPT, etc.)  
❌ Screen recording or screenshot tools  
❌ Copy-paste operations to public locations  
❌ Social engineering attacks (e.g., someone asking you to share files)

## Additional Resources

- [GitHub: Removing sensitive data from a repository](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
- [Git Documentation: .gitignore](https://git-scm.com/docs/gitignore)
- [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/)
- [git-filter-repo](https://github.com/newren/git-filter-repo)

## Summary

The `private/` directory is a **convenience feature** for local development, not a security guarantee. It protects against accidental Git exposure through automation, but **you** are the ultimate line of defense.

**Golden Rule**: If data is truly sensitive, consider whether it should be in a Git repository directory at all, even if ignored. For maximum security, store highly sensitive data in encrypted vaults outside your development workspace.

---

**Questions or Concerns?** Review this README regularly and update your team's security practices as needed.

