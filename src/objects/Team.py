import pandas as pd
import numpy as np


class Team:
    def __init__(self, name: str, df: pd.DataFrame):
        self.name = name
        self.df = df
        self.min_matches = 2

    def _calculate_win_rate(self, df: pd.DataFrame, num_matches: int) -> float:
        """
        Calculate the win rate (%) of the team in a filtered DataFrame.

        Parameters
        ----------
        df: pandas.DataFrame
            The filtered DataFrame to calculate the win rate on.
        num_matches: int
            Number of recent matches to include.

        Returns
        -------
        float
            Win percentage of the team over the selected matches. Returns np.nan if no matches.
        """
        df = df.sort_values(by="date", ascending=False)
        num_matches = min(num_matches, len(df))
        if num_matches < self.min_matches:
            return np.nan

        recent_matches = df.head(num_matches)
        win_rate = ((recent_matches["winner"] == self.name).sum()) / num_matches

        return round(win_rate, 5)

    def calc_recent_form(self, num_matches: int = 5) -> float:
        """
        Calculate the win rate (%) of the team in their last N matches.

        Parameters
        ----------
        num_matches: int, optional
            Number of recent matches to include. Defaults to 5.

        Returns
        -------
        float
            Win percentage of the team over the selected matches. Returns np.nan if no matches.
        """
        df = self.df
        df = df[(df["team1"] == self.name) | (df["team2"] == self.name)]

        return self._calculate_win_rate(df, num_matches)

    def calc_win_rate_defending(self, num_matches: int = 5) -> float:
        """
        Calculate the win rate (%) of the team in the last N matches they bat first in.

        Parameters
        ----------
        num_matches: int, optional
            Number of matches used to calculate the win %. Defaults to 5.

        Returns
        -------
        float
            Win percentage of the team over the matches they bat first in. Returns np.nan if no matches.
        """
        df = self.df
        df = df[(df["team1"] == self.name) | (df["team2"] == self.name)]
        df = df[(df["batting_first_team"] == self.name)]

        return self._calculate_win_rate(df, num_matches)

    def calc_win_rate_chasing(self, num_matches: int = 5) -> float:
        """
        Calculate the win rate (%) of the team in the last N matches they bowl first in.

        Parameters
        ----------
        num_matches: int, optional
            Number of matches used to calculate the win %. Defaults to 5.

        Returns
        -------
        float
            Win percentage of the team over the matches they bowl first in. Returns np.nan if no matches.
        """
        df = self.df
        df = df[(df["team1"] == self.name) | (df["team2"] == self.name)]
        df = df[(df["batting_first_team"] != self.name)]

        return self._calculate_win_rate(df, num_matches)

    def calc_head_to_head_win_rate(
        self, opposition: str, num_matches: int = 5
    ) -> float:
        """
        Calculate the win rate (%) of the team against a given opposition in the last N encounters.

        Parameters
        ---------
        opposition: str
            The opposition used for the head to head win rate
        num_matches: int, optional
            Number of matches used to calculate the win %. Defaults to 5.

        Returns
        -------
        float
            Win percentage of the team against the selected opposition. Returns np.nan if no matches.
        """
        df = self.df
        df = df[(df["team1"] == self.name) | (df["team2"] == self.name)]
        df = df[(df["team1"] == opposition) | (df["team2"] == opposition)]

        return self._calculate_win_rate(df, num_matches)

    def calc_venue_win_rate(self, venue: str, num_matches: int = 5) -> float:
        """
        Calculate the win rate (%) of the team at a given venue in the last N matches they played there.

        Parameters
        ----------
        venue:str
            The venue to calculate the win rate for
        num_matches: int, optional
            Number of matches used to calculate the win %. Defaults to 5.

        Returns
        -------
        float
            Win percentage of the team at a selected venue. Returns np.nan if no matches.
        """
        df = self.df
        df = df[(df["team1"] == self.name) | (df["team2"] == self.name)]
        df = df[(df["venue"] == venue)]

        return self._calculate_win_rate(df, num_matches)

    def get_name(self):
        return self.name

    def set_df(self, new_df: pd.DataFrame):
        self.df = new_df
