# Phase 1 UX Research Findings — CVS Legacy System Transformation

Research performed: 2026-03-16
Phase: 1 — Business Workflow and UX Design
Purpose: Web research to inform UX design document

---

## Tier 1 — Green Screen to Modern UI Patterns

### Query 1: 5250 Terminal Emulation Green Screen to Web UI Migration UX Patterns

**Focus**: How F-key navigation (F1-F24), screen codes, and keyboard-only workflows map to modern web UI equivalents

#### Key Findings

**Three Migration Approaches Identified**:

1. **Automatic/Model-Driven Transformation ("Facelift")**: Uses model-driven-transformation to convert a two-dimensional, text-based layout into a fully semantic UI model. Rich annotation tools and pattern-based transformation rules transform the original 3270/5250 dumb terminal model into a full-fledged, widget-based, modern web UI layout model.

2. **Web-Enablement/Screen Scraping**: Gives green screens a modern look without heavy development investment. Acts as a stopgap modernization solution until full modernization away from the 5250 stream is possible. Lowest effort, but limited UX improvement.

3. **Hybrid Approach (Recommended)**: The 80/20 rule applies — users spend 80% of their time on 20% of the screens. Best practice is to do a full conversion of the highly-used 20% and web-enable the other 80%, achieving modern interfaces across the board quickly.

**UI Element Mapping**:
- Menus become clickable links
- Subfiles become scrollable tables
- Function keys become buttons
- Screen codes become navigation routes/URLs

**Important Caveat**: Automatic templates depend on DDS style — not all screens look good out of the box. Some require small adjustments, others require significant rework. Manual refinement is necessary for optimal UX.

**F-Key to Web UI Mapping** (from mainframe emulation research):
- F1-F12 map to mainframe primary PF1-PF12
- Shift+F1 through Shift+F12 map to PF13-PF24
- In web applications, these can be mapped to toolbar buttons, contextual action menus, or keyboard shortcut bindings
- A key binding connects a key to an application function; when bound, the program performs that function on keystroke

