# eng-2026-004: Human Review Checklist

> **For Paul Prae only.** These items require your expert judgment, manual verification, or authorization decisions that Claude Code cannot make autonomously.

---

## 1. Technical Decisions to Validate

These are design choices where your domain expertise is the final authority.

| # | Decision | Current Choice | Your Action | Why You |
|---|----------|---------------|-------------|---------|
| TD-1 | **Autonomize AI deploys on Azure, not AWS** | Architecture assumes AWS PrivateLink to Autonomize AI. But their Azure Marketplace listing and Pegasus Program suggest Azure-native deployment. | Ask Autonomize AI in the interview: "What's your deployment model for AWS-primary payers?" Adjust deployment diagram if needed. | Only you can ask this in the interview. |
| TD-2 | **60% auto-determination target** | Set at 60% for Phase 1. Altais achieved 50%. Industry benchmarks: 50-76%. | Is 60% the right balance of ambition vs. credibility for this audience? Your Arine experience with similar scale processing is the benchmark. | Clinical operations judgment call. |
| TD-3 | **12-week timeline feasibility** | 5 phases, 13 FTEs, first LOB only. Aggressive if legacy DB connectors are complex. | Is 4 weeks for core integration build realistic with 4 senior devs? Consider your experience with similar enterprise integrations at AWS/Booz Allen. | You've done this at enterprise scale. |
| TD-4 | **Kafka partitions vs topics for LOB isolation** | Current: partition-level. STRIDE recommends topic-level. Trade-off: topic-level = stronger isolation but 20x more topics to manage. | Which matches your operational experience? At Arine, how is multi-tenant data isolation handled in streaming? | Your Kafka operational experience. |
| TD-5 | **TriZetto Facets API assumptions** | Assumed REST API + JDBC. Real Facets deployments vary. | If asked, acknowledge this is validated during Discovery (Week 1-2). Do you have Facets experience to draw on? | Payer core system knowledge. |
| TD-6 | **Hourly rates ($150-$250/hr)** | US market senior consulting rates. Not cited from specific source. | Do these feel right? Does Autonomize AI use different rate structures? | Market rate knowledge. |

---

## 2. Presentation Review (Read Aloud)

Do these before the interview. No AI can substitute for hearing yourself present.

| # | Check | Time | How |
|---|-------|------|-----|
| PR-1 | **Read all 12 slide speaker notes aloud** | 60 min | Time yourself. Target ~5 min/slide. Mark any notes that feel unnatural or too long. |
| PR-2 | **Review executive summary (Slide 2) as a CIO** | 5 min | Does it answer "why should I care?" in the first 30 seconds? |
| PR-3 | **Review security slide (8-9) for specificity** | 5 min | Are mitigations architectural patterns (PrivateLink, SMART on FHIR, KMS) not generic ("use encryption")? |
| PR-4 | **Review MLOps slide (11) for principal-level depth** | 5 min | Does it demonstrate strategic thinking beyond "we monitor for drift"? |
| PR-5 | **Review multi-tenant slide (12) for trade-off clarity** | 5 min | Is the multi-tenant vs multi-instance justification convincing? |
| PR-6 | **Verify your intro (Slide 1) establishes credibility** | 2 min | Does it mention Arine (50M members), AWS (3 years), and healthcare AI specifically? |

---

## 3. Diagrams — Visual Quality Check

SVGs are rendered in `outputs/eng-2026-004/diagrams/`. Open each in a browser.

