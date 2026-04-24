import json
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class ChurnModel:
    def __init__(self):
        self.model = RandomForestClassifier(random_state=42)
        self.umbral = 0.5

    def prepare_data(self, data):
        y = data["Exited"]

        X = data.drop(
            [
                "Exited",
                "RowNumber",
                "CustomerId",
                "Surname",
                "Geography",
                "Gender",
                "Card Type"
            ],
            axis=1,
            errors="ignore"
        )

        X = pd.get_dummies(X, drop_first=True)

        return X, y

    def train(self, data):
        X, y = self.prepare_data(data)

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)

        joblib.dump(self.model, "model.pkl")

        with open("umbral.json", "w") as file:
            json.dump({"umbral": self.umbral}, file)

        print("Modelo entrenado correctamente.")
        print(f"Accuracy: {accuracy}")

        return accuracy