import json
import random
import streamlit as st
import pandas as pd
from utility import Person

server = "your_server_name"
database = "your_database_name"
def is_user_manager(userid):
    # check if loggedin user is owner of request or manager of the owner
    q = '''
    select   isnull(case when count(1)>=1 then 1 else 0 end,0) 'query that pass userid and return 1 if hes’ a manager else 0'
       FROM [BIZSCORE_BANKING_RECP].DBO.RECP_EMPLOYEE a
       join [BIZSCORE_BANKING_RECP].DBO.RECP_EMPLOYEE  b on b.Emp_Manager_Code=a.Employee_Bkey
       where b.Emp_Manager_Code='3880'--,'6010','3965'
    '''
    return bool(random.getrandbits(1))


def get_manager_info_for_user(user_id):
    query = f'''
        SELECT b.Employee_Bkey Manager_Id
        , SUBSTRING(b.Ldap_User_Ind,CHARINDEX('/',b.Ldap_User_Ind,1)+1,LEN(b.Ldap_User_Ind)) Manager_Username
        FROM [BIZSCORE_BANKING_RECP].DBO.RECP_EMPLOYEE a
        join [BIZSCORE_BANKING_RECP].DBO.RECP_EMPLOYEE b on a.Emp_Manager_Code=b.Employee_Bkey
        WHERE a.Employee_Bkey='3965'
    '''
    return 412, "Manager Name"

def get_departments():
    pass

def get_plan_dropdown(userid):

    myplans = ['100', '200', '300']

    return myplans
def get_plans(user_id):
    # d = run(""" select * from table whrere  user {rmcode} """)
    df = pd.read_csv('pages/plans.csv')
    return df

def get_rms_list(userid):
    q = '''   
        SELECT B.EMPLOYEE_BKEY AS USERID,
        SUBSTRING(B.LDAP_USER_IND,CHARINDEX('/',B.LDAP_USER_IND,1)+1,LEN(B.LDAP_USER_IND)) USERNAME
        FROM [BIZSCORE_BANKING_RECP].DBO.RECP_EMPLOYEE A
        JOIN [BIZSCORE_BANKING_RECP].DBO.RECP_EMPLOYEE  B ON B.EMP_MANAGER_CODE=A.EMPLOYEE_BKEY
        JOIN [BIZSCORE_BANKING_FINTELLIX].DBO.DIM_RELATIONSHIP_MANAGER C ON LEFT(RM_NAME,8)=SUBSTRING(B.LDAP_USER_IND,CHARINDEX('/',B.LDAP_USER_IND,1)+1,LEN(B.LDAP_USER_IND))
        WHERE B.EMP_MANAGER_CODE='2089'
    '''
    # run(select those rms based on userid)
    # df = []
    # rm_list = [{row['ID']: row['Name']} for _, row in df.iterrows()]
    result = [{11: "Ahmad Sammer"}, {22: "Jonny b"}, {33: "Omar c"}]
    return result

# user id is the rm_id registered on the request


def get_rm_clients(rmId):
    #not implemented
    clients = ['Omar', 'Boss', "Bose"]
    return clients




def fetch_client_data(cif):
    # fetch the values from DB as df
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

    data2 = [data]  # to convert to dataframe
    df = pd.DataFrame(data2)
    st.dataframe(df)
    # fetch the values from DB as df
    # data = run (select ...)
    return data



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

def get_reports(user_id):
    # d = run(""" select * from table whrere  user {rmcode} """)
    df = pd.read_csv('pages/callreports.csv')
    return df


def save_plan(data_object):
    params = list(data_object.values())
    print(params)
    # must pass data_light now to save into db
    # record_id = execute_stored_procedure(server, database, username, password, procedure_name, params=params):

    record_id = 3
    return record_id


def save_report_plan(data_object):
    params = list(data_object.values())
    print(params)
    record_id = 2
    return record_id


def get_plans_by_userid(userid):
    return ['100', '200', '300']


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


def get_report_by_id(userId, pk):
    #call stored procedure
    procedrue = '''
        Exec [dbo].[GetCallReportsByUser]
        @user_id = 10,
        @report_id = 1
    '''

    data = {
        "rm_id": "userId",
        "client_name": "client_name",
        "client_type": "client_type",
        "referenced_by": "referenced_by",
        "the_place": "the_place",
        "called_list": [
            {
                "name": "sdsd",
                "title": "sd"
            }
            , {
                "name": "sd",
                "title": "sd"
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


def view_plan_by_id(id):
    df = pd.read_csv("pages/plans.csv")
    return df


def view_report_by_id(id):
    df = pd.read_csv("pages/callreports.csv")
    return df
