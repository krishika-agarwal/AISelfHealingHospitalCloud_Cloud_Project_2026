# AI-Driven Self-Healing Cloud Infrastructure for Hospital Information Systems using AIOps and Explainable AI

## Team Members

- **Krishika Agarwal** (24BIT0302)
- **Khushi Yadav** (24BIT0287)

## 1. Project Overview

This project demonstrates an AI-driven cloud monitoring and self-healing workflow for infrastructure supporting Hospital Information Systems. It combines machine-learning-based anomaly detection, metric-based explanations, diagnostic recommendations, recovery workflow simulation, and AWS monitoring integration.

The workflow is:

**Monitor → Detect → Explain → Diagnose → Recover → Verify**

The project uses the Server Machine Dataset (SMD) as a proxy for infrastructure telemetry. It does not use live hospital patient data.

## 2. Problem Statement

Traditional infrastructure monitoring can generate alerts without explaining the underlying issue or guiding administrators through recovery. This project explores how anomaly detection, explainable analysis, and cloud monitoring services can support faster investigation and more structured incident response.

## 3. Objectives

- Detect unusual patterns in server monitoring data.
- Explain detected anomalies using deviations in individual metrics.
- Generate diagnostic and recovery recommendations.
- Demonstrate a recovery and verification workflow.
- Integrate AWS CloudWatch alarms with an AWS Lambda function.
- Present results through a web-based dashboard.

## 4. System Architecture

The system contains the following components:

1. **Dataset and ML Model:** Processes the SMD test data using a trained Isolation Forest model.
2. **Anomaly Detection API:** Provides prediction results through Flask.
3. **Explainability Module:** Identifies metrics with significant deviations from training statistics.
4. **Diagnosis Module:** Generates a heuristic recommendation for investigating the anomaly.
5. **Recovery Module:** Demonstrates a simulated recovery state transition.
6. **Verification Module:** Checks the resulting simulated state.
7. **Web Dashboard:** Displays prediction, explanation, diagnosis, recovery, and verification results.
8. **AWS Monitoring Integration:** CloudWatch monitors EC2 CPU utilization and can invoke Lambda when the configured alarm changes state.

## 5. Technology Stack

- **Cloud:** Amazon Web Services (AWS)
- **Monitoring:** Amazon CloudWatch
- **Serverless processing:** AWS Lambda
- **Notifications:** Amazon SNS (subscription confirmation may be required)
- **Compute:** Amazon EC2
- **Backend:** Python and Flask
- **Machine learning:** Isolation Forest, scikit-learn, NumPy, pandas, joblib
- **Frontend:** HTML, CSS, JavaScript
- **Version control:** Git and GitHub
- **Development environment:** Visual Studio Code

## 6. Dataset

The project uses the **Server Machine Dataset (SMD)** associated with the OmniAnomaly research project.

- **Source:** [NetManAIOps OmniAnomaly repository](https://github.com/NetManAIOps/OmniAnomaly)
- **Data type:** Multivariate server time-series measurements
- **Purpose:** Demonstration and evaluation of infrastructure anomaly detection
- **Limitation:** The dataset is not hospital-specific and does not contain real patient information.

The current backend uses a static test split containing **28,479 data points**. Results are calculated from this recorded dataset and should not be interpreted as live hospital infrastructure monitoring.

## 7. Implemented Features

### Anomaly Detection

The trained Isolation Forest model identifies unusual observations in the server metrics. The backend provides dataset-level detection statistics through the `/predict` endpoint.

### Explainability

The `/explain` endpoint reports metric deviations, including z-scores relative to training statistics. These deviations help identify which metrics may have contributed to an anomaly. They are indicators for investigation, not proof of a confirmed root cause.

### Diagnosis

The `/diagnose` endpoint produces a heuristic diagnostic recommendation based on the available anomaly information.

### Recovery Simulation

The `/recover` endpoint demonstrates a simulated transition from an unhealthy state to a healthy state. It does not reboot, restart, or otherwise repair a real server.

### Verification

The `/verify` endpoint checks the resulting simulated state. It does not independently verify the health of a live hospital service.

### AWS Cloud Integration

An Amazon CloudWatch alarm named `Hospital-High-CPU-Alarm` monitors EC2 CPU utilization against a configured threshold. The alarm is configured to invoke the `HospitalSelfHealingRecovery` Lambda function.

A controlled alarm-state test confirmed that CloudWatch invoked Lambda and that the function processed the alarm event successfully.

**Important limitation:** The verified Lambda workflow returns a recovery decision of “Investigate high CPU utilization” and a status of “Recovery action requested.” Actual EC2 recovery has not been verified. The Lambda function's access to the EC2 recovery permissions is restricted by the AWS Academy environment.

## 8. Backend API Endpoints

The Flask backend runs locally on port `5001`.

| Endpoint | Purpose |
|---|---|
| `/` | Basic application response |
| `/health` | Health check |
| `/predict` | Dataset-level anomaly detection results |
| `/explain?index=95` | Explanation for a selected data point |
| `/diagnose?index=95` | Diagnostic recommendation |
| `/recover?index=95` | Simulated recovery |
| `/verify?index=95` | Verification of simulated state |

The example index `95` is a demonstration input; other indices may produce different results.

## 9. Running the Project Locally

### Prerequisites

- Python 3.13
- The project repository and required model files
- A terminal on Windows

### Step 1: Start the backend

Open Command Prompt and navigate to the backend directory:

```bat
cd path\to\AISelfHealingHospitalCloud_Cloud_Project_2026\src\backend
```

Activate your existing Python 3.13 virtual environment if you have one. Install the required project dependencies if they are not already installed.

Start Flask:

```bat
python app.py
```

The backend should be available at:

`http://127.0.0.1:5001`

### Step 2: Start the frontend

Open a second Command Prompt and run:

```bat
python -m http.server 8000 --directory "path\to\AISelfHealingHospitalCloud_Cloud_Project_2026\src\frontend"
```

Replace the example path with the actual location of your project folder.

Open the dashboard at:

`http://127.0.0.1:8000/`

Keep both terminal windows running while demonstrating the project.

## 10. Demonstration Workflow

1. Open the web dashboard.
2. Run anomaly detection on the available dataset.
3. Inspect the explanation for a selected data point.
4. Review the diagnostic recommendation.
5. Run the simulated recovery workflow.
6. Verify the resulting simulated state.
7. Explain the separate AWS CloudWatch-to-Lambda controlled test and its limitations.

## 11. Limitations and Future Scope

- Connect live infrastructure telemetry to the ML detection pipeline.
- Validate the model using additional datasets and evaluation metrics.
- Improve root-cause analysis with validated incident labels.
- Add authenticated, secure APIs for cloud status reporting.
- Enable actual EC2 recovery only after appropriate permissions, safeguards, and recovery tests are approved.
- Integrate real service-health checks and independent recovery verification.
- Evaluate the approach with representative hospital infrastructure telemetry.

## 12. Conclusion

This project demonstrates a modular approach to infrastructure anomaly detection, explainability, diagnostic recommendations, simulated recovery, and verification. It also demonstrates a controlled integration between AWS CloudWatch alarms and Lambda. The current implementation provides a foundation for further development toward a fully automated and independently verified self-healing cloud system.

## References

- Su et al., *Robust Anomaly Detection for Multivariate Time Series through Stochastic Recurrent Neural Network (OmniAnomaly)*, KDD 2019.
- [OmniAnomaly and SMD dataset repository](https://github.com/NetManAIOps/OmniAnomaly)
- [Amazon CloudWatch documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
- [AWS Lambda documentation](https://docs.aws.amazon.com/lambda/)
