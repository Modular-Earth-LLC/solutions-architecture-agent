# Slide Generation Prompts for Claude for PowerPoint

Each prompt below generates one slide. Use with the Claude for PowerPoint add-in.

**Workflow:**
1. Open [presentation.md](../presentation.md) — this is the single source of truth for all slide content
2. For each slide, paste the corresponding prompt into Claude for PowerPoint
3. The prompt references `presentation.md` as context — attach it or paste the relevant slide section when prompted

**Tip:** If Claude for PowerPoint supports file attachment, attach `presentation.md` once at the start of your session and reference slide numbers in each prompt. This avoids repeating content.

---

## Slide 01: Title & Introduction
**Prompt:** "Create a title slide. Use the content from Slide 1 in the attached presentation.md. Title: 'AI-Driven Prior Authorization'. Subtitle: 'Solution Architecture for a Large US Health Plan'. Presenter: 'Paul Prae | Principal AI Engineer & Architect'. Website: 'www.paulprae.com'. Clean, professional layout."
**Diagram:** None

## Slide 02: Why This Architecture
**Prompt:** "Create a slide titled 'Why This Architecture' using Slide 2 content from presentation.md. Three sections: The Problem (manual PA costs, physician burden), The Opportunity (Altais metrics: 45%, 54%, 50%), This Architecture Delivers (4 bullet points). Bold the key numbers. Use the existing slide master."
**Diagram:** None

## Slide 03: System Context
**Prompt:** "Create a slide titled 'System Context' using Slide 3 content from presentation.md. Insert the diagram image from diagrams/01-system-context.png on the left half. Place the 4-row actor/role/integration table on the right half."
**Diagram:** `diagrams/01-system-context.png`

## Slide 04: Component Architecture
**Prompt:** "Create a slide titled 'Component Architecture' using Slide 4 from presentation.md. Insert diagrams/02-component-architecture.png as the main visual. Below or beside it, include the 8-row component/Azure service/purpose table. Also include the smaller Azure↔AWS mapping table."
**Diagram:** `diagrams/02-component-architecture.png`

## Slide 05: PA Request Lifecycle
**Prompt:** "Create a slide titled 'PA Request Lifecycle' using Slide 5 from presentation.md. Insert diagrams/03-pa-request-flow.png as the main visual. Below it, include the 6-step summary line: Submit → Intake → Validate → AI Review → Route → Respond."
**Diagram:** `diagrams/03-pa-request-flow.png`

## Slide 06: Top 3 Security Risks
**Prompt:** "Create a slide titled 'Top 3 Security Risks & Mitigations' using Slide 6 from presentation.md. A 3-row table with columns: #, Risk (bold), Mitigation. Include the 'Additional controls' line below the table. Insert diagrams/05-security-zero-trust.png if space allows."
**Diagram:** `diagrams/05-security-zero-trust.png`

## Slide 07: Clinical Data Integration
**Prompt:** "Create a slide titled 'Clinical Data Integration' using Slide 7 from presentation.md. Insert diagrams/04-clinical-data-access.png. Include the source/protocol/auth table and the FHIR R4 role paragraph."
**Diagram:** `diagrams/04-clinical-data-access.png`

## Slide 08: AI Model Monitoring
**Prompt:** "Create a slide titled 'AI Model Monitoring & Feedback' using Slide 8 from presentation.md. Insert diagrams/06-llmops-pipeline.png. Two sections: 'Detect drift' (3 bullet points) and 'Feedback loop' (4 numbered steps)."
**Diagram:** `diagrams/06-llmops-pipeline.png`

## Slide 09: Progressive Delivery
**Prompt:** "Create a slide titled 'Progressive Delivery' using Slide 9 from presentation.md. A 4-row table: Phase/Focus/Key Deliverable. Include the note about decision gates between phases."
**Diagram:** None

## Slide 10: Scaling to 20 LOBs
**Prompt:** "Create a slide titled 'Scaling to 20 LOBs' using Slide 10 from presentation.md. Comparison table: Multi-tenant vs Multi-instance across Cost/Isolation/Complexity. Include the recommendation callout and honest unknowns note."
**Diagram:** None

## Slide 11: Discussion Starters
**Prompt:** "Create a slide titled 'Discussion Starters' using Slide 11 from presentation.md. Three sections: Business Strategy (2 questions), Technical Depth (2 questions), Implementation (2 questions). Conversational, open layout."
**Diagram:** None
