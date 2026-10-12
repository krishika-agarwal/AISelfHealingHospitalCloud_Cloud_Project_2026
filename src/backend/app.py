import sys
import os

# Allow importing preprocess.py and feature_engineering.py from ../ml_model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ML_MODEL_DIR = os.path.join(BASE_DIR, "..", "ml_model")
sys.path.insert(0, ML_MODEL_DIR)

from flask import Flask, jsonify, request
import numpy as np
import pandas as pd
import joblib
from datetime import datetime

from preprocess import load_machine_data
from feature_engineering import add_rolling_features

app = Flask(__name__)

MODEL_PATH = os.path.join(ML_MODEL_DIR, "model", "isolation_forest.pkl")
SCALER_PATH = os.path.join(ML_MODEL_DIR, "model", "scaler.pkl")
THRESHOLD_PATH = os.path.join(ML_MODEL_DIR, "model", "threshold.pkl")

# In-memory simulated health state (resets on server restart). NOT a real system.
SIMULATED_HEALTH = {}

REMEDIATION_RULES = {
    "default": {
        "likely_subsystem": "unspecified resource (metric name unknown)",
        "suggested_action": "Restart affected service / investigate logs for this metric channel."
    }
}


def files_exist():
    return [p for p in [MODEL_PATH, SCALER_PATH, THRESHOLD_PATH] if not os.path.exists(p)]


def smooth(scores, window):
    if window == 1:
        return scores
    return pd.Series(scores).rolling(window, min_periods=1).mean().values


def run_detection():
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    threshold_config = joblib.load(THRESHOLD_PATH)

    _, test, labels = load_machine_data()
    test_fe = add_rolling_features(test, window=5)
    test_scaled = scaler.transform(test_fe)
    scores = model.decision_function(test_scaled)

    w = threshold_config["smooth_window"]
    thr = threshold_config["threshold"]
    preds = (smooth(scores, w) < thr).astype(int)
    return test, labels, scaler, preds, w, thr


def get_top_deviations(test, scaler, idx, top_k=5):
    train_mean = scaler.mean_[:38]
    train_std = scaler.scale_[:38]
    raw_values = test[idx]
    z = (raw_values - train_mean) / (train_std + 1e-9)
    top_idx = np.argsort(-np.abs(z))[:top_k]
    return [{
        "metric": f"metric_{int(i)}",
        "z_score": round(float(z[i]), 2),
        "current_value": round(float(raw_values[i]), 4),
        "training_mean": round(float(train_mean[i]), 4),
        "direction": "above normal" if z[i] > 0 else "below normal"
    } for i in top_idx]


@app.route("/")
def home():
    return jsonify({
        "project": "AI-Driven Self-Healing Cloud Infrastructure for Hospital Information Systems",
        "status": "dataset demonstration API (not connected to live infrastructure)",
        "endpoints": ["/", "/health", "/predict", "/explain", "/diagnose", "/recover", "/verify"],
        "pipeline": "Monitor -> Detect -> Explain -> Diagnose -> Recover -> Verify",
        "note": "This API runs anomaly detection and a SIMULATED recovery workflow on a stored "
                "test dataset (SMD machine-1-1). It does not monitor or modify live AWS infrastructure."
    })


@app.route("/health")
def health():
    missing = files_exist()
    if missing:
        return jsonify({"status": "unhealthy", "missing_files": missing}), 500
    try:
        joblib.load(MODEL_PATH)
        joblib.load(SCALER_PATH)
        joblib.load(THRESHOLD_PATH)
    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 500
    return jsonify({"status": "healthy", "message": "Model, scaler, and threshold files loaded successfully."})


@app.route("/predict")
def predict():
    missing = files_exist()
    if missing:
        return jsonify({"error": "Required model files are missing.", "missing_files": missing}), 500
    try:
        _, labels, _, preds, w, thr = run_detection()
        return jsonify({
            "dataset": "ServerMachineDataset - machine-1-1 (test split)",
            "total_points": int(len(labels)),
            "labeled_anomaly_points": int(labels.sum()),
            "detected_anomaly_points": int(preds.sum()),
            "smoothing_window": int(w),
            "threshold": float(thr),
            "note": "This reflects detection on a static, pre-recorded test dataset. "
                    "It is not a live monitoring result."
        })
    except Exception as e:
        return jsonify({"error": "Prediction failed.", "details": str(e)}), 500


