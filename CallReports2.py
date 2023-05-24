import time
from datetime import datetime, date
from pathlib import Path
from st_aggrid import AgGrid, JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder
from navbar import *
from common import *
from utility import *
from popup import *

general_settings()
#get user info
qid = st.experimental_get_query_params()
q_userId = int(qid['user'][0])
userId = get_user(q_userId)

components.html(page_head(userId))
# st.markdown(page_head(userId), unsafe_allow_html=True)
# st.markdown(f"<p>Welcome, {userId}</p>",unsafe_allow_html=True)

# Hide the hamburger icon
plans_data_file = Path("pages/plans.csv")
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
     #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-uf99v8.egzxvld5 > div.block-container.css-z5fcl4.egzxvld4 > div:nth-child(1) > div > div.css-ybnenh.e1s6o5jp0 > ul > li > div.st-am.st-cl.st-cf.st-cg.st-ch > div > div:nth-child(1) > div > div.css-ocqkz7.e1tzin5v3 > div:nth-child(2) > div:nth-child(1) > div > div > div > button
    {margin-top:33px;}
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-uf99v8.egzxvld5 > div.block-container.css-z5fcl4.egzxvld4 > div:nth-child(1) > div > div.css-ybnenh.e1s6o5jp0 > ul > li > div.streamlit-expanderHeader.st-ae.st-bx.st-ag.st-ah.st-ai.st-aj.st-by.st-bz.st-c0.st-c1.st-c2.st-c3.st-c4.st-ar.st-as.st-b6.st-b5.st-b3.st-c5.st-c6.st-c7.st-b4.st-c8.st-c9.st-ca.st-cb.st-cc > div > p
    { font-size: 22px !important; font-weight: bold !important; }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-uf99v8.egzxvld5 > div.block-container.css-z5fcl4.egzxvld4 > div:nth-child(1) > div
    { margin-top:-60px; }
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)
# NAV

menu_list = ["Call Plans", "Call Reports"]
navmenu_selected = Navbar2(menu_list)


# @st.cache_data()
def load_data(file):
    data1 = pd.read_csv(file)
    return data1


def get_rm_clients(rmId):
    clients = ['Omar', 'Boss', "Bose"]
    return clients


if 'client_name' not in st.session_state:
    st.session_state.client_name = "c1"
if 'client_SOT' not in st.session_state:
    st.session_state.client_SOT = "0"
if 'client_outstanding' not in st.session_state:
    st.session_state.client_outstanding = "nothing"


def fetch_client_data(cif):
    cn = st.session_state.client_name = "Ericson Telecom"
    sot = st.session_state.client_SOT = "4000"
    out = st.session_state.client_outstanding = "Some outstanding data fetched"
    data = {
        'Client CIF': [cif],
        'Client Name': [cn],
        'Client SOT': [sot],
        'Client Outstanding': [out]
    }
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)
    st.dataframe(df)
    # st.write(f"cif: {cif} client name: -{st.session_state.client_name}-SOT: { st.session_state.client_SOT}-Outstanding: {st.session_state.client_outstanding}")


def get_RMs_list():
    # get the list from somewhere
    result = ['Ahmad', 'John', 'Cooper']
    return result


def call_plan_page():
    with st.expander("Schedule a new Plan"):
        # with st.form(key='my_form', clear_on_submit=False):
        # Get today's date
        today = date.today().strftime("%Y-%m-%d")
        # Display the date in the form header
        st.markdown(f"<h3>Request Date - {today}</h3>", unsafe_allow_html=True)
        RM_list = get_RMs_list()
        rm = st.selectbox('Select RM 🙎‍♂', RM_list)
        r1c1, r1c2 = st.columns(2)
        # client_name = r1c1.text_input("Client Name:", value='client name')
        client_cif = r1c1.text_input("Client CIF :", value='cif num')
        if r1c2.button("Fetch Client Data"):
            fetch_client_data(client_cif)

        purpose = st.text_area("Purpose", height=100, value='purpose of this')
        expected_call_date = st.date_input("Select Expected Call Date", key="exp_date", min_value=datetime.today())
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
                    "rm": rm,
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


def save_plan():
    # save into db
    pass


staff_list = []
if 'person_list' not in st.session_state:
    st.session_state.person_list = []
# radio state
if 'c_type' not in st.session_state:
    st.session_state.c_type = ""


def call_report_page():
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
        report_date = r1c1.date_input("Event Date", key="rep_date", min_value=datetime.today(), value=datetime.now())
        referenced_by = r1c2.text_input("Prospect Referenced By :", value='ref by')


        st.markdown(f"<h3>Call Details 📞</h3>", unsafe_allow_html=True)
        call_date_time = st.date_input("Call Date", key="call_datetime", min_value=datetime.today())
        the_place = st.text_input("Place", value='Riyad')
        # Create a two-column layout
        st.markdown(f"<h3>Clients/Staff List Details 📋</h3>", unsafe_allow_html=True)
        st.markdown("<p>Please use the template below to fill the list then upload it.</p>", unsafe_allow_html=True)
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

        submit_report = st.button(label='Submit')
        if submit_report:
            # st.write(st.session_state.person_list)
            json_obj = report_plan_json(

                client_name,
                client_type,
                referenced_by,
                str(call_date_time),
                the_place,
                st.session_state.person_list, staff_list,
                call_objective, points_of_discusstion, actionable_items
                , str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                , "Moubien"
            )
            st.json(json_obj)
            # st.dataframe(json_to_dataframe(json_obj))
            # Create an empty list to store the employees


