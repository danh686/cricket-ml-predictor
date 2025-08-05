import pandas as pd
import numpy as np


def standardise_match_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert an initial DataFrame into a standardised format with sanity checks

    Parameters
    ----------
    df: pd.DataFrame
        Original DataFrame passed from the data loader

    Returns
    -------
    pd.DataFrame
        New DataFrame with standardised structure, format and sanity checks

    """
    df = df.copy()

    # Standardise team names
    df["team1"] = df["team1"].str.strip()
    df["team2"] = df["team2"].str.strip()

    def randomise_teams(row):
        if np.random.rand() < 0.5:
            row["team1"], row["team2"] = row["team2"], row["team1"]
        return row

    df = df.apply(randomise_teams, axis=1)

    df["winner"] = df["winner"].fillna("").str.strip()

    # Parse date
    df["date"] = pd.to_datetime(df["date"])

    # Drop matches with no winner
    df = df[(df["winner"] == df["team1"]) | (df["winner"] == df["team2"])]

    # Standardise toss decision
    df["toss_decision"] = df["toss_decision"].str.lower().str.strip()

    # Add column for team1 win variable
    df["team1_win"] = np.where(df["winner"] == df["team1"], 1, 0)

    def get_batting_first(row):
        if row["toss_winner"] == row["team1"]:
            return row["team1"] if row["toss_decision"] == "bat" else row["team2"]
        else:
            return row["team2"] if row["toss_decision"] == "bat" else row["team1"]

    # Add variable for team batting first
    df["batting_first_team"] = df.apply(get_batting_first, axis=1)

    standard_cols = [
        "date",
        "season",
        "venue",
        "team1",
        "team2",
        "toss_winner",
        "toss_decision",
        "batting_first_team",
        "winner",
        "team1_win",
    ]
    df = df[standard_cols]

    df = df.sort_values(by="date").reset_index(drop=True)

    return df
