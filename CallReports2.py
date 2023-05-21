import json
import time
from datetime import datetime, date
from pathlib import Path
from st_aggrid import AgGrid, JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder
from library import *
from navbar import *
from utility import *

# Set page width to be wider than default
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
# Hide the hamburger icon
hide_menu_style = """
    <style>
    #MainMenu {visibility: block;}
    </style>

    """
st.markdown(hide_menu_style, unsafe_allow_html=True)
# NAV
menu_list = ["Call Plans", "Call Reports"]
navmenu_selected = Navbar2(menu_list)


@st.cache_data()
def load_data():
    data1 = pd.read_csv('pages/student.csv')
    return data1


def get_RMs_list():
    # get the list from somewhere
    result = ['Ahmad', 'John', 'Cooper']
    return result


def call_plan_page():
    with st.expander("Schedule a new Plan"):
        with st.form(key='my_form', clear_on_submit=False):
            # Get today's date
            today = date.today().strftime("%Y-%m-%d")
            # Display the date in the form header
            st.markdown(f"<h3>Request Date - {today}</h3>", unsafe_allow_html=True)
            RM_list = get_RMs_list()
            selected_cr_dr_id = st.selectbox('Select RM', RM_list)
            r1c1, r1c2 = st.columns(2)
            client_name = r1c1.text_input("Client Name:", value='')
            client_cif = r1c2.text_input("Client CIF :", value='')
            purpose = st.text_area("Purpose", height=100)
            expected_call_date = st.date_input("Select Expected Call Date", key="exp_date", min_value=datetime.today())

            submit_button = st.form_submit_button(label='Submit')

    # Process form submission
    if client_name != '' and client_cif != '':
        if submit_button:
            # Print submitted values
            with st.spinner(text='in progress'):
                time.sleep(1)
                save_plan()
                st.success('Add a new Call Plan Successfully.')
        # st.write("First Name:", fn)


def save_plan():
    # save into db
    pass

staff_list = []
if 'person_list' not in st.session_state:
    st.session_state.person_list = []
def call_report_page():
    with st.expander("Add new Call Report Record"):
        # with st.form(key='call_report', clear_on_submit=False):
        # Get today's date
        today = date.today().strftime("%Y-%m-%d")
        st.markdown(f"<h3>Report Details</h3>", unsafe_allow_html=True)

        r1c1, r1c2 = st.columns(2)
        report_date = r1c1.date_input("Event Date", key="rep_date", min_value=datetime.today(),value=datetime.now())
        from_department = r1c2.text_input("From Department :", value='fffff')

        st.markdown(f"<h3>Client Details</h3>", unsafe_allow_html=True)
        client_name = st.text_input("Client's Name", value='client name')

        r2c1, r2c2 = st.columns(2)
        client_type = r2c1.radio(
            "Select Client Type 👇",
            ["New", "Existing Client"],
            key="visibilityb",
            label_visibility="visible",
            disabled=False,
            horizontal=True,
        )
        # r2c1.radio("Client Type", ("New Client", "Existing Client"))
        referenced_by = r2c2.text_input("Prospect Referenced By :", value='ref by')

        st.markdown(f"<h3>Call Details</h3>", unsafe_allow_html=True)
        call_date_time = st.date_input("Call Date", key="call_datetime", min_value=datetime.today())
        the_place = st.text_input("Place", value='Riyad')
        # Create a two-column layout
        col1, col2 = st.columns(2)
        # Column 1
        with col1:
            st.header("Called On List")
            st.download_button(
                "Clients Template 📝", Path("student.csv").read_text(), "student.csv"
            )
            # upload the list
            uploaded_file = st.file_uploader("Upload a CSV file for called on List", type="csv", key="fupload1")
            # Check if a file was uploaded
            if uploaded_file is not None:
                # Read the uploaded CSV file
                df = pd.read_csv(uploaded_file)
                st.dataframe(df)

                for index, row in df.iterrows():
                    person = Person(row['name'], row['title'])
                    st.session_state.person_list.append(person)

        # Column 2
        with col2:
            st.header("Calling Officers List")
            st.download_button(
                "Staff Template 📝", Path("template.csv").read_text(), "student.csv"
            )
            uploaded_file = st.file_uploader("Upload a CSV file for called on List", type="csv", key="fupload2")
            # Check if a file was uploaded
            if uploaded_file is not None:
                # Read the uploaded CSV file
                df = pd.read_csv(uploaded_file)
                st.dataframe(df)

                for index, row in df.iterrows():
                    staff = Person(row['name'], row['title'])
                    staff_list.append(staff)

        st.markdown(f"<h3>Agenda Details</h3>", unsafe_allow_html=True)
        call_objective = st.text_area("Objective of the call", height=100, value="call pbjective")
        points_of_discusstion = st.text_area("Points of Discussion", height=100, value="points of discusion")
        actionable_items = st.text_area("Actionable Items", height=100, value="acional items")

        submit_report = st.button(label='Submit')
        if submit_report:
            # st.write(st.session_state.person_list)
            json_obj = report_plan_json(
                str(today),
                str(report_date),
                from_department,
                client_name,
                client_type,
                referenced_by,
                str(call_date_time),
                the_place,
                st.session_state.person_list, staff_list,
                                        call_objective, points_of_discusstion, actionable_items)
            st.write(json_obj)
            st.dataframe(json_to_dataframe(json_obj))
            # Create an empty list to store the employees


