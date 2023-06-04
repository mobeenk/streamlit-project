import time
from datetime import datetime, date
from pathlib import Path
from navbar import *
from common import *
from utility import *
from popup import *
from DAL.data_access import *


general_settings()
session_settings()
# get token from URL
token = get_query_param_by_name('token')

userId, token_expiry, username = get_user_claims(token)
if token_expiry is not None:
    token_expiry_date = datetime.fromtimestamp(token_expiry)


# is_token_expired

def plansGrid(data, cellsytle_jscode):
    show_grid(view_plan_url(token), edit_plan_url(token), data, cellsytle_jscode=cellsytle_jscode)


def callReportGrid(data, cellsytle_jscode):
    show_grid(view_report_url(token), edit_report_url(token),data,  cellsytle_jscode=cellsytle_jscode)


def main():
    if userId is None:
        st.markdown(notfound_page("Unauthorized-401"), unsafe_allow_html=True)
    elif userId is not None and token_expiry < int(round(datetime.now().timestamp())):
        st.markdown(notfound_page("Session Expired"), unsafe_allow_html=True)
    else:
        components.html(page_head(userId, token_expiry_date, username))
        page_settings()


        menu_list = ["Call Plans", "Call Reports"]
        navmenu_selected = Navbar2(menu_list)

        def call_plan_page():
            client_cif = ""
            with st.expander("Schedule a new Plan"):
                # with st.form(key='my_form', clear_on_submit=False):
                # Get today's date
                today = date.today().strftime("%Y-%m-%d")
                # Display the date in the form header
                # st.markdown(f"<h3>Request Date - {today}</h3>", unsafe_allow_html=True)
                selected_rm_result = 0
                if st.session_state.is_manager == True:
                    rm_list = get_rms_list(1)
                    selected_rm = st.selectbox(
                        "Relationship Manager 🙎‍",
                        range(len(rm_list)),
                        format_func=lambda x: list(rm_list[x].values())[0]
                    )
                    selected_rm_result = list(rm_list[selected_rm].keys())[0]

                    # selected_rm = st.selectbox('Relationship Manager 🙎‍♂',rm_list, index= 2, disabled=False, help="Select RM")
                else:
                    selected_rm_result = st.selectbox('Relationship Manager 🙎‍♂', str(userId), disabled=True)

                # st.markdown(f"<h3>Client Details</h3>", unsafe_allow_html=True)
                r2c1, r2c2 = st.columns(2)
                client_type = r2c1.radio(
                    "Select Client Type 👇",
                    ["New", "Existing Client"],
                    key="visibilityb",
                    label_visibility="visible",
                    disabled=False,
                    horizontal=True,
                )

                if client_type == 'New':
                    st.session_state.c_type = "n"
                else:
                    st.session_state.c_type = "e"
                    # st.write("Exists")

                if st.session_state.c_type == "n":
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.session_state.client_name = st.text_input("Client's Name", value='client name', key="cname")
                    with col2:
                        st.session_state.client_cr = st.text_input("Client's Name", value='client cr', key="ccr")
                    with col3:
                        st.session_state.client_ref = st.text_input("Prospect Referred By", value='reference name', key="refname")
                elif st.session_state.c_type == "e":
                    r1c1, r1c2 = st.columns(2)
                    client_cif = r1c1.text_input("Client CIF :", value='12323-JF22ffh-233', label_visibility="collapsed")
                    if r1c2.button("Show Client info"):
                        fetch_client_data(client_cif)
                    # client_name = st.selectbox("Client's Name", get_rm_clients(1))

                #     Old code
                # st.write("Client CIF")
                # r1c1, r1c2 = st.columns(2)
                #
                # client_cif = r1c1.text_input("Client CIF :", value='12323-JF22ffh-233', label_visibility="collapsed")
                # if r1c2.button("Fetch Client Data"):
                #     fetch_client_data(client_cif)

                purpose = st.text_input("Purpose", value="Purpose", key='purposethis')
                expected_call_date = st.date_input("Select Expected Call Date", key="exp_date",
                                                   min_value=datetime.today())
                # sot = st.text_input("Enter SOT")

                submit_button = st.button('Save & Submit')

                # Process form submission

                if submit_button:
                    # Print submitted values
                    with st.spinner(text='in progress'):
                        if st.session_state.c_type == "e":
                            fetch_client_data(client_cif)
                        time.sleep(1)
                        save_plan()
                        st.success('Add a new Call Plan Successfully.')

                        data = {
                            "rm_id": selected_rm_result,
                            "client_name": st.session_state.client_name,
                            "client_cif": "client_cif",
                            "client_sot": st.session_state.client_SOT,
                            "client_outstanding": st.session_state.client_outstanding,
                            "purpose": purpose,
                            "expected_call_date": str(expected_call_date),
                            "create_date": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                            "created_by": userId,
                            "referred_by": st.session_state.client_ref,
                            "client_cr": st.session_state.client_cr,
                            "client_risk_rating": st.session_state.client_risk_rating
                        }

                        st.json(json.dumps(data))

                # st.write("First Name:", fn)

        staff_list = []
        if 'person_list' not in st.session_state:
            st.session_state.person_list = []
        if 'staff_list' not in st.session_state:
            st.session_state.staff_list = []
        # radio state
        if 'c_type' not in st.session_state:
            st.session_state.c_type = ""

        def call_report_page():
            with st.expander("Add new Call Report Record"):
                plan_id = st.selectbox("Select Plan Id",['100','200','300'])

                r1c1, r1c2 = st.columns(2)
                report_date = r1c1.date_input("Event Date", key="rep_date", min_value=datetime.today(), value=datetime.now())
                the_place = r1c2.text_input("Venue", value='Riyad')
                # referenced_by = r1c2.text_input("Prospect Referenced By :", value='ref by')

                # st.markdown(f"<h3>Call Details 📞</h3>", unsafe_allow_html=True)
                c1, c2, c3, c4 = st.columns(4)
                with st.container():
                    call_date_start = c1.date_input("Call Start", key="call_datetime1", min_value=datetime.today())
                    call_time_start = c2.time_input("Call Time", key="jjh", label_visibility="hidden", value=None)
                    call_start = str(call_date_start) + " " + str(call_time_start)

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
                        client_name1 = st.text_input("", value='',key="cn1", label_visibility="collapsed")
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

                submit_report = st.button(label='Submit')
                if submit_report:
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
                    )
                    st.json(json_obj)

        def report_plan_json(
                plan_id, the_place
                , calledOnList, callingList, call_objective, points_of_discusstion, actionable_items
                , create_date, created_by, call_start, next_call):

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
                "created_by": created_by,
                "call_start": call_start,
                # "call_end": call_end,
                "next_call": next_call
            }

            return json.dumps(data)

        cellsytle_jscode = JsCode("""
        function(params) {
            if (params.value == 'Pending Approval' || params.value == 'New' ||  params.value == 'Pending') {
                return {
                    'color': '#d3d3d3',
                     'background': 'linear-gradient(to bottom, rgba(218, 218, 0, 0.8), rgba(163, 133, 0, 0.8))',
                    'borderRadius' : '5px'
                }
            } else if(params.value == 'Completed') {
                return {
                    'color':'white',
                     'background': 'linear-gradient(to bottom,rgba(0, 153, 0, 0.8), rgba(0, 51, 0, 0.8))',
                    'borderRadius' : '5px'
                }
            }
            else {
                return {
                    'color':'white',
                    'background': 'linear-gradient(to bottom,  rgba(153, 0, 0, 0.8), rgba(102, 0, 0, 0.8))',
                    'borderRadius' : '5px'
                }
            }
        };
        """)

        # ✍️ ✏️👁️✏️❌👁‍🗨

        # Nav bar on selection
        if navmenu_selected == 'Call Plans':
            call_plan_page()
            grid_title = "My Call Plans"
            st.markdown(f"<h3>{grid_title}</h3>", unsafe_allow_html=True)
            plansGrid(load_data('pages/plans.csv'), cellsytle_jscode)
            # st.markdown('<h2 style="color:red;"">Home</h2>', unsafe_allow_html=True)
        if navmenu_selected == 'Call Reports':
            call_report_page()
            grid_title = "My Calls Reports"
            st.markdown(f"<h3>{grid_title}</h3>", unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                pass
                # date_range = st.date_input("Select Creation Date range", value=(date.today(), date.today()), key="recorddate")
                # start_date = st.date_input('Date From')
                # report_creation_date_from = date_range[0]
                # report_creation_date_to = date_range[1]
            with col2:
                pass

            # load_btn = st.button("Load")
            # if load_btn:
            #     df = load_data('pages/callreports.csv')
            #     df['creation_date'] = pd.to_datetime(df['creation_date'])
            #     df = df.query('@report_creation_date_from <= creation_date <= @report_creation_date_to')

            # else:
            #     df = load_data('pages/callreports.csv')

            # all_btn = st.button("All Data")
            # if all_btn:
            #     df = []
            #     df = load_data('pages/callreports.csv')
            df = load_data('pages/callreports.csv')
            callReportGrid(df, cellsytle_jscode)


if __name__ == '__main__':
    main()
    #
    # with col1:
    #     st.header("Clients List")
    #     # upload the list
    #     uploaded_file = st.file_uploader("Upload a CSV file for called on List", type="csv", key="fupload1")
    #     # Check if a file was uploaded
    #     if uploaded_file is not None:
    #         df = pd.read_csv(uploaded_file)
    #         st.dataframe(df)
    #
    #         for index, row in df.iterrows():
    #             person = Person(row['name'], row['title'], row['department'], row['phone'])
    #             st.session_state.person_list.append(person)
    #
    # # Column 2
    # with col2:
    #     st.header("Staff Officers List")
    #     uploaded_file = st.file_uploader("Upload a CSV file for called on List", type="csv", key="fupload2")
    #     # Check if a file was uploaded
    #     if uploaded_file is not None:
    #         # Read the uploaded CSV file
    #         df = pd.read_csv(uploaded_file)
    #         st.dataframe(df)
    #
    #         for index, row in df.iterrows():
    #             staff = Person(row['name'], row['title'], row['department'], row['phone'])
    #             staff_list.append(staff)
    #
    #
    #
    #
