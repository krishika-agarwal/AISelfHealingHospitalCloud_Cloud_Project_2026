# Machine Learning Evaluation Results

## Dataset and Processing

- **Dataset:** Server Machine Dataset (SMD)
- **Model:** Isolation Forest
- **Recorded observations:** 28,479
- **Original features:** 38
- **Engineered features:** 114
- **Labelled anomaly observations:** 2,694
- **Observations flagged as anomalous:** 8,259

## Recorded Evaluation Metrics

| Metric | Recorded value |
|---|---:|
| Precision | 0.2906 |
| Recall | 0.8909 |
| Point-wise F1-score | 0.4382 |

## Observations

The recorded model run achieved high recall, indicating that it identified a large proportion of labelled anomalies. However, precision was relatively low, indicating that many flagged observations did not correspond to labelled anomalies.

The number of flagged observations is not equivalent to the number of correctly detected anomalies. The evaluation metrics should be interpreted using the same test split and evaluation method.

## Limitations

The model identifies unusual patterns in the selected dataset; it does not independently establish the actual cause of an infrastructure fault. The evaluation uses SMD data and does not establish the model's performance on live hospital infrastructure.

**Note:** Verify these values against the final evaluation run before submission.
