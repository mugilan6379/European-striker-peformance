
import streamlit as st
def bundesligaLogo():
    css = """
        <style>
        img {
            width: 20;  
            height: 10;  
            position: bottom;
            top: 50;
            left: 50;
            margin-top: -20px; /* Adjust this if necessary to align properly with the header */
        }
        header {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """

    st.sidebar.markdown(css, unsafe_allow_html=True)
    st.sidebar.image("https://i.gifer.com/origin/00/0082b693dcb25d3446bbd2d1d8641ca4_w200.webp")