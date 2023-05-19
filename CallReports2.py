import json
import time
from datetime import datetime, date
from pathlib import Path

from pandas import read_csv
from st_aggrid import AgGrid, JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder
from streamlit.components.v1 import components

from library import *
from navbar import *


class Person:
    def __init__(self, name, title):
        self.name = name
        self.title = title

# Set page width to be wider than default
st.set_page_config(layout="wide")
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
    data1 = pd.read_csv('student.csv')
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


def call_report_page():
    with st.expander("Add new Call Report Record"):
        # with st.form(key='call_report', clear_on_submit=False):
        # Get today's date
        today = date.today().strftime("%Y-%m-%d")
        st.markdown(f"<h3>Report Details</h3>", unsafe_allow_html=True)

        r1c1, r1c2 = st.columns(2)
        report_date = r1c1.date_input("Event Date", key="rep_date", min_value=datetime.today())
        from_department = r1c2.text_input("From Department :", value='')

        st.markdown(f"<h3>Client Details</h3>", unsafe_allow_html=True)
        client_name = st.text_input("Client's Name", value='')

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
        referenced_by = r2c2.text_input("Prospect Referenced By :", value='')

        st.markdown(f"<h3>Call Details</h3>", unsafe_allow_html=True)
        call_date_time = st.date_input("Call Date", key="call_datetime", min_value=datetime.today())
        the_place = st.text_input("Place", value='')
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
                person_list = []
                for index, row in df.iterrows():
                    person = Person(row['name'], row['title'])
                    person_list.append(person)

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
                # Display the DataFrame in a grid
                st.dataframe(df)

        st.markdown(f"<h3>Agenda Details</h3>", unsafe_allow_html=True)
        call_objective = st.text_area("Objective of the call", height=100, value="call pbjective")
        points_of_discusstion = st.text_area("Points of Discussion", height=100, value="points of discusion")
        actionable_items = st.text_area("Actionable Items", height=100, value="acional items")

        submit_report = st.button(label='Submit')
        if submit_report:
            json_obj = report_plan_json(None, None, st.session_state.calledOnList, st.session_state.callingList,
                                        call_objective, points_of_discusstion, actionable_items)
            st.write(json_obj)

            # Create an empty list to store the employees


def report_plan_json(staff_name, staff_title, calledOnList, callingList, call_objective, points_of_discusstion,
                     actionable_items):
    data = {
        "staff_name": staff_name,
        "staff_title": staff_title,
        "called_list": calledOnList,
        "calling_list": callingList,
        "call_objective": call_objective,
        "points_of_discusstion": points_of_discusstion,
        "actionable_items": actionable_items
    }

    return json.dumps(data)


def save_report_plan(reportPlanObject):
    pass


def show_grid():
#     cellRenderer = JsCode(
#         """
#         function(params){
#           return
#            "<a href='http://google.com/'>link </a>";
#         }
#
# """
#     )

    # callRenderer = JsCode(
    #     """
    #       function(params) {
    #                  return 'Value is <b>' + params.value + '</b>';
    #             }
    #     """
    # )


    # link_jscode = JsCode("""
    #  function(params) {
    #     var element = document.createElement("span");
    #     var linkElement = document.createElement("a");
    #     var linkText = document.createTextNode(params.value);
    #     link_url = params.value;
    #     linkElement.appendChild(linkText);
    #     linkText.title = params.value;
    #     linkElement.href = link_url;
    #     linkElement.target = "_blank";
    #     element.appendChild(linkElement);
    #     return element;
    #  };
    #  """)
    image_nation = JsCode(
        """
            function (params) {
                var htmlContent = '<h1>Hello, World!</h1><p>This is a dynamically rendered HTML content.</p>';
                return htmlContent;
            }
        """
    )
    gd = GridOptionsBuilder.from_dataframe(load_data())
    gd.configure_pagination(enabled=True, paginationAutoPageSize=False, paginationPageSize=10)
    # gd.configure_column("id"
    #                     , cellRenderer=image_nation
    #                     , cellStyle={'color': 'red'}
    #                     , unsafe_allow_html=True)
    #
    gd.configure_column(
        "id", "sdsddsds",
        cellRenderer=JsCode("""
            class UrlCellRenderer {
              init(params) {
                this.eGui = document.createElement('a');
                this.eGui.innerText = params.value;
                this.eGui.setAttribute("href", "https://www.google.com/search?q="+params.value);
                this.eGui.setAttribute('style', "text-decoration:underline");
                this.eGui.setAttribute('target', "_blank");
              }
              getGui() {
                return this.eGui;
              }
            }
        """)
    )
    # gd.configure_column("name", headerName="name", cellRenderer=JsCode(
    #     '''function(params) {return '<a href="https://drive.google.com/file/d/' + params.value + '/view" target="_blank">' + params.value + '</a>'}'''),
    #                     width=300)
    gd.configure_side_bar(filters_panel=True)
    # gd.configure_column("name", width=30)
    # gd.configure_columns(column_names, width=100)
    # gd.configure_default_column(editable=True, groupable=True)
    # gd.configure_selection(selection_mode='multiple', use_checkbox=True)
    gdOptions = gd.build()
    df = load_data()
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
    show_grid()
    # st.markdown('<h2 style="color:red;"">Home</h2>', unsafe_allow_html=True)
if navmenu_selected == 'Call Reports':
    call_report_page()
    grid_title = "My Call Report"
    st.markdown(f"<h3>{grid_title}</h3>", unsafe_allow_html=True)
    show_grid()
    # AgGrid(load_data(),default)


st.markdown(f"<h3>Agenda Details</h3>")
# components.html("<h1>ddsdsdds</h2>")

# op_menu = get_financial_trans_type_desc()
# selected_value22 = st.selectbox('Select an option', list(op_menu.keys()))
# value22 = op_menu[selected_value22]


# Define a class for the object

# Create a sample DataFrame
# df = pd.read_csv("template.csv")
# Convert DataFrame to list of objects


# Print the list of objects
# for person in person_list:


# for person in person_list:
#     print(person.name, person.title)
# st.write(person.name)
