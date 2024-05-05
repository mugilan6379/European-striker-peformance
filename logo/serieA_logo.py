import streamlit as st

def serieALogo():
    css = """
        <style>
        img {
            width: 150px;  /* Adjust the width as needed */
            height: 200;  /* Adjust the height as needed */
            position: bottom;
            top: 100;
            left: 100;
            margin-top: -20px; /* Adjust this if necessary to align properly with the header */
        }
        header {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """

    st.sidebar.markdown(css, unsafe_allow_html=True)
    st.sidebar.image("https://media0.giphy.com/media/Q2uk5XNnlATqumoDF7/giphy.gif?cid=6c09b9525gflhmb6jpmf6j963cn3h257gcitmdu4v6yssiqu&ep=v1_internal_gif_by_id&rid=giphy.gif&ct=s")