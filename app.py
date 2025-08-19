from flask import Flask, request, render_template,jsonify, url_for
import pandas as pd
import numpy as np
import pickle

# Load saved objects
with open("ct_ohe.pickle", "rb") as f:
    ct = pickle.load(f)

with open("minmax.pickle", "rb") as f:
    scaler = pickle.load(f)

with open("polyfeatures.pickle", "rb") as f:
    poly = pickle.load(f)

with open("medical_charges_prediction.pickle", "rb") as f:
    model_poly = pickle.load(f)

# List of skewed features you log-transformed
skewedFeatures = ["age", "bmi"]  # replace with your actual list

app = Flask(__name__)
application = app
@app.route("/")
def home():
    return render_template("index.html")  # serve the HTML form

@app.route("/health")
def health():
    return "OK", 200  # Explicitly says → everything fine


@app.route("/predict", methods=["POST"])
def predict():
    data = request.form  # read form data

    # Convert form data to proper types
    input_df = pd.DataFrame([{
        "age": int(data["age"]),
        "sex": data["sex"],
        "bmi": float(data["bmi"]),
        "children": int(data["children"]),
        "smoker": data["smoker"],
        "region": data["region"]
    }])

    # Apply preprocessing steps
    for feature in skewedFeatures:
        input_df[feature] = np.log1p(input_df[feature])

    input_encoded = ct.transform(input_df)
    input_scaled = scaler.transform(input_encoded)
    input_poly = poly.transform(input_scaled)

    prediction_log = model_poly.predict(input_poly)
    prediction_actual = np.expm1(prediction_log)

    return f"<h2>Predicted Charges: ${prediction_actual[0]:.2f}</h2>"

if __name__ == "__main__":
    # Local run only; EB runs via WSGI
    app.run(debug=True)


import os
secret = os.environ.get("SECRET_KEY")
api_key = os.environ.get("API_KEY")

