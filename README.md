# Cricket ML Predictor

> Predict pre-match win probabilities for T20 matches using machine learning and historical data.

This project uses historical franchise T20 match data to build a machine learning model that predicts the outcome of T20 cricket matches. It features a custom feature engineering pipeline, multiple classification models, and an interactive frontend for match-day predictions.

## Features

- **Domain-specific features**: team form, toss effect, venue advantage, head-to-head history
- **Machine learning model**: logistic regression
- **Data pipeline**: clean and transform raw match data into model-ready datasets
- **Frontend**: Streamlit web interface for making predictions
- **Modular structure**: reusable components for input loading, feature generation, modeling, and prediction

## Getting Started

### Clone the Repo

```
git clone https://github.com/your-username/cricket-ml-predictor.git
cd cricket-ml-predictor
```

### Set Up a Virtual Environment

This project uses a Python virtual environment for dependency isolation.

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Run the App

```bash
streamlit run app.py
```

## Project Structure

```
cricket-ml-predictor/
├── app.py                 # Streamlit frontend
├── data/                  # Raw and processed datasets
├── models/                # Trained ML models
├── requirements.txt       # Project dependencies
├── src/                   # Source code
│   ├── input/             # Data loaders & standardizers
│   ├── features/          # Feature generation logic
│   ├── objects/           # Domain objects (Team, Match, etc.)
│   ├── ml/                # Training, evaluation, prediction
│   └── interface/         # UI utilities
└── README.md
```

## License

This project is released under the [MIT License](LICENSE).