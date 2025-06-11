import pandas as pd

class Team:
    def __init__(self, name:str, df:pd.DataFrame):
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
        pass

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
    
    def calc_head_to_head_win_rate(self, opposition:str, num_matches=4) -> float:
        """
        Calculate the win rate of the team against a given opposition in the last N encounters

        Parameters
        ---------
        num_matches: int, optional 
            Number of matches used to calculate the win %. Defaults to 4.         
        
        Returns 
        -------
        float
            Win % of the team against the opposition in the last N matches
        """
        pass

