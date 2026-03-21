# eng-2026-004: Backlog — Fixes and Improvements

## P0 — Address Before Interview

| # | Item | Source | Impact |
|---|------|--------|--------|
| 1 | **Calibrate WA scores with parallel agent results** | Review RF-001 | WA scores in `architecture.json` are self-assessed (7.0-8.5). Parallel WA agents ran but read stale KB file (eng-2026-003 race condition). Re-run WA reviewers against current architecture.json to get calibrated scores. |
| 2 | **Validate all 6 Mermaid diagrams render correctly** | QA Phase 9 | Mermaid Chart MCP was unavailable during QA. Render each diagram to PNG/SVG and verify labels, edges, and layout before importing to PowerPoint. |
| 3 | **Add Altais case study reference to proposal** | Autonomize AI research | Altais Health Solutions (10K+ physicians, 500K patients) achieved 45% PA review time reduction with Autonomize AI. This is a verified, named case study — stronger than the anonymized "3 of top 5" claim. Add to executive summary or appendix. |
| 4 | **Verify CMS-0057-F turnaround requirements** | CMS research | Research confirmed: 72 hours urgent, 7 calendar days standard (effective Jan 1, 2026 — already in effect). Our architecture targets < 24 hours, which exceeds both. Verify proposal states this correctly. |

## P1 — Strengthen Technical Depth

| # | Item | Source | Impact |
|---|------|--------|--------|
| 5 | **Add SageMaker PSI note** | AWS verification agent | SageMaker Model Monitor supports KS test natively but PSI requires a custom monitoring container. Update architecture.json and slide 11 speaker notes to clarify: "KS test native, PSI via custom container." |
| 6 | **Strengthen audit trail with external anchoring** | STRIDE Tampering T-004 | Current DynamoDB hash chain is internally consistent but not externally anchored. STRIDE agent recommends AWS QLDB or RFC 3161 timestamping for tamper-proof external verification. Consider adding to security slide. |
| 7 | **Add per-LOB Kafka topics (not just partitions)** | STRIDE Info Disclosure T-004 | Current design uses partition-level LOB isolation. STRIDE agent recommends topic-level isolation (e.g., `pa-requests-commercial`) for stronger ACL enforcement. Evaluate trade-off: more topics = more operational overhead but stronger isolation. |
| 8 | **Address Snowflake PHI exposure risk** | STRIDE Info Disclosure T-005 | Analytics pipeline replicates PHI to Snowflake before dbt masking. Add Snowflake Dynamic Data Masking policies as first-stage transform. Mention in security slide. |
| 9 | **Incorporate FDA PCCP framework into MLOps slide** | MLOps research | FDA's Predetermined Change Control Plan (PCCP, Aug 2025) enables AI model updates post-clearance without new marketing applications. Relevant for interview — shows awareness of regulatory ML lifecycle. |

## P2 — Enrich Presentation

| # | Item | Source | Impact |
|---|------|--------|--------|
| 10 | **Add Q&A prep document** | Presentation strategy | Create anticipated questions and answers for the 1-hour panel. Cover: "Why Kafka over SQS?", "How do you handle fax OCR for handwritten notes?", "What happens if Autonomize AI goes down?", "How do you prevent prompt injection?", "Why multi-tenant not multi-instance?" |
| 11 | **Add state-level PA regulation awareness** | CMS research | 18+ states enacted PA reforms in 2025. Indiana requires 24-hour urgent turnaround (stricter than federal 72 hours). Gold carding programs in Texas/Arkansas. Mention awareness in security/compliance slide. |
| 12 | **Reference CAQH Index for cost benchmarks** | Autonomize AI research | Manual PA cost: $10.97-$12.88 per transaction (provider side), $3.14-$3.52 (payer side). Automated: ~$0.05 (payer). Use in executive summary to quantify per-transaction savings. |
| 13 | **Add Wasserstein Distance to drift detection** | MLOps research | Evidently AI benchmark study recommends Wasserstein Distance as best overall compromise for large datasets. More sensitive than PSI, less noisy than KS. Consider adding as third drift metric. |

## P3 — Future Enhancements (Post-Interview)

| # | Item | Source | Impact |
|---|------|--------|--------|
| 14 | **Convert proposal.md to PowerPoint** | Deliverable format | Use a markdown-to-pptx tool or manually create slides. Mermaid diagrams need PNG/SVG export first. |
| 15 | **Build the demo** | Implementation prompt | Use `outputs/eng-2026-004/plans/implementation-prompt.md` in Claude Code plan mode. Target: 12-16 hours to build a working demo. |
| 16 | **Add CCPA rights management to Phase 2 scope** | Security review F-004 | CCPA deletion and opt-out workflows deferred to Phase 2. Ensure data tagging in Phase 1 supports future compliance. |
| 17 | **Negotiate Autonomize AI contract terms** | Security review F-005 | Right-to-audit clause, annual SOC 2 report, HIPAA BAA, breach notification obligations, data handling on termination. |
