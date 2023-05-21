
import pandas as pd
from library import *
# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('../student.csv')

# Save the column names into an array
column_names = df.columns.values
# Use the st.multiselect widget to display the list of column names to the user
selected_column_names = st.multiselect('Select the columns:', column_names)