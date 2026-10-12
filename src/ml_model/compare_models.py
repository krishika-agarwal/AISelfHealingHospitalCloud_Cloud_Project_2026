import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import precision_score, recall_score, f1_score
from preprocess import load_machine_data

train, test, labels = load_machine_data()

scaler = StandardScaler()
train_scaled = scaler.fit_transform(train)
test_scaled = scaler.transform(test)

print("Contamination | Precision | Recall | F1 | Alerts")
print("-" * 55)

for contamination in [0.03, 0.05, 0.08, 0.10, 0.15]:
    model = IsolationForest(
        n_estimators=100,
        contamination=contamination,
        random_state=42,
        n_jobs=-1
    )
    model.fit(train_scaled)

    predictions = (model.predict(test_scaled) == -1).astype(int)

    precision = precision_score(labels, predictions, zero_division=0)
    recall = recall_score(labels, predictions, zero_division=0)
    f1 = f1_score(labels, predictions, zero_division=0)

    print(
        f"{contamination:13.2f} | {precision:9.3f} | "
        f"{recall:6.3f} | {f1:.3f} | {predictions.sum()}"
    )
