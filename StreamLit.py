import time
from datetime import datetime

from pandas import read_csv
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from library import *
from navbar import *

# Set page width to be wider than default
st.set_page_config(layout="wide")
# Hide the hamburger icon
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# NAV
navmenu_selected = Navbar2()
column_names = []
cifs_parameter = ""


def get_financial_trans_type_desc():
    return {'Value Added Tax': 24, 'Outgoing Local QUick': 60, 'Cash Withdrawl': 163}


@st.cache_data()
def load_data():
    data1 = pd.read_csv('student.csv')
    return data1


def trx_comp():
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv('student.csv')
    # Save the column names into an array
    column_names = df.columns.values

    # Create Streamlit file uploader widget
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
    column_names2 = []
    if uploaded_file is not None:
        # Call get_column_names function to extract column names
        column_names2, cif = get_column_names(uploaded_file)
        cifs_parameter = ', '.join(map(str, cif))
    else:
        cifs_parameter = "1"
    # for i, tab in enumerate(tabs):
    #     tabs[i].write(f"Tab {i+1}")

    # with st.expander("Click to expand"):
    with st.form(key='my_form', clear_on_submit=False):
        # Customer
        selected_column_names = st.multiselect('Select the columns you need to include:', column_names2, column_names2)
        options = ['All', 'D', 'C']
        selected_cr_dr_id = st.selectbox('Select Cr_Dr_ind', options)
        #
        r2c1, r2c2 = st.columns(2)
        from_date = r2c1.date_input("Transactions post Date from:", value=datetime.now())
        to_date = r2c2.date_input("Transactions post Date to:", value=datetime.now())

        r1c1, r1c2 = st.columns(2)
        posting = r1c1.text_input("Enter Posting :", value='All')
        inst_ref = r1c2.text_input("Enter Instrument Ref :", value='All')

        r2c1, r2c2 = st.columns(2)
        eqv_from = r2c1.text_input("SAR_EQV_TXN_AMT from :", value='All')
        eqv_to = r2c2.text_input("SAR_EQV_TXN_AMT to :", value='All')
        # selected_value = st.slider('Select SAR_EQV_TXN_AMT', -10000, 10000, value=1000)

        # financial_tran_type_desc
        trans_types = ['All', 'D', 'C']  # get_financial_trans_type_desc()
        selected_trans_type = st.selectbox('financial_tran_type_desc', trans_types)

        op_menu = get_financial_trans_type_desc()
        selected_value22 = st.selectbox('Select an option', list(op_menu.keys()))
        value22 = op_menu[selected_value22]

        trx_Bkey = st.text_input("Enter Transaction_BKey :", value='All')

        #submit button
        submit_button = st.form_submit_button(label='Submit')

    # Process form submission
    if submit_button:
        # Print submitted values
        with st.spinner(text='in progress'):
            time.sleep(1)
            st.success('done')
        # st.write("First Name:", fn)
        # print(cifs_parameter)
        # cifs_paras = ', '.join(cifs_parameter)


        if selected_column_names:
            my_selection = ', '.join(selected_column_names)
        else:
            my_selection = '*'
        st.markdown("<h3><b>Query Result:</b></h3><br><h4 style="'color:green;'" >{}</h4>"
        .format(
            query_build(my_selection, cifs_parameter, "\'" + str(from_date) + "\'", "\'" + str(to_date) + "\'"
            ,selected_cr_dr_id, posting, trx_Bkey)
        )
            , unsafe_allow_html=True)

        # st.write('<h1>{}</h1>'.format(selected_column_names), unsafe_allow_html=True)
        # st.write('<h1>{}</h1>'.format(join_strings(selected_column_names)), unsafe_allow_html=True)

        gd = GridOptionsBuilder.from_dataframe(load_data())
        gd.configure_pagination(enabled=True, paginationAutoPageSize=False, paginationPageSize=5)
        # gd.configure_column("name", width=30)
        gd.configure_columns(column_names, width=100)
        gd.configure_default_column(editable=True, groupable=True)
        gd.configure_selection(selection_mode='multiple', use_checkbox=True)
        gdOptions = gd.build()
        AgGrid(load_data(), gridOptions=gdOptions)

    # Read CSV file
    # df = pd.read_csv("student.csv")

    @st.cache_data()
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    csv = convert_df(df)

    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='student.csv',
        mime='text/csv',
    )


# Nav bar on selection
if navmenu_selected == 'Home':
    trx_comp()
    st.markdown('<h2 style="color:red;"">Home</h2>', unsafe_allow_html=True)
if navmenu_selected == 'Upload':
    trx_comp()
    # AgGrid(load_data(),default)
