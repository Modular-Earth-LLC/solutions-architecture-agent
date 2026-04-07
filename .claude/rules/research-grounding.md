# Research Grounding Rules

All technology, vendor, pricing, and capability claims in SA deliverables must be **research-backed and citation-verified**. These rules apply to any skill that recommends a technology or writes to a research/grounding document.

## Citation precedence

When multiple sources disagree or multiple are available, prefer in this order:

1. **Official vendor documentation on the vendor's learn/docs site** (e.g., Microsoft Learn, AWS docs, GCP docs, Anthropic docs)
2. **Vendor product pages** (pricing, service tiers, regional availability)
3. **Vendor engineering blogs** (for roadmap/preview context)
4. **Standards bodies** (NIST, HL7/FHIR, IETF, W3C, CMS, ONC)
5. **Reputable third-party benchmarks** (peer-reviewed papers, published benchmarks with methodology)
6. **Community tutorials and Stack Overflow** (last resort, flag as such)

Never cite Wikipedia as primary. Never cite a marketing case study as a capability claim.

## URL verification

Every non-obvious claim needs a citation with a URL. Before a research or architecture document is marked complete:

- Use **WebFetch** to confirm each cited URL returns 200 and the fetched content matches the claim
- Flag 404s, permanent redirects, and content drift explicitly — do not silently update the URL
- For Microsoft/Azure content, prefer the **microsoft-learn MCP server** (`microsoft_docs_search`, `microsoft_docs_fetch`) over generic WebFetch — it returns cleaner markdown and is the authoritative surface
- For library/framework docs, use the **context7 MCP** (`resolve-library-id`, `query-docs`) when available

## Currency checks

Technology facts decay. For every cited service, verify as of today's date:

- **Lifecycle state**: Preview, GA, deprecated, retired. Preview services require a documented risk section (see below).
- **Regional availability**: Is the service available in the client's required region?
- **Compliance coverage**: HIPAA/BAA, FedRAMP, SOC 2, PCI-DSS — is the specific service in scope?
- **Pricing tier limits**: Serverless vs. provisioned, free tier limits, quota ceilings
- **Retirement dates**: If a service has an announced retirement, cite the date and plan the migration path

## Preview-service risk documentation

When an architecture recommends a **preview** or **beta** service, the research/architecture doc MUST include:

- Current lifecycle state with citation
- Target GA date (if published)
- **Fallback path** — what to use if GA slips or the service is cancelled
- **BAA / compliance coverage** status for preview tier specifically
- Support / escalation contract terms
- Trigger conditions for executing the fallback (e.g., "if GA slips past Q3 or BAA is not extended")

Never recommend a preview service without this risk section. Never hide the preview status in footnotes.

## Model recommendation discipline

For LLM and generative model recommendations:

- Cite current (within 18 months) benchmarks or vendor model cards
- Match the benchmark dimension to the use case (photorealism ≠ prompt adherence ≠ reasoning)
- Never write "superior," "best-in-class," "state-of-the-art" without a cited source and metric
- For Claude models, consult `docs.anthropic.com/en/docs/about-claude/models` for the current roster
- Flag benchmark gaps explicitly as `benchmark_status: pending` with a re-evaluation date

## Research document structure

When a skill produces or refactors a research/grounding document, structure it as an **indexable database**:

- Stable section headings with anchor links
- Summary tables at the top (services, versions, statuses, compliance)
- Alphabetic glossary at the bottom
- Every claim inline-cited with a URL
- Verification timestamp per section (date + source URL confirmed live)
- A "Known gaps / unverified claims" section for anything flagged for human review

Downstream skills (architecture, security-review, estimate) cite the research doc by section anchor rather than duplicating facts.

## When research is unavailable

If WebFetch, WebSearch, and MCP servers are all unavailable:

- Proceed with general best practices from the skill's own domain knowledge
- Mark every vendor-specific claim with `[unverified - human review required]`
- List all unverified claims in the completion summary
- Do not remove STALE banners or mark the document `complete`
