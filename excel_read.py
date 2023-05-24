import streamlit as st
import pandas as pd


# pip install xlrd
def main():
    st.title("Excel File Upload and Display")
    st.header("Upload Excel File")
    uploaded_file = st.file_uploader("Choose an Excel file")
    if uploaded_file is not None:
        df1 = pd.read_excel(uploaded_file)
        st.dataframe(df1)


if __name__ == "__main__":
    main()
