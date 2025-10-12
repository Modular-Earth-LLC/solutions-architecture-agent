# Create Complete AWS CDK Infrastructure

**Agent:** AWS Infrastructure Agent  
**Category:** AWS Infrastructure  
**Complexity:** Advanced  
**Duration:** 4-6 hours

---

## Purpose

Build complete AWS infrastructure using CDK (Python) for deploying AI applications with ECS, RDS/DocumentDB (if needed), S3, and CloudWatch.

---

## Instructions

Create CDK project with:

1. **Project initialization**
2. **Stack structure** (compute, storage, monitoring)
3. **ECS service for Streamlit**
4. **S3 for document storage**
5. **CloudWatch dashboards**
6. **Parameter store for configuration**

---

## Expected Output

```python
# infra/app.py
#!/usr/bin/env python3

from aws_cdk import App, Environment
from stacks.compute_stack import ComputeStack
from stacks.storage_stack import StorageStack
from stacks.monitoring_stack import MonitoringStack

app = App()

env = Environment(account="123456789012", region="us-east-1")

# Storage first
storage = StorageStack(app, "AIAppStorage", env=env)

# Compute depends on storage
compute = ComputeStack(
    app, "AIAppCompute",
    bucket=storage.document_bucket,
    env=env
)

# Monitoring last
monitoring = MonitoringStack(
    app, "AIAppMonitoring",
    cluster=compute.cluster,
    service=compute.service,
    env=env
)

app.synth()

# infra/stacks/compute_stack.py
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns
)

class ComputeStack(Stack):
    def __init__(self, scope, id, bucket, **kwargs):
        super().__init__(scope, id, **kwargs)
        
        # VPC
        self.vpc = ec2.Vpc(self, "VPC", max_azs=2)
        
        # ECS Cluster
        self.cluster = ecs.Cluster(
            self, "Cluster",
            vpc=self.vpc,
            container_insights=True
        )
        
        # Fargate Service
        self.service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self, "Service",
            cluster=self.cluster,
            cpu=1024,
            memory_limit_mib=2048,
            task_image_options={
                "image": ecs.ContainerImage.from_asset("../app"),
                "container_port": 8501,
                "environment": {
                    "S3_BUCKET": bucket.bucket_name
                }
            }
        )
        
        # Grant S3 access
        bucket.grant_read_write(self.service.task_definition.task_role)

# infra/stacks/storage_stack.py
from aws_cdk import Stack, RemovalPolicy, aws_s3 as s3

class StorageStack(Stack):
    def __init__(self, scope, id, **kwargs):
        super().__init__(scope, id, **kwargs)
        
        self.document_bucket = s3.Bucket(
            self, "Documents",
            versioned=True,
            encryption=s3.BucketEncryption.S3_MANAGED,
            removal_policy=RemovalPolicy.RETAIN
        )
```

---

## Success Criteria

✅ CDK project structured properly  
✅ All stacks deploy successfully  
✅ Resources properly connected  
✅ CloudWatch monitoring operational  
✅ Infrastructure as code documented

---

## Deploy Commands

```bash
cd infra
cdk bootstrap  # First time only
cdk synth      # Generate CloudFormation
cdk deploy --all  # Deploy all stacks
```
