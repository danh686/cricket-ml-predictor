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

    return df
