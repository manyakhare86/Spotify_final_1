import pandas as pd
import numpy as np
import pickle
import streamlit as st

model = pickle.load(open("C:/Users/manya/PycharmProjects/celebal/Spotify/model.sav", "rb"))


def stream_pred(input_data):
    prediction = model.best_estimator_.predict([input_data])
    return prediction


def main():

    st.title("Stream prediction")

    artist_count = st.text_input("Total no of artist")
    released_year = st.text_input("In which year was song released")
    released_month = st.text_input("In which month was song released")
    released_day = st.text_input("On what was song released")
    in_spotify_playlists = st.text_input("In spotify playlist")
    in_spotify_charts = st.text_input("In spotify charts")
    in_apple_playlists = st.text_input("In apple playlist")
    in_apple_charts = st.text_input("In apple charts")
    in_deezer_playlists = st.text_input("In deezer playlist")
    in_deezer_charts = st.text_input("In deezer charts")
    bpm = st.text_input("Beats per minute")
    danceability_forML = st.text_input("Dancebility percentage")
    valence_forML = st.text_input("Valence percentage")
    energy_forML = st.text_input("Energy percentage")
    acousticness_forML = st.text_input("Acousticness percentage")
    instrumentalness_forML = st.text_input("Instrumental Percentage")
    liveness_forMl = st.text_input("Liveness percentage")
    speechiness_forMl = st.text_input("Speechiness percentage")
    key_encoded = st.text_input("Key")

    stream = ""

    if st.button("Get Total Streams"):
        stream = stream_pred([artist_count, released_year, released_month, released_day,
                              in_spotify_playlists, in_spotify_charts, in_apple_playlists,
                              in_apple_charts, in_deezer_playlists, in_deezer_charts, bpm,
                              danceability_forML, valence_forML, energy_forML, acousticness_forML,
                              instrumentalness_forML, liveness_forMl, speechiness_forMl, key_encoded])

    st.success(stream)


if __name__=="__main__":
    main()




