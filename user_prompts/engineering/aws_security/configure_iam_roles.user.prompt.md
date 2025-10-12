# Configure IAM Roles for Bedrock Agents

**Agent:** AWS Security & Networking Agent  
**Category:** AWS Security  
**Complexity:** Advanced  
**Duration:** 2-3 hours

---

## Purpose

Create IAM roles and policies following least-privilege principles for AWS Bedrock Agents and related services.

---

## Instructions

Create IAM configuration with:

1. **Bedrock Agent execution role**
2. **Lambda execution role** (for action groups)
3. **Knowledge base access role**
4. **Least-privilege policies**
5. **Trust relationships**

---

## Expected Output

```python
# src/iam/bedrock_roles.py

import boto3
import json

def create_bedrock_agent_role(role_name: str = "BedrockAgentRole"):
    """Create IAM role for Bedrock Agent"""
    iam = boto3.client('iam')
    
    # Trust policy
    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": {"Service": "bedrock.amazonaws.com"},
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "ACCOUNT_ID"
                }
            }
        }]
    }
    
    # Create role
    role = iam.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(trust_policy),
        Description="Execution role for Bedrock Agent"
    )
    
    # Least-privilege policy
    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "bedrock:InvokeModel",
                    "bedrock:InvokeModelWithResponseStream"
                ],
                "Resource": "arn:aws:bedrock:*::foundation-model/anthropic.claude-*"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "bedrock:Retrieve",
                    "bedrock:RetrieveAndGenerate"
                ],
                "Resource": "arn:aws:bedrock:*:ACCOUNT:knowledge-base/*"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "lambda:InvokeFunction"
                ],
                "Resource": "arn:aws:lambda:*:ACCOUNT:function:*"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents"
                ],
                "Resource": "arn:aws:logs:*:ACCOUNT:log-group:/aws/bedrock/*"
            }
        ]
    }
    
    # Attach inline policy
    iam.put_role_policy(
        RoleName=role_name,
        PolicyName="BedrockAgentPolicy",
        PolicyDocument=json.dumps(policy)
    )
    
    return role['Role']['Arn']

# Usage
if __name__ == "__main__":
    role_arn = create_bedrock_agent_role()
    print(f"Role created: {role_arn}")
```

---

## Success Criteria

✅ IAM roles follow least-privilege  
✅ Trust policies properly scoped  
✅ All required permissions included  
✅ No excessive permissions granted  
✅ Roles ready for Bedrock Agent use

---

## Security Checklist

- [ ] Scoped to specific account
- [ ] Limited to required actions only
- [ ] Resource ARNs specific (not *)
- [ ] CloudWatch logging enabled
- [ ] Documented for audit
