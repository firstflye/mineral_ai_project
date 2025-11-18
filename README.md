Mineral-predictor-AI - Prediction of Mineral Deposits Using Machine Learning

Mineral-predictor-AI is a simplistic machine learning application that predicts whether an area has copper or not based on real geological data:

Coordinates (latitude and longitude)

Soil PH

Magnetic field intensity

It contains a Random Forest ai model and training and prediction scripts.

🚀 What it does

Predict whether copper is present or not based on minerals.csv

Save and load a trained machine learning model (.pkl)

Predict whether copper is present or not based on own coordinates

 

📁 File Structure

mineral_ai_project/
│
├── data/
│ └── minerals.csv # The data used to train the model
│
├── models/
│ └── copper_model.pkl # The model that will be auto-saved after training
│
├── scripts/
│ ├── train_model.py # Script to train the model and save it for use later on
│ └── predict_model.py # Script that loads the model and makes a prediction based on user input
│
└── README.md # Information about the project

🛠️ How to Install

1. Clone this repository

2. Create a virtual environment (optional)

python3 -m venv venv
source venv/bin/activate # Linux / macOS
venv\Scripts\activate # Windows

3. Install requirements

pip install pandas numpy scikit-learn joblib

📚 How to train the model

You can run:

python3 scripts/train_model.py

This will load minerals.csv, train a Random Forest and print the relevant accuracy results before saving the model to: models/copper_model.pkl in the models folder.

🔮 How to predict whether copper is there or not

You can edit the test data provided in predict_model.py and run:

python3 scripts/predict_model.py

You'll get an output that tells you whether copper is presumed to be there or not:

   latitude  longitude  soil_ph  magnetic_field  has_copper_prediction
0    -1.23     36.82      6.5              40                        1
1     0.50     37.00      6.9              50                        0

📈 The Dataset

A small dataset is included as an example. You can replace minerals.csv with a file that contains real-world data to make this more applicable.

Column Descriptions of the dataset:

ColumnDescriptionlatitudeGeographic coordinateslongitudeGeographic coordinatessoil_phSoil phmagnetic_fieldMagnetic field measurementhas_copper1 = copper present, 0 = copper not present

🤝 Contributors

Feel free to make this model better or play around with GIS tools
