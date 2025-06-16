from src.input.loaders.load_ipl_csv import load_ipl_matches
from src.input.standardise import standardise_match_data
from src.objects.Venue import Venue
from src.objects.Team import Team
import pandas as pd


def build_feature_matrix(path: str) -> pd.DataFrame:
    raw_df = load_ipl_matches(path)
    df = standardise_match_data(raw_df)

    features = []

    for i, row in df.iterrows():
        team1 = Team(name=row["team1"], df=df.iloc[:i])
        team2 = Team(name=row["team2"], df=df.iloc[:i])
        venue = Venue(name=row["venue"], df=df.iloc[:i])

        match_features = {
            "team1_recent_form": team1.calc_recent_form(),
            "team2_recent_form": team2.calc_recent_form(),
            "team1_venue_win_rate": team1.calc_venue_win_rate(row["venue"]),
            "team2_venue_win_rate": team2.calc_venue_win_rate(row["venue"]),
            "venue_chasing_win_rate": venue.calc_win_rate_chasing(),
            "venue_defending_win_rate": venue.calc_win_rate_defending(),
            "team1_vs_team2_record": team1.calc_head_to_head_win_rate(team2.name),
            "toss_winner": 1 if row["toss_winner"] == row["team1"] else 0,
            "toss_decision_bat": (
                1 if row["batting_first_team"] == row["toss_winner"] else 0
            ),
            "team1_win": row["team1_win"],
        }

        if row["batting_first_team"] == row["team1"]:
            # Team 1 is batting first
            match_features["team1_defending_win_rate"] = team1.calc_win_rate_defending()
            match_features["team2_chasing_win_rate"] = team2.calc_win_rate_chasing()
        else:
            # Team 1 is chasing
            match_features["team1_chasing_win_rate"] = team1.calc_win_rate_chasing()
            match_features["team2_defending_win_rate"] = team2.calc_win_rate_defending()

        features.append(match_features)

    feature_df = pd.DataFrame(features)
    feature_df.to_csv("data/processed/feature_matrix.csv", index=False)
