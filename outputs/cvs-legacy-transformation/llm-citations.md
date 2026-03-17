# LLM Citation Framework

> Transparent attribution of AI assistance in this solution architecture document

## Tools Used

| Tool | Purpose | Scope |
|------|---------|-------|
| **Claude** (Anthropic) via Claude Code CLI | Research synthesis, structured artifact generation, drafting, quality review | All phases |
| **Solutions Architecture Agent** (Claude Code plugin, v1.0.0) | Skill-based SA lifecycle: requirements discovery, architecture design, data modeling, security review, estimation, project planning, quality review | Phases 0-4 |
| **Web search** (integrated via Claude Code) | Primary source research, technology validation, pricing verification, compliance framework lookup | Phases 0-4 |

**Model**: Anthropic Claude (via Claude Code plugin)
**Platform**: Claude Code CLI with Solutions Architecture Agent plugin (v1.0.0, single-agent-with-skills architecture, 9 SA lifecycle skills, 2 sub-agents)

## Human vs. AI Attribution

The table below maps each major section of the solution architecture document to the human and AI contributions. "Human" means Paul directed, decided, or wrote. "AI-assisted" means AI drafted under Paul's direction and Paul reviewed. "AI-generated" means AI produced the artifact with human review at phase gates.

| Document Section | Human Contribution | AI Contribution | Attribution |
|-----------------|-------------------|-----------------|-------------|
| **Executive Summary** | Framing, voice, key messages, differentiator positioning | Draft synthesis from all phases | Human-directed, AI-drafted |
| **Understanding the Challenge** | Scope definition, success criteria selection | Research synthesis (54 sources), requirements structuring | Human-directed, AI-researched |
| **Legacy System Integration** | Pattern selection (strangler fig), migration sequencing, fallback decisions | IBMi vendor research (11 sources), IWS/CDC technical details, API contract drafting | Human-decided, AI-researched |
| **Human-Centered Design** | Design philosophy (Cognitive Science grounding), persona selection, principle authoring | WCAG 2.2 research, CVS accessibility assessment, wireframe structuring | Human-authored, AI-assisted |
| **Solution Architecture** | Three-option structure (pivot from original plan), GCP recommendation rationale, technology selection | Vendor reference architecture research, Mermaid diagram generation, WA scoring | Human-decided, AI-executed |
| **IAM Strategy** | Zero trust approach, RBAC/ABAC model, phased migration design | SMART on FHIR research, compliance mapping (21 controls), threat-to-control traceability | Human-designed, AI-researched |
| **Security Architecture** | Defense-in-depth layering, AI security control design, open finding transparency | STRIDE threat enumeration (30 threats), compliance section citations, CVE research | Human-directed, AI-analyzed |
| **Change Management** | ADKAR application to pharmacy context, coaching approach, champion network design | Prosci/Kotter framework research, adoption metrics, training program structuring | Human-designed, AI-researched |
| **Implementation Roadmap** | Phase structure, decision gate criteria, critical path identification | Three-point estimation (PERT), infrastructure cost modeling, sprint planning | Human-directed, AI-calculated |
| **AI Methodology** | Collaboration model description, quality assessment, honest capability mapping | Productivity research synthesis, citation formatting | Human-authored, AI-assisted |
| **Honesty Map** | All self-assessments (8 areas, 1-5 ratings), interview strategy | Evidence organization, framework alignment | **Human-authored** (no AI judgment) |
| **Data Model** | Entity selection, PBM domain validation, governance decisions | Schema generation (13 entities), vector schema, ontology structuring | Human-directed, AI-generated |
| **Mermaid Diagrams** | Architecture decisions reflected in diagrams, layout direction | Diagram syntax generation, rendering validation | Human-directed, AI-generated |

## Attribution Summary

| Category | Count | Percentage |
|----------|-------|------------|
| Human-authored (minimal AI) | 2 sections | ~15% |
| Human-directed, AI-drafted | 4 sections | ~30% |
| Human-decided, AI-researched | 4 sections | ~30% |
| Human-directed, AI-generated | 3 sections | ~25% |

**No section was AI-generated without human review.** Every artifact passed through at least one human review gate. Seven formal quality reviews (average 8.2/10) provided structured assessment.

## Citation Standards Applied

This framework follows emerging professional standards for AI disclosure in technical deliverables:

- **IEEE**: Requires disclosure in Acknowledgments section with tool name, version, specific purpose, and confirmation that authors reviewed all AI-generated content and take full responsibility. AI cannot be listed as an author. (IEEE AI Standards Committee, 2025)
- **ACM**: Authorship implies responsibilities that only humans can perform. AI tools must be fully disclosed but cannot be authors. (ACM Policy on Authorship, updated 2025)
- **ISO/IEC 42001:2023**: AI management system standard requiring documentation of AI system capabilities, limitations, intended use, and evaluation results. The attribution table above satisfies the transparency requirement.
- **NIST AI RMF 1.0**: Accountability and transparency as core trustworthiness characteristics. Document the model used, its version, what data it was grounded on, and what validation was applied.

**Industry context**: No Big 4 or MBB consulting firm currently uses a standardized in-document AI citation format. Disclosure is typically handled through engagement letter clauses, not deliverable footers. This framework goes further — providing per-section attribution — as a demonstration of responsible AI practice.

## Disclosure Statement

*This solution architecture document was produced by Paul Prae with AI assistance from Anthropic's Claude via the Claude Code CLI and the Solutions Architecture Agent plugin. AI tools were used for research synthesis, structured artifact generation, and draft preparation. All architecture decisions, experience assessments, quality judgments, and narrative framing are Paul's. The AI methodology section (Section 9) and this attribution appendix provide full transparency on the human-AI collaboration model used.*

*Paul reviewed and approved every section of this document. He is prepared to discuss, defend, and elaborate on all technical content in interview settings.*

### For Document Footer

> **AI Disclosure**: Produced with AI assistance (Anthropic Claude via Claude Code). Architecture decisions, experience claims, and quality assessments are the author's. See Section 9 and Appendix D for full methodology and attribution.
