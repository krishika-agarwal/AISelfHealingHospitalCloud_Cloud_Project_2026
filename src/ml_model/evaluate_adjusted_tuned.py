import numpy as np
import pandas as pd
import joblib
from preprocess import load_machine_data
from feature_engineering import add_rolling_features
from evaluate_adjusted import point_adjust

def smooth(scores, window):
    if window == 1:
        return scores
    return pd.Series(scores).rolling(window, min_periods=1).mean().values

train, test, labels = load_machine_data()
test_fe = add_rolling_features(test, window=5)

scaler = joblib.load("model/scaler.pkl")
model = joblib.load("model/isolation_forest.pkl")
threshold_config = joblib.load("model/threshold.pkl")

test_scaled = scaler.transform(test_fe)
scores = model.decision_function(test_scaled)

w = threshold_config["smooth_window"]
thr = threshold_config["threshold"]

smoothed_scores = smooth(scores, w)
preds = (smoothed_scores < thr).astype(int)

tp = ((preds == 1) & (labels == 1)).sum()
fp = ((preds == 1) & (labels == 0)).sum()
fn = ((preds == 0) & (labels == 1)).sum()
precision = tp / (tp + fp + 1e-9)
recall = tp / (tp + fn + 1e-9)
f1 = 2 * precision * recall / (precision + recall + 1e-9)

print(f"--- Raw point-wise metrics (tuned threshold: window={w}, thr={thr:.4f}) ---")
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

print("\n--- Point-adjusted metrics (tuned threshold + point adjustment) ---")
print("Precision:", round(precision2, 4))
print("Recall:", round(recall2, 4))
print("F1:", round(f1_2, 4))
print("\nNOTE: Threshold was tuned on the full test set (Experiment A, exploratory).")
print("This result combines in-sample threshold tuning with point-adjustment,")
print("and should be labeled as a best-case/optimistic estimate, not generalization performance.")
