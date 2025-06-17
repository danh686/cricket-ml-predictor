import pandas as pd


def load_ipl_matches(path: str) -> pd.DataFrame:
    # Target columns: team1, team2, winner, toss_winner, toss_decision, venue, date, season
    df = pd.read_csv(path)

    # Keep only the required columns
    target_columns = [
        "team1",
        "team2",
        "winner",
        "toss_winner",
        "toss_decision",
        "venue",
        "date",
        "season",
    ]
    df = df[target_columns]

    # Check for missing columns
    missing = [col for col in target_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing expected columns: {missing}")

    # Standardise team names
    TEAM_NAME_FIX = {
        "Royal Challengers Bangalore": "Royal Challengers Bengaluru",
        "Kings XI Punjab": "Punjab Kings",
        "Delhi Daredevils": "Delhi Capitals",
        "Rising Pune Supergiants": "Rising Pune Supergiant",
    }
    for col in ["team1", "team2", "winner", "toss_winner"]:
        df[col] = df[col].replace(TEAM_NAME_FIX)

    return df
