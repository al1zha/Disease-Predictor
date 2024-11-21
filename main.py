from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

app = FastAPI()

# Serve static files like HTML, CSS, and JS
app.mount("/static", StaticFiles(directory="static"), name="static")

class Symptoms(BaseModel):
    symptoms: list

# Load training data
df = pd.read_csv("Training.csv")

# List of symptoms (features)
symptom_list = df.columns.values[:-1]

# List of diseases
disease_list = df['prognosis'].unique()
disease_mapping = {disease: idx for idx, disease in enumerate(disease_list)}
disease_reverse_mapping = {v: k for k, v in disease_mapping.items()}

# Replace disease names with numerical indices in the dataset
df.replace({'prognosis': disease_mapping}, inplace=True)

# Features and labels
X = df[symptom_list]
y = df[["prognosis"]]
y = np.ravel(y)

# Train the machine learning models
clf_dt = tree.DecisionTreeClassifier()
clf_dt = clf_dt.fit(X, y)

clf_rf = RandomForestClassifier()
clf_rf = clf_rf.fit(X, y)

clf_nb = GaussianNB()
clf_nb = clf_nb.fit(X, y)

@app.get("/")
def serve_homepage():
    return FileResponse("static/index.html")

@app.post("/predict")
async def predict_disease(symptoms: Symptoms):
    # Process symptoms from the request
    psymptoms = symptoms.symptoms
    input_vector = [0] * len(symptom_list)
    
    for idx, symptom in enumerate(symptom_list):
        if symptom in psymptoms:
            input_vector[idx] = 1
    
    # Make predictions using the models
    dt_prediction = clf_dt.predict([input_vector])[0]
    rf_prediction = clf_rf.predict([input_vector])[0]
    nb_prediction = clf_nb.predict([input_vector])[0]

    # Return the predicted diseases from each model
    return JSONResponse({
        "DecisionTree": disease_reverse_mapping.get(dt_prediction, "Not Found"),
        "RandomForest": disease_reverse_mapping.get(rf_prediction, "Not Found"),
        "NaiveBayes": disease_reverse_mapping.get(nb_prediction, "Not Found")
    })
