# Knowledge Base Schema Design for 9-Skill SA Agent

**Version:** 1.0.0
**Date:** 2026-03-16
**Status:** Implemented — historical design context preserved

---

## Design Decisions

### 1. File topology: Engagement-centered hybrid

**Decision:** One engagement envelope file + domain-specific section files + one cross-cutting review file.

**Rationale:**
- The existing 3-file model (system_config, user_requirements, design_decisions) puts too many concerns into `design_decisions.json` (architecture + estimates + costs + project plan + security + compliance all in one 525-line file).
- A single monolithic engagement file would exceed reasonable context windows and violate progressive disclosure.
- Pure one-file-per-skill creates coupling problems: `/architecture` needs requirements context, `/estimate` needs architecture context, `/proposal` needs everything.

**Resolution:** Split by domain boundary, not by skill. Some skills share a file (e.g., `/requirements` writes to `requirements.json`, which `/architecture` reads). An `engagement.json` envelope file carries metadata, status, and cross-references. Each domain file is independently valid and self-contained.

### 2. Engagement types: 0-to-1 vs. migration

**Decision:** A single `engagement_type` enum at the engagement level, with conditional sections in domain files (e.g., `legacy_system` in requirements, `migration_strategy` in integration plan).

**Rationale:** The core lifecycle is identical for both types. The differences are additive sections, not separate schemas. Using `if/then/else` in JSON Schema handles conditional requirements cleanly.

### 3. State flow direction

**Decision:** Unidirectional data flow with explicit dependencies. Each file declares `$depends_on` listing which files it reads from. Skills never write to files they don't own.

```
system_config.json (READ-ONLY, human-managed)
       |
       v
engagement.json (envelope, written by any skill that starts an engagement)
       |
       v
requirements.json (/requirements writes)
       |
       v
architecture.json (/architecture writes, reads requirements)
       |
       +---> estimate.json (/estimate writes, reads requirements + architecture)
       |
       +---> data_model.json (/data-model writes, reads requirements + architecture)
       |
       +---> security_review.json (/security-review writes, reads requirements + architecture)
       |
       +---> integration_plan.json (/integration-plan writes, reads requirements + architecture)
       |
       v
project_plan.json (/project-plan writes, reads requirements + architecture + estimate)
       |
       v
reviews.json (/review writes, reads ANY skill output)
       |
       v
proposal output (/proposal reads ALL, writes to outputs/ not KB)
```

### 4. Review tracking

**Decision:** A dedicated `reviews.json` file with an array of review records, each referencing a target file, version hash, scores, and findings. This supports iteration history without polluting domain files.

### 5. Backward compatibility

**Decision:** The existing `user_requirements.json` and `design_decisions.json` remain functional during migration. New skills write to the new files. A `_migration` section in `engagement.json` tracks which format is active.

---

## File Inventory

| File | Owner skill(s) | Readers | Size target |
|------|---------------|---------|-------------|
| `system_config.json` | Human (READ-ONLY) | All skills | Unchanged |
| `engagement.json` | Any (creates), all (update status) | All skills | < 100 lines |
| `requirements.json` | `/requirements` | All downstream | < 400 lines |
| `architecture.json` | `/architecture` | estimate, data-model, security, integration, project-plan, proposal, review | < 500 lines |
| `estimate.json` | `/estimate` | project-plan, proposal, review | < 300 lines |
| `project_plan.json` | `/project-plan` | proposal, review | < 300 lines |
| `data_model.json` | `/data-model` | architecture (feedback), security, integration, proposal, review | < 400 lines |
| `security_review.json` | `/security-review` | architecture (feedback), proposal, review | < 300 lines |
| `integration_plan.json` | `/integration-plan` | project-plan, proposal, review | < 300 lines |
| `reviews.json` | `/review` | All skills (for iteration) | Grows over time |

---

## Schema Definitions

### engagement.json

```json
{
  "$schema": "./schemas/engagement.schema.json",
  "engagement_id": "eng-2026-001",
  "title": "Customer Support AI Assistant",
  "engagement_type": "greenfield",
  "status": "in_progress",
  "created_date": "2026-03-15",
  "last_updated": "2026-03-15",
  "client": {
    "name": "Acme Corp",
    "industry": "SaaS",
    "contact": "Jane Smith, CTO"
  },
  "lifecycle_state": {
    "requirements":     { "status": "complete",    "version": "1.2", "file": "requirements.json" },
    "architecture":     { "status": "in_progress", "version": "0.3", "file": "architecture.json" },
    "estimate":         { "status": "not_started", "version": null,  "file": "estimate.json" },
    "data_model":       { "status": "not_started", "version": null,  "file": "data_model.json" },
    "security_review":  { "status": "not_started", "version": null,  "file": "security_review.json" },
    "integration_plan": { "status": "not_started", "version": null,  "file": "integration_plan.json" },
    "project_plan":     { "status": "not_started", "version": null,  "file": "project_plan.json" }
  },
  "review_summary": {
    "total_reviews": 0,
    "latest_overall_score": null,
    "blocking_findings": 0
  },
  "_migration": {
    "legacy_requirements_file": "user_requirements.json",
    "legacy_decisions_file": "design_decisions.json",
    "migration_complete": false
  }
}
```

