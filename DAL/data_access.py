import random
import streamlit as st
import pandas as pd


def is_user_manager(userid):
    return bool(random.getrandbits(1))


def get_purpose_options():
    return ["Purpose 1", "Purpose 2", "Purpose 3"]


def load_data(file):
    data1 = pd.read_csv(file)
    return data1


def get_rm_clients(rmId):
    clients = ['Omar', 'Boss', "Bose"]
    return clients


def get_rms_list(userid):
    # get the list from somewhere
    # CHOICES = {1: "dataset a", 2: "dataset b", 3: "dataset c"}
    # selected_rm = st.selectbox("Select option", CHOICES.keys(), format_func = lambda x: CHOICES[x])
    # st.write(f"You selected option {selected_rm} ")
    result = [{11: "dataset a"}, {22: "dataset b"}, {33: "dataset c"}]
    return result


def fetch_client_data(cif):
    cn = st.session_state.client_name = "Ericson Telecom"
    sot = st.session_state.client_SOT = "4000"
    out = st.session_state.client_outstanding = "Some outstanding data fetched"
    data = {
        'Client CIF': [cif],
        'Client Name': [cn],
        'Client SOT': [sot],
        'Client Outstanding': [out]
    }
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)
    st.dataframe(df)


def save_plan():
    # save into db
    pass


def save_report_plan(reportPlanObject):
    pass
