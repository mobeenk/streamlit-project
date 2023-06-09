import json
from DAL.data_access import  get_report_by_id, get_plans_by_userid
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
            f"<i class=\"fas fa-wrench\"></i> Edit Report #{get_query_param_by_name('id')}"
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
    plan_data = get_report_by_id(userId, extracted_id)
    record = json.loads(plan_data)
    print(record['called_list'][0]['title'])
    st.markdown(f"<h3>Client Details</h3>", unsafe_allow_html=True)
    with st.form('myform'):
        plan_id = st.selectbox("Select Plan Id", get_plans_by_userid(userId), disabled=True)

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
                cases = [
                    (0, 'cn1'),
                    (1, 'cn2'),
                    (2, 'cn3'),
                    (3, 'cn4'),
                    (4, 'cn5')
                ]
                input_values = {}  # Dictionary to store the input values
                for index, key in cases:
                    if 'called_list' in record and len(record['called_list']) > index:
                        name = record['called_list'][index]['name']
                    else:
                        name = ""
                    value = st.text_input("", value=name, key=key, label_visibility="collapsed")
                    input_values[key] = value  # Store the value in the dictionary
                # Access the input values separately
                client_name1 = input_values['cn1']
                client_name2 = input_values['cn2']
                client_name3 = input_values['cn3']
                client_name4 = input_values['cn4']
                client_name5 = input_values['cn5']

            with c2:
                st.markdown("<p>Designation</p>", unsafe_allow_html=True)
                cases = [
                    (0, 'ct1'),
                    (1, 'ct2'),
                    (2, 'ct3'),
                    (3, 'ct4'),
                    (4, 'ct5')
                ]

                input_values = {}  # Dictionary to store the input values

                for index, key in cases:
                    if 'called_list' in record and len(record['called_list']) > index:
                        title = record['called_list'][index]['title']
                    else:
                        title = ""
                    value = st.text_input("", value=title, key=key, label_visibility="collapsed")
                    input_values[key] = value  # Store the value in the dictionary

                # Access the input values separately
                client_title1 = input_values['ct1']
                client_title2 = input_values['ct2']
                client_title3 = input_values['ct3']
                client_title4 = input_values['ct4']
                client_title5 = input_values['ct5']

        with col_staff:
            st.markdown("<p>Staff list</p>", unsafe_allow_html=True)
            c1, c2 = st.columns(2)

            with c1:
                st.markdown("<p>Name</p>", unsafe_allow_html=True)
                cases = [
                    (0, 'sn1'),
                    (1, 'sn2'),
                    (2, 'sn3'),
                    (3, 'sn4'),
                    (4, 'sn5')
                ]
                input_values = {}  # Dictionary to store the input values
                for index, key in cases:
                    if 'calling_list' in record and len(record['calling_list']) > index:
                        name = record['calling_list'][index]['name']
                    else:
                        name = ""
                    value = st.text_input("", value=name, key=key, label_visibility="collapsed")
                    input_values[key] = value  # Store the value in the dictionary
                # Access the input values separately
                staff_name1 = input_values['sn1']
                staff_name2 = input_values['sn2']
                staff_name3 = input_values['sn3']
                staff_name4 = input_values['sn4']
                staff_name5 = input_values['sn5']

            with c2:
                st.markdown("<p>Designation</p>", unsafe_allow_html=True)
                cases = [
                    (0, 'st1'),
                    (1, 'st2'),
                    (2, 'st3'),
                    (3, 'st4'),
                    (4, 'st5')
                ]
                input_values = {}  # Dictionary to store the input values
                for index, key in cases:
                    if 'calling_list' in record and len(record['calling_list']) > index:
                        name = record['calling_list'][index]['title']
                    else:
                        name = ""
                    value = st.text_input("", value=name, key=key, label_visibility="collapsed")
                    input_values[key] = value  # Store the value in the dictionary
                # Access the input values separately
                staff_title1 = input_values['st1']
                staff_title2 = input_values['st2']
                staff_title3 = input_values['st3']
                staff_title4 = input_values['st4']
                staff_title5 = input_values['st5']

        # st.markdown(f"<h3>Agenda Details 📒</h3>", unsafe_allow_html=True)
        call_objective = st.text_area("Objective of the call", height=100, value="call pbjective")
        points_of_discusstion = st.text_area("Points of Discussion", height=100, value="points of discusion")
        actionable_items = st.text_area("Actionable Items", height=100, value="acional items")

        c1, c2 = st.columns(2)
        with st.container():
            next_call_date = c1.date_input("Next Call Date", key="nxtd", min_value=datetime.today())
            next_call_time = c2.time_input("Call Time", key="nxtt", label_visibility="hidden", value=None)

        next_call = str(next_call_date) + " " + str(next_call_time)

        submit_report = st.form_submit_button("Save & Update", disabled=st.session_state.btn_submit_report)

        if submit_report:  # st.button(label='Save & Submit'):
            if not st.session_state.btn_submit_report:
                clients = [
                    (client_name1, client_title1),
                    (client_name2, client_title2),
                    (client_name3, client_title3),
                    (client_name4, client_title4),
                    (client_name5, client_title5)
                ]

                staff = [
                    (staff_name1, staff_title1),
                    (staff_name2, staff_title2),
                    (staff_name3, staff_title3),
                    (staff_name4, staff_title4),
                    (staff_name5, staff_title5)
                ]

                for name, title in clients:
                    if name != "" and title != "":
                        client = Person(name, title)
                        st.session_state.person_list.append(client)

                for name, title in staff:
                    if name != "" and title != "":
                        staff_member = Person(name, title)
                        st.session_state.staff_list.append(staff_member)

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
                st.warning("Already Update the Report.")


if is_token_authorized():
    render_edit_report()
else:
    st.markdown(notfound_page("You are not authorized to edit this report "), unsafe_allow_html=True)
