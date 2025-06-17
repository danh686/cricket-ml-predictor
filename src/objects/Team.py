import pandas as pd
import numpy as np


class Team:
    def __init__(self, name: str, df: pd.DataFrame):
        self.name = name
        self.df = df

    def calc_recent_form(self, num_matches=5) -> float:
        """
        Calculate the win % of the team in their last N matches

        Parameters
        ----------
        num_matches: int, optional
            Number of matches used to calculate recent form. Defaults to 5.

        Returns
        -------
        float
            Win % of the team in their last N matches
        """
        df = self.df.sort_values(by="date", ascending=False)

        df = df[(df["team1"] == self.name) | (df["team2"] == self.name)]
        num_matches = min(num_matches, len(df))

        if num_matches == 0:
            return np.nan

        recent_matches = df.head(num_matches)
        win_rate = (((recent_matches["winner"] == self.name).sum()) / num_matches) * 100

        return win_rate

    def calc_win_rate_defending(self, num_matches=5) -> float:
        """
        Calculate the win rate of the team in the last N matches they bat first in.

        Parameters
        ----------
        num_matches: int, optional
            Number of matches used to calculate the win %. Defaults to 5.

        Returns
        -------
        float
            Win % of the team the last N times they have batted first
        """
        pass

    def calc_win_rate_chasing(self, num_matches=5) -> float:
        """
        Calculate the win rate of the team in the last N matches they bowl first in.

        Parameters
        ----------
        num_matches: int, optional
            Number of matches used to calculate the win %. Defaults to 5.

        Returns
        -------
        float
            Win % of the team the last N times they have bowled first
        """
        pass

    def calc_head_to_head_win_rate(self, opposition: str, num_matches=5) -> float:
        """
        Calculate the win rate of the team against a given opposition in the last N encounters

        Parameters
        ---------
        opposition: str
            The opposition used for the head to head win rate
        num_matches: int, optional
            Number of matches used to calculate the win %. Defaults to 5.

        Returns
        -------
        float
            Win % of the team against the opposition in the last N matches
        """
        pass

    def calc_venue_win_rate(self, venue: str, num_matches=5) -> float:
        """
        Calculate the win rate of the team at a given venue in the last N matches they have played there

        Parameters
        ----------
        venue:str
            The venue to calculate the win rate for
        num_matches: int, optional
            Number of matches used to calculate the win %. Defaults to 5.

        Returns
        -------
        float
            Win % of the team at a given venue
        """
        pass

    def get_name(self):
        return self.name

    def set_df(self, new_df: pd.DataFrame):
        self.df = new_df
