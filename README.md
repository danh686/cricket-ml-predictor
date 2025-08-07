# Cricket ML Predictor

A hobby project exploring machine learning models for predicting pre-match win probabilities in franchise T20 cricket. It uses historical match data from [Cricsheet](https://cricsheet.org/) and a simple logistic regression model to estimate which team is more likely to win.

## What's inside

- **Feature engineering** for team form, venue advantage, toss impact and head-to-head results.
- **Training scripts** for a logistic regression classifier (see `src/ml`).
- **Streamlit app** (`app.py`) for making match-day predictions.
- CSV data for IPL, BBL and T20 Blast stored in `data/`.
- `update_data.py` helper to convert Cricsheet JSON files into match CSVs.

This code is meant for learning and experimentation; results are not intended for betting or professional use.

## Quick start

```
git clone https://github.com/your-username/cricket-ml-predictor.git
cd cricket-ml-predictor
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Project layout

```
cricket-ml-predictor/
├── app.py               # Streamlit frontend
├── data/                # CSV match datasets
├── src/                 # Feature engineering and ML code
│   ├── features/
│   ├── input/
│   ├── ml/
│   ├── objects/
│   └── interface/
└── update_data.py       # Convert Cricsheet data
```

## License

Released under the [MIT License](LICENSE).