**Schema: `engagement.schema.json`**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "engagement.schema.json",
  "title": "Engagement Envelope",
  "description": "Top-level engagement metadata, lifecycle tracking, and cross-references between skill outputs.",
  "type": "object",
  "required": ["engagement_id", "title", "engagement_type", "status", "created_date", "lifecycle_state"],
  "properties": {
    "$schema": { "type": "string" },
    "engagement_id": {
      "type": "string",
      "pattern": "^eng-\\d{4}-\\d{3,}$",
      "description": "Unique engagement identifier: eng-YYYY-NNN"
    },
    "title": {
      "type": "string",
      "maxLength": 200,
      "description": "Human-readable engagement title"
    },
    "engagement_type": {
      "type": "string",
      "enum": ["greenfield", "migration", "modernization", "augmentation", "assessment"],
      "description": "greenfield = 0-to-1 new build. migration = move from legacy. modernization = upgrade existing. augmentation = add AI to existing. assessment = review only."
    },
    "status": {
      "type": "string",
      "enum": ["draft", "in_progress", "in_review", "approved", "on_hold", "completed", "cancelled"]
    },
    "created_date": { "type": "string", "format": "date" },
    "last_updated": { "type": "string", "format": "date" },
    "client": {
      "type": "object",
      "required": ["name"],
      "properties": {
        "name":     { "type": "string" },
        "industry": { "type": "string" },
        "contact":  { "type": "string" },
        "size":     { "type": "string", "enum": ["startup", "smb", "mid_market", "enterprise"] }
      }
    },
    "lifecycle_state": {
      "type": "object",
      "description": "Status of each skill domain. Skills update their own entry.",
      "required": ["requirements", "architecture"],
      "patternProperties": {
        "^[a-z_]+$": {
          "type": "object",
          "required": ["status", "version", "file"],
          "properties": {
            "status":  { "type": "string", "enum": ["not_started", "in_progress", "draft", "complete", "approved"] },
            "version": { "type": ["string", "null"], "pattern": "^\\d+\\.\\d+$" },
            "file":    { "type": "string" },
            "last_updated": { "type": "string", "format": "date" },
            "reviewed": { "type": "boolean", "default": false }
          }
        }
      }
    },
    "review_summary": {
      "type": "object",
      "properties": {
        "total_reviews":       { "type": "integer", "minimum": 0 },
        "latest_overall_score": { "type": ["number", "null"], "minimum": 0, "maximum": 10 },
        "blocking_findings":   { "type": "integer", "minimum": 0 }
      }
    },
    "tags": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Free-form tags for engagement categorization"
    },
    "_migration": {
      "type": "object",
      "properties": {
        "legacy_requirements_file": { "type": "string" },
        "legacy_decisions_file":    { "type": "string" },
        "migration_complete":       { "type": "boolean" }
      }
    }
  }
}
```

---

### requirements.json

```json
{
  "$schema": "./schemas/requirements.schema.json",
  "$depends_on": ["system_config.json"],
  "engagement_id": "eng-2026-001",
  "version": "1.2",
  "last_updated": "2026-03-15",
  "status": "complete",

  "client_context": {
    "legal_name": "Acme Corp",
    "brand_name": "Acme",
    "industry": "SaaS / Customer Success",
    "company_size": "mid_market",
    "ai_maturity": "intermediate",
    "ai_history": "Prior chatbot project with basic rule-based routing, no LLM experience"
  },

  "problem_statement": {
    "title": "AI-Powered Tier 1 Support Automation",
    "summary": "Automate 60% of tier-1 customer support inquiries using AI",
    "current_state": {
      "process_description": "Manual ticket triage by support agents",
      "tools_in_use": ["Zendesk", "Salesforce", "Internal KB wiki"],
      "pain_points": [
        "Average response time: 4 hours",
        "60% of tickets are repetitive FAQ-type questions",
        "Agent burnout from repetitive work"
      ],
      "annual_cost": "$1.2M support team cost",
      "volume": "2,000 tickets/month"
    },
    "desired_state": {
      "description": "AI handles FAQ-level inquiries instantly, escalates complex issues to humans",
      "target_improvements": [
        "Response time < 30 seconds for tier-1",
        "40-60% ticket deflection rate",
        "Higher agent satisfaction (focus on complex issues)"
      ]
    }
  },

  "ai_suitability_assessment": {
    "score": 8,
    "rationale": "High volume of repetitive, text-based inquiries with existing knowledge base",
    "favorable_factors": [
      "Large existing FAQ corpus",
      "Well-defined escalation criteria",
      "Measurable success metrics"
    ],
    "risk_factors": [
      "Customer trust concerns with AI responses",
      "Edge cases in product-specific troubleshooting"
    ],
    "recommendation": "strong_fit"
  },

  "success_criteria": [
    {
      "id": "SC-001",
      "metric": "ticket_deflection_rate",
      "description": "Percentage of tier-1 tickets resolved without human intervention",
      "baseline": 0,
      "target": 0.5,
      "measurement": "Zendesk API ticket resolution tracking",
      "timeframe": "3 months post-launch"
    },
    {
      "id": "SC-002",
      "metric": "first_response_time_seconds",
      "description": "Time to first meaningful response for tier-1 inquiries",
      "baseline": 14400,
      "target": 30,
      "measurement": "Zendesk response time analytics",
      "timeframe": "Immediate post-launch"
    }
  ],

  "stakeholders": [
    {
      "name": "Jane Smith",
      "role": "CTO",
      "type": "decision_maker",
      "approval_authority": ["technical", "budget"],
      "communication_preference": "weekly email"
    },
    {
      "name": "John Doe",
      "role": "VP Customer Success",
      "type": "decision_maker",
      "approval_authority": ["strategic", "operational"],
      "communication_preference": "bi-weekly demo"
    }
  ],

  "functional_requirements": [
    {
      "id": "FR-001",
      "title": "Natural language query understanding",
      "description": "System must understand customer inquiries in natural language and match to knowledge base articles",
      "priority": "must_have",
      "complexity": "high",
      "acceptance_criteria": [
        "Correctly classifies 90%+ of tier-1 inquiries",
        "Handles misspellings and colloquial language"
      ],
      "dependencies": []
    }
  ],

  "non_functional_requirements": {
    "performance": {
      "response_time_p95_ms": 2000,
      "throughput_rps": 50,
      "concurrent_users": 100
    },
    "availability": {
      "target_percent": 99.5,
      "planned_maintenance_window": "Sunday 2-4 AM EST"
    },
    "scalability": {
      "current_volume": "2000 tickets/month",
      "projected_growth": "20% year over year",
      "peak_multiplier": 3.0,
      "geographic_regions": ["us-east-1"]
    },
    "security": {
      "authentication": ["SSO via Okta"],
      "authorization_model": "RBAC",
      "data_classification": "internal_confidential",
      "encryption_requirements": ["AES-256 at rest", "TLS 1.3 in transit"],
      "compliance_frameworks": ["SOC2", "GDPR"]
    },
    "data_residency": {
      "required_regions": ["US"],
      "prohibited_regions": [],
      "data_retention_days": 365
    }
  },

  "data_landscape": {
    "sources": [
      {
        "name": "Zendesk tickets",
        "type": "api",
        "format": "JSON",
        "volume": "2000 records/month",
        "pii_present": true,
        "quality_notes": "Well-structured, some missing categories"
      },
      {
        "name": "Internal knowledge base",
        "type": "wiki",
        "format": "HTML/Markdown",
        "volume": "500 articles",
        "pii_present": false,
        "quality_notes": "30% articles outdated, needs curation"
      }
    ],
    "integration_points": [
      {
        "system": "Zendesk",
        "direction": "bidirectional",
        "protocol": "REST API",
        "auth_method": "API key"
      },
      {
        "system": "Salesforce",
        "direction": "read",
        "protocol": "REST API",
        "auth_method": "OAuth 2.0"
      }
    ]
  },

  "constraints": {
    "budget_range": "$75,000 - $100,000",
    "timeline_weeks": 12,
    "timeline_flexibility": "moderate",
    "technology_restrictions": ["No OpenAI (data privacy policy)", "AWS services preferred"],
    "team_constraints": "4 engineers, 60% capacity available"
  },

  "assumptions": [
    "Zendesk API access will be available within 2 weeks",
    "Knowledge base content will be curated before Phase 2",
    "SSO integration via Okta is already configured"
  ],

  "_metadata": {
    "discovery_method": "standard_discovery",
    "discovery_date": "2026-03-10",
    "discovery_duration_minutes": 45,
    "participants": ["Jane Smith (CTO)", "John Doe (VP CS)", "Alice Johnson (PM)"],
    "completeness": "complete",
    "validation_status": "approved"
  }
}
```

**Schema: `requirements.schema.json`** (key parts)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "requirements.schema.json",
  "title": "Requirements",
  "description": "Client context, problem statement, success criteria, and requirements gathered by /requirements skill.",
  "type": "object",
  "required": ["engagement_id", "version", "status", "client_context", "problem_statement", "success_criteria", "functional_requirements"],
  "properties": {
    "$schema":     { "type": "string" },
    "$depends_on": { "type": "array", "items": { "type": "string" } },
    "engagement_id": { "type": "string", "pattern": "^eng-\\d{4}-\\d{3,}$" },
    "version":     { "type": "string", "pattern": "^\\d+\\.\\d+$" },
    "last_updated": { "type": "string", "format": "date" },
    "status":      { "type": "string", "enum": ["draft", "in_progress", "complete", "approved"] },

    "client_context": {
      "type": "object",
      "required": ["legal_name", "industry"],
      "properties": {
        "legal_name":   { "type": "string" },
        "brand_name":   { "type": "string" },
        "industry":     { "type": "string" },
        "company_size": { "type": "string", "enum": ["startup", "smb", "mid_market", "enterprise"] },
        "ai_maturity":  { "type": "string", "enum": ["beginner", "intermediate", "advanced"] },
        "ai_history":   { "type": "string" }
      }
    },

    "problem_statement": {
      "type": "object",
      "required": ["title", "summary", "current_state", "desired_state"],
      "properties": {
        "title":   { "type": "string", "maxLength": 200 },
        "summary": { "type": "string", "maxLength": 2000 },
        "current_state": {
          "type": "object",
          "properties": {
            "process_description": { "type": "string" },
            "tools_in_use":        { "type": "array", "items": { "type": "string" } },
            "pain_points":         { "type": "array", "items": { "type": "string" }, "minItems": 1 },
            "annual_cost":         { "type": "string" },
            "volume":              { "type": "string" }
          }
        },
        "desired_state": {
          "type": "object",
          "properties": {
            "description":         { "type": "string" },
            "target_improvements": { "type": "array", "items": { "type": "string" } }
          }
        }
      }
    },

    "ai_suitability_assessment": {
      "type": "object",
      "properties": {
        "score":             { "type": "integer", "minimum": 1, "maximum": 10 },
        "rationale":         { "type": "string" },
        "favorable_factors": { "type": "array", "items": { "type": "string" } },
        "risk_factors":      { "type": "array", "items": { "type": "string" } },
        "recommendation":    { "type": "string", "enum": ["strong_fit", "good_fit", "conditional_fit", "poor_fit", "not_recommended"] }
      }
    },

    "success_criteria": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["id", "metric", "target"],
        "properties": {
          "id":          { "type": "string", "pattern": "^SC-\\d{3}$" },
          "metric":      { "type": "string" },
          "description": { "type": "string" },
          "baseline":    { "type": "number" },
          "target":      { "type": "number" },
          "measurement": { "type": "string" },
          "timeframe":   { "type": "string" }
        }
      }
    },

    "stakeholders": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["name", "role", "type"],
        "properties": {
          "name": { "type": "string" },
          "role": { "type": "string" },
          "type": { "type": "string", "enum": ["decision_maker", "contributor", "end_user", "reviewer"] },
          "approval_authority":        { "type": "array", "items": { "type": "string" } },
          "communication_preference":  { "type": "string" }
        }
      }
    },

    "functional_requirements": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "title", "priority"],
        "properties": {
          "id":          { "type": "string", "pattern": "^FR-\\d{3}$" },
          "title":       { "type": "string" },
          "description": { "type": "string" },
          "priority":    { "type": "string", "enum": ["must_have", "should_have", "nice_to_have"] },
          "complexity":  { "type": "string", "enum": ["low", "medium", "high", "very_high"] },
          "acceptance_criteria": { "type": "array", "items": { "type": "string" } },
          "dependencies": { "type": "array", "items": { "type": "string" } }
        }
      }
    },

    "non_functional_requirements": {
      "type": "object",
      "properties": {
        "performance":  {
          "type": "object",
          "properties": {
            "response_time_p95_ms": { "type": "integer", "minimum": 0 },
            "throughput_rps":       { "type": "integer", "minimum": 0 },
            "concurrent_users":     { "type": "integer", "minimum": 0 }
          }
        },
        "availability": {
          "type": "object",
          "properties": {
            "target_percent":             { "type": "number", "minimum": 0, "maximum": 100 },
            "planned_maintenance_window": { "type": "string" }
          }
        },
        "scalability": {
          "type": "object",
          "properties": {
            "current_volume":     { "type": "string" },
            "projected_growth":   { "type": "string" },
            "peak_multiplier":    { "type": "number" },
            "geographic_regions": { "type": "array", "items": { "type": "string" } }
          }
        },
        "security": {
          "type": "object",
          "properties": {
            "authentication":         { "type": "array", "items": { "type": "string" } },
            "authorization_model":    { "type": "string" },
            "data_classification":    { "type": "string", "enum": ["public", "internal", "internal_confidential", "restricted"] },
            "encryption_requirements": { "type": "array", "items": { "type": "string" } },
            "compliance_frameworks":  { "type": "array", "items": { "type": "string" } }
          }
        },
        "data_residency": {
          "type": "object",
          "properties": {
            "required_regions":   { "type": "array", "items": { "type": "string" } },
            "prohibited_regions": { "type": "array", "items": { "type": "string" } },
            "data_retention_days": { "type": "integer", "minimum": 0 }
          }
        }
      }
    },

    "data_landscape": {
      "type": "object",
      "properties": {
        "sources": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["name", "type"],
            "properties": {
              "name":          { "type": "string" },
              "type":          { "type": "string", "enum": ["database", "api", "file", "wiki", "streaming", "data_warehouse"] },
              "format":        { "type": "string" },
              "volume":        { "type": "string" },
              "pii_present":   { "type": "boolean" },
              "quality_notes": { "type": "string" }
            }
          }
        },
        "integration_points": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["system", "direction"],
            "properties": {
              "system":      { "type": "string" },
              "direction":   { "type": "string", "enum": ["read", "write", "bidirectional"] },
              "protocol":    { "type": "string" },
              "auth_method": { "type": "string" }
            }
          }
        }
      }
    },

    "constraints": {
      "type": "object",
      "properties": {
        "budget_range":            { "type": "string" },
        "timeline_weeks":          { "type": "integer", "minimum": 0 },
        "timeline_flexibility":    { "type": "string", "enum": ["hard", "moderate", "soft"] },
        "technology_restrictions":  { "type": "array", "items": { "type": "string" } },
        "team_constraints":        { "type": "string" }
      }
    },

    "assumptions": {
      "type": "array",
      "items": { "type": "string" }
    },

    "_metadata": {
      "type": "object",
      "properties": {
        "discovery_method":           { "type": "string", "enum": ["quick_discovery", "standard_discovery", "comprehensive_workshop", "extraction_from_notes"] },
        "discovery_date":             { "type": "string", "format": "date" },
        "discovery_duration_minutes": { "type": "integer", "minimum": 0 },
        "participants":               { "type": "array", "items": { "type": "string" } },
        "completeness":               { "type": "string", "enum": ["incomplete", "partial", "complete"] },
        "validation_status":          { "type": "string", "enum": ["draft", "reviewed", "approved"] }
      }
    }
  }
}
```

