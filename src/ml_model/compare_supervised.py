from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from preprocess import load_machine_data

train, test, labels = load_machine_data()

# Split labeled test observations into validation and holdout sets
X_fit, X_hold, y_fit, y_hold = train_test_split(
    test, labels, test_size=0.5, random_state=42, stratify=labels
)

scaler = StandardScaler()
X_fit = scaler.fit_transform(X_fit)
X_hold = scaler.transform(X_hold)

model = RandomForestClassifier(
    n_estimators=100,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)

model.fit(X_fit, y_fit)
preds = model.predict(X_hold)

print(classification_report(
    y_hold, preds,
    target_names=["Normal", "Anomaly"],
    zero_division=0
))