def report_plan_json(
        client_name, client_type, referenced_by, call_date_time, the_place
        , calledOnList, callingList, call_objective, points_of_discusstion, actionable_items
        , create_date, created_by):
    called_list = [person_to_dict(person) for person in calledOnList]
    calling_list = [person_to_dict(person) for person in callingList]
    data = {
        "client_name": client_name,
        "client_type": client_type,
        "referenced_by": referenced_by,
        "call_date_time": call_date_time,
        "the_place": the_place,
        "called_list": called_list,
        "calling_list": calling_list,
        "call_objective": call_objective,
        "points_of_discusstion": points_of_discusstion,
        "actionable_items": actionable_items,
        "create_date": create_date,
        "created_by": created_by

    }

    return json.dumps(data)


def save_report_plan(reportPlanObject):
    pass


# <i class="fas fa-eye"></i>
# st.markdown('<i class="fas fa-eye"></i> Star', unsafe_allow_html=True)
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
def show_grid(url, df):
    injected_javascript = f"""
        class UrlCellRenderer {{
            init(params) {{
                this.eGui = document.createElement('a');
                this.eGui.innerText = "👁️";
                this.eGui.setAttribute('title', params.value);
                this.eGui.setAttribute("href", "{url}" + params.value);
                this.eGui.setAttribute('style', "text-decoration:underline");
                this.eGui.setAttribute('style', "color:white");
                this.eGui.setAttribute('target', "_blank");
 
            }}
            getGui() {{
                return this.eGui;
            }}
        }}
    """
    gd = GridOptionsBuilder.from_dataframe(df)
    gd.configure_pagination(enabled=True, paginationAutoPageSize=False, paginationPageSize=10)
    gd.configure_column(
        "id", "Id",
        cellRenderer=JsCode(injected_javascript)
    )
    # gd.configure_column("class", cellStyle=cellsytle_jscode)
    gd.configure_side_bar(filters_panel=True)
    gd.configure_column("id", width=40)
    # gd.configure_columns(column_names, width=100)
    # gd.configure_default_column(editable=True, groupable=True)
    # gd.configure_selection(selection_mode='multiple', use_checkbox=True)
    gdOptions = gd.build()
    # df = load_data()
    custom_css = {
        ".ag-row-hover": {"background-color": " #C09C20 !important"},
        #".ag-header-cell-label": {"background-color": "orange !important"}
    }
    AgGrid(df
           , gridOptions=gdOptions
           , allow_unsafe_jscode=True
           , enable_enterprise_modules=True
           , theme="streamlit"
           , enable_quicksearch=True
           , reload_data=True
           , fit_columns_on_grid_load=True
            , custom_css =custom_css,
           )


def plansGrid():
    show_grid("http://localhost:8502/view_plan?q=", load_data('pages/plans.csv'))


def callReportGrid(df):
    show_grid("http://localhost:8502/view_report?q=", df)


# Nav bar on selection
if navmenu_selected == 'Call Plans':
    call_plan_page()
    grid_title = "My Call Plans"
    st.markdown(f"<h3>{grid_title}</h3>", unsafe_allow_html=True)
    plansGrid()
    # st.markdown('<h2 style="color:red;"">Home</h2>', unsafe_allow_html=True)
if navmenu_selected == 'Call Reports':
    call_report_page()
    grid_title = "My Calls Reports"
    st.markdown(f"<h3>{grid_title}</h3>", unsafe_allow_html=True)

    report_creation_date_from = ""
    report_creation_date_to = ""
    report_from = ""
    report_to = ""

    col1, col2 = st.columns(2)
    with col1:
        date_range = st.date_input("Select Creation Date range", value=(date.today(), date.today()), key="recorddate")
        # start_date = st.date_input('Date From')
        report_creation_date_from = date_range[0]
        report_creation_date_to = date_range[1]
    with col2:
        pass
        # date_range = st.date_input("Select Call Date range", value=(date.today(), date.today()), key="calldate")
        # callfrom = date_range[0]
        # callto = date_range[1]
        # end_date = st.date_input('To')

    load_btn = st.button("Load")
    if load_btn:
        df = load_data('pages/callreports.csv')
        df['creation_date'] = pd.to_datetime(df['creation_date'])
        df = df.query('@report_creation_date_from <= creation_date <= @report_creation_date_to')

    else:
        df = load_data('pages/callreports.csv')
    all_btn = st.button("All Data")
    if all_btn:
        df = []
        df = load_data('pages/callreports.csv')
    callReportGrid(df)
    # AgGrid(load_data(),default)

# popup("Title", "impsum dolor ipsupm")
