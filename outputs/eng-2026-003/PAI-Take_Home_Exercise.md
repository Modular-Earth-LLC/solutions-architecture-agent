# Take-Home Exercise: Product Packaging Variant Generator

Please plan to spend 4-6 hours on the overall assignment. Complete deliverables described in the task. This exciting role involves leveraging advanced AWS core and managed services including Generative AI technologies for solving complex technology problems for Adobe's Enterprise customers. We expect you to be a thought leader who can uplevel our team starting Day 1. This is a challenge for the winner in you. Bring your best!!

## Technology Stack Requirement

1. Please create an AWS Free Tier account for deploying your solution.
2. Host the code in your Github account. Working CICD will be bonus points for evaluation.
3. Deployment of resources in AWS should be using CloudFormation or Terraform.

---

## Scenario: Product Packaging Automation for CPG at Scale

A global consumer packaged goods (CPG) manufacturer launching hundreds of localized product packaging variants (labels, boxes, seasonal editions) monthly across regional markets.

### Business Goals

1. **Accelerate time-to-market**: Rapidly design, produce, approve, and launch regional product variants and seasonal editions per month to drive market relevance and shelf visibility.
2. **Ensure brand consistency**: Maintain global brand guidelines, trademark compliance, and visual identity across all markets and languages.
3. **Maximize local relevance & personalization**: Adapt packaging design, cultural imagery, flavor-specific graphics, and messaging to resonate with regional preferences and seasonal trends.
4. **Optimize packaging ROI**: Increase design efficiency by reducing time-to-approval and manual rework while maintaining premium shelf appeal and regulatory compliance.
5. **Gain actionable insights**: Track design effectiveness across markets and learn what packaging designs, imagery, and regional variants drive consumer preference and conversion.

### Pain Points

1. **Manual packaging design overload**: Creating and localizing design variants for hundreds of SKUs per month is slow, expensive, and error-prone.
2. **Inconsistent quality & compliance**: Risk of off-brand, non-compliant, or low-quality packaging due to decentralized design processes and multiple agencies.
3. **Slow approval cycles**: Bottlenecks in regulatory review and brand approval with multiple stakeholders in each region and market.
4. **Difficulty tracking regulatory compliance at scale**: Siloed design files and manual compliance checking hinder learning and prevent non-compliant designs from reaching production.
5. **Resource drain**: Skilled design and brand teams are overloaded with repetitive layout/resizing requests instead of strategic creative work.

### Objective

Design a packaging automation pipeline that enables the design team to generate regional variants and format-specific designs for product SKUs while maintaining regulatory compliance and brand consistency.

### Data Sources

- **User inputs**: SKU briefs and brand assets uploaded manually.
- **Storage**: Storage to save generated or transient assets in AWS S3.
- **Gen AI**: Best-fit APIs available for generating region-specific imagery, cultural graphics, and design variations.

---

## Task: Build a Packaging Automation Pipeline (Proof of Concept)

### Goal

Demonstrate a working proof-of-concept that automates packaging asset generation for product SKUs using Gen AI. The implementation should show your technical approach, problem solving, and ability to integrate creative technologies with compliance requirements.

### Requirements

- Accept an SKU brief (in JSON) with:
  - Product(s) — at least two different products/flavors
  - Target region/market
  - Target audience/demographics
  - Key product attributes (examples like organic, vegan, seasonal)
- Accept input assets (stored in AWS S3) and reuse them when available.
- When assets are missing, generate new assets using any Gen AI image model of your choice.
- Create packaging designs for at least three aspect ratios (e.g., front label 1:1, back label 9:16, wraparound 16:9).
- Display product messaging, key attributes, and regulatory information on the final packaging designs (English at least, localized is a plus).
- Run/Execute in AWS (command-line tool or simple local app; your choice of framework).
- Save generated outputs to an AWS S3 folder, clearly organized by SKU, Region and format.
- Include basic documentation (README) explaining:
  - How to run it
  - Example input and output
  - Key design decisions
  - Any assumptions or limitations

### Nice to Have (optional for bonus points)

- Brand compliance checks (e.g., presence of logo, required color usage, font consistency).
- Regulatory content checks (e.g., flagging missing allergen disclosures, ingredient lists, certifications for target regions).
- Approval status tracking and logging of design generation results.

Please ensure that your solution reflects thoughtful design choices and demonstrates a clear understanding of the code. These aspects will be part of the evaluation.

---

## Deliverables

Please share with us the following deliverables for the tasks described above:

1. A public GitHub repository containing:
   - The creative automation pipeline code.
   - A comprehensive README file.

---

## Interview Structure

1. Present technical code and do a live demo/edit with engineers on tasks above — 20–30 mins.
2. Foundational technical questions (do not need to be related to deliverables above) — 10–15 mins.
3. Questions from candidate — 5–10 mins.
