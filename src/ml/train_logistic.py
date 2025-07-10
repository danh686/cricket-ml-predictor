from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib


def train_logistic(
    df, c=0.01, class_weight="balanced", save_path="models/logistic.pkl"
):
    # Load features
    X = df.drop(columns=["team1_win"])
    y = df["team1_win"]

    # Remove rows with NaNs in X or y
    mask = ~X.isnull().any(axis=1) & y.notnull()
    X = X[mask]
    y = y[mask]

    # Split into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Create and train model
    model = LogisticRegression(C=c, class_weight=class_weight, max_iter=1000)
    model.fit(X_train, y_train)

    joblib.dump(model, save_path)

    return model
