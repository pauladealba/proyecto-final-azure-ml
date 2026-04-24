import json
import os
import joblib
import numpy as np
import pandas as pd

def init():
    global model

    model_dir = os.getenv("AZUREML_MODEL_DIR")

    if model_dir is None:
        raise EnvironmentError("No existe la variable AZUREML_MODEL_DIR. Este archivo debe correr dentro de Azure.")

    model_file = None

    for root, dirs, files in os.walk(model_dir):
        if "model.pkl" in files:
            model_file = os.path.join(root, "model.pkl")
            break

    if model_file is None:
        raise FileNotFoundError(f"No se encontró model.pkl dentro de {model_dir}")

    model = joblib.load(model_file)

def run(raw_data):
    try:
        data = json.loads(raw_data)

        if "data" in data:
            data = data["data"]
        else:
            return json.dumps({"error": "El JSON debe tener una llave llamada data"})

        if isinstance(data, list) and len(data) > 0:
            if isinstance(data[0], list):
                data = data[0]

        data = pd.DataFrame(data)

        columns_to_drop = [
            "RowNumber",
            "CustomerId",
            "Surname",
            "Geography",
            "Gender",
            "Card Type"
        ]

        data_dummies = data.drop(columns_to_drop, axis=1, errors="ignore")

        prediction = model.predict(data_dummies)

        return json.dumps(prediction.tolist())

    except Exception as e:
        return json.dumps({"error": str(e)})