---

### architecture.json

```json
{
  "$schema": "./schemas/architecture.schema.json",
  "$depends_on": ["system_config.json", "requirements.json"],
  "engagement_id": "eng-2026-001",
  "version": "0.3",
  "last_updated": "2026-03-15",
  "status": "in_progress",

  "executive_summary": {
    "recommended_approach": "RAG-powered support agent using Claude on AWS Bedrock with Zendesk integration",
    "confidence_level": "high",
    "go_no_go": "go",
    "key_benefits": [
      "50%+ ticket deflection within 3 months",
      "Sub-30-second response times"
    ],
    "key_risks": [
      "Knowledge base quality may limit accuracy in first 2 months"
    ],
    "total_investment_range": "$75K-$95K"
  },

  "tech_stack": {
    "llm": {
      "provider": "anthropic",
      "primary_model": "claude-sonnet-4-6",
      "fallback_model": "claude-haiku-4-5-20251001",
      "hosting": "aws_bedrock",
      "rationale": "Client requires AWS. Sonnet for complex queries, Haiku for FAQ classification."
    },
    "orchestration": {
      "framework": "langchain",
      "version": "0.3.x",
      "pattern": "rag_with_routing",
      "rationale": "Mature RAG tooling, Bedrock integration, team familiarity"
    },
    "backend": {
      "language": "python",
      "framework": "fastapi",
      "api_style": "rest"
    },
    "frontend": {
      "framework": "none",
      "type": "embedded_widget",
      "rationale": "Embedded in Zendesk via Web Widget SDK"
    },
    "data_stores": {
      "primary_db": { "technology": "postgresql", "hosting": "rds", "purpose": "Conversation history, analytics" },
      "vector_db":  { "technology": "pgvector",   "hosting": "rds", "purpose": "Knowledge base embeddings" },
      "cache":      { "technology": "redis",      "hosting": "elasticache", "purpose": "Session state, rate limiting" }
    },
    "infrastructure": {
      "cloud_provider": "aws",
      "compute": "ecs_fargate",
      "container_orchestration": "ecs",
      "deployment_strategy": "blue_green",
      "region": "us-east-1",
      "monitoring": "cloudwatch",
      "logging": "cloudwatch_logs"
    }
  },

  "component_design": [
    {
      "id": "C-001",
      "name": "Query Router",
      "technology": "LangChain + Claude Haiku",
      "purpose": "Classifies incoming queries as tier-1 (AI-handleable) or tier-2+ (human escalation)",
      "inputs": ["raw customer query"],
      "outputs": ["classification label", "confidence score", "routed query"],
      "scalability": "Stateless, horizontally scalable",
      "cost_driver": true
    },
    {
      "id": "C-002",
      "name": "RAG Knowledge Engine",
      "technology": "LangChain + pgvector + Claude Sonnet",
      "purpose": "Retrieves relevant KB articles and generates contextual responses",
      "inputs": ["classified query", "conversation history"],
      "outputs": ["generated response", "source citations", "confidence score"],
      "scalability": "Stateless compute, vector DB scales independently",
      "cost_driver": true
    }
  ],

  "data_flows": [
    {
      "id": "DF-001",
      "name": "Customer Query Flow",
      "source": "Zendesk Web Widget",
      "destination": "Query Router",
      "protocol": "HTTPS/REST",
      "data_type": "Customer inquiry text + metadata",
      "latency_target_ms": 500,
      "encryption": "TLS 1.3"
    }
  ],

  "diagrams": {
    "system_context": {
      "format": "mermaid",
      "code": "graph TD\n  Customer-->|Query|Widget[Zendesk Widget]\n  Widget-->|API|Router[Query Router]\n  Router-->|Tier 1|RAG[RAG Engine]\n  Router-->|Tier 2+|Agent[Human Agent]\n  RAG-->|Response|Widget\n  RAG<-->|Embeddings|VectorDB[(pgvector)]\n  RAG<-->|History|DB[(PostgreSQL)]"
    },
    "deployment": {
      "format": "mermaid",
      "code": ""
    }
  },

  "well_architected_scores": {
    "operational_excellence": 7.5,
    "security": 8.0,
    "reliability": 7.0,
    "performance_efficiency": 8.5,
    "cost_optimization": 7.5,
    "sustainability": 6.0,
    "overall": 7.4,
    "notes": {
      "security": "SOC2 and GDPR addressed. PII handling via tokenization.",
      "reliability": "Single-region deployment. DR plan needed for Phase 2."
    }
  },

  "alternatives_considered": [
    {
      "name": "OpenAI GPT-4 on Azure",
      "summary": "Higher accuracy benchmarks but violates client data privacy policy",
      "why_rejected": "Client policy prohibits OpenAI data processing"
    }
  ],

  "_metadata": {
    "architect": "SA Agent",
    "design_method": "component_based",
    "validation_status": "draft"
  }
}
```