#### Sources
- [3270/5250 TUI Modernization | Synchrony Systems](https://www.sync-sys.com/3270-5250-dumb-terminal)
- [Green Screen Modernization | Profound Logic Software](https://core.profoundlogic.com/solutions/green-screen-modernization.html)
- [The Next Big Thing in IBM i 5250 Applications | LANSA](https://lansa.com/blog/application-modernization/ibm-i-modernization/the-next-big-thing-in-ibm-i-5250-applications/)
- [Web enable 5250 Applications | aXes/LANSA](https://lansa.com/axeslive/web-enable-5250-applications.htm)
- [Project "Facelift" — 5250 Terminal Modernization](https://blog.greenscreens.io/project-facelift-5250-terminal-modernization/)
- [Mainframe Emulator Common Keyboard Mappings | F1 for Mainframe](https://mainframesf1.com/2020/02/05/mainframe-emulator-common-keyboard-mappings-and-options-that-save-you-time/)

---

### Query 2: AS/400 Green Screen Modernization User Experience Best Practices 2025-2026

**Focus**: What UX patterns work best when migrating power users from text-only terminals to graphical interfaces

#### Key Findings

**Measurable UX Improvements from Modernization**:
- Real-time prompts, dropdown menus, and automated field validation **reduced data-entry errors by 40%** and accelerated order fulfillment
- New employee onboarding dropped from **6-8 weeks** (green screen) to **less than 10 days** (modern UI) — a ~80% reduction in training time
- These are significant statistics for the CVS proposal's ROI section

**Core UX Challenges with Green Screens**:
- No graphics, buttons, or mouse interaction
- Keyboard-driven with dozens of cryptic function keys
- Requires extensive training, slows onboarding
- Resists direct connection with cloud services, mobile platforms, or analytics dashboards

**Best Practice Patterns**:
- **Partial modernization** preserves AS/400 power while delivering intuitive experience
- Apply modern design systems (e.g., Google Material Design themes)
- Include mobile-native features (camera, GPS) when applicable
- Use drag-and-drop interface builders and pre-built templates (aXes, Rocket LegaSuite) to simplify conversion without extensive coding

**Top Modernization Tools (2025)**:
- aXes (LANSA) — transforms green screens to web-based UIs with drag-and-drop
- Rocket LegaSuite — low-code platform for green screen to web conversion
- Profound Logic — Profound UI layer between green screen program and web server
- FRESCHE — comprehensive modernization suite

#### Sources
- [AS400 Green Screen Modernization | Srinsoft Technologies](https://www.srinsofttech.com/blog/as400-green-screen-modernization/)
- [AS400 Green Screen Modernization | Integrative Systems](https://www.integrativesystems.com/as400-green-screen-modernization/)
- [IBM i Green Screen Modernization with aXes | LANSA](https://lansa.com/products/axes/)
- [Top 20 AS400 Modernization Tools in 2025 | Nalashaa](https://www.nalashaa.com/top-twenty-as400-modernization-tools/)
- [AS400 Modernization Best Practices | Damco](https://www.damcogroup.com/blogs/as400-application-modernization-best-practices)
- [Complete Guide to IBM i/AS400 GUI Modernization | DEV Community](https://dev.to/vijendra22/a-complete-guide-to-ibm-ias400-application-gui-modernization-42j3)

---

### Query 3: IBM i Green Screen Keyboard Shortcuts to Web Application Command Palette

**Focus**: Bridge patterns that let experienced green screen users maintain productivity

#### Key Findings

**Command Palette as Bridge Pattern**:
The command palette is a design pattern that provides a searchable list of commands in a popup window, allowing users to quickly access any command within an application by typing a few letters of the command's name. This is the ideal bridge pattern for green screen power users because:

- Users don't need to take their hands away from the keyboard
- Keyboard shortcuts are easy to discover and explore
- Helps users unlock extreme speed and achieve a "state of flow"
- The main difference from traditional search: command palettes aren't just for finding things — they are for **doing things and taking action**

**Ideal Use Cases (directly applicable to PBM transformation)**:
- Products with a large number of features or functionalities
- Complex navigation structures
- Power users who rely on keyboard shortcuts
- Complex apps with many features (dashboards, dev tools, productivity apps)
- Users who perform repetitive actions or navigate between many pages

**Keyboard-First Design Principles**:
- Pick a keyboard shortcut that is simple, memorable, and doesn't clash with common shortcuts (Cmd+C, Cmd+V, Cmd+S)
- Standard trigger: Ctrl+K or Cmd+K
- Command palette restores the single hotkey, keyboard-centric workflow that power users want

**Real-World Examples**:
- VS Code (Ctrl+Shift+P)
- Figma (Ctrl+/)
- Notion (Ctrl+K)
- Superhuman email (Cmd+K)
- Microsoft PowerToys Command Palette

**Green Screen Preservation in Web Modernization**:
- When green screen applications are modernized to run in web browsers, all keyboard shortcuts, function keys, and screen data can remain fully functional
- Power users who have memorized function keys and macro key-combos can retain productivity
- However, web-based versions should also reduce dependence on function key combinations in favor of modern navigation patterns, offering a dual-mode experience

#### Sources
- [Command Palette | UX Patterns | Alicja Suska](https://medium.com/design-bootcamp/command-palette-ux-patterns-1-d6b6e68f30c1)
- [Command Palette UI Design: Best Practices | Mobbin](https://mobbin.com/glossary/command-palette)
- [How to Build a Remarkable Command Palette | Superhuman](https://blog.superhuman.com/how-to-build-a-remarkable-command-palette/)
- [Designing Command Palettes | Sam Solomon](https://solomon.io/designing-command-palettes/)
- [What is a Command Palette? Keyboard-First Navigation | HashBuilds](https://www.hashbuilds.com/patterns/what-is-command-palette)
- [The UX of Keyboard Shortcuts | Medium](https://medium.com/design-bootcamp/the-art-of-keyboard-shortcuts-designing-for-speed-and-efficiency-9afd717fc7ed)
- [Modernizing AS400 Green Screens | Nick Litten](https://www.nicklitten.com/modernizing-as400-green-screens/)
- [Green Screens Modernization | Strumenta](https://tomassetti.me/what-to-do-with-green-screens/)

---

### Query 4: Legacy Terminal Application to Responsive Web Design — Data Density

**Focus**: Data density challenges — green screens display 80x24 characters of dense data, modern UIs need to preserve information density while improving readability

#### Key Findings

**Information Density Design Principles**:

1. **Consistency and Pattern Recognition**: When dealing with a large number of UI components on one screen, inconsistency kills usability. Pattern recognition reduces user learning, increases confidence, and improves task completion rates. This is critical — green screen users rely heavily on spatial memory of where data appears on screen.

2. **Design Systems for Data-Dense Products**: Implementing a design system is recommended for data-dense products. A basic set of core styles (spacing, colors, type scale) and core elements (buttons, text fields, dropdowns) creates instant consistency throughout the design.

3. **Tables for Structured Data**: Tables remain a vital UI element for data-dense products. Their grid layout supports fast scanning, sorting, and comparison — the same strengths of green screen subfile displays. Tables help users identify patterns, filter relevant data, and make informed decisions.

4. **Typography and Accessibility**: Density doesn't override the need for an accessible, user-friendly experience. Color, contrast, size, and spacing must all meet WCAG standards regardless of information density.

5. **Progressive Disclosure / High-Level to Low-Level**: Manage data density by presenting high-level summaries first with drill-down capability. This addresses the 80x24 limitation — modern UIs can show summary views that expand to full detail on demand.

**UI Design Trends 2026 (Relevant)**:
- Dense, information-rich interfaces can be clearer and more usable than sparse layouts when designed with proper hierarchy
- Data tables with inline editing, sorting, and filtering are returning as a primary pattern
- Split-pane views for comparison workflows are gaining adoption

**Migration-Specific Data Density Challenges**:
- Legacy systems often have data trapped in formats complex to access and analyze
- Modern databases offer better organization, faster retrieval, and advanced analytics
- Real-time dashboards, AI-driven insights, and automated reporting become possible
- Responsive design must handle the same data density across desktop, tablet, and mobile breakpoints

#### Sources
- [Interface Information Density Best Practices | Envy Labs](https://envylabs.com/insights/interface-information-density-best-practices)
- [Balancing Information Density in Web Development | LogRocket](https://blog.logrocket.com/balancing-information-density-in-web-development/)
- [Designing for Data Density | Paul Wallas](https://paulwallas.medium.com/designing-for-data-density-what-most-ui-tutorials-wont-teach-you-091b3e9b51f4)
- [Layout Density | Material Design 3](https://m3.material.io/foundations/layout/understanding-layout/density)
- [Balancing Space and Data Density | Radiant Digital](https://www.radiant.digital/balancing-space-and-data-density-in-designs/)
- [UI/UX Principle #52: Manage Data Density | Fresh Consulting](https://www.freshconsulting.com/insights/blog/ui-ux-principle-52-manage-data-density-high-level-to-low-level/)
- [UI Design Trends 2026 | Landdding](https://landdding.com/blog/ui-design-trends-2026)

---

## Tier 1 — CVS Health Brand/Design Language

### Query 5: CVS Health App Design, User Interface, and Digital Experience

**Focus**: CVS Health's consumer-facing digital design, any public design system or brand guidelines

#### Key Findings

**Scale and Reach**:
- Over **60 million users** engaging with the CVS Health app
- Design components play a critical role in delivering seamless UX across both mobile and desktop platforms

**Key Design Characteristics**:
- **Integrated Experience**: Brings together features that were once spread across multiple platforms into a single, user-friendly interface
- **Intuitive Navigation**: Simple and efficient navigation system with streamlined interface and bright icons
- **Complete E-Commerce + Pharmacy**: Full e-commerce capabilities integrated with pharmacy help
- **Cross-Platform Consistency**: Visual identity (colors, icons, typography) aligned across iOS, Android, and tablet

**Accessibility Features**:
- High-contrast color options
- Scalable font sizes for users with visual impairments
- Voice-over compatibility
- Screen reader support for those with limited vision or dexterity

**Virtual Care Platform**:
- Achieved **95% conversion rate** from scheduling start to virtual care visit completion
- Success attributed to usability testing and quick team brainstorms based on user feedback

**Design Team Structure**:
- CVS Health actively hires UX Designers, UI/UX Designers across multiple locations
- Salary range: $85k-$173k for UI/UX roles (indicates significant investment in design)

#### Sources
- [CVS Health — UI/UX Professional Franz Alvarado](https://www.franzalvarado.com/cvsh)
- [How to Build a Healthcare App Like CVS Health | Code Brew Labs](https://www.code-brew.com/how-to-build-a-healthcare-app-like-cvs-health/)
- [ActiveHealth: CVS Health Digital Transformation Case Study | Seamgen](https://www.seamgen.com/work/active-health)
- [CVS Health Virtual Care Design Project | Dan Staton](https://www.danrstaton.com/cvs-health-virtual-care-design-project)
- [CVS App Design Review | DesignRush](https://www.designrush.com/best-designs/apps/cvs)
- [CVS Health — Irene Inouye Portfolio](https://www.ireneinouye.com/cvs-health)

---

### Query 6: CVS Health Digital Accessibility Commitment and WCAG

**Focus**: CVS Health's public accessibility commitments, accessibility statements, VPAT documentation

#### Key Findings

**WCAG Standards**:
- CVS Health strives to meet and exceed WCAG A and AA standards
- Their design system aims to conform to standards **beyond the minimum requirement of WCAG 2.1 AA**
- Active work toward **WCAG 2.2 conformance** through their design system

**Organizational Commitment**:
- Digital accessibility is a **foundational pillar** in every phase of product development — from research and design through engineering and testing
- CVS Health is a **member of the World Wide Web Consortium (W3C)** and participates in W3C working groups
- Hired **over 120 accessibility professionals** at record speed, transforming accessibility into a full-fledged department
- **Nearly 50% of accessibility team members have disabilities themselves**

**Open-Source Contributions** (significant for proposal alignment):
- Released **Accessibility Annotations Kit** for Figma — open-source
  - Available on GitHub: [github.com/cvs-health/annotations](https://github.com/cvs-health/annotations)
  - Became one of CVS Health's **top Figma libraries**
  - **150,000+ annotations** made across **1,100+ design files**
  - Contributed to a **22% decrease in accessibility defects** across the organization
  - **First open-sourced project** from CVS Health's Design team
  - Downloaded over **3,000+ times**
  - Used as the **foundation for GitHub's own accessibility annotation kit**
- Annotation types include: Buttons, Headings, Images, Landmarks, Links, Inputs, Focus Order, Reading Order, Notes

**Compliance History**:
- Settlement agreement with the US DOJ regarding ADA compliance (historical)
- This history likely drives their current strong commitment to accessibility

#### Sources
- [Accessibility | CVS Health](https://www.cvshealth.com/accessibility.html)
- [Our Commitment to Digital Accessibility and Inclusion | CVS Health](https://www.cvshealth.com/news/diversity-equity-inclusion/our-commitment-to-digital-accessibility-and-inclusion.html)
- [Accessibility at CVS Health App](https://www.cvshealth.com/app-accessibility.html)
- [CVS Health Case Study | Onward Search](https://onwardsearch.com/case-studies/cvs-health-digital-accessibility-staffing/)
- [Accessibility Annotations Kit for iOS | CVS Health Tech Blog](https://medium.com/cvs-health-tech-blog/introducing-the-accessibility-annotations-kit-for-ios-from-cvs-health-inclusive-design-19be1bf2fcc5)
- [Path to WCAG 2.2 Conformance Through Design System | CVS Health Tech Blog](https://medium.com/cvs-health-tech-blog/the-path-to-wcag-2-2-conformance-through-our-design-system-59913a8bf876)
- [New Web Accessibility Annotation Kit | CVS Health Tech Blog](https://medium.com/cvs-health-tech-blog/behind-the-scenes-of-creating-a-new-web-accessibility-annotation-kit-1834815544d3)
- [CVS Health Annotations GitHub](https://github.com/cvs-health/annotations)
- [Settlement Agreement US DOJ and CVS](https://archive.ada.gov/cvs_sa.pdf)

---

### Query 7: CVS Health Pharmacy Benefits Management Portal Design — myPBM

**Focus**: myPBM client portal design and user experience patterns

#### Key Findings

**Platform Overview**:
- myPBM is a **cloud-based platform** where clients manage all contracted services with CVS Caremark
- Built on **Microsoft Azure** — described as "tech-forward PBM leveraging latest cloud technology"
- Positioned as "best-in-class client experience"

**Key UX Features**:
- **Homepage Quick Access**: Formulary search tool accessible from homepage to view drug placement/tier for a selected formulary
- **Global Document Management System**: Centralized location for all documents with quick digital sign-off capability
- **Guided Implementation Process**: Clients can review clinical requirements, benefits requirements, and eligibility requirements in a structured flow
- **Self-Service Plan Management**: Streamlines, automates, and simplifies key plan management processes
- **Speed**: Plan changes implemented in **hours rather than months**
- **Fingertip Strategy Transformation**: Gives plan sponsors ability to transform strategy at their fingertips

**Design Implications for Legacy Transformation**:
- myPBM represents CVS's vision for modern PBM interfaces
- Cloud-native (Azure) architecture already in place
- Self-service model with guided workflows is the target pattern
- The contrast between myPBM (modern, cloud-native) and legacy green screens (AS/400) is the exact problem space of this engagement

#### Sources
- [The Value of Pharmacy Benefit Managers | CVS Health](https://www.cvshealth.com/services/prescription-drug-coverage/pharmacy-benefits-management.html)
- [myPBM | CVS Caremark Business](https://business.caremark.com/employer-solutions/innovation/mypbm.html)
- [CVS Health Introduces New Service for PBM Clients](https://www.cvshealth.com/news/pbm/cvs-health-introduces-new-service-to-help-pbm-clients-manage.html)
- [Improve Plan Performance with myPBM | CVS Caremark](https://business.caremark.com/insights/2024/improve-plan-performance-with-mypbm.html)
- [CVS Launching PBM Client Platform | Fierce Healthcare](https://www.fiercehealthcare.com/payer/cvs-launching-platform-to-allow-pbm-clients-to-manage-supplemental-benefit-contracts)
- [myPBM Portal](https://portal-web.core.mypbm.caremark.com/)

---

### Query 8: CVS Health Digital Transformation and User Experience 2025-2026

**Focus**: Recent CVS Health UX/design initiatives, consumer experience design

#### Key Findings

**AI-Native Consumer Engagement Platform (December 2025 Investor Day)**:
- CVS Health introduced an AI-native consumer engagement platform
- Connects interactions across **CVS Pharmacy, CVS Caremark, Aetna, and healthcare delivery businesses** into a single digital interface
- AI is at the core: enabling personalization, automation, and predictive insights across consumer and operational workflows

**Redesigned Mobile App (January 2025)**:
- Replaced legacy CVS Pharmacy app with new all-in-one solution
- Provides customers greater visibility into healthcare journey and tools to navigate challenges
- Serves **60 million digital customers**
- Manages prescriptions, tracks health spending, accesses wellness content
- Spans CVS Pharmacy, CVS Caremark, and CVS Specialty pharmacies

**AI Integration — Aetna Conversational AI**:
- Aetna launched market-leading generative AI-powered conversational experience
- Embedded throughout end-to-end digital experience
- Described as "paradigm shift from traditional transactional experiences to a consumer health experience"

**$20 Billion Technology Investment**:
- CVS Health plans to invest **$20 billion in technology over the next 10 years**
- Focus: more consumer-centric health experience
- Key goal: improving **interoperability of health tech systems**
- This is directly relevant — legacy system transformation is part of this investment thesis

**Generative Agent Simulations**:
- Over the past year, CVS Health has used generative agent simulations to guide decision-making
- Built on **2.9 million consented responses** from **400,000+ participants** across **200+ behavioral scenarios**
- This indicates CVS values data-driven UX decisions, which aligns with evidence-based design approach

**Digital Optimization Phase**:
- CVS has moved from "digital transformation" to "digital optimization"
- Indicates maturity in their digital journey — they are past the initial transformation and now optimizing

#### Sources
- [CVS Health Details AI-Driven Digital Strategy | Digital Commerce 360](https://www.digitalcommerce360.com/2026/01/05/cvs-health-ai-digital-strategy/)
- [How CVS Health Test-Drives Better Care Experiences Using Generative Agents](https://www.cvshealth.com/news/innovation/how-cvs-health-test-drives-better-care-experiences-using-generative-agents.html)
- [Aetna Launches Conversational AI Navigation | CVS Health](https://www.cvshealth.com/news/innovation/aetna-launches-leading-edge-conversational-ai-navigation.html)
- [CVS Unveils AI-Powered App | PYMNTS](https://www.pymnts.com/healthcare/2025/cvs-health-all-in-one-app-aims-personalize-healthcare/)
- [CVS Health's Next Big Goal: Solve Interoperability | AHA](https://www.aha.org/aha-center-health-innovation-market-scan/2025-06-17-cvs-healths-next-big-goal-solve-interoperability)
- [CVS Health Advances Digital Strategy | Yahoo Finance](https://finance.yahoo.com/news/cvs-health-advances-digital-strategy-123100795.html)
- [CVS to Launch Engagement Platform | Healthcare Dive](https://www.healthcaredive.com/news/cvs-launches-health-engagement-platform/807432/)
- [CVS Health Digital Transformation to Digital Optimization](https://www.intelligentautomation.network/transformation/articles/cvs-health-goes-from-digital-transformation-to-digital-optimization)
- [CVS Health to Invest $20 Billion | PYMNTS](https://www.pymnts.com/healthcare/2025/cvs-health-to-invest-20-billion-to-build-tech-enabled-consumer-health-experience/)

---

## Cross-Cutting Insights for UX Design Document

### Key Statistics for Proposal ROI
| Metric | Value | Source |
|--------|-------|--------|
| Data-entry error reduction from modernization | 40% | Srinsoft/Integrative Systems |
| Onboarding time reduction | 6-8 weeks to <10 days (~80%) | Srinsoft/Integrative Systems |
| CVS digital users | 60 million | CVS Health / PYMNTS |
| Virtual care scheduling conversion | 95% | Dan Staton portfolio |
| Accessibility defect reduction (annotation kit) | 22% | CVS Health Tech Blog |
| CVS accessibility professionals hired | 120+ | CVS Health |
| CVS 10-year tech investment | $20 billion | PYMNTS |
| Generative agent simulation responses | 2.9 million | CVS Health |

### Design Pattern Recommendations (Emerging from Research)
1. **Command Palette (Ctrl+K)** — Primary bridge for green screen power users to maintain keyboard-first productivity
2. **Dual-Mode Interface** — Support both keyboard-power-user and mouse-discovery modes simultaneously
3. **Progressive Disclosure** — High-level summaries that drill down to green-screen-level data density on demand
4. **Data Tables with Inline Editing** — Modern equivalent of 5250 subfile displays; support sorting, filtering, comparison
5. **Guided Workflows** — Match myPBM's guided implementation pattern for complex multi-step processes
6. **Split-Pane Views** — For comparison workflows currently done across multiple green screens
7. **Design System Approach** — Consistent core styles and components; align with CVS's own accessibility annotation kit methodology

### CVS Alignment Opportunities
- CVS already has a strong accessibility practice (120+ professionals, W3C membership, open-source tools) — our UX design should reference and build upon their existing standards
- myPBM on Azure represents CVS's target state — our design should feel like an extension of this platform
- CVS is investing $20B in tech over 10 years with interoperability as a key goal — frame legacy transformation as enabling this vision
- CVS uses generative agent simulations for UX decisions — propose similar evidence-based testing approach
- CVS has moved from "digital transformation" to "digital optimization" — position this engagement as the next optimization frontier for internal tools

### Gaps Identified (Needs Further Research in Phase 1 Execution)
- Specific CVS brand color palette and typography (not publicly documented for internal tools)
- CVS internal design system details beyond the open-source annotation kit
- Actual green screen workflows used in CVS PBM operations (will need to be researched/assumed based on industry patterns)
- Pharmacy-specific UX patterns (Cluster 2 from phase plan — not yet researched)
- WCAG 2.2 specific requirements for healthcare (Cluster 3 from phase plan — not yet researched)
