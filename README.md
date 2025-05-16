# Scalable Cloud Architecture on AWS

This project demonstrates how to design and implement a scalable cloud-based architecture on AWS using a combination of Terraform, CloudFormation, Boto3 scripting, and various AWS services. The goal was to deploy a web application with integrated storage, compute, database, and automation components while following Infrastructure-as-Code (IaC) principles.

---

## Project Structure

```
terraform/             → Terraform scripts to create VPC, subnets, internet gateway, route tables, and security groups
cloudformation/        → CloudFormation templates to launch EC2 with ALB, RDS, Lambda functions, and Auto Scaling Group
step2c_scripts/        → Python scripts using Boto3 to interact with AWS (EC2, S3, Lambda)
architecture.png       → AWS Architecture diagram (visual summary of deployed components)
README.md              → Project documentation and setup steps
```

---

## Deployment Instructions

### A. Infrastructure Deployment

#### Terraform (Networking Setup)

```bash
cd terraform
terraform init
terraform plan
terraform apply -auto-approve
```

Creates VPC, public/private subnets, route tables, internet gateway, and security groups.

#### CloudFormation (Resource Deployment)

Upload each template in the `cloudformation/` folder to create:

* EC2 instance with Apache + Load Balancer
* RDS MySQL Database
* Lambda function to log S3 uploads
* Auto Scaling Group with Launch Template

### B. Web Application

* A simple web page is served from the EC2 instance.
* Connected to an RDS backend.
* Auto Scaling Group automatically adds new instances.
* ALB distributes traffic across all autoscaled EC2s.

---

## AWS Lambda (Logging S3 Uploads)

A Lambda function was created to log every S3 file upload to CloudWatch Logs. It is triggered by an S3 event. A sample payload was also tested using Boto3 for manual invocation.

---

## Step 2C – AWS Interaction with Python & CLI

Python scripts written using Boto3 (in `step2c_scripts/`) demonstrate programmatic access:

* **create\_s3\_upload.py**
  Creates an S3 bucket and uploads a test file.

* **get\_metadata.py**
  Retrieves instance metadata from inside an EC2 instance.

* **list\_ec2.py**
  Lists all running EC2 instances using Boto3.

* **invoke\_lambda.py**
  Manually triggers the Lambda function with a simulated S3 event.

AWS CLI commands such as `aws ec2 describe-instances`, `aws s3 ls`, and `aws lambda list-functions` were also used to verify deployments.

---

## Technologies Used

* **AWS Services**: EC2, S3, Lambda, RDS, ALB, Auto Scaling, CloudWatch
* **Infrastructure-as-Code**: Terraform & CloudFormation
* **Automation & Interaction**: Python (Boto3) and AWS CLI

---

### Components and Flow

* **VPC**: A custom Virtual Private Cloud containing both public and private subnets.
* **Public Subnets**: Host EC2 instances managed by Auto Scaling Group and ALB.
* **Private Subnets**: Host the RDS MySQL database.
* **ALB**: Distributes incoming HTTP traffic across EC2 instances.
* **Auto Scaling Group**: Dynamically manages EC2 instance count based on traffic.
* **EC2**: Apache web servers serving HTML content and connecting to RDS.
* **S3**: Triggers Lambda function on file upload.
* **Lambda**: Logs uploads to CloudWatch.
* **Security Groups**: Control inbound/outbound access for ALB, EC2, RDS.

### Workflow Summary

1. User sends a request to ALB DNS.
2. ALB (in public subnet via IGW) forwards request to EC2.
3. EC2 responds or interacts with RDS in private subnet.
4. Files uploaded to S3 trigger Lambda.
5. Lambda logs to CloudWatch.
6. Auto Scaling ensures elasticity.

---


## Author & Course Info

**Name**: Praveesha Gongura
**Course**: Cloud Computing
**Semester**: Spring 2025