**Schema: `architecture.schema.json`** (key structural types)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "architecture.schema.json",
  "title": "Architecture Design",
  "description": "System architecture, tech stack, component design, and diagrams produced by /architecture skill.",
  "type": "object",
  "required": ["engagement_id", "version", "status", "tech_stack", "component_design"],
  "properties": {
    "$schema":     { "type": "string" },
    "$depends_on": { "type": "array", "items": { "type": "string" } },
    "engagement_id": { "type": "string" },
    "version":       { "type": "string" },
    "last_updated":  { "type": "string", "format": "date" },
    "status":        { "type": "string", "enum": ["draft", "in_progress", "complete", "approved"] },

    "executive_summary": {
      "type": "object",
      "properties": {
        "recommended_approach":   { "type": "string" },
        "confidence_level":       { "type": "string", "enum": ["high", "medium", "low"] },
        "go_no_go":               { "type": "string", "enum": ["go", "go_with_conditions", "pause", "no_go"] },
        "key_benefits":           { "type": "array", "items": { "type": "string" } },
        "key_risks":              { "type": "array", "items": { "type": "string" } },
        "total_investment_range": { "type": "string" }
      }
    },

    "tech_stack": {
      "type": "object",
      "required": ["llm", "backend", "infrastructure"],
      "properties": {
        "llm": {
          "type": "object",
          "required": ["provider", "primary_model"],
          "properties": {
            "provider":       { "type": "string" },
            "primary_model":  { "type": "string" },
            "fallback_model": { "type": "string" },
            "hosting":        { "type": "string" },
            "rationale":      { "type": "string" }
          }
        },
        "orchestration": {
          "type": "object",
          "properties": {
            "framework": { "type": "string" },
            "version":   { "type": "string" },
            "pattern":   { "type": "string", "enum": ["direct_api", "rag_with_routing", "agent_loop", "multi_agent", "pipeline"] },
            "rationale": { "type": "string" }
          }
        },
        "backend": {
          "type": "object",
          "properties": {
            "language":  { "type": "string" },
            "framework": { "type": "string" },
            "api_style": { "type": "string", "enum": ["rest", "graphql", "grpc", "websocket"] }
          }
        },
        "frontend": {
          "type": "object",
          "properties": {
            "framework": { "type": "string" },
            "type":      { "type": "string", "enum": ["web_app", "mobile_app", "desktop_app", "embedded_widget", "cli", "none"] },
            "rationale": { "type": "string" }
          }
        },
        "data_stores": {
          "type": "object",
          "patternProperties": {
            ".*": {
              "type": "object",
              "properties": {
                "technology": { "type": "string" },
                "hosting":    { "type": "string" },
                "purpose":    { "type": "string" }
              }
            }
          }
        },
        "infrastructure": {
          "type": "object",
          "properties": {
            "cloud_provider":           { "type": "string" },
            "compute":                  { "type": "string" },
            "container_orchestration":  { "type": "string" },
            "deployment_strategy":      { "type": "string", "enum": ["blue_green", "canary", "rolling", "recreate"] },
            "region":                   { "type": "string" },
            "monitoring":               { "type": "string" },
            "logging":                  { "type": "string" }
          }
        }
      }
    },

    "component_design": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "name", "purpose"],
        "properties": {
          "id":          { "type": "string", "pattern": "^C-\\d{3}$" },
          "name":        { "type": "string" },
          "technology":  { "type": "string" },
          "purpose":     { "type": "string" },
          "inputs":      { "type": "array", "items": { "type": "string" } },
          "outputs":     { "type": "array", "items": { "type": "string" } },
          "scalability": { "type": "string" },
          "cost_driver": { "type": "boolean" }
        }
      }
    },

    "data_flows": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "name", "source", "destination"],
        "properties": {
          "id":                { "type": "string", "pattern": "^DF-\\d{3}$" },
          "name":              { "type": "string" },
          "source":            { "type": "string" },
          "destination":       { "type": "string" },
          "protocol":          { "type": "string" },
          "data_type":         { "type": "string" },
          "latency_target_ms": { "type": "integer" },
          "encryption":        { "type": "string" }
        }
      }
    },

    "diagrams": {
      "type": "object",
      "patternProperties": {
        ".*": {
          "type": "object",
          "properties": {
            "format": { "type": "string", "enum": ["mermaid", "ascii", "plantuml"] },
            "code":   { "type": "string" }
          }
        }
      }
    },

    "well_architected_scores": {
      "type": "object",
      "properties": {
        "operational_excellence":  { "type": "number", "minimum": 0, "maximum": 10 },
        "security":                { "type": "number", "minimum": 0, "maximum": 10 },
        "reliability":             { "type": "number", "minimum": 0, "maximum": 10 },
        "performance_efficiency":  { "type": "number", "minimum": 0, "maximum": 10 },
        "cost_optimization":       { "type": "number", "minimum": 0, "maximum": 10 },
        "sustainability":          { "type": "number", "minimum": 0, "maximum": 10 },
        "overall":                 { "type": "number", "minimum": 0, "maximum": 10 },
        "notes":                   { "type": "object" }
      }
    },

    "alternatives_considered": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["name", "why_rejected"],
        "properties": {
          "name":         { "type": "string" },
          "summary":      { "type": "string" },
          "why_rejected": { "type": "string" }
        }
      }
    },

    "_metadata": { "type": "object" }
  }
}
```

---

### estimate.json

```json
{
  "$schema": "./schemas/estimate.schema.json",
  "$depends_on": ["requirements.json", "architecture.json"],
  "engagement_id": "eng-2026-001",
  "version": "1.0",
  "last_updated": "2026-03-15",
  "status": "complete",

  "methodology": "bottom_up",
  "confidence_level": "medium",
  "currency": "USD",

  "team_composition": [
    {
      "role": "Senior ML Engineer",
      "count": 1,
      "experience_level": "senior",
      "allocation_percent": 80,
      "duration_weeks": 12,
      "hourly_rate": 175,
      "total_cost": 67200,
      "responsibilities": ["RAG pipeline", "Model integration", "Prompt engineering"]
    },
    {
      "role": "Backend Developer",
      "count": 1,
      "experience_level": "mid_level",
      "allocation_percent": 100,
      "duration_weeks": 10,
      "hourly_rate": 125,
      "total_cost": 50000,
      "responsibilities": ["API development", "Zendesk integration", "Database design"]
    },
    {
      "role": "DevOps Engineer",
      "count": 1,
      "experience_level": "mid_level",
      "allocation_percent": 50,
      "duration_weeks": 12,
      "hourly_rate": 140,
      "total_cost": 33600,
      "responsibilities": ["Infrastructure", "CI/CD", "Monitoring"]
    }
  ],

  "loe_breakdown": {
    "total_hours": 1520,
    "by_phase": [
      { "phase": "Planning & Design",    "hours": 120, "weeks": 2, "parallel": false },
      { "phase": "Foundation & Infra",    "hours": 200, "weeks": 3, "parallel": true },
      { "phase": "Core Development",      "hours": 640, "weeks": 4, "parallel": true },
      { "phase": "Integration & Testing", "hours": 320, "weeks": 2, "parallel": true },
      { "phase": "Deployment & Handoff",  "hours": 240, "weeks": 1, "parallel": false }
    ],
    "by_component": [
      { "component": "Query Router (C-001)",        "hours": 200, "complexity": "high" },
      { "component": "RAG Knowledge Engine (C-002)", "hours": 400, "complexity": "high" },
      { "component": "Zendesk Integration",          "hours": 160, "complexity": "medium" },
      { "component": "Infrastructure & CI/CD",       "hours": 240, "complexity": "medium" },
      { "component": "Testing & QA",                 "hours": 280, "complexity": "medium" },
      { "component": "Documentation & Handoff",      "hours": 120, "complexity": "low" },
      { "component": "Project Management",           "hours": 120, "complexity": "low" }
    ],
    "risk_buffer": {
      "percent": 20,
      "hours": 304,
      "rationale": "First AI project for client, Zendesk API complexity uncertain"
    }
  },

  "cost_model": {
    "development": {
      "internal_team": 150800,
      "contractors": 0,
      "training": 5000,
      "total": 155800
    },
    "infrastructure_monthly": {
      "compute_ecs": 450,
      "rds_postgresql": 200,
      "elasticache_redis": 150,
      "bedrock_api": 800,
      "cloudwatch": 50,
      "networking": 100,
      "total": 1750
    },
    "infrastructure_first_year": 21000,
    "third_party_monthly": {
      "zendesk_api": 0,
      "total": 0
    },
    "total_first_year": 176800,
    "tco_3_year": {
      "year_1": 176800,
      "year_2": 25000,
      "year_3": 27000,
      "total": 228800
    },
    "roi": {
      "annual_savings_estimate": 480000,
      "payback_period_months": 5,
      "roi_3_year_percent": 525
    }
  },

  "assumptions": [
    "Hourly rates based on US market mid-2026 averages",
    "Bedrock API costs assume 50K queries/month at average 2K tokens each",
    "No Zendesk licensing costs (client already has enterprise plan)",
    "Internal team has Python and AWS experience"
  ],

  "complexity_rating": "high",
  "complexity_factors": [
    "RAG pipeline tuning and evaluation",
    "Zendesk bidirectional integration",
    "PII handling across systems"
  ],

  "_metadata": {
    "estimator": "SA Agent",
    "estimation_date": "2026-03-15",
    "validation_status": "draft"
  }
}
```

**Schema: `estimate.schema.json`**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "estimate.schema.json",
  "title": "Estimate",
  "description": "Cost models, LOE breakdowns, team composition, and infrastructure costs produced by /estimate skill.",
  "type": "object",
  "required": ["engagement_id", "version", "status", "methodology", "team_composition", "loe_breakdown", "cost_model"],
  "properties": {
    "$schema":     { "type": "string" },
    "$depends_on": { "type": "array", "items": { "type": "string" } },
    "engagement_id": { "type": "string" },
    "version":       { "type": "string" },
    "last_updated":  { "type": "string", "format": "date" },
    "status":        { "type": "string", "enum": ["draft", "in_progress", "complete", "approved"] },

    "methodology": {
      "type": "string",
      "enum": ["bottom_up", "top_down", "three_point", "analogous", "parametric"]
    },
    "confidence_level": {
      "type": "string",
      "enum": ["high", "medium", "low"]
    },
    "currency": { "type": "string", "default": "USD" },

    "team_composition": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["role", "count", "duration_weeks"],
        "properties": {
          "role":              { "type": "string" },
          "count":             { "type": "integer", "minimum": 1 },
          "experience_level":  { "type": "string", "enum": ["junior", "mid_level", "senior", "expert"] },
          "allocation_percent": { "type": "number", "minimum": 0, "maximum": 100 },
          "duration_weeks":    { "type": "integer", "minimum": 1 },
          "hourly_rate":       { "type": "number", "minimum": 0 },
          "total_cost":        { "type": "number", "minimum": 0 },
          "responsibilities":  { "type": "array", "items": { "type": "string" } }
        }
      }
    },

    "loe_breakdown": {
      "type": "object",
      "required": ["total_hours", "by_phase"],
      "properties": {
        "total_hours": { "type": "number", "minimum": 0 },
        "by_phase": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["phase", "hours", "weeks"],
            "properties": {
              "phase":    { "type": "string" },
              "hours":    { "type": "number", "minimum": 0 },
              "weeks":    { "type": "number", "minimum": 0 },
              "parallel": { "type": "boolean" }
            }
          }
        },
        "by_component": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["component", "hours"],
            "properties": {
              "component":  { "type": "string" },
              "hours":      { "type": "number", "minimum": 0 },
              "complexity": { "type": "string", "enum": ["low", "medium", "high", "very_high"] }
            }
          }
        },
        "risk_buffer": {
          "type": "object",
          "properties": {
            "percent":   { "type": "number", "minimum": 0, "maximum": 100 },
            "hours":     { "type": "number", "minimum": 0 },
            "rationale": { "type": "string" }
          }
        }
      }
    },

    "cost_model": {
      "type": "object",
      "required": ["development", "infrastructure_monthly", "total_first_year"],
      "properties": {
        "development": {
          "type": "object",
          "properties": {
            "internal_team": { "type": "number" },
            "contractors":   { "type": "number" },
            "training":      { "type": "number" },
            "total":         { "type": "number" }
          }
        },
        "infrastructure_monthly": {
          "type": "object",
          "description": "Monthly recurring infrastructure costs. Keys are service names, values are USD amounts.",
          "properties": {
            "total": { "type": "number" }
          },
          "additionalProperties": { "type": "number" }
        },
        "infrastructure_first_year": { "type": "number" },
        "third_party_monthly": {
          "type": "object",
          "properties": {
            "total": { "type": "number" }
          },
          "additionalProperties": { "type": "number" }
        },
        "total_first_year": { "type": "number" },
        "tco_3_year": {
          "type": "object",
          "properties": {
            "year_1": { "type": "number" },
            "year_2": { "type": "number" },
            "year_3": { "type": "number" },
            "total":  { "type": "number" }
          }
        },
        "roi": {
          "type": "object",
          "properties": {
            "annual_savings_estimate":  { "type": "number" },
            "payback_period_months":    { "type": "number" },
            "roi_3_year_percent":       { "type": "number" }
          }
        }
      }
    },

    "assumptions":         { "type": "array", "items": { "type": "string" } },
    "complexity_rating":   { "type": "string", "enum": ["low", "medium", "high", "very_high"] },
    "complexity_factors":  { "type": "array", "items": { "type": "string" } },
    "_metadata": { "type": "object" }
  }
}
```