| # | Diagram | File | What to Check |
|---|---------|------|---------------|
| DG-1 | System Context | `01-system-context.svg` | All 5 subgroups visible? Edge labels readable? No overlapping nodes? |
| DG-2 | Ingestion Flow | `02-ingestion-flow.svg` | 3 channels clearly separated? Processing pipeline reads top-to-bottom? |
| DG-3 | Clinical Data | `03-clinical-data.svg` | FHIR vs Legacy paths distinct? "JDBC via PrivateLink" label visible? |
| DG-4 | MLOps | `04-mlops.svg` | Feedback loop clearly circular? Daily/Weekly/Monthly cadence readable? |
| DG-5 | Multi-Tenant | `05-multi-tenant.svg` | Shared vs LOB-specific model path clear? All 4 LOB rules visible? |
| DG-6 | Deployment | `06-deployment.svg` | Multi-AZ visible? PrivateLink connections to on-prem clear? |

---

## 4. Authorization and Tooling Decisions

Things only you can approve or configure.

| # | Decision | Options | Your Action |
|---|----------|---------|-------------|
| AT-1 | **Mermaid Chart account** | See comparison below. Free tier sufficient for this project. Paid adds team collaboration and API. | Sign up at mermaid.ai. Free account lets you edit diagrams in browser. Paid ($8/mo) adds API access for MCP integration. |
| AT-2 | **Mermaid MCP vs CLI** | See comparison below. CLI (`mmdc`) works now. MCP adds live editing but cloud connector is currently broken. | CLI is working and diagrams are rendered. MCP is optional upgrade. |
| AT-3 | **PowerPoint conversion** | Options: (a) Manual — paste SVGs into slides, (b) `md-to-docx` pipeline, (c) Marp CLI for markdown-to-pptx | Choose your preferred method. Claude Code can help with any of them. |
| AT-4 | **Remote monitoring** | `/remote-control eng-2026-004` in terminal enables iOS monitoring. | Run the command when you want to monitor Claude Code remotely. |

### Mermaid Chart: MCP vs CLI vs Free vs Paid

| Feature | `mmdc` CLI (installed) | Mermaid Chart MCP (cloud) | Free Account | Pro ($8/mo) |
|---------|----------------------|--------------------------|-------------|-------------|
| **Render to SVG/PNG** | Yes | Yes | Yes (in browser) | Yes |
| **Validate syntax** | Yes (fails on error) | Yes (returns error details) | Yes | Yes |
| **Edit in browser** | No | No | Yes (mermaid.ai editor) | Yes |
| **API access** | N/A | Via cloud connector | No | Yes |
| **Team collaboration** | No | No | No | Yes |
| **Diagram storage** | Local files only | No (renders only) | 5 diagrams | Unlimited |
| **Custom themes** | Yes (`-t` flag) | Limited | Limited | Full |
| **Works offline** | Yes | No | No | No |
| **Current status** | Working | Broken (-32600 error) | Available | Available |
| **Recommendation** | **Use this now** | Try again later | Sign up to edit | Upgrade if you want API |

**Bottom line**: `mmdc` CLI handles everything we need (render + validate). The Mermaid Chart web editor (free account) is useful for visually tweaking diagrams before the interview. The MCP cloud connector adds no value over CLI until the -32600 error is resolved.

---

## 5. Contract and Compliance (Manual Only)

| # | Item | Your Action |
|---|------|-------------|
| CC-1 | **Autonomize AI HIPAA BAA** | Verify BAA is in place or will be before production deployment. Mention in interview as a contractual requirement. |
| CC-2 | **Autonomize AI right-to-audit clause** | Negotiate into contract: right to audit, annual SOC 2 report delivery, breach notification SLA. |
| CC-3 | **Inter-agent security attestation** | Request formal documentation of Genesis Platform inter-agent authentication controls. Frame as BAA requirement. |
| CC-4 | **Pen test vendor selection** | Identify and engage a third-party pen test firm for pre-go-live assessment. Scope: cross-tenant isolation + prompt injection. |

---

## Sign-Off

| Reviewer | Date | Status | Notes |
|----------|------|--------|-------|
| AI Agent (Claude Opus 4.6) | 2026-03-21 | PASS (8.8/10) | Automated checks complete. Human items flagged above. |
| Paul Prae | | | |
