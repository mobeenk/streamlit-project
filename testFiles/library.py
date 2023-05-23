import streamlit as st
import pandas as pd


def prt():
    print("Test")


def tabs():
    tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

    with tab1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

    with tab2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

    with tab3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


def build_string(str_list):
    # Use the join() method to concatenate the strings in the list into a single string
    result_string = ", ".join(str_list)

    # Return the resulting string
    return result_string


def join_strings(arr):
    return ', '.join(arr)


def get_column_names(file):
    # Read CSV file
    df = pd.read_csv(file)
    # Extract column names
    column_names = list(df.columns)
    first_column = df.iloc[:, 0].to_numpy()
    return column_names, first_column


def query_build(selection, f1, f2, f3):
    result = """
        select {} from
        t1
        where filter in ({} or 1=1 )
        and data between {} and {} 
    """.format(selection, f1, f2, f3)
    return result


def query_build(selection, customer_list, trx_from, trx_to, cr_dr_id, posting, trx_bkey):
    trx_q = """
        select {} from
        t1
        where (customer in ({}) or 1={} )
        and transacion_post_date between {} and {} 
        and (Cr_Dr_ind = {} or 'All'='{}')
        and (posting = {} or 'All'='{}')
        and (Transaction_BKey = '{}' or 'All' = '{}')
        
    """.format(selection
               , customer_list, customer_list
               , trx_from, trx_to
               , cr_dr_id, cr_dr_id
               , posting, posting
               , trx_bkey, trx_bkey
               )
    return trx_q