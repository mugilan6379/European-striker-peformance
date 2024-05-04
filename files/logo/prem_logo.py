import streamlit as st

def premLogo():
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
    st.sidebar.image("https://media.tenor.com/2aQYQ9w8I58AAAAi/premier-league.gif")