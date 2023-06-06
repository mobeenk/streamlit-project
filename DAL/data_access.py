import json
import random
import streamlit as st
import pandas as pd
from utility import  Person

def is_user_manager(userid):
    #check if loggedin user is owner of request or manager of the owner

    return bool(random.getrandbits(1))

def get_plans_by_userid(userid):
    return ['100', '200', '300']
def get_departments():
    pass




def load_data(file):
    #d = run(""" select * from table whrere  user {rmcode} """)
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
    result = [{11: "Ahmad Sammer"}, {22: "Jonny b"}, {33: "Omar c"}]
    return result


def fetch_client_data(cif):
    #fetch the values from DB
    cn = st.session_state.client_name = "Ericson Telecom"
    sot = st.session_state.client_SOT = "100000"
    out = st.session_state.client_outstanding = "Some outstanding data fetched"
    cr = st.session_state.client_cr = "53342342332"
    risk_rating = st.session_state.client_risk_rating = 6
    data = {
        'Client CIF': cif,
        'Client Name': cn,
        'Client SOT': sot,
        'Client Outstanding': out,
        "Risk Rating": risk_rating
    }

    data2 = [data] #to convert to dataframe
    df = pd.DataFrame(data2)
    st.dataframe(df)
    return data


def save_plan():
    # save info into DB and return the record id
    record_id = 3
    return record_id


def save_report_plan(reportPlanObject):
    #save info into DB and return the record id
    record_id = 2
    return record_id


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


def get_report_by_id(id):
    data = {
        "rm_id": "userId",
        "client_name": "client_name",
        "client_type": "client_type",
        "referenced_by": "referenced_by",
        "the_place": "the_place",
        "called_list": [
                            {
                            "name":"sdsd",
                            "title":"sd"
                            }
                            ,{
                            "name":"sd",
                            "title":"sd"
                            }
                     , {
                    "name": "sd",
                    "title": "sd"
                }
        ],
        "calling_list": [
            {
                "name": "staff1",
                "title": "CEO"
            }
            , {
                "name": "Staff2",
                "title": "M"
            }
        ],
        "call_objective": "call_objective",
        "points_of_discusstion": "points_of_discusstion",
        "actionable_items": "actionable_items",
        "create_date": "2023-01-01",
        "created_by": "Moubien",
        "call_start": "2023-01-01",
        "call_end": "2023-01-01",
        "next_call": "2023-01-01"
    }

    json_data = json.dumps(data)
    return json_data
def getStaffList():
    person_list_1 = [
        Person("John Doe", "Manager"),
        Person("Jane Smith", "Engineer"),
        Person("Mike Johnson", "Analyst"),
        Person("John Doe", "Manager"),
        Person("Jane Smith", "Engineer"),
        Person("Mike Johnson", "Analyst")
    ]
    return person_list_1
def getClientsList():
    person_list_2 = [
        Person("Alice Johnson", "Designer"),
        Person("Mark Davis", "Developer"),
        Person("Emily Brown", "Project Manager")
    ]
    return person_list_2


def view_plan_by_id(id):
    df = pd.read_csv("pages/plans.csv")
    return df


def view_report_by_id(id):
    df = pd.read_csv("pages/callreports.csv")
    return df


def get_manager_info_for_user(user_id):
    return 412, "Manager Name"


