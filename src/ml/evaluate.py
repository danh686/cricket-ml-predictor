from sklearn.metrics import confusion_matrix, roc_auc_score, classification_report


def evaluate_model(model, X_test, y_test):
    """Evaluate model on test data and print metrics"""

    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    print(f"Classification Report:\n{classification_report(y_test, y_pred)}")
    print(f"AUC Score:\n{roc_auc_score(y_test, y_proba)}")
    print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")
