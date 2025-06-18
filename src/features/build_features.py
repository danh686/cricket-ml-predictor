from src.objects.Venue import Venue
from src.objects.Team import Team
import pandas as pd


def build_feature_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generates a feature matrix from a processed DataFrame of match data.

    Parameters
    ----------
    df: pandas.DataFrame
        Preprocessed match data.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing one row per match and engineered features for modeling.
    """

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
            "team1_chasing_win_rate": team1.calc_win_rate_chasing(),
            "team1_defending_win_rate": team1.calc_win_rate_defending(),
            "team2_chasing_win_rate": team2.calc_win_rate_chasing(),
            "team2_defending_win_rate": team2.calc_win_rate_defending(),
            "venue_chasing_win_rate": venue.calc_win_rate_chasing(),
            "venue_defending_win_rate": venue.calc_win_rate_defending(),
            "team1_vs_team2_record": team1.calc_head_to_head_win_rate(team2.get_name()),
            "toss_winner": 1 if row["toss_winner"] == row["team1"] else 0,
            "toss_decision_bat": (
                1 if row["batting_first_team"] == row["toss_winner"] else 0
            ),
            "team1_win": row["team1_win"],
        }

        features.append(match_features)

    feature_df = pd.DataFrame(features)

    return feature_df
