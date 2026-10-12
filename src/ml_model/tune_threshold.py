import numpy as np
import pandas as pd
import joblib
from preprocess import load_machine_data
from feature_engineering import add_rolling_features

def segments(binary):
    segs, in_seg, start = [], False, 0
    for i, v in enumerate(binary):
        if v == 1 and not in_seg:
            start, in_seg = i, True
        elif v == 0 and in_seg:
            segs.append((start, i)); in_seg = False
    if in_seg:
        segs.append((start, len(binary)))
    return segs

def point_metrics(labels, preds):
    tp = int(((preds == 1) & (labels == 1)).sum())
    fp = int(((preds == 1) & (labels == 0)).sum())
    fn = int(((preds == 0) & (labels == 1)).sum())
    p = tp / (tp + fp + 1e-9)
    r = tp / (tp + fn + 1e-9)
    f = 2 * p * r / (p + r + 1e-9)
    return p, r, f, fp

def event_metrics(labels, preds):
    segs = segments(labels)
    detected, delays = 0, []
    for s, e in segs:
        hits = np.where(preds[s:e] == 1)[0]
        if len(hits):
            detected += 1
            delays.append(int(hits[0]))
    false_events = sum(1 for s, e in segments(preds) if labels[s:e].sum() == 0)
    return detected, len(segs), false_events, delays

def smooth(scores, w):
    return scores if w == 1 else pd.Series(scores).rolling(w, min_periods=1).mean().values

def sweep(scores, labels, sl):
    best = None
    for w in [1, 5, 10, 20, 30]:
        s, lab = smooth(scores, w)[sl], labels[sl]
        for pct in np.arange(1, 40.5, 0.5):
            thr = np.percentile(s, pct)
            preds = (s < thr).astype(int)
            p, r, f, fp = point_metrics(lab, preds)
            if best is None or f > best["f1"]:
                best = dict(w=w, pct=float(pct), thr=float(thr), f1=f)
    return best

def report(title, scores, labels, sl, w, thr):
    s, lab = smooth(scores, w)[sl], labels[sl]
    preds = (s < thr).astype(int)
    p, r, f, fp = point_metrics(lab, preds)
    det, n, fe, delays = event_metrics(lab, preds)
    print(f"\n{title}")
    print(f"  smoothing window={w}, threshold={thr:.4f}, alerts raised={int(preds.sum())}")
    print(f"  Point-wise : P={p:.4f}  R={r:.4f}  F1={f:.4f}  (false-alarm points: {fp})")
    med = int(np.median(delays)) if delays else "n/a"
    print(f"  Event-level: incidents detected {det}/{n}, false-alarm events {fe}, "
          f"median detection delay {med} steps")

train, test, labels = load_machine_data()
test_fe = add_rolling_features(test, window=5)
scaler = joblib.load("model/scaler.pkl")
model = joblib.load("model/isolation_forest.pkl")
scores = model.decision_function(scaler.transform(test_fe))

segs = segments(labels)
print("Incidents in test set:", len(segs), "| lengths:", [e - s for s, e in segs])

full = slice(0, len(labels))
bestA = sweep(scores, labels, full)
report("A) Tuned on full test set (objective: point-wise F1)",
       scores, labels, full, bestA["w"], bestA["thr"])

h = len(labels) // 2
bestB = sweep(scores, labels, slice(0, h))
report("B) Tuned on FIRST half only -> evaluated on SECOND half (held-out)",
       scores, labels, slice(h, len(labels)), bestB["w"], bestB["thr"])

joblib.dump({"threshold": bestA["thr"], "smooth_window": int(bestA["w"])}, "model/threshold.pkl")
print("\nSaved setting A to model/threshold.pkl")
