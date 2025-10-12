# Deploy Streamlit App to AWS ECS

**Agent:** AWS Infrastructure Agent  
**Category:** AWS Infrastructure  
**Complexity:** Advanced  
**Duration:** 3-5 hours

---

## Purpose

Deploy Streamlit application to AWS ECS using AWS CDK (Python) with proper networking, monitoring, and scaling configuration.

---

## Instructions

Create ECS deployment with:

1. **VPC and networking** (from Security Agent)
2. **ECS cluster and task definition**
3. **Fargate service**
4. **Application Load Balancer**
5. **CloudWatch monitoring**
6. **Auto-scaling policies**

---

## Expected Output

```python
# infra/app.py

#!/usr/bin/env python3

from aws_cdk import App
from stacks.ecs_stack import StreamlitECSStack

app = App()

StreamlitECSStack(
    app,
    "StreamlitAIApp",
    env={
        "account": "123456789012",
        "region": "us-east-1"
    }
)

app.synth()

# infra/stacks/ecs_stack.py

from aws_cdk import (
    Stack,
    Duration,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    aws_logs as logs,
    aws_applicationautoscaling as appscaling
)
from constructs import Construct

class StreamlitECSStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)
        
        # VPC (from Security Agent)
        vpc = ec2.Vpc(
            self, "AppVPC",
            max_azs=2,
            nat_gateways=1
        )
        
        # ECS Cluster
        cluster = ecs.Cluster(
            self, "StreamlitCluster",
            vpc=vpc,
            container_insights=True
        )
        
        # Fargate Service with ALB
        fargate_service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self, "StreamlitService",
            cluster=cluster,
            cpu=1024,
            memory_limit_mib=2048,
            desired_count=1,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_asset("../app"),
                container_port=8501,
                environment={
                    "STREAMLIT_SERVER_PORT": "8501",
                    "STREAMLIT_SERVER_ADDRESS": "0.0.0.0"
                },
                log_driver=ecs.LogDrivers.aws_logs(
                    stream_prefix="streamlit",
                    log_retention=logs.RetentionDays.ONE_WEEK
                )
            ),
            public_load_balancer=True
        )
        
        # Auto-scaling
        scaling = fargate_service.service.auto_scale_task_count(
            min_capacity=1,
            max_capacity=10
        )
        
        scaling.scale_on_cpu_utilization(
            "CpuScaling",
            target_utilization_percent=70,
            scale_in_cooldown=Duration.seconds(60),
            scale_out_cooldown=Duration.seconds(60)
        )
        
        # Health check
        fargate_service.target_group.configure_health_check(
            path="/",
            interval=Duration.seconds(30),
            timeout=Duration.seconds(5)
        )

# Deploy
# cd infra
# cdk deploy
```

---

## Success Criteria

✅ ECS infrastructure created  
✅ Streamlit app accessible via ALB  
✅ Auto-scaling configured  
✅ Monitoring operational  
✅ Health checks passing

---

## Deployment Commands

```bash
# Install CDK
npm install -g aws-cdk
pip install -r infra/requirements.txt

# Bootstrap CDK (first time only)
cdk bootstrap aws://ACCOUNT/REGION

# Deploy
cd infra
cdk deploy

# Destroy
cdk destroy
```

---

## Integration

**Requires:**
- AWS Security Agent (VPC, security groups)
- Streamlit UI Agent (application code)

**Provides:** Production ECS deployment
