import os
import joblib
import pandas as pd

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Paths
MODEL_PATH = os.path.join(BASE_DIR, "models", "copper_model.pkl")

# Load trained model
model = joblib.load(MODEL_PATH)

# Example: create a new sample to predict
# Columns must match training data: latitude, longitude, soil_ph, magnetic_field
sample_data = pd.DataFrame([
    {"latitude": -1.33, "longitude": 56.82, "soil_ph": 9.5, "magnetic_field": 20},
    {"latitude": 0.7, "longitude": 38.00, "soil_ph": 2.9, "magnetic_field": 50}
])

# Predict
predictions = model.predict(sample_data)
sample_data["has_copper_prediction"] = predictions

print(sample_data)
