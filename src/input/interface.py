import joblib
import os
import pandas as pd
from src.input.normalisation import fix_team_and_venue_names
from src.input.standardise import standardise_match_data
from src.features.build_features import build_feature_matrix
from src.ml.train_logistic import train_logistic


def load_clean_match_data(league: str) -> pd.DataFrame:
    raw = pd.read_csv(f"data/{league}_matches.csv")
    df = fix_team_and_venue_names(raw, league)
    df = standardise_match_data(df)
    return df


def get_teams_and_venues(df: pd.DataFrame) -> tuple[list[str], list[str]]:
    teams_array = df[["team1", "team2"]].to_numpy().flatten()
    teams = sorted(pd.unique(teams_array))
    venues = sorted(df["venue"].unique())
    return teams, venues


def load_model(league: str):
    model_path = f"models/{league}_model.pkl"
    if os.path.isfile(model_path):
        return joblib.load(model_path)

    df = load_clean_match_data(league)
    features = build_feature_matrix(df)

    path = f"data/features/{league}_features.csv"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    features.to_csv(path, index=False)

    return train_logistic(features, save_path=f"models/{league}_model.pkl")


def build_match_features(
    team1, team2, venue, toss_winner, toss_decision
) -> pd.DataFrame:
    team1_batting = (
        1
        if (toss_winner == team1.get_name() and toss_decision == "Bat")
        or (toss_winner == team2.get_name() and toss_decision == "Bowl")
        else 0
    )

    features = {
        "team1_recent_form": team1.calc_recent_form(),
        "team2_recent_form": team2.calc_recent_form(),
        "team1_venue_win_rate": team1.calc_venue_win_rate(venue.get_name()),
        "team2_venue_win_rate": team2.calc_venue_win_rate(venue.get_name()),
        "team1_chasing_win_rate": team1.calc_win_rate_chasing(),
        "team1_defending_win_rate": team1.calc_win_rate_defending(),
        "team2_chasing_win_rate": team2.calc_win_rate_chasing(),
        "team2_defending_win_rate": team2.calc_win_rate_defending(),
        "venue_chasing_win_rate": venue.calc_win_rate_chasing(),
        "venue_defending_win_rate": venue.calc_win_rate_defending(),
        "team1_vs_team2_record": team1.calc_head_to_head_win_rate(team2.get_name()),
        "toss_winner": 1 if toss_winner == team1.get_name() else 0,
        "team1_batting": team1_batting,
    }

    return pd.DataFrame([features])
