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
if 'btn_submit_report' not in st.session_state:
    st.session_state.btn_submit_report = False
if 'person_list' not in st.session_state:
    st.session_state.person_list = []
if 'staff_list' not in st.session_state:
    st.session_state.staff_list = []

token = get_query_param_by_name('token')
userId, token_expiry, username = get_user_claims(token)

st.markdown(f"<h2 style=\"color:{COLOR_DARK_YELLOW};\">"
            "<i class=\"fas fa-wrench\"></i> Under Construction"
            "</h2>", unsafe_allow_html=True)


def report_plan_json(
        plan_id, the_place
        , calledOnList, callingList, call_objective, points_of_discusstion, actionable_items
        , create_date, created_by, call_start, next_call, from_department, report_date):
    called_list = [person_to_dict(person) for person in calledOnList]
    calling_list = [person_to_dict(person) for person in callingList]
    data = {
        "rm_id": userId,
        "plan_id": plan_id,
        "the_place": the_place,
        "called_list": called_list,
        "calling_list": calling_list,
        "call_objective": call_objective,
        "points_of_discusstion": points_of_discusstion,
        "actionable_items": actionable_items,
        "create_date": create_date,
        "created_by": userId,
        "call_start": call_start,
        "next_call": next_call,
        "from_department": from_department,
        "report_date": report_date,
        "status": "New"
    }

    return json.dumps(data)


