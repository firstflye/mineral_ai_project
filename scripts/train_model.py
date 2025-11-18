import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Paths
DATA_PATH = os.path.join(BASE_DIR, "data", "minerals.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "copper_model.pkl")

# Load dataset
data = pd.read_csv(DATA_PATH)

# Features and target
X = data.drop("has_copper", axis=1)
y = data["has_copper"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))

# Save model
joblib.dump(model, MODEL_PATH)
print(f"Model saved to {MODEL_PATH}")
