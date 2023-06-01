import json
import random
import streamlit as st
import pandas as pd
from utility import  Person

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
    #fetch the values from DB
    cn = st.session_state.client_name = "Ericson Telecom"
    sot = st.session_state.client_SOT = "4000"
    out = st.session_state.client_outstanding = "Some outstanding data fetched"
    data = {
        'Client CIF': cif,
        'Client Name': cn,
        'Client SOT': sot,
        'Client Outstanding': out
    }

    data2 = [data] #to convert to dataframe
    df = pd.DataFrame(data2)
    st.dataframe(df)
    return data


def save_plan():
    # save into db
    pass


def save_report_plan(reportPlanObject):
    pass


def get_plan_by_id(id):
    data = {
        "rm_id": "0054556",
        "client_name": "st.session_state.client_name",
        "client_cif": "client_cif",
        "client_sot": "client_SOT",
        "client_outstanding": "client_outstanding",
        "purpose": "Purpose 2",
        "expected_call_date": "2023-05-30",
        "create_date": "02-01-2019",
        "created_by": "Me!"
    }

    json_data = json.dumps(data)
    return json_data



def getStaffList():
    person_list_1 = [
        Person("John Doe", "Manager", "MIS", "123123123"),
        Person("Jane Smith", "Engineer", "MIS", "123123123"),
        Person("Mike Johnson", "Analyst", "MIS" ,"123123123")
    ]
    return person_list_1
def getClientsList():
    person_list_2 = [
        Person("Alice Johnson", "Designer","MIS","123123123"),
        Person("Mark Davis", "Developer","MIS","123123123"),
        Person("Emily Brown", "Project Manager","MIS","123123123")
    ]
    return person_list_2

