# Slide 06: Security & Zero Trust
## Assignment Question Answered: Part 1 Section 3 - Security Architecture

### Claude for PowerPoint Prompt:

"Create a slide titled 'Top 3 Security Risks & Mitigations'. In the upper portion of the slide, insert the image from the path shown in the Diagram to Insert section below — this is the security zero-trust diagram, sized to occupy approximately 40% of the slide height. Below the image, insert a three-column table with headers '#', 'Risk', 'Mitigation Pattern' and the following three rows: Row 1: '1' | 'PHI exposure through AI pipeline' | 'PHI tokenization before LLM processing. Patient identifiers replaced with tokens — AI sees clinical facts without patient identity.'; Row 2: '2' | 'Prompt injection via clinical documents' | 'Multi-layer defense: document sanitization, system prompt isolation, output validation requiring evidence citations.'; Row 3: '3' | 'Untraceable AI decisions (audit failure)' | 'Tamper-proof audit trail: every determination includes model version, input hash, full reasoning, confidence score, evidence citations. Immutable storage, 7-year HIPAA retention.'. Bold the Risk column text. Below the table, add a single caption line in smaller text: 'Additional controls: Microsoft Entra ID (RBAC), AES-256 at rest, TLS 1.2+ in transit, private endpoints, no auto-deny without human review.' Use the existing slide master layout. Speaker notes: Three risks, three architectural mitigations. I led with AI-specific controls because that is the novel attack surface. The first two are unique to AI systems — prompt injection and PHI in the model pipeline."

### Diagram to Insert:
C:\dev\solutions-architecture-agent\outputs\eng-2026-004-v2\diagrams\05-security-zero-trust.png
