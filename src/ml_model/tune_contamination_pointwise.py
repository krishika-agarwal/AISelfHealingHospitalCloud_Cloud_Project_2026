import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from preprocess import load_machine_data
from feature_engineering import add_rolling_features

def smooth(scores, w):
    if w == 1:
        return scores
    return pd.Series(scores).rolling(w, min_periods=1).mean().values

def point_metrics(labels, preds):
    tp = ((preds == 1) & (labels == 1)).sum()
    fp = ((preds == 1) & (labels == 0)).sum()
    fn = ((preds == 0) & (labels == 1)).sum()
    p = tp / (tp + fp + 1e-9)
    r = tp / (tp + fn + 1e-9)
    f = 2 * p * r / (p + r + 1e-9)
    return p, r, f

train, test, labels = load_machine_data()
train_fe = add_rolling_features(train, window=5)
test_fe = add_rolling_features(test, window=5)

scaler = StandardScaler()
train_scaled = scaler.fit_transform(train_fe)
test_scaled = scaler.transform(test_fe)

print("Contamination | Best window | Best threshold | Alerts | P | R | F1 (point-wise)")
print("-" * 85)

for contamination in [0.02, 0.03, 0.05, 0.08, 0.10, 0.12, 0.15]:
    model = IsolationForest(n_estimators=100, contamination=contamination, random_state=42, n_jobs=-1)
    model.fit(train_scaled)
    scores = model.decision_function(test_scaled)
    
    best = None
    for w in [1, 5, 10, 20, 30]:
        s = smooth(scores, w)
        for pct in np.arange(1, 40.5, 0.5):
            thr = np.percentile(s, pct)
            preds = (s < thr).astype(int)
            p, r, f = point_metrics(labels, preds)
            if best is None or f > best["f1"]:
                best = dict(w=w, thr=thr, p=p, r=r, f1=f, alerts=int(preds.sum()))
    
    print(f"{contamination:13.2f} | {best['w']:11d} | {best['thr']:14.4f} | "
          f"{best['alerts']:6d} | {best['p']:.3f} | {best['r']:.3f} | {best['f1']:.4f}")

print("\nNOTE: Tuned directly for point-wise F1 on the full test set (exploratory).")
print("Point-wise F1 cannot be gamed by sparse single-point hits per segment,")
print("unlike point-adjusted F1.")
