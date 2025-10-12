# Deploy to Claude Projects

**Agent:** Claude Projects Deployment Agent  
**Category:** Platform Deployment  
**Complexity:** Simple  
**Duration:** 30-60 minutes

---

## Purpose

Deploy AI application to Anthropic Claude Projects with custom instructions and knowledge base.

---

## Instructions

Deploy to Claude Projects:

1. **Prepare custom instructions** (system prompt, <32K chars)
2. **Organize knowledge base files**
3. **Create project in Claude console**
4. **Upload knowledge base**
5. **Configure and test**

---

## Deployment Steps

### Step 1: Prepare Custom Instructions

```markdown
# custom_instructions.md

# AI Assistant

## Role
You are a [describe role] specializing in [domain].

## Capabilities
- [Capability 1]
- [Capability 2]
- [Capability 3]

## Instructions
[Detailed step-by-step instructions]

## Knowledge Base Usage
Reference uploaded documents in Project Knowledge to provide accurate answers.
Cite sources when using information from knowledge base.

## Output Format
[Specify expected response format]
```

### Step 2: Organize Knowledge Base

```
knowledge_base/
├── INDEX.md              # Overview of all files
├── core_knowledge.md     # Main domain knowledge
├── examples.md           # Example interactions
├── faq.md                # Frequently asked questions
└── reference_data.csv    # Structured data
```

### Step 3: Deploy to Claude Projects

1. Go to https://console.anthropic.com/
2. Click "Create Project"
3. Name: `[Project Name]`
4. Description: `[Brief description]`
5. Click "Add knowledge"
6. Upload all files from knowledge_base/
7. Wait for processing (shows "Ready")
8. Click "Custom instructions"
9. Paste content from custom_instructions.md
10. Save configuration
11. Test with sample queries

### Step 4: Validation

Test these scenarios:
- Basic conversation
- Knowledge retrieval from uploaded files
- Source citation accuracy
- Response format compliance

---

## Success Criteria

✅ Project created successfully  
✅ All knowledge files uploaded  
✅ Custom instructions saved  
✅ Knowledge retrieval working  
✅ Responses meet quality standards

---

## File Limits

- Max 100 files
- Max 10MB per file
- Supported: .txt, .md, .pdf, .csv
- Total <1GB
