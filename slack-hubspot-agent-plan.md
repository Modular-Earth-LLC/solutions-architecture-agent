# Slack ↔ HubSpot Demo-Assignment Bot — Starter Plan

Optimized for shipping fast with minimal ops.

## Architecture

One container, two SaaS APIs, no database.

- Slack app using **Bolt for Python** in **Socket Mode** (no public URL, no API gateway)
- **Azure OpenAI in Microsoft Foundry**, model `gpt-5-mini` — fast, cheap, plenty for parsing intent
- **HubSpot CRM Tasks API** (2026-03 date-versioned release) for CRUD
- Round-robin: query HubSpot for AI-engineer owners and assign to the one with the fewest open tasks — derived live, no state to manage
- Host on **Azure Container Apps**, scale-to-zero, system-assigned **managed identity** → Foundry (keyless)
- Slack + HubSpot tokens in **Key Vault**, referenced from ACA secrets
- Source in **GitHub**, deploy via GitHub Actions → ACR → ACA

## Reference Architecture

Microsoft published a production-ready guide that uses the exact same pattern (Bolt + Socket Mode + Container Apps + Key Vault + managed identity). Treat it as the skeleton:

[Azure Support Slack Bot on Container Apps — Microsoft guide](https://techcommunity.microsoft.com/blog/startupsatmicrosoftblog/azure-support-slack-bot-on-azure-container-apps-production-ready-guide/4436423)

## Starter Template

Fork this and swap the OpenAI client for Azure OpenAI with `DefaultAzureCredential`:

[slack-samples/bolt-python-ai-chatbot](https://github.com/slack-samples/bolt-python-ai-chatbot) — official Slack sample, Azure OpenAI provider already supported via `OPENAI_PROVIDER=azure`

## Build Order

1. Fork the template, get it talking in a dev workspace with your own bot tokens
2. Point it at a `gpt-5-mini` deployment in Foundry, auth via managed identity locally with `az login`
3. Add a `hubspot.py` with three functions: `find_least_loaded_owner()`, `create_task()`, `post_assignment()`
4. Replace the chat handler with: parse message → choose owner → create HubSpot task → post to the assignments channel
5. Deploy to Container Apps with `az containerapp up`, point it at Key Vault for secrets

## Key Docs

- [Bolt for Python quickstart](https://docs.slack.dev/tools/bolt-python/getting-started/)
- [Slack Socket Mode](https://docs.slack.dev/apis/events-api/using-socket-mode/)
- [Azure OpenAI in Foundry quickstart](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/quickstart)
- [Foundry managed identity setup](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/managed-identity?view=foundry-classic)
- [HubSpot Tasks API guide (v3)](https://developers.hubspot.com/docs/api-reference/crm-tasks-v3/guide)
- [Azure Container Apps overview](https://learn.microsoft.com/en-us/azure/container-apps/overview)

## Avoid (Intentionally)

- The `azure-ai-inference` SDK — it's retiring Aug 26, 2026. Use the stable OpenAI Python SDK pointed at the Foundry endpoint.
- A database — round-robin is re-derived from HubSpot each call.
- APIM, Service Bus, or anything between Slack and the worker — Socket Mode plus direct calls is enough at this scale.
- GPT-4.1 — known issues in the 4.1 series; `gpt-5-mini` is the current sweet spot for cost-to-quality.

## Goal

Working end-to-end flow in a dev workspace by end of week. The Foundry deployment and RBAC step is the one place this usually stalls — pair on that if needed.