---

### project_plan.json

```json
{
  "$schema": "./schemas/project_plan.schema.json",
  "$depends_on": ["requirements.json", "architecture.json", "estimate.json"],
  "engagement_id": "eng-2026-001",
  "version": "1.0",
  "last_updated": "2026-03-15",
  "status": "draft",

  "approach": "agile",
  "total_duration_weeks": 12,
  "start_date": "2026-04-01",
  "target_end_date": "2026-06-24",

  "phases": [
    {
      "id": "P-001",
      "name": "Planning & Design",
      "start_week": 1,
      "end_week": 2,
      "objectives": ["Finalize architecture", "Set up infrastructure", "Sprint planning"],
      "deliverables": ["Architecture document approved", "Dev environment provisioned", "Sprint backlog created"],
      "success_criteria": ["All team members onboarded", "CI/CD pipeline running"],
      "team_allocation": ["ML Engineer 80%", "DevOps 100%"],
      "dependencies": [],
      "risks": ["Infrastructure provisioning delays"]
    },
    {
      "id": "P-002",
      "name": "Foundation & RAG Pipeline",
      "start_week": 3,
      "end_week": 5,
      "objectives": ["Build RAG pipeline", "Integrate vector DB", "Build query router"],
      "deliverables": ["Working RAG prototype", "Query classification model", "API scaffolding"],
      "success_criteria": ["RAG returns relevant results for 80% of test queries"],
      "team_allocation": ["ML Engineer 100%", "Backend Dev 100%"],
      "dependencies": ["P-001"],
      "risks": ["Knowledge base quality issues"]
    },
    {
      "id": "P-003",
      "name": "Integration & Polish",
      "start_week": 6,
      "end_week": 9,
      "objectives": ["Zendesk integration", "Conversation UI", "Error handling", "Prompt tuning"],
      "deliverables": ["End-to-end working system", "Zendesk widget deployed to staging"],
      "success_criteria": ["Full ticket lifecycle works in staging"],
      "team_allocation": ["ML Engineer 80%", "Backend Dev 100%", "DevOps 50%"],
      "dependencies": ["P-002"],
      "risks": ["Zendesk API rate limits", "Edge cases in routing"]
    },
    {
      "id": "P-004",
      "name": "Testing & Deployment",
      "start_week": 10,
      "end_week": 12,
      "objectives": ["Load testing", "Security audit", "Production deployment", "Handoff"],
      "deliverables": ["Production system live", "Runbook", "Training materials"],
      "success_criteria": ["System handles 3x peak load", "Zero critical security findings"],
      "team_allocation": ["ML Engineer 50%", "Backend Dev 80%", "DevOps 100%"],
      "dependencies": ["P-003"],
      "risks": ["Production issues during rollout"]
    }
  ],

  "milestones": [
    { "id": "M-001", "name": "Architecture Approved",    "target_date": "2026-04-14", "phase": "P-001", "gate_type": "approval" },
    { "id": "M-002", "name": "RAG Prototype Demo",       "target_date": "2026-04-28", "phase": "P-002", "gate_type": "demo" },
    { "id": "M-003", "name": "Staging Deployment",       "target_date": "2026-05-26", "phase": "P-003", "gate_type": "demo" },
    { "id": "M-004", "name": "Production Go-Live",       "target_date": "2026-06-17", "phase": "P-004", "gate_type": "approval" },
    { "id": "M-005", "name": "Handoff Complete",         "target_date": "2026-06-24", "phase": "P-004", "gate_type": "signoff" }
  ],

  "critical_path": ["P-001", "P-002", "P-003", "P-004"],

  "dependencies": {
    "internal": [
      { "from": "P-002", "to": "P-003", "type": "finish_to_start" },
      { "from": "P-003", "to": "P-004", "type": "finish_to_start" }
    ],
    "external": [
      { "dependency": "Zendesk API access", "owner": "Client IT", "needed_by": "2026-04-15", "status": "pending" },
      { "dependency": "Knowledge base curation", "owner": "Client CS team", "needed_by": "2026-05-01", "status": "not_started" }
    ]
  },

  "communication_plan": {
    "stakeholder_updates": "Weekly email to CTO, bi-weekly demo to VP CS",
    "demo_schedule": ["2026-04-28", "2026-05-12", "2026-05-26", "2026-06-09"],
    "decision_points": [
      { "date": "2026-04-14", "decision": "Architecture sign-off", "decider": "CTO" },
      { "date": "2026-06-10", "decision": "Go-live approval", "decider": "CTO + VP CS" }
    ]
  },

  "_migration_specific": null,

  "_metadata": {
    "planner": "SA Agent",
    "planning_date": "2026-03-15",
    "validation_status": "draft"
  }
}
```

**Note on migration engagements:** When `engagement_type` is `migration` or `modernization`, the project_plan includes a `_migration_specific` object:

```json
{
  "_migration_specific": {
    "legacy_system": "Monolithic Java ERP",
    "migration_strategy": "strangler_fig",
    "parallel_run_weeks": 4,
    "data_migration_phases": [
      { "phase": "Schema mapping", "weeks": 2 },
      { "phase": "Historical data ETL", "weeks": 3 },
      { "phase": "Live cutover", "weeks": 1 }
    ],
    "rollback_plan": "DNS failover to legacy system within 30 minutes",
    "feature_parity_checklist": []
  }
}
```

---

### data_model.json

```json
{
  "$schema": "./schemas/data_model.schema.json",
  "$depends_on": ["requirements.json", "architecture.json"],
  "engagement_id": "eng-2026-001",
  "version": "1.0",
  "last_updated": "2026-03-15",
  "status": "draft",

  "entities": [
    {
      "id": "E-001",
      "name": "Conversation",
      "description": "A customer support conversation session",
      "storage": "postgresql",
      "fields": [
        { "name": "id",            "type": "uuid",      "nullable": false, "primary_key": true },
        { "name": "customer_id",   "type": "varchar",   "nullable": false, "indexed": true },
        { "name": "channel",       "type": "varchar",   "nullable": false },
        { "name": "status",        "type": "enum",      "nullable": false, "values": ["active", "resolved", "escalated"] },
        { "name": "created_at",    "type": "timestamp", "nullable": false },
        { "name": "resolved_at",   "type": "timestamp", "nullable": true },
        { "name": "zendesk_ticket_id", "type": "varchar", "nullable": true, "indexed": true }
      ],
      "relationships": [
        { "target": "E-002", "type": "one_to_many", "foreign_key": "conversation_id" }
      ]
    },
    {
      "id": "E-002",
      "name": "Message",
      "description": "Individual message within a conversation",
      "storage": "postgresql",
      "fields": [
        { "name": "id",              "type": "uuid",      "nullable": false, "primary_key": true },
        { "name": "conversation_id", "type": "uuid",      "nullable": false, "indexed": true },
        { "name": "role",            "type": "enum",      "nullable": false, "values": ["customer", "agent", "system"] },
        { "name": "content",         "type": "text",      "nullable": false },
        { "name": "confidence_score", "type": "float",    "nullable": true },
        { "name": "source_citations", "type": "jsonb",   "nullable": true },
        { "name": "created_at",      "type": "timestamp", "nullable": false }
      ],
      "relationships": [
        { "target": "E-001", "type": "many_to_one", "foreign_key": "conversation_id" }
      ]
    }
  ],

  "vector_schemas": [
    {
      "name": "knowledge_base_embeddings",
      "storage": "pgvector",
      "embedding_model": "amazon.titan-embed-text-v2",
      "dimensions": 1024,
      "distance_metric": "cosine",
      "source": "Internal knowledge base articles",
      "chunk_strategy": {
        "method": "recursive_character",
        "chunk_size": 1000,
        "overlap": 200
      },
      "metadata_fields": [
        { "name": "article_id",   "type": "varchar" },
        { "name": "title",        "type": "varchar" },
        { "name": "category",     "type": "varchar" },
        { "name": "last_updated", "type": "date" }
      ],
      "index_type": "ivfflat",
      "index_lists": 100
    }
  ],

  "graph_schemas": [],

  "ontology": {
    "domain": "customer_support",
    "key_concepts": [
      { "concept": "Inquiry",   "definition": "A customer request or question", "related_to": ["Product", "Issue"] },
      { "concept": "Product",   "definition": "A product or service the customer uses", "related_to": ["Feature", "KBArticle"] },
      { "concept": "Issue",     "definition": "A problem or bug report", "related_to": ["Severity", "Resolution"] },
      { "concept": "KBArticle", "definition": "A knowledge base article with solution steps", "related_to": ["Product", "Issue"] }
    ],
    "taxonomy": {
      "inquiry_types": ["billing", "technical", "account", "feature_request", "bug_report"],
      "severity_levels": ["critical", "high", "medium", "low"]
    }
  },

  "data_governance": {
    "pii_fields": ["customer_id", "content"],
    "retention_policy": "365 days, then anonymize",
    "encryption": "AES-256 at rest via RDS encryption",
    "access_control": "Row-level security by tenant"
  },

  "_metadata": {
    "modeler": "SA Agent",
    "modeling_date": "2026-03-15",
    "validation_status": "draft"
  }
}
```

