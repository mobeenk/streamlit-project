import time
import datetime
from datetime import date, timedelta
import streamlit as st
from DAL.data_access import *
from common import get_query_param_by_name, is_token_authorized
from navbar import notfound_page

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")


def render_edit_page():
    extracted_value = get_query_param_by_name('id')
    st.markdown("<h1 style=\"color: #C09C20\">Edit plan #" + str(extracted_value) + "</h1>", unsafe_allow_html=True)

    plan_data = get_plan_by_id(extracted_value)
    record = json.loads(plan_data)
    # st.write(record['client_cif'])

    st.write("Client CIF")
    r1c1, r1c2 = st.columns(2)
    if 'jsonobj' not in st.session_state:
        st.session_state.jsonobj = {}

    client_cif = r1c1.text_input("Client CIF :", value=record['client_cif'], label_visibility="collapsed", disabled=True)
    if r1c2.button("Show Client Info"):
        st.session_state.jsonobj = fetch_client_data(client_cif)
        # st.json(data)
        # st.write(jsonobj['Client CIF'])

    # index = get_purpose_options().index(record['purpose'])
    # purpose = st.selectbox("Purpose", get_purpose_options(), key='purposethis', index=index)
    purpose = st.text_input("Purpose", value=record['purpose'], key='purposethis')

    default_date_str = record['expected_call_date']  # Date string
    default_date = datetime.datetime.strptime(default_date_str, '%Y-%m-%d').date()
    # today = date.today()
    # default_date_yesterday = today - timedelta(days=1)
    expected_call_date = st.date_input("Select Expected Call Date", default_date)
    # sot = st.text_input("Enter SOT")

    submit_button = st.button('Submit')
    if submit_button:
        # Print submitted values
        st.session_state.jsonobj = fetch_client_data(client_cif)
        with st.spinner(text='in progress'):
            time.sleep(1)

            st.success('Updated a new Call Plan Successfully.')
            data = {
                "rm_id": "selected_rm_result",
                "client_name": st.session_state.jsonobj['Client CIF'],
                "client_cif": st.session_state.jsonobj['Client CIF'],
                "client_sot": st.session_state.jsonobj['Client SOT'],
                "client_outstanding": st.session_state.jsonobj['Client Outstanding'],
                "purpose": purpose,
                "expected_call_date": str(expected_call_date),
                "create_date": record['purpose'],
                "created_by": record['purpose']
            }
            save_plan(
                data
            )

            st.json(json.dumps(data))


# only if authorized open the page
if is_token_authorized():
    render_edit_page()
else:
    st.markdown(notfound_page("You are not authorized to edit this plan"), unsafe_allow_html=True)

