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

userId, token_expiry = get_user_claims(token)
if token_expiry is not None:
    token_expiry_date = datetime.fromtimestamp(token_expiry)


# is_token_expired

def plansGrid(data):
    show_grid(view_plan_url(token), edit_plan_url(token), data)


def callReportGrid(data):
    show_grid(view_report_url(token), edit_report_url(token), data)


def main():
    if userId is None:
        st.markdown(notfound_page("Unauthorized-401"), unsafe_allow_html=True)
    elif userId is not None and token_expiry < int(round(datetime.now().timestamp())):
        st.markdown(notfound_page("Session Expired"), unsafe_allow_html=True)
    else:
        components.html(page_head(userId, token_expiry_date))
        page_settings()


        menu_list = ["Call Plans", "Call Reports"]
        navmenu_selected = Navbar2(menu_list)

        def call_plan_page():
            with st.expander("Schedule a new Plan"):
                # with st.form(key='my_form', clear_on_submit=False):
                # Get today's date
                today = date.today().strftime("%Y-%m-%d")
                # Display the date in the form header
                st.markdown(f"<h3>Request Date - {today}</h3>", unsafe_allow_html=True)
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
                    selected_rm = st.selectbox('Relationship Manager 🙎‍♂', str(userId), disabled=True)

                st.write("Client CIF")
                r1c1, r1c2 = st.columns(2)

                client_cif = r1c1.text_input("Client CIF :", value='12323-JF22ffh-233', label_visibility="collapsed")
                if r1c2.button("Fetch Client Data"):
                    fetch_client_data(client_cif)

                purpose = st.selectbox("Purpose", get_purpose_options(), key='purposethis')
                expected_call_date = st.date_input("Select Expected Call Date", key="exp_date",
                                                   min_value=datetime.today())
                # sot = st.text_input("Enter SOT")

                submit_button = st.button('Submit')

                # Process form submission

                if submit_button:
                    # Print submitted values
                    with st.spinner(text='in progress'):
                        time.sleep(1)
                        save_plan()
                        st.success('Add a new Call Plan Successfully.')

                        data = {
                            "rm_id": selected_rm_result,
                            "client_name": st.session_state.client_name,
                            "client_cif": client_cif,
                            "client_sot": st.session_state.client_SOT,
                            "client_outstanding": st.session_state.client_outstanding,
                            "purpose": purpose,
                            "expected_call_date": str(expected_call_date),
                            "create_date": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                            "created_by": st.session_state.client_name
                        }

                        st.json(json.dumps(data))

                # st.write("First Name:", fn)

        staff_list = []
        if 'person_list' not in st.session_state:
            st.session_state.person_list = []
        # radio state
        if 'c_type' not in st.session_state:
            st.session_state.c_type = ""

        def call_report_page():
            call_start = ""
            call_end = ""
            next_call = ""
            with st.expander("Add new Call Report Record"):
                # with st.form(key='call_report', clear_on_submit=False):
                # Get today's date
                # today = date.today().strftime("%Y-%m-%d")
                st.markdown(f"<h3>Client Details</h3>", unsafe_allow_html=True)
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
                    client_name = st.text_input("Client's Name", value='client name')
                elif st.session_state.c_type == "e":
                    client_name = st.selectbox("Client's Name", get_rm_clients(1))
                # r2c1.radio("Client Type", ("New Client", "Existing Client"))

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

                submit_report = st.button(label='Submit')
                if submit_report:
                    # st.write(st.session_state.person_list)
                    json_obj = report_plan_json(
                        client_name,
                        client_type,
                        referenced_by,
                        the_place,
                        st.session_state.person_list, staff_list,
                        call_objective, points_of_discusstion, actionable_items
                        , str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                        , "Moubien"
                        , call_start
                        , call_end
                        , next_call
                    )
                    st.json(json_obj)

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

        cellsytle_jscode = JsCode("""
        function(params) {
            if (params.value == 'A') {
                return {
                    'color': 'white',
                    'backgroundColor': 'darkred'
                }
            } else {
                return {
                    'color':'black',
                    'backgroundColor': 'white'
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
            plansGrid(load_data('pages/plans.csv'))
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
            callReportGrid(df)


if __name__ == '__main__':
    main()