**Schema: `data_model.schema.json`**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "data_model.schema.json",
  "title": "Data Model",
  "description": "Entity relationships, schema definitions, vector/graph schemas, and ontology specs produced by /data-model skill.",
  "type": "object",
  "required": ["engagement_id", "version", "status", "entities"],
  "properties": {
    "$schema":       { "type": "string" },
    "$depends_on":   { "type": "array", "items": { "type": "string" } },
    "engagement_id": { "type": "string" },
    "version":       { "type": "string" },
    "last_updated":  { "type": "string", "format": "date" },
    "status":        { "type": "string", "enum": ["draft", "in_progress", "complete", "approved"] },

    "entities": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "name", "storage", "fields"],
        "properties": {
          "id":          { "type": "string", "pattern": "^E-\\d{3}$" },
          "name":        { "type": "string" },
          "description": { "type": "string" },
          "storage":     { "type": "string", "enum": ["postgresql", "dynamodb", "mongodb", "redis", "s3"] },
          "fields": {
            "type": "array",
            "items": {
              "type": "object",
              "required": ["name", "type", "nullable"],
              "properties": {
                "name":        { "type": "string" },
                "type":        { "type": "string" },
                "nullable":    { "type": "boolean" },
                "primary_key": { "type": "boolean" },
                "indexed":     { "type": "boolean" },
                "values":      { "type": "array", "items": { "type": "string" } }
              }
            }
          },
          "relationships": {
            "type": "array",
            "items": {
              "type": "object",
              "required": ["target", "type"],
              "properties": {
                "target":      { "type": "string" },
                "type":        { "type": "string", "enum": ["one_to_one", "one_to_many", "many_to_one", "many_to_many"] },
                "foreign_key": { "type": "string" },
                "join_table":  { "type": "string" }
              }
            }
          }
        }
      }
    },

    "vector_schemas": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["name", "storage", "dimensions", "distance_metric"],
        "properties": {
          "name":            { "type": "string" },
          "storage":         { "type": "string" },
          "embedding_model": { "type": "string" },
          "dimensions":      { "type": "integer", "minimum": 1 },
          "distance_metric": { "type": "string", "enum": ["cosine", "euclidean", "dot_product"] },
          "source":          { "type": "string" },
          "chunk_strategy": {
            "type": "object",
            "properties": {
              "method":     { "type": "string" },
              "chunk_size": { "type": "integer" },
              "overlap":    { "type": "integer" }
            }
          },
          "metadata_fields": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "name": { "type": "string" },
                "type": { "type": "string" }
              }
            }
          },
          "index_type":  { "type": "string" },
          "index_lists": { "type": "integer" }
        }
      }
    },

    "graph_schemas": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name":       { "type": "string" },
          "storage":    { "type": "string" },
          "node_types": { "type": "array", "items": { "type": "object" } },
          "edge_types": { "type": "array", "items": { "type": "object" } }
        }
      }
    },

    "ontology": {
      "type": "object",
      "properties": {
        "domain":       { "type": "string" },
        "key_concepts": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["concept", "definition"],
            "properties": {
              "concept":    { "type": "string" },
              "definition": { "type": "string" },
              "related_to": { "type": "array", "items": { "type": "string" } }
            }
          }
        },
        "taxonomy": { "type": "object" }
      }
    },

    "data_governance": {
      "type": "object",
      "properties": {
        "pii_fields":       { "type": "array", "items": { "type": "string" } },
        "retention_policy":  { "type": "string" },
        "encryption":        { "type": "string" },
        "access_control":    { "type": "string" }
      }
    },

    "_metadata": { "type": "object" }
  }
}
```

---

### security_review.json

```json
{
  "$schema": "./schemas/security_review.schema.json",
  "$depends_on": ["requirements.json", "architecture.json"],
  "engagement_id": "eng-2026-001",
  "version": "1.0",
  "last_updated": "2026-03-15",
  "status": "draft",

  "threat_model": {
    "methodology": "STRIDE",
    "scope": "Full system including Zendesk integration and Bedrock API",
    "threats": [
      {
        "id": "T-001",
        "category": "spoofing",
        "description": "Attacker impersonates customer via Zendesk widget",
        "affected_components": ["C-001"],
        "severity": "high",
        "likelihood": "medium",
        "risk_score": 6,
        "mitigation": "Zendesk SSO authentication, session validation",
        "residual_risk": "low",
        "status": "mitigated"
      },
      {
        "id": "T-002",
        "category": "injection",
        "description": "Prompt injection via customer query to manipulate LLM behavior",
        "affected_components": ["C-001", "C-002"],
        "severity": "high",
        "likelihood": "high",
        "risk_score": 9,
        "mitigation": "Input sanitization, system prompt hardening, output filtering, Bedrock Guardrails",
        "residual_risk": "medium",
        "status": "mitigated"
      }
    ]
  },

  "compliance_checklist": [
    {
      "framework": "SOC2",
      "requirement": "CC6.1 - Logical and Physical Access Controls",
      "status": "compliant",
      "evidence": "RBAC via Cognito, VPC isolation, encrypted data stores",
      "notes": ""
    },
    {
      "framework": "GDPR",
      "requirement": "Article 17 - Right to Erasure",
      "status": "partial",
      "evidence": "Deletion API implemented for user data",
      "notes": "Need to verify vector embedding deletion cascades"
    }
  ],

  "security_architecture": {
    "authentication": {
      "method": "Okta SSO via SAML 2.0",
      "mfa_required": true,
      "session_management": "JWT with 1-hour expiry, refresh token rotation"
    },
    "authorization": {
      "model": "RBAC",
      "roles": ["admin", "agent", "viewer"],
      "enforcement_point": "API Gateway + application middleware"
    },
    "network": {
      "vpc_design": "Public subnet (ALB) + Private subnet (ECS, RDS)",
      "security_groups": ["ALB-SG (443 inbound)", "ECS-SG (ALB only)", "RDS-SG (ECS only)"],
      "waf_enabled": true,
      "ddos_protection": "AWS Shield Standard"
    },
    "encryption": {
      "at_rest": "AES-256 via AWS KMS (RDS, S3, ElastiCache)",
      "in_transit": "TLS 1.3 everywhere",
      "key_management": "AWS KMS with automatic key rotation"
    },
    "secrets_management": "AWS Secrets Manager for API keys and DB credentials",
    "logging_and_monitoring": {
      "audit_log": "CloudTrail for API calls",
      "application_log": "CloudWatch Logs with 90-day retention",
      "alerting": "CloudWatch Alarms for auth failures, error rates"
    }
  },

  "ai_specific_security": {
    "prompt_injection_protection": ["Input validation regex", "System prompt isolation", "Bedrock Guardrails"],
    "output_filtering": ["PII detection before response", "Content moderation via Bedrock"],
    "model_access_control": "Bedrock IAM policies, no direct model API exposure",
    "data_poisoning_prevention": "KB article changes require human approval",
    "hallucination_mitigation": "Citation requirements, confidence thresholds, fallback to human"
  },

  "findings_summary": {
    "critical": 0,
    "high": 1,
    "medium": 3,
    "low": 2,
    "open_items": [
      {
        "id": "F-001",
        "severity": "high",
        "finding": "Vector embedding deletion not cascading on GDPR erasure requests",
        "recommendation": "Implement embedding deletion trigger on user data purge",
        "owner": "Backend Dev",
        "due_date": "2026-04-15"
      }
    ]
  },

  "_metadata": {
    "reviewer": "SA Agent",
    "review_date": "2026-03-15",
    "validation_status": "draft"
  }
}
```

**Schema: `security_review.schema.json`**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "security_review.schema.json",
  "title": "Security Review",
  "description": "Threat model, compliance checklist, security architecture, and AI-specific security produced by /security-review skill.",
  "type": "object",
  "required": ["engagement_id", "version", "status", "threat_model", "security_architecture"],
  "properties": {
    "$schema":       { "type": "string" },
    "$depends_on":   { "type": "array", "items": { "type": "string" } },
    "engagement_id": { "type": "string" },
    "version":       { "type": "string" },
    "last_updated":  { "type": "string", "format": "date" },
    "status":        { "type": "string", "enum": ["draft", "in_progress", "complete", "approved"] },

    "threat_model": {
      "type": "object",
      "required": ["methodology", "threats"],
      "properties": {
        "methodology": { "type": "string", "enum": ["STRIDE", "PASTA", "DREAD", "attack_tree", "custom"] },
        "scope":       { "type": "string" },
        "threats": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["id", "category", "description", "severity"],
            "properties": {
              "id":                   { "type": "string", "pattern": "^T-\\d{3}$" },
              "category":             { "type": "string", "enum": ["spoofing", "tampering", "repudiation", "information_disclosure", "denial_of_service", "elevation_of_privilege", "injection"] },
              "description":          { "type": "string" },
              "affected_components":  { "type": "array", "items": { "type": "string" } },
              "severity":             { "type": "string", "enum": ["critical", "high", "medium", "low"] },
              "likelihood":           { "type": "string", "enum": ["high", "medium", "low"] },
              "risk_score":           { "type": "integer", "minimum": 1, "maximum": 10 },
              "mitigation":           { "type": "string" },
              "residual_risk":        { "type": "string", "enum": ["high", "medium", "low", "negligible"] },
              "status":               { "type": "string", "enum": ["identified", "mitigated", "accepted", "transferred"] }
            }
          }
        }
      }
    },

    "compliance_checklist": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["framework", "requirement", "status"],
        "properties": {
          "framework":   { "type": "string" },
          "requirement": { "type": "string" },
          "status":      { "type": "string", "enum": ["compliant", "partial", "non_compliant", "not_applicable"] },
          "evidence":    { "type": "string" },
          "notes":       { "type": "string" }
        }
      }
    },

    "security_architecture": {
      "type": "object",
      "properties": {
        "authentication":         { "type": "object" },
        "authorization":          { "type": "object" },
        "network":                { "type": "object" },
        "encryption":             { "type": "object" },
        "secrets_management":     { "type": "string" },
        "logging_and_monitoring": { "type": "object" }
      }
    },

    "ai_specific_security": {
      "type": "object",
      "properties": {
        "prompt_injection_protection": { "type": "array", "items": { "type": "string" } },
        "output_filtering":            { "type": "array", "items": { "type": "string" } },
        "model_access_control":        { "type": "string" },
        "data_poisoning_prevention":   { "type": "string" },
        "hallucination_mitigation":    { "type": "string" }
      }
    },

    "findings_summary": {
      "type": "object",
      "properties": {
        "critical":   { "type": "integer", "minimum": 0 },
        "high":       { "type": "integer", "minimum": 0 },
        "medium":     { "type": "integer", "minimum": 0 },
        "low":        { "type": "integer", "minimum": 0 },
        "open_items": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["id", "severity", "finding"],
            "properties": {
              "id":             { "type": "string", "pattern": "^F-\\d{3}$" },
              "severity":       { "type": "string", "enum": ["critical", "high", "medium", "low"] },
              "finding":        { "type": "string" },
              "recommendation": { "type": "string" },
              "owner":          { "type": "string" },
              "due_date":       { "type": "string", "format": "date" }
            }
          }
        }
      }
    },

    "_metadata": { "type": "object" }
  }
}
```

