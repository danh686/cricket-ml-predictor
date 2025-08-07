import streamlit as st
import hashlib
from src.input.interface import (
    load_clean_match_data,
    get_teams_and_venues,
    load_model,
    build_match_features,
)
from src.ml.predict import predict_from_row
from src.objects.Team import Team
from src.objects.Venue import Venue


def hash_inputs(*args):
    return hashlib.md5("".join(map(str, args)).encode()).hexdigest()


def run_ui():
    try:
        st.title("Cricket Match Win Predictor")
        st.write(
            "Select match details below. Features like team form or venue stats are be computed automatically behind the scenes."
        )

        league = st.selectbox("Select League", ["IPL", "BBL", "T20 Blast"])
        league = league.lower().replace(" ", "")

        match_data = load_clean_match_data(league)
        teams, venues = get_teams_and_venues(match_data)

        col1, col2 = st.columns(2)
        with col1:
            team1_selection = st.selectbox("Select Team 1", teams)
        with col2:
            team2_selection = st.selectbox(
                "Select Team 2", [t for t in teams if t != team1_selection]
            )

        col3, col4 = st.columns(2)
        with col3:
            venue_selection = st.selectbox("Select Venue", venues)
        with col4:
            toss_winner = st.selectbox(
                "Who won the toss?", [team1_selection, team2_selection]
            )

        toss_decision = st.radio("Toss decision", ["Bat", "Bowl"], horizontal=True)

        team1 = Team(team1_selection, match_data)
        team2 = Team(team2_selection, match_data)
        venue = Venue(venue_selection, match_data)

        feature_df = build_match_features(
            team1, team2, venue, toss_winner=toss_winner, toss_decision=toss_decision
        )

        input_hash = hash_inputs(
            league,
            team1_selection,
            team2_selection,
            venue_selection,
            toss_winner,
            toss_decision,
        )
        if "prediction_hash" not in st.session_state:
            st.session_state.prediction_hash = None
        if "probability" not in st.session_state:
            st.session_state.probability = None

        if st.button("Predict"):
            with st.spinner("Loading/training model..."):
                model = load_model(league)

            prob = predict_from_row(feature_df, model)
            st.session_state.probability = round(prob * 100, 2)
            st.session_state.prediction_hash = input_hash

        if st.session_state.probability is not None:
            prob_percent = st.session_state.probability
            st.progress(min(int(prob_percent), 100))

            col5, col6 = st.columns([1, 1])
            with col5:
                st.markdown(
                    f"{team1_selection} ({prob_percent}%)",
                )
            with col6:
                st.markdown(
                    f"<div style='text-align: right'>{team2_selection} ({100 - prob_percent:.2f}%)</div>",
                    unsafe_allow_html=True,
                )

            if input_hash != st.session_state.prediction_hash:
                st.caption(
                    "Prediction is based on previous inputs. Press 'Predict' to update."
                )
    except Exception as e:
        st.error(f"Something went wrong: {e}")
