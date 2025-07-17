import os
import json
import pandas as pd

def parse_cricsheet(folder_path: str) -> pd.DataFrame:
    """Parses all Cricsheet JSON files in a folder and extracts summary match info.

    Parameters
    ----------
    folder_path : str
        Path to the folder containing Cricsheet-style JSON files.

    Returns
    -------
    pandas.DataFrame
        A DataFrame with one row per match, including columns:
        date, season, venue, team1, team2, toss_winner, toss_decision, winner.
    """
    rows = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            full_path = os.path.join(folder_path, filename)
            with open(full_path, 'r') as f:
                data = json.load(f)
                info = data["info"]
                row = {
                    "date": info["dates"][0],
                    "season": info.get("season", ""),
                    "venue": info.get("venue", ""),
                    "team1": info["teams"][0],
                    "team2": info["teams"][1],
                    "toss_winner": info["toss"]["winner"],
                    "toss_decision": info["toss"]["decision"],
                    "winner": info["outcome"].get("winner", "")
                }
                rows.append(row)
    
    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")    

    return df