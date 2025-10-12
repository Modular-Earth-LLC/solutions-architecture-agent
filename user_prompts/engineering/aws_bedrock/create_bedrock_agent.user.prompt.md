# Create AWS Bedrock Agent

**Agent:** AWS Bedrock Agent Engineering Agent  
**Category:** AWS Bedrock  
**Complexity:** Advanced  
**Duration:** 3-4 hours

---

## Purpose

Create a production-ready AWS Bedrock Agent with action groups, knowledge base integration, and guardrails.

---

## Instructions

Create Bedrock Agent with:

1. **Agent creation** (boto3)
2. **Action group configuration** (Lambda-backed)
3. **Knowledge base association**
4. **Guardrails configuration**
5. **Testing and validation**

---

## Expected Output

```python
# src/bedrock/create_agent.py

import boto3
import json

def create_agent_with_config(
    agent_name: str,
    instruction: str,
    action_groups: list[dict],
    knowledge_base_id: str,
    guardrail_id: str
):
    """
    Create fully configured Bedrock Agent
    
    Args:
        agent_name: Name for the agent
        instruction: System instruction for agent behavior
        action_groups: List of action group configs
        knowledge_base_id: ID of knowledge base to associate
        guardrail_id: ID of guardrail to apply
    
    Returns:
        dict: Agent configuration with IDs
    """
    client = boto3.client('bedrock-agent')
    
    # Step 1: Create agent
    agent_response = client.create_agent(
        agentName=agent_name,
        foundationModel="anthropic.claude-3-5-sonnet-20241022-v2:0",
        instruction=instruction,
        agentResourceRoleArn="arn:aws:iam::ACCOUNT:role/BedrockAgentRole",
        idleSessionTTLInSeconds=600
    )
    
    agent_id = agent_response['agent']['agentId']
    
    # Step 2: Add action groups
    for action_group in action_groups:
        client.create_agent_action_group(
            agentId=agent_id,
            agentVersion='DRAFT',
            actionGroupName=action_group['name'],
            actionGroupExecutor={'lambda': action_group['lambda_arn']},
            apiSchema={'payload': json.dumps(action_group['schema'])}
        )
    
    # Step 3: Associate knowledge base
    client.associate_agent_knowledge_base(
        agentId=agent_id,
        agentVersion='DRAFT',
        knowledgeBaseId=knowledge_base_id,
        description="Knowledge base for agent",
        knowledgeBaseState='ENABLED'
    )
    
    # Step 4: Add guardrails
    client.update_agent(
        agentId=agent_id,
        agentName=agent_name,
        guardrailConfiguration={
            'guardrailIdentifier': guardrail_id,
            'guardrailVersion': 'DRAFT'
        }
    )
    
    # Step 5: Prepare agent
    client.prepare_agent(agentId=agent_id)
    
    # Step 6: Create alias
    alias_response = client.create_agent_alias(
        agentId=agent_id,
        agentAliasName="production"
    )
    
    return {
        "agent_id": agent_id,
        "alias_id": alias_response['agentAlias']['agentAliasId'],
        "status": "ready"
    }

# Example usage
if __name__ == "__main__":
    config = create_agent_with_config(
        agent_name="CustomerSupportAgent",
        instruction="You are a helpful customer support assistant.",
        action_groups=[
            {
                'name': 'SearchKnowledgeBase',
                'lambda_arn': 'arn:aws:lambda:us-east-1:ACCOUNT:function:SearchKB',
                'schema': {...}  # OpenAPI schema
            }
        ],
        knowledge_base_id="KB123",
        guardrail_id="GR123"
    )
    
    print(f"Agent created: {config['agent_id']}")
```

---

## Success Criteria

✅ Bedrock agent created successfully  
✅ Action groups functional  
✅ Knowledge base integrated  
✅ Guardrails active  
✅ Agent alias ready for production

---

## Integration

**Requires:**
- AWS Security Agent (IAM roles)
- Knowledge Engineering Agent (knowledge base)

**Provides:** Production-ready Bedrock Agent
