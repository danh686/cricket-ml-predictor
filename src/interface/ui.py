import streamlit as st
from src.input.interface import (
    load_clean_match_data,
    get_teams_and_venues,
    load_model,
    build_match_features,
)
from src.objects.Team import Team
from src.objects.Venue import Venue


def run_ui():
    st.title("Cricket Match Win Predictor")
    st.write(
        "Select match details below. Features like team form or venue stats would be computed automatically behind the scenes."
    )

    league = st.selectbox("Select League", ["IPL", "BBL", "T20 Blast"])
    if league == "T20 Blast":
        league = "t20blast"
    match_data = load_clean_match_data(league)
    teams, venues = get_teams_and_venues(match_data)

    team1_selection = st.selectbox("Select Team 1", teams)
    team2_selection = st.selectbox(
        "Select Team 2", [t for t in teams if t != team1_selection]
    )
    venue_selection = st.selectbox("Select Venue", venues)

    toss_winner = st.selectbox("Who won the toss?", [team1_selection, team2_selection])
    toss_decision = st.radio("Toss decision", ["Bat", "Bowl"])

    team1 = Team(team1_selection, match_data)
    team2 = Team(team2_selection, match_data)
    venue = Venue(venue_selection, match_data)

    feature_df = build_match_features(
        team1, team2, venue, toss_winner=toss_winner, toss_decision=toss_decision
    )

    st.dataframe(feature_df)

    if st.button("Predict"):
        with st.spinner("Loading/training model..."):
            model = load_model(league)

        prob = model.predict_proba(feature_df)[0][1]
        st.success(
            f"Predicted probability of {team1_selection} winning: {round(prob * 100, 2)}%"
        )
