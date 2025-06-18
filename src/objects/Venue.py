import pandas as pd
import numpy as np


class Venue:
    def __init__(self, name: str, df: pd.DataFrame):
        self.name = name
        self.df = df

    def _calculate_win_rate(
        self, df: pd.DataFrame, num_matches: int, mode: str
    ) -> float:
        """
        Calculate the win rate (%) of teams at the venue given they are defending or chasing

        Parameters
        ----------
        df: pandas.DataFrame
            The filtered DataFrame that includes the relevant matches.
        num_matches: int
            Number of recent matches to include.
        mode: str
            Mode of win rate calculation - either 'chasing' or 'defending'

        Returns
        -------
        float
            Win percentage of the team over the selected matches. Returns np.nan if no matches.
        """
        if mode not in ["defending", "chasing"]:
            raise ValueError(
                f"Invalid mode '{mode}'. Must be 'defending' or 'chasing'."
            )

        df = df[(df["venue"] == self.name)]
        df = df.sort_values(by="date", ascending=False)

        num_matches = min(num_matches, len(df))
        if num_matches == 0:
            return np.nan

        recent_matches = df.head(num_matches)

        if mode == "defending":
            win_rate = (
                (recent_matches["batting_first_team"] == recent_matches["winner"]).sum()
                / num_matches
            ) * 100
        elif mode == "chasing":
            win_rate = (
                (recent_matches["batting_first_team"] != recent_matches["winner"]).sum()
                / num_matches
            ) * 100

        return round(win_rate, 2)

    def calc_win_rate_defending(self, num_matches=10) -> float:
        """
        Calculate the win rate of teams batting first at the venue in the last N matches

        Parameters
        ----------
        num_matches: int, optional
            Number of matches used to calculate the win %. Defaults to 10.

        Returns
        -------
        float
            Win % of teams batting first in the last N matches at the venue
        """
        return self._calculate_win_rate(self.df, num_matches, mode="defending")

    def calc_win_rate_chasing(self, num_matches=10) -> float:
        """
        Calculate the win rate of teams bowling first at the venue in the last N matches

        Parameters
        ----------
        num_matches: int, optional
            Number of matches used to calculate the win %. Defaults to 10.

        Returns
        -------
        float
            Win % of teams bowling first in the last N matches at the venue
        """
        return self._calculate_win_rate(self.df, num_matches, mode="chasing")

    def get_name(self):
        return self.name

    def set_df(self, new_df: pd.DataFrame):
        self.df = new_df
