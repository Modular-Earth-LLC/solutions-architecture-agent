# Slide 07: Clinical Data Integration
## Assignment Question Answered: Part 1 Section 2 - Clinical Data Access

### Claude for PowerPoint Prompt:

"Create a slide titled 'How AI Accesses Clinical Data'. In the upper portion of the slide, insert the image from the path shown in the Diagram to Insert section below — this is the clinical data access diagram, sized to occupy approximately 45% of the slide height. Below the image, present a two-column comparison layout with the heading 'Two source types, one unified interface:'. Insert a four-column table with headers 'Source', 'Protocol', 'Auth', 'Notes' and the following two rows: Row 1: 'Modern EMRs' | 'FHIR R4 REST API' | 'OAuth 2.0 / SMART on FHIR' | 'Structured, standardized'; Row 2: 'Legacy Systems' | 'DB connector / HL7 v2' | 'Service account + VNet isolation' | 'Requires normalization'. Below the table, add two caption lines in smaller text: Line 1: 'FHIR R4 role: Interoperability standard for clinical data exchange. Modern sources expose FHIR natively. Legacy data normalized before AI processing.' Line 2: 'Security boundary: All clinical data passes through PHI tokenization before reaching the AI engine.' Use the existing slide master layout. Speaker notes: Clinical data comes from two worlds — modern FHIR R4 endpoints and legacy databases. The aggregation service presents a unified clinical context to the AI engine, regardless of source."

### Diagram to Insert:
C:\dev\solutions-architecture-agent\outputs\eng-2026-004-v2\diagrams\04-clinical-data-access.png
