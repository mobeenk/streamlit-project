import sys
from pathlib import Path
from common import *
from utility import *
import streamlit as st
from DAL.data_access import getStaffList, getClientsList, view_report_by_id

general_settings()


def render_view_report():
    # Use Font Awesome icons in your Streamlit app
    # st.markdown('<i class="fas fa-star"></i>', unsafe_allow_html=True)
    extracted_value = get_query_param_by_name('id')
    df = view_report_by_id(extracted_value)  # pd.read_csv("pages/callreports.csv")

    record = df.query(f"id == {extracted_value}")
    # df2 = df[df['id'] == '3']
    # Generate HTML tables
    html_table_1 = "<div style='display: inline-block; text-align: left; color:black; margin-top:20px;'>"
    html_table_1 += "<table>"
    html_table_1 += "<tr>" \
                    "<th class='th-style'>Name</th>" \
                    "<th class='th-style'>Title</th>" \
                    "<th class='th-style'>Department</th>" \
                    "<th class='th-style'>Phone</th>" \
                    "</tr>"
    for person in getStaffList():
        html_table_1 += f"<tr>" \
                        f"<td class='td-stylex'>{person.name}</td>" \
                        f"<td class='td-stylex'>{person.title}</td>" \
                        f"<td class='td-stylex'>{person.department}</td>" \
                        f"<td class='td-stylex'>{person.phone}</td>" \
                        f"</tr>"
    html_table_1 += "</table>"
    html_table_1 += "</div>"

    html_table_2 = "<div style='display: inline-block; text-align: left; color:black;margin-top:2px;'>"

    html_table_2 += "<table>"
    html_table_2 += "<tr>" \
                    "<th class='th-style'>Name</th>" \
                    "<th class='th-style'>Title</th>" \
                    "<th class='th-style'>Department</th>" \
                    "<th class='th-style'>Phone</th>" \
                    "</tr>"
    for person in getClientsList():
        html_table_2 += f"<tr>" \
                        f"<td class='td-stylex'>{person.name}</td>" \
                        f"<td class='td-stylex'>{person.title}</td>" \
                        f"<td class='td-stylex'>{person.department}</td>" \
                        f"<td class='td-stylex'>{person.phone}</td>" \
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
      </style>
    </head>
    <body>
      <div class="report" style="background: radial-gradient(circle at 18.7% 37.8%, rgb(250, 250, 250) 0%, rgb(225, 234, 238) 90%);;border-radius:10px; box-shadow: 0 8px 6px -6px black;">
        <div class="report-header">Call Report View</div>
        <div class="report-columns">
          <div class="report-field">
            <span class="field-label">RM Name:</span>
            <span class="field-value">{record.iat[0, 3]}</span>
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
              <span class="field-label">Next Call Date:</span>
              <span class="field-value">{record.iat[0, 13]}</span>
            </div>
            <div class="report-field">
              <span class="field-label"></span>
              <span class="field-value"></span>
            </div>
            <div class="report-field">
              <span class="field-label">Called List:</span>
              <div class="field-value">{html_table_1}</div>
            </div>
            <div class="report-field" >
              <span class="field-label">Calling List:</span>
              <div class="field-value" style="margin-top:18px;">{html_table_2}</div>
            </div>
        </div>
        <div class="report-field">
          <span class="field-label">Call Objective:</span>
          <span class="field-value">{record.iat[0, 10]}</span>
        </div>
        <div class="report-field">
          <span class="field-label">Points of Discussion:</span>
          <span class="field-value">{record.iat[0, 11]}</span>
        </div>
        <div class="report-field">
          <span class="field-label">Actionable Items:</span>
          <span class="field-value">{record.iat[0, 12]}</span>
        </div>
      </div>
    </body>
    </html>
    """

    # st.write(df2['name'])
    st.markdown(html_markdown2, unsafe_allow_html=True)


# only if authorized open the page
is_authorized(render_view_report)
