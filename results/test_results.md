# Implementation Test Results

## 1. AI Application Tests

- **Anomaly detection:** Executed on the selected Server Machine Dataset (SMD).
- **Explainable analysis:** Generated metric-level deviations from training-data statistics.
- **Diagnosis:** Produced possible causes and suggested corrective actions.
- **Recovery simulation:** Demonstrated a simulated recovery-status change.
- **Verification simulation:** Returned the recorded simulated status.

## 2. AWS Implementation Tests

- **Amazon EC2:** The `Hospital-SelfHealing-Server` instance was launched.
- **Amazon CloudWatch:** The `Hospital-High-CPU-Alarm` CPU-utilisation alarm was configured with a threshold above 80% over a five-minute evaluation period.
- **AWS Lambda:** The `HospitalSelfHealingRecovery` function processed test events.
- **CloudWatch-to-Lambda invocation:** Invocation evidence and execution logs were recorded.
- **IAM permissions:** An organisational policy blocked the required permission change for live EC2 recovery.
- **Amazon SNS:** The email subscription remained pending confirmation; successful delivery was not verified.
- **Amazon S3:** The project bucket was created, but no project data was present during the recorded inspection.

## 3. Overall Result

The AI pipeline, simulated recovery workflow, and selected AWS monitoring and event-processing components were demonstrated. Live EC2 recovery and complete end-to-end autonomous self-healing remain unverified.

These results document the current proof of concept and should not be interpreted as evidence of production readiness.
