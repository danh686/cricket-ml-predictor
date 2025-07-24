import pandas as pd

TEAM_FIXES = {
    "IPL": {
        "Royal Challengers Bangalore": "Royal Challengers Bengaluru",
        "Kings XI Punjab": "Punjab Kings",
        "Delhi Daredevils": "Delhi Capitals",
        "Rising Pune Supergiants": "Rising Pune Supergiant",
    },
    "t20blast": {
        "Birmingham Bears": "Warwickshire",
    },
}

VENUE_FIXES = {
    "IPL": {
        "M Chinnaswamy Stadium": "M. Chinnaswamy Stadium, Bengaluru",
        "M.Chinnaswamy Stadium": "M. Chinnaswamy Stadium, Bengaluru",
        "M Chinnaswamy Stadium, Bengaluru": "M. Chinnaswamy Stadium, Bengaluru",
        "Wankhede Stadium": "Wankhede Stadium, Mumbai",
        "Eden Gardens": "Eden Gardens, Kolkata",
        "MA Chidambaram Stadium": "MA Chidambaram Stadium, Chepauk, Chennai",
        "MA Chidambaram Stadium, Chepauk": "MA Chidambaram Stadium, Chepauk, Chennai",
        "Feroz Shah Kotla": "Arun Jaitley Stadium, Delhi",
        "Arun Jaitley Stadium": "Arun Jaitley Stadium, Delhi",
        "Rajiv Gandhi International Stadium": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "Rajiv Gandhi International Stadium, Uppal": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
        "Dr DY Patil Sports Academy": "Dr DY Patil Sports Academy, Mumbai",
        "Himachal Pradesh Cricket Association Stadium": "HPCA Stadium, Dharamsala",
        "Himachal Pradesh Cricket Association Stadium, Dharamsala": "HPCA Stadium, Dharamsala",
        "Punjab Cricket Association Stadium, Mohali": "IS Bindra Stadium, Mohali",
        "Punjab Cricket Association IS Bindra Stadium": "IS Bindra Stadium, Mohali",
        "Punjab Cricket Association IS Bindra Stadium, Mohali": "IS Bindra Stadium, Mohali",
        "Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh": "IS Bindra Stadium, Mohali",
        "Dr DY Patil Sports Academy": "Dr DY Patil Sports Academy, Mumbai",
        "Maharashtra Cricket Association Stadium": "Maharashtra Cricket Association Stadium, Pune",
        "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium": "ACA-VDCA Cricket Stadium, Visakhapatnam",
        "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam": "ACA-VDCA Cricket Stadium, Visakhapatnam",
        "Sawai Mansingh Stadium": "Sawai Mansingh Stadium, Jaipur",
        "Brabourne Stadium": "Brabourne Stadium, Mumbai",
        "Sheikh Zayed Stadium": "Zayed Cricket Stadium, Abu Dhabi",
        "Maharaja Yadavindra Singh International Cricket Stadium, New Chandigarh": "Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur",
    },
    "BBL": {
        "Brisbane Cricket Ground, Woolloongabba": "Brisbane Cricket Ground, Brisbane",
        "Brisbane Cricket Ground, Woolloongabba, Brisbane": "Brisbane Cricket Ground, Brisbane",
        "Brisbane Cricket Ground": "Brisbane Cricket Ground, Brisbane",
        "Western Australia Cricket Association Ground": "WACA Ground, Perth",
        "W.A.C.A. Ground": "WACA Ground, Perth",
        "Docklands Stadium, Melbourne": "Docklands Stadium",
        "Aurora Stadium, Launceston": "Aurora Stadium",
        "Bellerive Oval, Hobart": "Bellerive Oval",
        "Manuka Oval, Canberra": "Manuka Oval",
        "GMHBA Stadium, South Geelong, Victoria": "GMHBA Stadium",
        "International Sports Stadium, Coffs Harbour": "International Sports Stadium",
        "Aurora Stadium": "University of Tasmania Stadium, Launceston",
        "Simonds Stadium, South Geelong, Victoria": "GMHBA Stadium",
        "Aurora Stadium": "University of Tasmania Stadium, Launceston",
    },
    "t20blast": {
        "Grace Road": "Grace Road, Leicester",
        "Trent Bridge": "Trent Bridge, Nottingham",
        "Riverside Ground": "Riverside Ground, Chester-le-Street",
        "The Rose Bowl": "The Rose Bowl, Southampton",
        "Headingley": "Headingley, Leeds",
        "Lord's": "Lord's, London",
        "Old Trafford": "Old Trafford, Manchester",
        "Sophia Gardens": "Sophia Gardens, Cardiff",
        "St Lawrence Ground": "St Lawrence Ground, Canterbury",
        "Kennington Oval": "Kennington Oval, London",
        "College Ground": "College Ground, Cheltenham",
        "County Ground, New Road": "County Ground, New Road, Worcester",
        "Merchant Taylors' School Ground": "Merchant Taylors' School Ground, Northwood",
        "Queen's Park": "Queen's Park, Chesterfield",
        "Radlett Cricket Club": "Radlett Cricket Club, Radlett",
        "The Cooper Associates County Ground": "The Cooper Associates County Ground, Taunton",
        "Edgbaston": "Edgbaston, Birmingham",
        "The Kent County Cricket Ground": "The Kent County Cricket Ground, Beckenham",
        "Kent County Cricket Ground": "The Kent County Cricket Ground, Beckenham",
    },
}


def fix_team_and_venue_names(df: pd.DataFrame, league: str = "ipl") -> pd.DataFrame:
    """
    Standardizes team and venue names based on league-specific replacement dictionaries.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame containing match data.
    league : str, optional
        The name of the league (e.g., "ipl", "bbl"). Defaults to "ipl".

    Returns
    -------
    pandas.DataFrame
        The updated DataFrame with normalized team and venue names.
    """
    team_fix = TEAM_FIXES.get(league, {})
    venue_fix = VENUE_FIXES.get(league, {})

    for col in ["team1", "team2", "winner", "toss_winner"]:
        df[col] = df[col].replace(team_fix)

    df["venue"] = df["venue"].replace(venue_fix)

    if league == "t20blast":
        df = df[df["venue"] != "County Ground"]

    return df
