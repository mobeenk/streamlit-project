import streamlit as st



PLAN_ADD_URL = "http://localhost:8502/view_plan?q="
PLAN_EDIT_URL = "http://localhost:8502/view_plan?q="
PLAN_REMOVE_URL = "http://localhost:8502/remove?q="

CALLREPORT_ADD_URL = "http://localhost:8502/view_report?q="
CALLREPORT_EDIT_URL = "http://localhost:8502/view_report?q="
CALLREPORT_REMOVE_URL = "http://localhost:8502/remove?q="
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



