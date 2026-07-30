# Novelty

The proposed project focuses on integrating AI-based anomaly detection, Explainable AI (XAI), root-cause analysis, and automated remediation into a unified AIOps framework for AWS-hosted Hospital Information System (HIS) infrastructure.

The reviewed literature shows that these capabilities are generally addressed separately, with studies focusing on anomaly detection, diagnosis, explainability, self-healing, or healthcare cloud architecture individually.

The proposed framework brings these stages together through a closed-loop workflow:

> **Monitor → Detect → Explain → Diagnose → Recover → Verify**

## New Feature

A unified detect–explain–heal workflow is proposed where an infrastructure anomaly is not only detected but also associated with an explanation and probable root cause before a suitable recovery action is considered. A verification stage further checks whether normal system behaviour has been restored after remediation.

## Better Algorithm

The proposed approach combines anomaly detection with an XAI layer and root-cause information. Instead of producing only an anomaly alert or score, the framework is intended to identify the infrastructure metrics contributing to abnormal behaviour, providing additional information for diagnosis and remediation decisions.

## Better Architecture

A modular closed-loop architecture connects monitoring, AI-based detection, explanation, diagnosis, remediation, and recovery verification. This reduces the separation between detection and recovery observed across several existing approaches.

## Better AWS Integration

AWS is used as part of the complete AIOps workflow rather than only for application hosting.

- Amazon CloudWatch for infrastructure monitoring
- Amazon S3 for monitoring data storage
- AWS Lambda for event-driven processing and remediation
- Amazon SNS for administrator notifications

## Better Security

The architecture considers the sensitivity of healthcare environments through separation of infrastructure telemetry from patient information wherever possible, along with least-privilege IAM access, encryption, logging, auditing, and restricted permissions for automated remediation.

## Better Automation

For selected and authorised infrastructure faults, the framework can connect anomaly detection and explanation with controlled automated recovery, followed by verification of the system state and administrator notification. This reduces the need for manual intervention at every stage.

## Better Accuracy

The anomaly-detection component will be evaluated using accuracy, precision, recall, F1-score, and false-positive rate. The aim is reliable detection while also providing explainability and remediation capabilities.

## Better Scalability

The framework is designed using modular and event-driven AWS components so that monitoring, AI analysis, explanation, and remediation can be scaled independently according to workload requirements.