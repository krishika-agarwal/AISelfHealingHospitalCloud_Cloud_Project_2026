# Project Results

This directory contains the evaluation results and implementation evidence for the **AI-Driven Self-Healing Cloud Infrastructure for Hospital Information Systems using AIOps and Explainable AI** project.

## Contents

- `ml_evaluation.md` — Recorded anomaly detection metrics and dataset evaluation details.
- `test_results.md` — Summary of functional tests and AWS event-processing results.
- `screenshots/` — Directory for selected screenshots supporting the reported results.

## Evaluation Scope

The project evaluates anomaly detection using the Server Machine Dataset (SMD), presents metric-level explanations, and demonstrates diagnosis and recovery-status handling. AWS testing covers EC2 monitoring, a CloudWatch CPU alarm, and Lambda event processing.

The dashboard's recovery and verification workflow is simulated. Live EC2 recovery, complete SNS email delivery, and fully integrated end-to-end self-healing have not been verified.

## Limitations

The recorded results demonstrate the current proof of concept. They do not establish production readiness, live autonomous recovery, or validated performance on hospital infrastructure.