def report_plan_json(
    today, report_date, from_department, client_name, client_type, referenced_by, call_date_time, the_place
        , calledOnList, callingList, call_objective, points_of_discusstion,  actionable_items):
    called_list = [person_to_dict(person) for person in calledOnList]
    calling_list = [person_to_dict(person) for person in callingList]
    data = {
        "today": today,
        "report_date": report_date,
        "from_department": from_department,
        "client_name": client_name,
        "client_type": client_type,
        "referenced_by": referenced_by,
        "call_date_time": call_date_time,
        "the_place": the_place,
        "called_list": called_list,
        "calling_list": calling_list,
        "call_objective": call_objective,
        "points_of_discusstion": points_of_discusstion,
        "actionable_items": actionable_items
    }

    return json.dumps(data)


def save_report_plan(reportPlanObject):
    pass


def show_grid(url, df):
    injected_javascript = f"""
        class UrlCellRenderer {{
            init(params) {{
                this.eGui = document.createElement('a');
                this.eGui.innerText = params.value;
                this.eGui.setAttribute("href", "{url}" + params.value);
                this.eGui.setAttribute('style', "text-decoration:underline");
                this.eGui.setAttribute('style', "color:red");
                this.eGui.setAttribute('target', "_blank");
            }}
            getGui() {{
                return this.eGui;
            }}
        }}
    """
    gd = GridOptionsBuilder.from_dataframe(load_data())
    gd.configure_pagination(enabled=True, paginationAutoPageSize=False, paginationPageSize=10)
    gd.configure_column(
        "id", "Id",
        cellRenderer=JsCode(injected_javascript)
    )
    gd.configure_side_bar(filters_panel=True)
    # gd.configure_column("name", width=30)
    # gd.configure_columns(column_names, width=100)
    # gd.configure_default_column(editable=True, groupable=True)
    # gd.configure_selection(selection_mode='multiple', use_checkbox=True)
    gdOptions = gd.build()
    # df = load_data()
    AgGrid(df
           , gridOptions=gdOptions
           , allow_unsafe_jscode=True
           , enable_enterprise_modules=True
           , theme="streamlit"
           , enable_quicksearch=True
           , reload_data=True
           , fit_columns_on_grid_load=True
           )


# Nav bar on selection
if navmenu_selected == 'Call Plans':
    call_plan_page()
    grid_title = "My Call Plans"
    st.markdown(f"<h3>{grid_title}</h3>", unsafe_allow_html=True)
    show_grid("http://localhost:8502/view_plan?q=", load_data())
    # st.markdown('<h2 style="color:red;"">Home</h2>', unsafe_allow_html=True)
if navmenu_selected == 'Call Reports':
    call_report_page()
    grid_title = "My Calls Reports"
    st.markdown(f"<h3>{grid_title}</h3>", unsafe_allow_html=True)
    show_grid("http://localhost:8502/view_report?q=", load_data())
    # AgGrid(load_data(),default)

