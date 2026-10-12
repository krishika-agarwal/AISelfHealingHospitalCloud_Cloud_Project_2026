import numpy as np
import joblib
from preprocess import load_machine_data
from feature_engineering import add_rolling_features

def point_adjust(labels, preds):
    preds = preds.copy()
    anomaly_state = False
    for i in range(len(labels)):
        if labels[i] == 1 and preds[i] == 1 and not anomaly_state:
            anomaly_state = True
            for j in range(i, -1, -1):
                if labels[j] == 0:
                    break
                else:
                    preds[j] = 1
        elif labels[i] == 0:
            anomaly_state = False
        if anomaly_state:
            preds[i] = 1
    return preds

train, test, labels = load_machine_data()
test_fe = add_rolling_features(test, window=5)

scaler = joblib.load("model/scaler.pkl")
model = joblib.load("model/isolation_forest.pkl")

test_scaled = scaler.transform(test_fe)
preds = (model.predict(test_scaled) == -1).astype(int)

tp = ((preds == 1) & (labels == 1)).sum()
fp = ((preds == 1) & (labels == 0)).sum()
fn = ((preds == 0) & (labels == 1)).sum()
precision = tp / (tp + fp + 1e-9)
recall = tp / (tp + fn + 1e-9)
f1 = 2 * precision * recall / (precision + recall + 1e-9)

print("--- Raw point-wise metrics ---")
print("Precision:", round(precision, 4))
print("Recall:", round(recall, 4))
print("F1:", round(f1, 4))

adjusted_preds = point_adjust(labels, preds)
tp2 = ((adjusted_preds == 1) & (labels == 1)).sum()
fp2 = ((adjusted_preds == 1) & (labels == 0)).sum()
fn2 = ((adjusted_preds == 0) & (labels == 1)).sum()
precision2 = tp2 / (tp2 + fp2 + 1e-9)
recall2 = tp2 / (tp2 + fn2 + 1e-9)
f1_2 = 2 * precision2 * recall2 / (precision2 + recall2 + 1e-9)

print("\n--- Point-adjusted metrics (standard SMD evaluation) ---")
print("Precision:", round(precision2, 4))
print("Recall:", round(recall2, 4))
print("F1:", round(f1_2, 4))
