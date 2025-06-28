import joblib
import pandas as pd


def predict_from_row(row, model_path="models/logistic.pkl"):
    """Predict win probability for a single match row."""

    model = joblib.load(model_path)
    if isinstance(row, dict):
        row = pd.DataFrame([row])
    prob = model.predict_proba(row)[0][1]
    return prob
