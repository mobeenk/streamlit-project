import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

qid = st.experimental_get_query_params()
extracted_value = int(qid['q'][0])
st.write("<h1>Report Details for id #{}</h1>".format(extracted_value), unsafe_allow_html=True)

df = pd.read_csv("pages/callreports.csv")

record = df.query(f"id == {extracted_value}")
# df2 = df[df['id'] == '3']


# Report content variables
report_date = "May 22, 2023"
from_department = "Marketing Department"
client_name = "John Doe"
client_type = "Premium"
referenced_by = "Jane Smith"
call_date_time = "May 21, 2023 10:00 AM"
the_place = "Conference Room"
called_list = "Person A, Person B, Person C"
calling_list = "Person X, Person Y, Person Z"
call_objective = "Discuss new marketing campaign"
points_of_discussion = "Budget allocation, target audience, creative strategy"
actionable_items = "Assign tasks, set deadlines"

html_markdown2 = f"""
<!DOCTYPE html>
<html>
<head>
  <style>
    /* Define the report container */
    .report {{
      border: 1px solid #ccc;
      padding: 20px;
      width: 1000px;
      margin: 0 auto;
    }}

    /* Define the report header style */
    .report-header {{
      text-align: center;
      font-size: 20px;
      font-weight: bold;
      margin-bottom: 20px;
      background-color: #C09C20; /* Dark yellow background color */
      color: white; /* Text color */
      padding: 10px; /* Add padding for better visual */
    }}

    /* Define the report field style */
    .report-field {{
      margin-bottom: 10px;
    }}

    /* Define the field label style */
    .field-label {{
      font-weight: bold;
    }}

    /* Define the field value style */
    .field-value {{
      margin-left: 10px;
      color: #C09C20; /* Dark yellow color */
    }}

    /* Add hover effect */
    .field-value:hover {{
      animation: shine 1s forwards;
      border-radius: 5px; /* Add border radius */
      padding: 5px;
    }}

    @keyframes shine {{
      0% {{
        background-color: transparent;
      }}
      50% {{
        background-color: #C09C20;
        color: white;
      }}
      100% {{
        background-color: transparent;
      }}
    }}

    /* Add hover effect to Schedule View */
    .report-header:hover {{
      animation: shake 0.5s ease-in-out;
    }}

    @keyframes shake {{
      0% {{
        transform: translateX(0);
      }}
      25% {{
        transform: translateX(-5px);
      }}
      50% {{
        transform: translateX(5px);
      }}
      75% {{
        transform: translateX(-5px);
      }}
      100% {{
        transform: translateX(0);
      }}
    }}
  </style>
</head>
<body>
  <div class="report">
    <div class="report-header">Call Report View</div>
    <div class="report-field">
      <span class="field-label">Today:</span>
      <span class="field-value">{record.iat[0, 0]}</span>
    </div>
    <div class="report-field">
      <span class="field-label">Report Date:</span>
      <span class="field-value">{record.iat[0, 1]}</span>
    </div>
    <div class="report-field">
      <span class="field-label">From Department:</span>
      <span class="field-value">{record.iat[0, 2]}</span>
    </div>
    <div class="report-field">
      <span class="field-label">Client Name:</span>
      <span class="field-value">{record.iat[0, 3]}</span>
    </div>
    <div class="report-field">
      <span class="field-label">Client Type:</span>
      <span class="field-value">{record.iat[0, 4]}</span>
    </div>
    <div class="report-field">
      <span class="field-label">Referenced By:</span>
      <span class="field-value">{record.iat[0, 5]}</span>
    </div>
    <div class="report-field">
      <span class="field-label">Call Date/Time:</span>
      <span class="field-value">{record.iat[0, 6]}</span>
    </div>
    <div class="report-field">
      <span class="field-label">The Place:</span>
      <span class="field-value">{record.iat[0, 7]}</span>
    </div>
    <div class="report-field">
      <span class="field-label">Called List:</span>
      <span class="field-value">{record.iat[0, 0]}</span>
    </div>
    <div class="report-field">
      <span class="field-label">Calling List:</span>
      <span class="field-value">{record.iat[0, 0]}</span>
    </div>
    <div class="report-field">
      <span class="field-label">Call Objective:</span>
      <span class="field-value">{record.iat[0, 8]}</span>
    </div>
    <div class="report-field">
      <span class="field-label">Points of Discussion:</span>
      <span class="field-value">{record.iat[0, 9]}</span>
    </div>
    <div class="report-field">
      <span class="field-label">Actionable Items:</span>
      <span class="field-value">{record.iat[0, 10]}</span>
    </div>
  </div>
</body>
</html>
"""

# st.write(df2['name'])
st.markdown(html_markdown2, unsafe_allow_html=True)
