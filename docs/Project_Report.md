# Project Report

## Project Title

AI-Driven Self-Healing Cloud Infrastructure for Hospital Information Systems using AIOps and Explainable AI

---

## Team Members

- Krishika Agarwal (24BIT0302)
- Khushi Yadav (24BIT0287)

---

## Abstract

Hospital Information Systems (HIS) are increasingly being deployed on cloud infrastructure to support real-time patient data exchange, scalability, and continuous availability. However, this shift introduces significant reliability challenges, as infrastructure failures, performance anomalies, and security incidents can directly disrupt critical healthcare operations where downtime may affect essential services. Existing research addresses these challenges individually rather than as an integrated solution. Studies on anomaly detection often lack root-cause explanations, while Explainable AI (XAI) techniques are rarely validated for cloud infrastructure environments, and self-healing frameworks frequently stop at diagnosis without automated recovery or healthcare-specific evaluation. Similarly, cloud-based healthcare architectures emphasize interoperability and data exchange while providing limited attention to intelligent infrastructure monitoring and operational resilience. Consequently, there is limited research on unified frameworks that integrate anomaly detection, explanation, diagnosis, and automated remediation within a single closed-loop architecture tailored for hospital cloud environments.
This project proposes an AI-Driven Self-Healing Cloud Infrastructure for Hospital Information Systems using AIOps and Explainable AI. The proposed framework follows a continuous Monitor → Detect → Explain → Diagnose → Recover → Verify workflow, in which infrastructure metrics and logs are continuously analyzed to identify abnormal system behaviour. Explainable AI techniques generate interpretable insights that support root-cause analysis, after which a policy-based decision engine determines whether an automated recovery action should be initiated or the incident should be escalated for human intervention. The proposed architecture utilizes AWS services including Application Load Balancer (ALB), Amazon EC2 (Auto Scaling), Amazon RDS, Amazon S3, Amazon CloudWatch, Amazon EventBridge, AWS Lambda, Amazon SNS, and AWS IAM to provide scalable hosting, continuous monitoring, secure access control, event-driven remediation, and administrator notifications. The proposed framework aims to support reliable, transparent, and efficient management of hospital cloud infrastructure by reducing manual intervention through controlled and explainable automation.


---

## Problem Statement

Traditional cloud monitoring systems mainly generate alerts after failures occur, requiring manual intervention from administrators. This increases system downtime and delays recovery. There is a need for an intelligent cloud infrastructure capable of predicting failures, identifying their causes, and automatically recovering affected services while providing explainable decisions.

---

## Objectives

Refer to [Objectives.md](Objectives.md)

---

## Literature Survey

Refer to [Literature_Survey.md](Literature_Survey.md)

---

## Research Gap

Refer to [Research_Gap.md](Research_Gap.md)

---

## Novelty

Refer to [Novelty.md](Novelty.md)

---

## Proposed Methodology

The detailed implementation methodology will be developed during Phase II of the project. The proposed system will follow an AI-driven closed-loop workflow for cloud monitoring, anomaly detection, explainable root-cause analysis, automated recovery, and verification using AWS cloud services.

---

## Technology Stack

- Amazon Web Services (AWS)
- Amazon EC2
- Amazon RDS
- Amazon CloudWatch
- Amazon EventBridge
- AWS Lambda
- Amazon SNS
- Amazon S3
- AWS IAM
- Python
- Flask
- Machine Learning
- Explainable AI (XAI)
- Git
- GitHub

---

## Repository Structure

```
architecture/
dataset/
docs/
presentation/
results/
src/
```

---

## Project Status

Phase I Completed

Current work includes:

- Literature Survey
- Research Gap Analysis
- Novelty Identification
- AWS Cloud Architecture Design
- System Architecture Design
- Project Planning

---

## Future Work

The next phase of the project will focus on implementing the proposed AWS cloud infrastructure, developing the AIOps-based anomaly detection model, integrating Explainable AI for root-cause analysis, implementing automated self-healing mechanisms, and evaluating the framework using cloud monitoring datasets and performance metrics.