def _resolve_index(preds, request):
    anomaly_indices = np.where(preds == 1)[0]
    index_param = request.args.get("index")
    if index_param is not None:
        idx = int(index_param)
        if idx < 0 or idx >= len(preds):
            return None, jsonify({"error": f"index must be between 0 and {len(preds)-1}"}), 400
        if preds[idx] != 1:
            return None, jsonify({
                "message": f"Point {idx} was NOT flagged as an anomaly.",
                "hint": "Choose a flagged point.",
                "example_flagged_indices": anomaly_indices[:10].tolist()
            }), 200
        return idx, None, None
    if len(anomaly_indices) == 0:
        return None, jsonify({"message": "No anomalies detected with current threshold."}), 200
    return int(anomaly_indices[0]), None, None


@app.route("/explain")
def explain():
    missing = files_exist()
    if missing:
        return jsonify({"error": "Required model files are missing.", "missing_files": missing}), 500
    try:
        test, labels, scaler, preds, w, thr = run_detection()
        idx, early_response, code = _resolve_index(preds, request)
        if early_response is not None:
            return early_response, code

        top_metrics = get_top_deviations(test, scaler, idx)
        return jsonify({
            "flagged_point_index": idx,
            "ground_truth_label_at_point": int(labels[idx]),
            "explanation_type": "metric deviation analysis (z-score vs training baseline)",
            "top_deviating_metrics": top_metrics,
            "interpretation": "These metrics deviate most from their normal training-time behavior "
                              "at this point. This is a POSSIBLE INDICATION of what is abnormal, "
                              "not a confirmed root cause.",
            "limitations": "SMD does not publish metric names, so columns are labeled metric_0 to "
                           "metric_37. Deviation analysis identifies abnormal signals, not causality."
        })
    except Exception as e:
        return jsonify({"error": "Explanation failed.", "details": str(e)}), 500


@app.route("/diagnose")
def diagnose():
    missing = files_exist()
    if missing:
        return jsonify({"error": "Required model files are missing.", "missing_files": missing}), 500
    try:
        test, labels, scaler, preds, w, thr = run_detection()
        idx, early_response, code = _resolve_index(preds, request)
        if early_response is not None:
            return early_response, code

        top_metrics = get_top_deviations(test, scaler, idx)
        top_metric_name = top_metrics[0]["metric"]

        rule = REMEDIATION_RULES.get(top_metric_name, REMEDIATION_RULES["default"])

        SIMULATED_HEALTH[idx] = {
            "status": "unhealthy",
            "diagnosed_at": datetime.now().isoformat(),
            "top_metric": top_metric_name,
            "z_score": top_metrics[0]["z_score"]
        }

        return jsonify({
            "flagged_point_index": idx,
            "diagnosis_type": "heuristic rule-based suggestion (illustrative, not validated)",
            "most_deviating_metric": top_metric_name,
            "z_score": top_metrics[0]["z_score"],
            "likely_subsystem": rule["likely_subsystem"],
            "suggested_action": rule["suggested_action"],
            "simulated_health_status": "unhealthy",
            "note": "This is a SIMULATED diagnosis for demonstration purposes. No real "
                    "infrastructure has been inspected or diagnosed."
        })
    except Exception as e:
        return jsonify({"error": "Diagnosis failed.", "details": str(e)}), 500


@app.route("/recover")
def recover():
    index_param = request.args.get("index")
    if index_param is None:
        return jsonify({"error": "Provide ?index=N for a point already diagnosed via /diagnose."}), 400
    idx = int(index_param)

    if idx not in SIMULATED_HEALTH:
        return jsonify({
            "error": f"Point {idx} has not been diagnosed yet. Call /diagnose?index={idx} first."
        }), 400

    before_status = SIMULATED_HEALTH[idx]["status"]
    SIMULATED_HEALTH[idx]["status"] = "healthy"
    SIMULATED_HEALTH[idx]["recovered_at"] = datetime.now().isoformat()

    return jsonify({
        "flagged_point_index": idx,
        "action_taken": "SIMULATED remediation applied (no real system modified).",
        "status_before": before_status,
        "status_after": "healthy",
        "simulated": True,
        "note": "This demonstrates the recovery step of the pipeline using an in-memory "
                "simulated health flag. Real AWS/cloud resources were not modified."
    })


@app.route("/verify")
def verify():
    index_param = request.args.get("index")
    if index_param is None:
        return jsonify({"error": "Provide ?index=N for a point already processed."}), 400
    idx = int(index_param)

    if idx not in SIMULATED_HEALTH:
        return jsonify({
            "error": f"Point {idx} has no recorded health state. Run /diagnose and /recover first."
        }), 400

    record = SIMULATED_HEALTH[idx]
    return jsonify({
        "flagged_point_index": idx,
        "current_simulated_status": record["status"],
        "history": record,
        "simulated": True,
        "note": "This reflects the in-memory simulated health state only, not a real "
                "infrastructure health check."
    })


if __name__ == "__main__":
    app.run(debug=True, port=5001)
