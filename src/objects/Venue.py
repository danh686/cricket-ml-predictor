import pandas as pd

class Venue:
    def __init__(self, name:str, df:pd.DataFrame):
        self.name = name
        self.df = df

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
        pass

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
        pass