---

### integration_plan.json

```json
{
  "$schema": "./schemas/integration_plan.schema.json",
  "$depends_on": ["requirements.json", "architecture.json"],
  "engagement_id": "eng-2026-001",
  "version": "1.0",
  "last_updated": "2026-03-15",
  "status": "draft",

  "api_contracts": [
    {
      "id": "API-001",
      "name": "Zendesk Ticket Webhook",
      "direction": "inbound",
      "protocol": "REST",
      "method": "POST",
      "endpoint": "/api/v1/webhooks/zendesk/ticket",
      "authentication": "HMAC signature verification",
      "request_schema": {
        "ticket_id": "string",
        "requester_id": "string",
        "subject": "string",
        "description": "string",
        "priority": "string",
        "tags": ["string"]
      },
      "response_schema": {
        "status": "string",
        "conversation_id": "string"
      },
      "rate_limit": "100 rps",
      "error_handling": "Retry with exponential backoff, dead letter queue after 3 failures",
      "sla": { "latency_p95_ms": 500, "availability_percent": 99.5 }
    },
    {
      "id": "API-002",
      "name": "AI Response to Zendesk",
      "direction": "outbound",
      "protocol": "REST",
      "method": "POST",
      "endpoint": "https://api.zendesk.com/api/v2/tickets/{id}/comments",
      "authentication": "API key (Bearer token)",
      "request_schema": {
        "ticket_id": "string",
        "body": "string",
        "public": "boolean",
        "author_id": "string"
      },
      "response_schema": {
        "comment_id": "string",
        "created_at": "string"
      },
      "rate_limit": "Zendesk rate limit: 700 rps",
      "error_handling": "Queue and retry, alert on persistent failures",
      "sla": { "latency_p95_ms": 1000, "availability_percent": 99.9 }
    }
  ],

  "data_flow_mappings": [
    {
      "id": "DFM-001",
      "name": "Ticket to Conversation",
      "source_system": "Zendesk",
      "target_system": "AI Agent",
      "source_format": "Zendesk ticket JSON",
      "target_format": "Internal conversation model",
      "field_mappings": [
        { "source": "ticket.id",          "target": "conversation.zendesk_ticket_id", "transform": "string" },
        { "source": "ticket.requester_id", "target": "conversation.customer_id",      "transform": "string" },
        { "source": "ticket.description",  "target": "message.content",               "transform": "html_to_text" },
        { "source": "ticket.priority",     "target": "conversation.priority",          "transform": "enum_map" }
      ],
      "validation_rules": [
        "ticket.id must not be null",
        "ticket.description must not exceed 10000 characters"
      ]
    }
  ],

  "migration_strategy": null,

  "legacy_bridging": [],

  "error_handling_patterns": {
    "circuit_breaker": {
      "threshold": 5,
      "timeout_seconds": 60,
      "half_open_requests": 3
    },
    "retry_policy": {
      "max_retries": 3,
      "backoff": "exponential",
      "base_delay_ms": 1000,
      "max_delay_ms": 30000
    },
    "dead_letter_queue": {
      "enabled": true,
      "retention_days": 14,
      "alerting": "SNS notification on DLQ message"
    }
  },

  "_metadata": {
    "planner": "SA Agent",
    "planning_date": "2026-03-15",
    "validation_status": "draft"
  }
}
```

**Schema: `integration_plan.schema.json`**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "integration_plan.schema.json",
  "title": "Integration Plan",
  "description": "API contracts, data flow mappings, migration strategies, and legacy bridging patterns produced by /integration-plan skill.",
  "type": "object",
  "required": ["engagement_id", "version", "status", "api_contracts"],
  "properties": {
    "$schema":       { "type": "string" },
    "$depends_on":   { "type": "array", "items": { "type": "string" } },
    "engagement_id": { "type": "string" },
    "version":       { "type": "string" },
    "last_updated":  { "type": "string", "format": "date" },
    "status":        { "type": "string", "enum": ["draft", "in_progress", "complete", "approved"] },

    "api_contracts": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "name", "direction", "protocol"],
        "properties": {
          "id":             { "type": "string", "pattern": "^API-\\d{3}$" },
          "name":           { "type": "string" },
          "direction":      { "type": "string", "enum": ["inbound", "outbound", "bidirectional"] },
          "protocol":       { "type": "string", "enum": ["REST", "GraphQL", "gRPC", "WebSocket", "AMQP", "Kafka"] },
          "method":         { "type": "string" },
          "endpoint":       { "type": "string" },
          "authentication": { "type": "string" },
          "request_schema": { "type": "object" },
          "response_schema": { "type": "object" },
          "rate_limit":     { "type": "string" },
          "error_handling": { "type": "string" },
          "sla": {
            "type": "object",
            "properties": {
              "latency_p95_ms":      { "type": "integer" },
              "availability_percent": { "type": "number" }
            }
          }
        }
      }
    },

    "data_flow_mappings": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "name", "source_system", "target_system"],
        "properties": {
          "id":            { "type": "string", "pattern": "^DFM-\\d{3}$" },
          "name":          { "type": "string" },
          "source_system": { "type": "string" },
          "target_system": { "type": "string" },
          "source_format": { "type": "string" },
          "target_format": { "type": "string" },
          "field_mappings": {
            "type": "array",
            "items": {
              "type": "object",
              "required": ["source", "target"],
              "properties": {
                "source":    { "type": "string" },
                "target":    { "type": "string" },
                "transform": { "type": "string" }
              }
            }
          },
          "validation_rules": { "type": "array", "items": { "type": "string" } }
        }
      }
    },

    "migration_strategy": {
      "type": ["object", "null"],
      "properties": {
        "approach":      { "type": "string", "enum": ["big_bang", "strangler_fig", "parallel_run", "blue_green", "phased"] },
        "source_system": { "type": "string" },
        "target_system": { "type": "string" },
        "data_migration": {
          "type": "object",
          "properties": {
            "approach":      { "type": "string" },
            "volume":        { "type": "string" },
            "downtime_plan": { "type": "string" }
          }
        },
        "rollback_plan": { "type": "string" }
      }
    },

    "legacy_bridging": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "legacy_system":  { "type": "string" },
          "bridge_pattern": { "type": "string", "enum": ["adapter", "facade", "anti_corruption_layer", "event_bridge", "api_gateway"] },
          "description":    { "type": "string" },
          "lifespan":       { "type": "string" }
        }
      }
    },

    "error_handling_patterns": {
      "type": "object",
      "properties": {
        "circuit_breaker":   { "type": "object" },
        "retry_policy":      { "type": "object" },
        "dead_letter_queue": { "type": "object" }
      }
    },

    "_metadata": { "type": "object" }
  }
}
```

---

### reviews.json

This is the cross-cutting file that `/review` writes to. It tracks quality scores and iteration history for any skill output.

```json
{
  "$schema": "./schemas/reviews.schema.json",
  "engagement_id": "eng-2026-001",
  "last_updated": "2026-03-15",

  "reviews": [
    {
      "review_id": "R-001",
      "target_file": "architecture.json",
      "target_version": "0.2",
      "review_date": "2026-03-14",
      "review_type": "quality",

      "scores": {
        "completeness":         { "score": 7, "max": 10, "notes": "Missing deployment diagram" },
        "technical_soundness":  { "score": 8, "max": 10, "notes": "Tech stack well-justified" },
        "well_architected":     { "score": 7, "max": 10, "notes": "Single-region is a reliability gap" },
        "clarity":              { "score": 9, "max": 10, "notes": "Clear component descriptions" },
        "feasibility":          { "score": 8, "max": 10, "notes": "Within team capability" },
        "overall":              { "score": 7.8, "max": 10 }
      },

      "findings": [
        {
          "id": "RF-001",
          "severity": "medium",
          "category": "completeness",
          "finding": "Deployment diagram is empty",
          "recommendation": "Add Mermaid deployment diagram showing VPC, subnets, and service placement",
          "status": "open"
        },
        {
          "id": "RF-002",
          "severity": "low",
          "category": "well_architected",
          "finding": "No DR strategy for single-region deployment",
          "recommendation": "Document DR plan even if implementation is Phase 2",
          "status": "open"
        }
      ],

      "blockers": [],

      "iteration_history": [
        {
          "iteration": 1,
          "date": "2026-03-12",
          "target_version": "0.1",
          "overall_score": 5.5,
          "key_changes_requested": ["Add component IDs", "Add data flow definitions", "Missing executive summary"]
        },
        {
          "iteration": 2,
          "date": "2026-03-14",
          "target_version": "0.2",
          "overall_score": 7.8,
          "key_changes_requested": ["Add deployment diagram", "Document DR plan"]
        }
      ]
    }
  ],

  "aggregate_stats": {
    "total_reviews": 1,
    "average_score": 7.8,
    "files_reviewed": ["architecture.json"],
    "files_not_reviewed": ["requirements.json", "estimate.json", "project_plan.json", "data_model.json", "security_review.json", "integration_plan.json"],
    "open_findings_count": 2,
    "blocker_count": 0
  }
}
```

**Schema: `reviews.schema.json`**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "reviews.schema.json",
  "title": "Reviews",
  "description": "Quality reviews, scores, findings, and iteration history tracked by /review skill. Cross-cuts all other skill outputs.",
  "type": "object",
  "required": ["engagement_id", "reviews"],
  "properties": {
    "$schema":       { "type": "string" },
    "engagement_id": { "type": "string" },
    "last_updated":  { "type": "string", "format": "date" },

    "reviews": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["review_id", "target_file", "target_version", "review_date", "review_type", "scores"],
        "properties": {
          "review_id":      { "type": "string", "pattern": "^R-\\d{3}$" },
          "target_file":    { "type": "string", "description": "Which KB file was reviewed (e.g., architecture.json)" },
          "target_version": { "type": "string", "description": "Version of the target file at time of review" },
          "review_date":    { "type": "string", "format": "date" },
          "review_type":    { "type": "string", "enum": ["quality", "security", "compliance", "completeness", "pre_proposal"] },

          "scores": {
            "type": "object",
            "required": ["overall"],
            "properties": {
              "completeness":        { "$ref": "#/$defs/score_entry" },
              "technical_soundness": { "$ref": "#/$defs/score_entry" },
              "well_architected":    { "$ref": "#/$defs/score_entry" },
              "clarity":             { "$ref": "#/$defs/score_entry" },
              "feasibility":         { "$ref": "#/$defs/score_entry" },
              "security":            { "$ref": "#/$defs/score_entry" },
              "overall":             { "$ref": "#/$defs/score_entry" }
            },
            "additionalProperties": { "$ref": "#/$defs/score_entry" }
          },

          "findings": {
            "type": "array",
            "items": {
              "type": "object",
              "required": ["id", "severity", "finding"],
              "properties": {
                "id":             { "type": "string", "pattern": "^RF-\\d{3}$" },
                "severity":       { "type": "string", "enum": ["critical", "high", "medium", "low", "info"] },
                "category":       { "type": "string" },
                "finding":        { "type": "string" },
                "recommendation": { "type": "string" },
                "status":         { "type": "string", "enum": ["open", "resolved", "wont_fix", "deferred"] }
              }
            }
          },

          "blockers": {
            "type": "array",
            "items": { "type": "string" },
            "description": "Critical issues that must be resolved before the target file can be approved"
          },

          "iteration_history": {
            "type": "array",
            "items": {
              "type": "object",
              "required": ["iteration", "date", "target_version", "overall_score"],
              "properties": {
                "iteration":             { "type": "integer", "minimum": 1 },
                "date":                  { "type": "string", "format": "date" },
                "target_version":        { "type": "string" },
                "overall_score":         { "type": "number", "minimum": 0, "maximum": 10 },
                "key_changes_requested": { "type": "array", "items": { "type": "string" } }
              }
            }
          }
        }
      }
    },

    "aggregate_stats": {
      "type": "object",
      "properties": {
        "total_reviews":        { "type": "integer", "minimum": 0 },
        "average_score":        { "type": "number", "minimum": 0, "maximum": 10 },
        "files_reviewed":       { "type": "array", "items": { "type": "string" } },
        "files_not_reviewed":   { "type": "array", "items": { "type": "string" } },
        "open_findings_count":  { "type": "integer", "minimum": 0 },
        "blocker_count":        { "type": "integer", "minimum": 0 }
      }
    }
  },

  "$defs": {
    "score_entry": {
      "type": "object",
      "required": ["score", "max"],
      "properties": {
        "score": { "type": "number", "minimum": 0 },
        "max":   { "type": "number", "minimum": 1 },
        "notes": { "type": "string" }
      }
    }
  }
}
```

