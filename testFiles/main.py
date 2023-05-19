import streamlit as st
import json
import pandas as pd

# Load the data from the JSON file
with open('people.json') as f:
    data = json.load(f)

# Convert the data to a Pandas DataFrame
df = pd.DataFrame(data['people'])

# Display the data in a table
st.table(df)

# Add a button to export the table as an Excel file
if st.button('Export to Excel'):
    file_name = 'people.xlsx'
    df.to_excel(file_name, index=False)
    st.success(f'Table exported to {file_name}!')


