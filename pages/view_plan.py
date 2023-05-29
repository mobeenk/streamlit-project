import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

qid = st.experimental_get_query_params()
extracted_value = int(qid['q'][0])
# st.write("<h1>Schedule Details for id #{}</h1>".format(extracted_value), unsafe_allow_html=True)

df = pd.read_csv("pages/plans.csv")

record = df.query(f"id == {extracted_value}")
# df2 = df[df['id'] == '3']


html_markdown = f"""
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
        word-wrap: break-word;
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
        color:white;
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
    <div class="report-header">Plan View</div>
    <div class="report-field">
      <span class="field-label">RM:</span>
      <span class="field-value">{record.iat[0, 0]}</span>
    </div>
    <div class="report-field">
      <span class="field-label">Client Name:</span>
      <span class="field-value">{record.iat[0, 1]}</span>
    </div>
    <div class="report-field">
      <span class="field-label">Client CIF:</span>
      <span class="field-value">{record.iat[0, 2]}</span>
    </div>
    <div class="report-field">
      <span class="field-label">Purpose:</span>
      <span class="field-value">{record.iat[0, 3]}</span>
    </div>
    <div class="report-field">
      <span class="field-label">Expected Call Date:</span>
      <span class="field-value">{record.iat[0, 4]}</span>
    </div>
  </div>
</body>
</html>
"""

# st.write(df2['name'])
st.markdown(html_markdown, unsafe_allow_html=True)


def remove_component(pk):
    html_code = f"""
        <!DOCTYPE html>
        <html>
        <head>
          <title>Remove Button</title>
          <style>
            button {{
              padding: 10px 20px;
              background-color: #f44336;
              color: white;
              border: none;
              border-radius: 4px;
              cursor: pointer;
            }}
          </style>
          <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
          <script>
            $(document).ready(function() {{
              // Add click event handler to the remove button
              $('#removeButton').click(function() {{
                // Show the confirm dialog
                var confirmed = confirm("Are you sure you want to delete?");
                if (confirmed) {{
                  // Make the HTTP DELETE request to the API
                  $.ajax({{
                    url: 'https://jsonplaceholder.typicode.com/posts/1',
                    type: 'GET',
                    success: function(response) {{
                       alert('Request has been deleted'+JSON.stringify(response))
                    }},
                    error: function(xhr, status, error) {{
                      alert('Failed')
                      console.log(error)
                    }}
                  }});
                }}
              }});
            }});
          </script>
        </head>
        <body>
          <button style="margin: 25px 0px 0px 120px;" id="removeButton">Remove Plan</button>
        </body>
        </html>
        """

    return html_code


# /* top, right, bottom, left */
# call on delete compoenent
components.html(remove_component(extracted_value))
# components.
