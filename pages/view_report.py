import sys
from pathlib import Path
import random

from common import *
from components import admin_approval_component, owner_action_component
from utility import *
import streamlit as st
from DAL.data_access import getStaffList, getClientsList, view_report_by_id
import datetime
import streamlit.components.v1 as components

general_settings()
print_date = datetime.datetime.now()
formatted_datetime = print_date.strftime("%Y-%m-%d %H:%M:%S")

def get_report():
    report_id = get_query_param_by_name('id')
    df = view_report_by_id(report_id)
    record = df.query(f"id == {report_id}")
    return record

def render_view_report():
    record = get_report()
    # must get rm_id and check if this user is an admin and a manager of this rm to take action on it

    # df2 = df[df['id'] == '3']
    # Generate HTML tables
    html_table_1 = "<div style='display: inline-block; text-align: left; color:black; margin-top:20px;'>"
    html_table_1 += "<table>"
    html_table_1 += "<tr>" \
                    "<th class='th-style'>Name</th>" \
                    "<th class='th-style'>Title</th>" \
                    "</tr>"
    for person in getStaffList():
        html_table_1 += f"<tr>" \
                        f"<td class='td-stylex'>{person.name}</td>" \
                        f"<td class='td-stylex'>{person.title}</td>" \
                        f"</tr>"
    html_table_1 += "</table>"
    html_table_1 += "</div>"

    html_table_2 = "<div style='display: inline-block; text-align: left; color:black;margin-top:2px;'>"

    html_table_2 += "<table>"
    html_table_2 += "<tr>" \
                    "<th class='th-style'>Name</th>" \
                    "<th class='th-style'>Title</th>" \
                    "</tr>"
    for person in getClientsList():
        html_table_2 += f"<tr>" \
                        f"<td class='td-stylex'>{person.name}</td>" \
                        f"<td class='td-stylex'>{person.title}</td>" \
                        f"</tr>"
    html_table_2 += "</table>"
    html_table_2 += "</div>"

    # Display the HTML tables
    # st.write(html_table_1 + html_table_2, unsafe_allow_html=True)
    png_file = Path("images/saib.png")
    bin_str = get_base64_of_bin_file(png_file)

    html_markdown2 = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <style>
        /* Define the report container */
        td, th {{ border: 1px solid black !important; }}
        .report {{
          border: 1px solid black !important;
          padding: 20px;
          width: 1000px;
          margin: 0 auto;
        }}
        .report:after {{
          border: 1px solid black !important;
          padding: 20px;
          width: 700px;
          margin: 0 auto;
          content: "";
          background-image: url("data:image/png;base64,{bin_str}");
          background-size: 70%;
          background-repeat: no-repeat;
          background-position: center center;
          opacity: 0.1;
          top: 0;
          left: 0;
          bottom: 0;
          right: 0;
          position: absolute;
          z-index: 10;  
        }}

        /* Define the columns layout */
        .report-columns {{
          display: grid;
          grid-template-columns: repeat(2, 1fr);
          grid-gap: 3px;
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
          color: black;
        }}

        /* Define the field value style */
        .field-value {{
          margin-left: 10px;
          color: black; /* Dark yellow color */
          word-wrap: break-word;
        }}

        /* Add hover effect */
        .field-value:hover {{
          /* animation: shine 1s forwards;
          border-radius: 5px; Add border radius 
          padding: 5px; */
        }}

        @keyframes shine {{
          0% {{
            background-color: transparent;
          }}
          50% {{
            background-color: #C09C20;
            color: black;
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
         @keyframes flashing {{
          0% {{
            background-color: #FFD700; /* Golden color */
            box-shadow: 0 0 20px #FFD700, 0 0 20px #FFD700; /* Golden box shadow */
          }}
          50% {{
            background-color: #f1c232; /* Light golden color */
            box-shadow: 0 0 20px #FFD700, 0 0 20px #FFD700; /* Light golden box shadow */
          }}
          100% {{
            background-color: #FFD700; /* Golden color */
            box-shadow: 0 0 20px #FFD700, 0 0 20px #FFD700; /* Golden box shadow */
            
          }}
        }}

        .flashing-effect {{
          animation: flashing 1s infinite;
          padding: 10px;
          border-radius: 20px;
        }}
      </style>
    </head>
    <body>
      <div class="report" style="background-color: #FFFFD5">
        <div class="report-header"><span class='flashing-effect'>{record.iat[0, 1]}<span/></div>
        <div class="report-columns">
          <div class="report-field">
            <span class="field-label">RM Name:</span>
            <span class="field-value">{record.iat[0, 3]}</span>
          </div>
          <div class="report-field">
            <span class="field-label">Report Date:</span>
            <span class="field-value">{record.iat[0, 4]}</span>
          </div>
          <div class="report-field">
            <span class="field-label">From Department:</span>
            <span class="field-value">{record.iat[0, 5]}</span>
          </div>
          <div class="report-field">
            <span class="field-label">Client Name:</span>
            <span class="field-value">{record.iat[0, 6]}</span>
          </div>
          <div class="report-field">
            <span class="field-label">Client Type:</span>
            <span class="field-value">{record.iat[0, 7]}</span>
          </div>
          <div class="report-field">
            <span class="field-label">Referenced By:</span>
            <span class="field-value">{record.iat[0, 8]}</span>
          </div>
          <div class="report-field">
            <span class="field-label">Call Date/Time:</span>
            <span class="field-value">{record.iat[0, 9]}</span>
          </div>
          <div class="report-field">
            <span class="field-label">Place/Venue:</span>
            <span class="field-value">{record.iat[0, 10]}</span>
          </div>
            <div class="report-field">
              <span class="field-label">Next Call Date:</span>
              <span class="field-value">{record.iat[0, 14]}</span>
            </div>
            <div class="report-field">
              <span class="field-label">Manager Remarks</span>
              <span class="field-value">{record.iat[0, 16]}</span>
            </div>
            <div class="report-field">
              <span class="field-label">Clients List</span>
              <div class="field-value">{html_table_1}</div>
            </div>
            <div class="report-field">
              <span class="field-label">Staff List</span>
              <div class="field-value" style="margin-top:18px;">{html_table_2}</div>
            </div>
        </div>
        <div class="report-field">
          <span class="field-label">Call Objective:</span>
          <span class="field-value">{record.iat[0, 11]}</span>
        </div>
        <div class="report-field">
          <span class="field-label">Points of Discussion:</span>
          <span class="field-value">{record.iat[0, 12]}</span>
        </div>
        <div class="report-field">
          <span class="field-label">Actionable Items:</span>
          <span class="field-value">{record.iat[0, 13]}</span>
        </div>
        <p style="color: black;text-align:center;margin-top:50px;font-weight: bold;">Printed on: {formatted_datetime}</p>
      </div>
      
    </body>
    </html>
    """

    # st.write(df2['name'])
    st.markdown(html_markdown2, unsafe_allow_html=True)


# if token was valid
if is_token_authorized():
    token = get_query_param_by_name('token')
    userId, token_expiry, username = get_user_claims(token)
    report_id = get_query_param_by_name('id')
    report_data =  view_report_by_id(report_id) #dataframe
    # if report_data['rm_id'] == userId: #owner

    record = get_report()

    if record.iat[0, 1] == "New" or record.iat[0, 1] == "Returned":
        print(userId)
        print(record.iat[0,15])
        if record.iat[0, 15] == userId:
            components.html(owner_action_component(report_id))
        render_view_report()
    elif record.iat[0, 1] == "Pending Approval":
        if is_user_manager(userId):
            components.html(admin_approval_component(report_id))
        render_view_report()
    elif record.iat[0, 1] == "Completed" :
        render_view_report()
    else:
        st.markdown(notfound_page("You are not authorized to view this request"), unsafe_allow_html=True)

else:
    st.markdown("<h3 style='color:yellow'>Expired Url or Invalid Authentication, Login from CBG portal</h3>"
                "<a href='https://google.com' target='_blank'>Login</a>", unsafe_allow_html=True)

# radial-gradient(circle at 18.7% 37.8%, rgb(250, 250, 250) 0%, rgb(225, 234, 238) 90%);;border-radius:10px; box-shadow: 0 8px 6px -6px black;
