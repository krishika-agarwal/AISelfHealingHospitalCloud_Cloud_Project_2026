# AWS Configuration and Implementation

## 1. Project Overview

This project demonstrates cloud monitoring and a preliminary self-healing workflow for hospital information systems using AWS services.

## 2. AWS Resources

### Amazon EC2
An EC2 instance named `Hospital-SelfHealing-Server` was created to represent the hospital application server.

### Amazon CloudWatch
A CloudWatch alarm named `Hospital-High-CPU-Alarm` was configured to monitor the EC2 instance's CPU utilization. The alarm threshold was set to trigger when average CPU utilization exceeded 80% over a five-minute evaluation period.

### AWS Lambda
A Lambda function named `HospitalSelfHealingRecovery` was created to process high-risk events and return a recovery-action status. The function was invoked through CloudWatch monitoring during testing.

### Amazon SNS
An SNS topic named `Hospital-CPU-Alerts` was configured for CPU alert notifications. Email subscription confirmation remained pending during the recorded testing.

### Amazon S3
An S3 bucket was created for potential project evidence and storage. The bucket was empty at the time of verification.

## 3. Monitoring Workflow

1. CloudWatch monitors EC2 CPU utilization.
2. The configured alarm evaluates CPU utilization against its threshold.
3. When the alarm enters the ALARM state, the configured Lambda action can be invoked.
4. Lambda processes the event and records the requested recovery action.

## 4. Implementation Limitations

The CloudWatch-to-Lambda invocation was demonstrated. However, successful automatic recovery of the EC2 instance was not verified. AWS organizational permission restrictions prevented the required IAM policy changes. SNS email delivery was also not confirmed.

The AI anomaly-detection model and dashboard are project components; their end-to-end integration with AWS monitoring should not be assumed.

## 5. Evidence

Screenshots of the AWS configuration and testing results are maintained in the repository's `results/screenshots/` directory.
