import numpy as np
import joblib
import os
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from preprocess import load_machine_data
from feature_engineering import add_rolling_features

os.makedirs("model", exist_ok=True)

train, test, labels = load_machine_data()

# Apply rolling-window feature engineering
train_fe = add_rolling_features(train, window=5)
test_fe = add_rolling_features(test, window=5)

# Scale using training data only
scaler = StandardScaler()
train_scaled = scaler.fit_transform(train_fe)
test_scaled = scaler.transform(test_fe)

model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42, n_jobs=-1)
model.fit(train_scaled)

joblib.dump(model, "model/isolation_forest.pkl")
joblib.dump(scaler, "model/scaler.pkl")

preds = model.predict(test_scaled)
preds_binary = np.where(preds == -1, 1, 0)

accuracy = (preds_binary == labels).mean()
tp = ((preds_binary == 1) & (labels == 1)).sum()
fp = ((preds_binary == 1) & (labels == 0)).sum()
fn = ((preds_binary == 0) & (labels == 1)).sum()
precision = tp / (tp + fp + 1e-9)
recall = tp / (tp + fn + 1e-9)
f1 = 2 * precision * recall / (precision + recall + 1e-9)

print("Accuracy:", round(accuracy, 4))
print("Precision:", round(precision, 4))
print("Recall:", round(recall, 4))
print("F1 Score:", round(f1, 4))
print("Detected anomalies:", preds_binary.sum(), "/ Actual anomalies:", labels.sum())
print("Model and scaler saved to model/")
