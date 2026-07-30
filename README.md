# # AI-Driven Self-Healing Cloud Infrastructure for Hospital Information Systems using AIOps and Explainable AI

---

## Team Members

- Krishika Agarwal (24BIT0302)
- Khushi Yadav (24BIT0287)

---

## Problem Statement

Traditional cloud monitoring systems mainly generate alerts after failures occur, requiring manual intervention from administrators. This increases system downtime and delays recovery. There is a need for an intelligent cloud infrastructure capable of predicting failures, identifying their causes, and automatically recovering affected services while providing explainable decisions.

---

## Objectives

- Design an AI-driven self-healing cloud architecture for Hospital Information Systems.
- Monitor cloud infrastructure using AWS monitoring services.
- Detect anomalies using AIOps techniques.
- Explain anomalies and recovery decisions using Explainable AI (XAI).
- Automatically execute recovery actions using AWS services.
- Improve system availability, reliability, and fault tolerance.

---

## Proposed Architecture

The proposed solution consists of:

- Hospital Information System
- AWS Cloud Infrastructure
- Cloud Monitoring Layer
- AIOps Engine
- Anomaly Detection
- Explainable AI Module
- Root Cause Analysis
- Decision Engine
- Automated Self-Healing
- Recovery Verification
- Administrator Dashboard
- Audit Logging System

---

## Technology Stack

### Cloud Platform
- Amazon Web Services (AWS)

### AWS Services
- Amazon EC2
- Amazon RDS
- Amazon S3
- Amazon CloudWatch
- Amazon EventBridge
- AWS Lambda
- Amazon SNS
- AWS IAM

### Artificial Intelligence & Machine Learning
- AIOps
- Explainable AI (XAI)
- Machine Learning

### Programming Languages
- Python
- JavaScript

### Frameworks
- Flask

### Development Tools
- Git
- GitHub
- Visual Studio Code
- draw.io

---

## Dataset

The proposed system uses the **Server Machine Dataset (SMD)** as the primary dataset for developing and evaluating the anomaly detection component. Since no publicly available dataset exists for real hospital cloud infrastructure telemetry, SMD serves as a realistic proxy for monitoring cloud-based Hospital Information Systems.

| Field | Details |
|--------|---------|
| **Dataset Name** | Server Machine Dataset (SMD) |
| **Source** | Su et al. (2019), NetManAIOps Lab, released with the KDD 2019 paper *"Robust Anomaly Detection for Multivariate Time Series through Stochastic Recurrent Neural Network (OmniAnomaly)."* |
| **Repository** | https://github.com/NetManAIOps/OmniAnomaly |
| **Monitoring Duration** | 5 weeks of continuous monitoring data collected from 28 server machines |
| **Number of Records** | Approximately 708,000 timestamps sampled at 1-minute intervals, with separate training and testing datasets |
| **Number of Features** | 38 monitoring metrics per machine, including CPU utilization, memory usage, network traffic, and disk I/O |
| **Data Type** | Multivariate time-series data (CSV format) with binary anomaly labels and dimension-level interpretation labels |
| **License** | Open-source dataset released for research and academic purposes |

### Purpose of Using the Dataset

The Server Machine Dataset is used as a representative cloud infrastructure monitoring dataset to train, validate, and evaluate the proposed AIOps-based anomaly detection framework. Its multivariate monitoring metrics closely resemble infrastructure telemetry collected from cloud-hosted applications. Furthermore, the provided interpretation labels enable validation of the Explainable AI (XAI) module by comparing generated explanations with the actual metrics responsible for detected anomalies.

### Preprocessing

Before model training, the following preprocessing steps will be performed:

- Normalize the 38 monitoring metrics for each server machine.
- Convert the time-series into fixed-length input windows.
- Align anomaly interpretation labels with the corresponding anomaly windows.
- Use the predefined training and testing split provided with the dataset.