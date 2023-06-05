import streamlit as st
# from CallReports2 import get_jwt_token
from jwt_generator import *
from DAL.data_access import is_user_manager

# JWT_TOKEN = get_jwt_token()
BASE_URL = "http://localhost:8502"
TOKEN_KEY = "'your_secret_key'"
COLOR_DARK_YELLOW = "#C09C20"
def view_plan_url(token):
    return f"{BASE_URL}/view_plan?token={token}&id="


def edit_plan_url(token):
    return f"{BASE_URL}/edit_plan?token={token}&id="


def view_report_url(token):
    return f"{BASE_URL}/view_report?token={token}&id="


def edit_report_url(token):
    return f"{BASE_URL}/edit_report?token={token}&id="


# PLAN_REMOVE_URL = "http://localhost:8502/remove?q="
def get_query_param_by_name(query_param_name):
    qid = st.experimental_get_query_params()
    token = (qid[query_param_name][0])
    return token


def get_user_claims(token):
    isValid = is_valid_jwt(token, "your_secret_key")
    print('is valid jwt: '+ token)
    print(isValid)
    if isValid == True:
        user_id = read_jwt_token(token)[0]
        # token_expiry_date = datetime.fromtimestamp(read_jwt_token(token)[1])
        return user_id, read_jwt_token(token)[1], read_jwt_token(token)[2]
    else:
        return None, None, None


# CALLREPORT_REMOVE_URL = "http://localhost:8502/remove?q="
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


def session_settings(loggedUserId):
    if 'is_manager' not in st.session_state:
        st.session_state.is_manager = False
        st.session_state.is_manager = is_user_manager(loggedUserId)
    if 'client_name' not in st.session_state:
        st.session_state.client_name = ""
    if 'client_SOT' not in st.session_state:
        st.session_state.client_SOT = ""
    if 'client_outstanding' not in st.session_state:
        st.session_state.client_outstanding = ""
    if 'client_ref' not in st.session_state:
        st.session_state.client_ref = ""
    if 'client_cr' not in st.session_state:
        st.session_state.client_cr = ""
    if 'client_risk_rating' not in st.session_state:
        st.session_state.client_risk_rating = 0


def page_settings():
    # Hide the hamburger icon
    hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
         #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-uf99v8.egzxvld5 > div.block-container.css-z5fcl4.egzxvld4 > div:nth-child(1) > div > div.css-ybnenh.e1s6o5jp0 > ul > li > div.st-am.st-cm.st-cg.st-ch.st-ci > div > div:nth-child(1) > div > div.css-ocqkz7.e1tzin5v3 > div:nth-child(2) > div:nth-child(1) > div
        {margin-top:0px;}
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-uf99v8.egzxvld5 > div.block-container.css-z5fcl4.egzxvld4 > div:nth-child(1) > div > div.css-ybnenh.e1s6o5jp0 > ul > li > div.streamlit-expanderHeader.st-ae.st-by.st-ag.st-ah.st-ai.st-aj.st-bz.st-c0.st-c1.st-c2.st-c3.st-c4.st-c5.st-ar.st-as.st-b6.st-b5.st-b3.st-c6.st-c7.st-c8.st-b4.st-c9.st-ca.st-cb.st-cc.st-cd > div > p
        { font-size: 22px !important; font-weight: bold !important; }
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-uf99v8.egzxvld5 > div.block-container.css-z5fcl4.egzxvld4 > div:nth-child(1) > div
        { margin-top:-60px; }
        </style>
        """
    st.markdown(hide_menu_style, unsafe_allow_html=True)


def is_token_expired(token_expiry):
    if token_expiry is not None:
        token_expiry_date = datetime.fromtimestamp(token_expiry)
    isExpired = token_expiry < int(round(datetime.now().timestamp()))


from navbar import notfound_page
from jwt_generator import is_valid_jwt


def is_authorized(exce_func):
    token = get_query_param_by_name('token')
    # print('my token\n'+token)
    try:
        userId, token_expiry, username = get_user_claims(token)
        # print(userId)
        # print(token_expiry)
        if not is_valid_jwt(token, TOKEN_KEY):
            st.markdown(notfound_page("Unauthorized-401"), unsafe_allow_html=True)
            print('not valid token')
            return None
        elif token_expiry is None:
            st.markdown(notfound_page("Session Expired"), unsafe_allow_html=True)
            return None
        else:
            exce_func()
            return 1

    except Exception as e:
        # Exception handling code
        print("An error occurred:", str(e))



