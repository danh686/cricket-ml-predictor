import pandas as pd


def load_ipl_matches(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    # Standardise team names
    TEAM_NAME_FIX = {
        "Royal Challengers Bangalore": "Royal Challengers Bengaluru",
        "Kings XI Punjab": "Punjab Kings",
        "Delhi Daredevils": "Delhi Capitals",
        "Rising Pune Supergiants": "Rising Pune Supergiant",
    }
    for col in ["team1", "team2", "winner", "toss_winner"]:
        df[col] = df[col].replace(TEAM_NAME_FIX)

    VENUE_NAME_FIX = {
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
    }

    df["venue"] = df["venue"].replace(VENUE_NAME_FIX)

    return df
