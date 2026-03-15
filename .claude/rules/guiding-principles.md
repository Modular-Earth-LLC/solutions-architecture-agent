# Guiding Technology Principles

These principles govern all work in this repository. Apply them when designing architectures, writing code, making recommendations, and reviewing outputs.

## Human-Centered

1. **Augment humans over replacing human labor** — Eliminate undesirable tasks, not desirable humans. Build systems that improve job quality, assist workers to higher performance, or remove mundane work.
2. **Use data and AI to encourage sustainable human flourishing** — ML should help people reach their highest aspirations, not addict, distract, or divide. Align AI to support growth, not just optimize engagement.
3. **Build technology as a means to a social or environmental end** — The goal is human flourishing, not technology for its own sake. Help people live meaningful lives, not just productive ones.
4. **Individual Flow Over Interruptions** — Prioritize deep work and flow states over interruptions.
5. **Conservation Of Willpower Over A Paradox Of Choice** — Conserve user willpower rather than overwhelming with excessive choices.
6. **Easy-To-Remember User Flows Over Flashy Design Trends** — Prioritize memorable, intuitive user flows over trendy design.
7. **Human factors like sleep and stress affect code quality more than linters and static typing** — Recognize that human well-being has greater impact on quality than purely technical tooling.
8. **The better you are at writing, the more effective you will be at building software** — Strong writing skills translate directly to effective software development.

## Architecture & Design

9. **Architecture is leadership; Always be architecting** — Architecture is a continuous leadership activity, not a one-time phase.
10. **KISS: Keep it stupid simple** — Good design is less design. Value simplicity and beautiful UX above all else.
11. **Separation of Concerns** — Software should be separated based on the kinds of work it performs.
12. **Don't repeat yourself (DRY)** — Avoid specifying behavior in multiple places; duplication is a frequent source of errors.
13. **Encapsulation** — Different parts of an application should use encapsulation to insulate them from other parts.
14. **Interface Segregation Principle** — Clients should never be forced to implement interfaces they don't use or depend on methods they don't need.
15. **Make frequent, small, reversible changes** — Design for regular updates in small increments that can be reversed. Find two-way doors.
16. **Anticipate failure** — Perform pre-mortems to identify potential failures. Test failure scenarios and response procedures.
17. **Ship. Deliver for people. Create value as fast as possible.**

## Security & Trust

18. **Assume breach** — Minimize blast radius and segment access. Verify end-to-end encryption. Use analytics for threat detection.
19. **Verify explicitly** — Always authenticate and authorize based on all available data points: identity, location, device health, service, data classification, anomalies.
20. **Use least privileged access** — Limit access with JIT/JEA, risk-based adaptive policies, and data protection.
21. **Protect the privacy and security of individuals represented in our data.**

## AI & Data

22. **Ground AI systems in truth** — Use ground truth as a safeguard against AI bias. Knowledge graphs can guide LLMs to reliable results.
23. **Leverage specialized ontologies to make LLMs most effective** — Domain-specific ontologies enable LLMs to work within specialized terminology and relationships.
24. **Always fine-tune Machine Learning models when possible** — Fine-tuning increases effectiveness in specific contexts beyond general-domain capabilities.
25. **Include domain and subject matter experts in the design of systems** — Integration of deep domain knowledge with AI technology is crucial for effective systems.
26. **Evidence-based decision-making** — Support decisions with scientific research whenever possible.
27. **Recognize and mitigate bias in ourselves and in the data we use.**

## Operations & Infrastructure

28. **Automate everything. Build systems that build themselves.** — Use IaC, RPA, and automation to eliminate routine, repetitive work.
29. **Refine operations procedures frequently** — As workloads evolve, evolve procedures. Look for improvement opportunities continuously.
30. **Build local-first** — Enable collaboration and ownership. Work offline, collaborate across devices, improve security and user control.
31. **Build on our own or our client's infrastructure as soon as possible** — Cloud is cheaper early, costlier later. Architect to avoid lock-in. Think about repatriation up front.
32. **Use and build open source** — Commit to the four freedoms. Bootstrap with closed source if needed, then build a data flywheel and fine-tune your own models.

## Ethics

33. **Do not implement dark patterns** — Never use deceptive design that tricks users, makes unsubscribing harder, or nudges into unwanted purchases.
34. **Prevent systems from evolving into walled gardens** — It is unethical to lock clients and their data in. Keep systems open.
