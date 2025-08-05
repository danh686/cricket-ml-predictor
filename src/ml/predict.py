import pandas as pd


def predict_from_row(row, model):
    """Predict win probability for a single match row."""
    if isinstance(row, dict):
        row = pd.DataFrame([row])
    row = row.fillna(0.5)
    prob = model.predict_proba(row)[0][1]
    return prob
