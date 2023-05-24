import streamlit as st

def general_settings():
    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
    st.markdown(
        """
        <head>
            <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" rel="stylesheet">
        </head>
        """,
        unsafe_allow_html=True
    )