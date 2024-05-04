import streamlit as st

def ligue2Logo():
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
    st.sidebar.image("https://media4.giphy.com/media/xauvJRS2UZap7hwgKM/giphy.gif?cid=6c09b952wfv5qkx4njx8icjg26futrwynxvs5inyfh5iccea&ep=v1_internal_gif_by_id&rid=giphy.gif&ct=s")