def render_edit_report():

    extracted_id = get_query_param_by_name('id')
    plan_data = get_report_by_id(extracted_id)
    record = json.loads(plan_data)
    st.markdown(f"<h3>Client Details</h3>", unsafe_allow_html=True)
    with st.form('myform'):
        plan_id = st.selectbox("Select Plan Id", ['100', '200', '300'])

        r1c1, r1c2 = st.columns(2)
        report_date = r1c1.date_input("Report Date", key="rep_date", min_value=datetime.today(),
                                      value=datetime.now())
        from_department = r1c2.text_input("Department", value='IT')
        # referenced_by = r1c2.text_input("Prospect Referenced By :", value='ref by')

        # st.markdown(f"<h3>Call Details 📞</h3>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with st.container():
            call_date_start = c1.date_input("Call Start", key="call_datetime1", min_value=datetime.today())
            call_time_start = c2.time_input("Call Time", key="jjh", label_visibility="hidden", value=None)
            call_start = str(call_date_start) + " " + str(call_time_start)
            the_place = c3.text_input("Venue", value='Riyad')
        # st.markdown(f"<h3>Clients/Staff List Details 📋</h3>", unsafe_allow_html=True)
        # st.download_button( "👉 People List Template 📝", Path("pages/plans.csv").read_text(), "plans.csv")
        col_clients, col_staff = st.columns(2)
        # Column 1
        client_name1 = ""
        client_name2 = ""
        client_name3 = ""
        client_name4 = ""
        client_name5 = ""
        client_title1 = ""
        client_title2 = ""
        client_title3 = ""
        client_title4 = ""
        client_title5 = ""

        staff_name1 = ""
        staff_name2 = ""
        staff_name3 = ""
        staff_name4 = ""
        staff_name5 = ""
        staff_title1 = ""
        staff_title2 = ""
        staff_title3 = ""
        staff_title4 = ""
        staff_title5 = ""
        with col_clients:
            st.markdown("<p>Clients list</p>", unsafe_allow_html=True)
            c, c1, c2 = st.columns([1, 7, 7])
            with c:
                st.markdown("<p style='margin: 5px;'>#</p>", unsafe_allow_html=True)
                st.markdown("<p style='margin: 15px;'>1</p>", unsafe_allow_html=True)
                st.markdown("<p style='margin: 13px;'>2</p>", unsafe_allow_html=True)
                st.markdown("<p style='margin: 14px;'>3</p>", unsafe_allow_html=True)
                st.markdown("<p style='margin: 14px;'>4</p>", unsafe_allow_html=True)
                st.markdown("<p style='margin: 14px;'>5</p>", unsafe_allow_html=True)

            with c1:
                st.markdown("<p>Name</p>", unsafe_allow_html=True)
                client_name1 = st.text_input("", value='', key="cn1", label_visibility="collapsed")
                client_name2 = st.text_input("", value='', key="cn2", label_visibility="collapsed")
                client_name3 = st.text_input("", value='', key="cn3", label_visibility="collapsed")
                client_name4 = st.text_input("", value='', key="cn4", label_visibility="collapsed")
                client_name5 = st.text_input("", value='', key="cn5", label_visibility="collapsed")

            with c2:
                st.markdown("<p>Designation</p>", unsafe_allow_html=True)
                client_title1 = st.text_input("", value='', key="ct1", label_visibility="collapsed")
                client_title2 = st.text_input("", value='', key="ct2", label_visibility="collapsed")
                client_title3 = st.text_input("", value='', key="ct3", label_visibility="collapsed")
                client_title4 = st.text_input("", value='', key="ct4", label_visibility="collapsed")
                client_title5 = st.text_input("", value='', key="ct5", label_visibility="collapsed")

        with col_staff:
            st.markdown("<p>Staff list</p>", unsafe_allow_html=True)
            c1, c2 = st.columns(2)

            with c1:
                st.markdown("<p>Name</p>", unsafe_allow_html=True)
                staff_name1 = st.text_input("", value='', key="sn1", label_visibility="collapsed")
                staff_name2 = st.text_input("", value='', key="sn2", label_visibility="collapsed")
                staff_name3 = st.text_input("", value='', key="sn3", label_visibility="collapsed")
                staff_name4 = st.text_input("", value='', key="sn4", label_visibility="collapsed")
                staff_name5 = st.text_input("", value='', key="sn5", label_visibility="collapsed")

            with c2:
                st.markdown("<p>Designation</p>", unsafe_allow_html=True)
                staff_title1 = st.text_input("", value='', key="st1", label_visibility="collapsed")
                staff_title2 = st.text_input("", value='', key="st2", label_visibility="collapsed")
                staff_title3 = st.text_input("", value='', key="st3", label_visibility="collapsed")
                staff_title4 = st.text_input("", value='', key="st4", label_visibility="collapsed")
                staff_title5 = st.text_input("", value='', key="st5", label_visibility="collapsed")

        # st.markdown(f"<h3>Agenda Details 📒</h3>", unsafe_allow_html=True)
        call_objective = st.text_area("Objective of the call", height=100, value="call pbjective")
        points_of_discusstion = st.text_area("Points of Discussion", height=100, value="points of discusion")
        actionable_items = st.text_area("Actionable Items", height=100, value="acional items")

        c1, c2 = st.columns(2)
        with st.container():
            next_call_date = c1.date_input("Next Call Date", key="nxtd", min_value=datetime.today())
            next_call_time = c2.time_input("Call Time", key="nxtt", label_visibility="hidden", value=None)

        next_call = str(next_call_date) + " " + str(next_call_time)

        # submit_report =

        if st.session_state.btn_submit_report == False:
            if st.form_submit_button("Save & Update"):  # st.button(label='Save & Submit'):
                if client_name1 != "" and client_title1 != "":
                    client1 = Person(client_name1, client_title1)
                    st.session_state.person_list.append(client1)
                if client_name2 != "" and client_title2 != "":
                    client2 = Person(client_name2, client_title2)
                    st.session_state.person_list.append(client2)
                if client_name3 != "" and client_title3 != "":
                    client3 = Person(client_name3, client_title3)
                    st.session_state.person_list.append(client3)
                if client_name4 != "" and client_title4 != "":
                    client4 = Person(client_name4, client_title4)
                    st.session_state.person_list.append(client4)
                if client_name5 != "" and client_title5 != "":
                    client5 = Person(client_name5, client_title5)
                    st.session_state.person_list.append(client5)
                #     ############# STAFF
                if staff_name1 != "" and staff_title1 != "":
                    staff1 = Person(staff_name1, staff_title1)
                    st.session_state.staff_list.append(staff1)
                if staff_name2 != "" and staff_title2 != "":
                    staff2 = Person(staff_name2, staff_title2)
                    st.session_state.staff_list.append(staff2)
                if staff_name3 != "" and staff_title3 != "":
                    staff3 = Person(staff_name3, staff_title3)
                    st.session_state.staff_list.append(staff3)
                if staff_name4 != "" and staff_title4 != "":
                    staff4 = Person(staff_name4, staff_title4)
                    st.session_state.staff_list.append(staff4)
                if staff_name5 != "" and staff_title5 != "":
                    staff5 = Person(staff_name5, staff_title5)
                    st.session_state.staff_list.append(staff5)

                # st.write(st.session_state.person_list)
                json_obj = report_plan_json(
                    plan_id,
                    the_place,
                    st.session_state.person_list, st.session_state.staff_list,
                    call_objective, points_of_discusstion, actionable_items
                    , str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    , "Moubien"
                    , call_start
                    , next_call
                    , from_department
                    , str(report_date)

                )
                st.json(json_obj)
                st.session_state.btn_submit_report = True
        else:
            st.warning("Already Submitted a report, Refresh the page to submit a new report")


# only if authorized open the page
is_authorized(render_edit_report)
