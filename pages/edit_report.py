import json
from pathlib import Path
import pandas as pd
from DAL.data_access import get_rm_clients, get_report_by_id
from common import *
import streamlit as st

from utility import Person, person_to_dict

general_settings()

staff_list = []
if 'person_list' not in st.session_state:
    st.session_state.person_list = []
token = get_query_param_by_name('token')
userId, token_expiry, username = get_user_claims(token)

st.markdown(f"<h2 style=\"color:{COLOR_DARK_YELLOW};\">"
            "<i class=\"fas fa-wrench\"></i> Under Construction"
            "</h2>", unsafe_allow_html=True)


def report_plan_json(
        client_name, client_type, referenced_by, the_place
        , calledOnList, callingList, call_objective, points_of_discusstion, actionable_items
        , create_date, created_by, call_start, call_end, next_call):
    called_list = [person_to_dict(person) for person in calledOnList]
    calling_list = [person_to_dict(person) for person in callingList]
    data = {
        "rm_id": userId,
        "client_name": client_name,
        "client_type": client_type,
        "referenced_by": referenced_by,
        "the_place": the_place,
        "called_list": called_list,
        "calling_list": calling_list,
        "call_objective": call_objective,
        "points_of_discusstion": points_of_discusstion,
        "actionable_items": actionable_items,
        "create_date": create_date,
        "created_by": created_by,
        "call_start": call_start,
        "call_end": call_end,
        "next_call": next_call
    }

    return json.dumps(data)


def render_edit_report():
    extracted_id = get_query_param_by_name('id')
    plan_data = get_report_by_id(extracted_id)
    record = json.loads(plan_data)
    st.markdown(f"<h3>Client Details</h3>", unsafe_allow_html=True)




    client_name = st.text_input("Client's Name", value='client name', disabled=True)
    st.markdown(f"<h3>Report Details 📋</h3>", unsafe_allow_html=True)

    r1c1, r1c2 = st.columns(2)
    report_date = r1c1.date_input("Event Date", key="rep_date", min_value=datetime.today(),
                                  value=datetime.now())
    referenced_by = r1c2.text_input("Prospect Referenced By :", value='ref by')

    st.markdown(f"<h3>Call Details 📞</h3>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with st.container():
        call_date_start = c1.date_input("Call Start", key="call_datetime1", min_value=datetime.today())
        call_time_start = c2.time_input("Call Time", key="jjh", label_visibility="hidden", value=None)
        # st.write(str(call_date_start)+" "+str(call_time_start))
        call_start = str(call_date_start) + " " + str(call_time_start)
        call_date_end = c3.date_input("Call end", key="call_datetime3", min_value=datetime.today())
        call_time_end = c4.time_input("Call end", key="call_datetime4", label_visibility="hidden")
        # st.write(str(call_date_end) + " " + str(call_time_end))
        call_end = str(call_date_end) + " " + str(call_time_end)

    the_place = st.text_input("Place", value='Riyad')
    # Create a two-column layout
    st.markdown(f"<h3>Clients/Staff List Details 📋</h3>", unsafe_allow_html=True)
    st.markdown("<p>Please use the template below to fill the list then upload it.</p>",
                unsafe_allow_html=True)
    st.download_button(
        "👉 People List Template 📝", Path("pages/plans.csv").read_text(), "plans.csv"
    )
    col1, col2 = st.columns(2)
    # Column 1
    with col1:
        st.header("Clients List")
        # upload the list
        uploaded_file = st.file_uploader("Upload a CSV file for called on List", type="csv", key="fupload1")
        # Check if a file was uploaded
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.dataframe(df)

            for index, row in df.iterrows():
                person = Person(row['name'], row['title'], row['department'], row['phone'])
                st.session_state.person_list.append(person)

    # Column 2
    with col2:
        st.header("Staff Officers List")
        uploaded_file = st.file_uploader("Upload a CSV file for called on List", type="csv", key="fupload2")
        # Check if a file was uploaded
        if uploaded_file is not None:
            # Read the uploaded CSV file
            df = pd.read_csv(uploaded_file)
            st.dataframe(df)

            for index, row in df.iterrows():
                staff = Person(row['name'], row['title'], row['department'], row['phone'])
                staff_list.append(staff)

    st.markdown(f"<h3>Agenda Details 📒</h3>", unsafe_allow_html=True)
    call_objective = st.text_area("Objective of the call", height=100, value="call pbjective")
    points_of_discusstion = st.text_area("Points of Discussion", height=100, value="points of discusion")
    actionable_items = st.text_area("Actionable Items", height=100, value="acional items")

    c1, c2 = st.columns(2)
    with st.container():
        next_call_date = c1.date_input("Next Call Date", key="nxtd", min_value=datetime.today())
        next_call_time = c2.time_input("Call Time", key="nxtt", label_visibility="hidden", value=None)

    next_call = str(next_call_date) + " " + str(next_call_time)

    submit_report = st.button(label='Update')
    if submit_report:
        # st.write("ok")
        json_obj = report_plan_json(
            "client_name",
            "client_type",
            "referenced_by",
            "the_place"
            , st.session_state.person_list
            , staff_list,
            call_objective, points_of_discusstion, actionable_items
            , str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            , "Moubien"
            , "call_start"
            , "call_end"
            , "next_call"
        )
        st.json(json_obj)


# only if authorized open the page
is_authorized(render_edit_report)
