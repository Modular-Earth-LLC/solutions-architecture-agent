# Slide 04: System Architecture Detail
## Assignment Question Answered: Part 1 Section 1 - Component Architecture (detail)

### Claude for PowerPoint Prompt:

"Create a slide titled 'Component Architecture'. In the upper half of the slide, insert the image from the path shown in the Diagram to Insert section below — this is the component architecture diagram. Below the image, insert a three-column table with headers 'Component', 'Azure Service', 'Purpose' and the following eight rows: Row 1: 'Ingestion Gateway' | 'API Management + Functions' | 'Receives all PA channels'; Row 2: 'Document Processing' | 'AI Document Intelligence' | 'OCR for faxes, extraction'; Row 3: 'Eligibility Service' | 'Payer Core REST API' | 'Member validation'; Row 4: 'Clinical Data Aggregation' | 'Health Data Services (FHIR R4)' | 'Unified clinical context'; Row 5: 'PA Copilot (AI Engine)' | 'Genesis Platform + Claude' | 'Clinical review + determination'; Row 6: 'Determination Router' | 'Functions + Rules' | 'Confidence-based routing'; Row 7: 'Clinical Review Dashboard' | 'AI Studio' | 'Human reviewer interface'; Row 8: 'Audit & Compliance' | 'Immutable Blob Storage' | 'Tamper-proof decision trail'. Use the existing slide master layout. Use a small font for the table to fit all 8 rows. Speaker notes: Here's the component view with Azure service labels. Ten components, each with a clear responsibility. The AI engine is Autonomize's PA Copilot — I'm integrating it, not rebuilding it."

### Diagram to Insert:
C:\dev\solutions-architecture-agent\outputs\eng-2026-004-v2\diagrams\02-component-architecture.png