---

## Cross-Skill Data Flow Map

This table shows which fields flow from upstream files into downstream skills. Skills read specific sections, not entire files.

| Downstream skill | Reads from | Specific sections needed |
|---|---|---|
| `/architecture` | requirements.json | `client_context`, `problem_statement`, `functional_requirements`, `non_functional_requirements`, `data_landscape`, `constraints` |
| `/estimate` | requirements.json | `constraints.budget_range`, `constraints.timeline_weeks`, `functional_requirements` (count + complexity) |
| `/estimate` | architecture.json | `tech_stack`, `component_design` (count + cost_driver), `well_architected_scores` |
| `/data-model` | requirements.json | `data_landscape`, `non_functional_requirements.security` |
| `/data-model` | architecture.json | `tech_stack.data_stores`, `component_design` (data-related components) |
| `/security-review` | requirements.json | `non_functional_requirements.security`, `non_functional_requirements.data_residency`, `constraints` |
| `/security-review` | architecture.json | `tech_stack.infrastructure`, `component_design`, `data_flows`, `well_architected_scores.security` |
| `/integration-plan` | requirements.json | `data_landscape.integration_points`, `non_functional_requirements.performance` |
| `/integration-plan` | architecture.json | `tech_stack`, `component_design`, `data_flows` |
| `/project-plan` | requirements.json | `constraints.timeline_weeks`, `stakeholders`, `assumptions` |
| `/project-plan` | architecture.json | `component_design` (work breakdown), `executive_summary` |
| `/project-plan` | estimate.json | `loe_breakdown`, `team_composition`, `cost_model` |
| `/proposal` | ALL files | Full read access. Assembles executive summary from all sources. |
| `/review` | ANY single file | Full read of the target file + its schema for validation. |

---

## Shared Conventions

### ID patterns

All IDs follow the pattern `PREFIX-NNN` where NNN is zero-padded:

| Entity | Pattern | Example |
|--------|---------|---------|
| Engagement | `eng-YYYY-NNN` | `eng-2026-001` |
| Success Criteria | `SC-NNN` | `SC-001` |
| Functional Requirement | `FR-NNN` | `FR-001` |
| Component | `C-NNN` | `C-001` |
| Data Flow | `DF-NNN` | `DF-001` |
| Entity | `E-NNN` | `E-001` |
| Threat | `T-NNN` | `T-001` |
| Security Finding | `F-NNN` | `F-001` |
| API Contract | `API-NNN` | `API-001` |
| Data Flow Mapping | `DFM-NNN` | `DFM-001` |
| Review | `R-NNN` | `R-001` |
| Review Finding | `RF-NNN` | `RF-001` |
| Phase | `P-NNN` | `P-001` |
| Milestone | `M-NNN` | `M-001` |

### Version strings

All domain files use `MAJOR.MINOR` versioning (e.g., `"1.2"`). Major increments on structural changes; minor increments on content updates. The engagement envelope tracks which version of each file is current.

### Status enum

Every domain file uses the same status progression:

```
not_started -> draft -> in_progress -> complete -> approved
```

### Common `_metadata` fields

Every domain file includes a `_metadata` object with at minimum:

```json
{
  "_metadata": {
    "author": "SA Agent | Human",
    "created_date": "YYYY-MM-DD",
    "validation_status": "draft | reviewed | approved"
  }
}
```

### `$depends_on` convention

Each file declares its upstream dependencies as a `$depends_on` array of filenames. This is informational (not enforced by JSON Schema) but used by skills to know what context to load.

---

## Migration Path from Current KB

| Current file | Maps to | Migration action |
|---|---|---|
| `system_config.json` | `system_config.json` (unchanged) | No change. READ-ONLY stays. Remove `technical_references` and `validation_framework` sections to separate reference files. |
| `user_requirements.json` | `requirements.json` | Restructure: flatten `customer`/`use_case`/`business`/`technical` into `client_context`/`problem_statement`/`functional_requirements`. Add `ai_suitability_assessment`. |
| `design_decisions.json` | `architecture.json` + `estimate.json` + `project_plan.json` | Split: tech_stack + architecture_design -> `architecture.json`. team_composition + estimates + costs -> `estimate.json`. project_plan -> `project_plan.json`. |
| (new) | `engagement.json` | Create: engagement envelope with lifecycle tracking. |
| (new) | `data_model.json` | Create: currently implicit in architecture, now explicit. |
| (new) | `security_review.json` | Create: currently buried in `compliance_and_security` section of design_decisions. |
| (new) | `integration_plan.json` | Create: currently implicit in architecture `integration_approach`. |
| (new) | `reviews.json` | Create: no review tracking existed in old KB. |

---

## `/proposal` Skill Output

The `/proposal` skill does NOT write to the knowledge base. It reads all KB files and produces output documents in `outputs/`:

```
outputs/
└── eng-2026-001/
    ├── discovery_proposal.md
    ├── implementation_proposal.md
    └── executive_summary.md
```

This keeps the KB as the source of truth for structured data, while proposals are the human-readable presentation layer.

---

## Summary of All Schema Files Needed

```
knowledge_base/schemas/
├── engagement.schema.json           # NEW
├── requirements.schema.json         # REWRITE (from user_requirements.schema.json)
├── architecture.schema.json         # REWRITE (from design_decisions.schema.json, architecture portion)
├── estimate.schema.json             # NEW (from design_decisions.schema.json, cost/team portion)
├── project_plan.schema.json         # NEW (from design_decisions.schema.json, plan portion)
├── data_model.schema.json           # NEW
├── security_review.schema.json      # NEW
├── integration_plan.schema.json     # NEW
├── reviews.schema.json              # NEW
├── system_config.schema.json        # KEEP (minor updates to remove bloat sections)
└── .repo-metadata.schema.json       # KEEP
```

Total: 11 schema files (up from 4). Each is focused, independently valid, and under 200 lines.
