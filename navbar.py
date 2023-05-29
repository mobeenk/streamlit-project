from datetime import datetime

import streamlit as st
from streamlit_option_menu import option_menu

# 1. as sidebar menu
# with st.sidebar:
#     selected = option_menu("Main Menu", ["Home", 'Settings'],
#         icons=['house', 'gear'], menu_icon="cast", default_index=1)
#     selected

# 2. horizontal menu
def Navbar2(menu_list):
    selected2 = option_menu(None, menu_list ,
        icons=['house', 'cloud-upload', "list-task", 'gear'],
        menu_icon="cast", default_index=0, orientation="horizontal"
          , styles="black"                 )
    return selected2

# 3. CSS style definitions

def Navbar3(menu_list):
    selected3 = option_menu(None, menu_list,
        icons=['house', 'cloud-upload', "list-task", 'gear'],
        menu_icon="cast", default_index=0, orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {"color": "black","font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "green"},
        }
    )
    return selected3

def page_head(username, token_expiry):

    int_timestamp = int(token_expiry.timestamp())*1000 # 1685015047 * 1000 to milisecond
    html_css_page = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed&display=swap" rel="stylesheet">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" rel="stylesheet">
      <script>
            document.addEventListener('DOMContentLoaded', function() {{
            function doDate()
                {{
                    var str = "";
                    var days = new Array("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday");
                    var months = new Array("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December");
                    var now = new Date(); 
                    var secs = now.getSeconds() <=9  ? "0"+now.getSeconds(): now.getSeconds()
                    var mins = now.getMinutes() <=9  ? "0"+now.getMinutes(): now.getMinutes()
                    var hours =  now.getHours() <=9  ? "0"+now.getHours(): now.getHours()
                    str +=  days[now.getDay()] + ", " + now.getDate() + " " + months[now.getMonth()] + " " + now.getFullYear() + " " 
                    + hours +":" + mins + ":" + secs;
                    document.getElementById("todaysDate").innerHTML = str;
                }}
                setInterval(doDate, 1000);
            }});
            var countDownDate = {int_timestamp};
            // Update the count down every 1 second
            var x = setInterval(function() {{
              // Get today's date and time
              var now = new Date().getTime();
              // Find the distance between now and the count down date
              var distance = countDownDate - now;

              var days = Math.floor(distance / (1000 * 60 * 60 * 24));
              var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
              var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
              var seconds = Math.floor((distance % (1000 * 60)) / 1000);
            
              // Display the result in the element with id="demo"
              document.getElementById("demo").innerHTML = days + "d " + hours + "h "
              + minutes + "m " + seconds + "s ";
            
              // If the count down is finished, write some text
              if (distance < 0) {{
                clearInterval(x);
                document.getElementById("demo").innerHTML = "EXPIRED";
                document.getElementById("demo").style.color = 'red';
              }}
              else {{
                document.getElementById("demo").style.color = 'green';
              }}
            }}, 1000);
      </script>
      <style>
        .flex-container {{
          display: flex;
          flex-direction: row;
          flex-wrap: nowrap;
          justify-content: space-between;
          align-items: stretch;
          align-content: normal;
          background-color: white; 
          border-radius: 10px;
          margin-bottom: -50px;
        }}
        .flex-items {{
          /* background-color: orange; */
        }}
        .flex-items-text {{
            color: black;
            font-size: 20px;
            font-weight: bold;
            padding: 15px;
            font-family:'Barlow Condensed', sans-serif;
        }}
        .bg {{
            background: rgb(240,240,207);
            background: linear-gradient(221deg, rgba(240,240,207,1) 0%, rgba(255,255,255,1) 100%);
            index:-5;
            margin:10px; 
            border-radius: 15px;
            box-shadow: 7px 2px 9px -7px rgba(0,0,0,0.75);
        }}
      </style>
    </head>
    <body>
      <div class="flex-container">
           <div class="flex-items" >
             <img class="my-image" src="https://www.saib.com.sa/sites/default/files/logo.png" alt="Logo">
           </div>
           <div class="flex-items flex-items-text bg">Welcome, 
                <span style="color: #C09C20;">{username}</span>
                <div id="todaysDate"></div>
                <div><i class="fas fa-star"></i>
                    Session Expire in: <span id="demo"></span>
                </div>
           </div>
        </div>
    </body>
    </html>
    """
    return html_css_page


def notfound_page(title):
    html_css_page = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <title>401 Unauthorized</title>
      <style>
        body {{
          font-family: Arial, sans-serif;
          margin: 0;
        }}

        .container {{
          margin-top: -50px;
          height: 80vh;
          background-color: #ffffcc;
          border-radius: 5px;
          box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          text-align: center;
        }}

        h1 {{
          font-size: 36px;
          color: red;
          margin-bottom: 20px;
        }}

        p {{
          font-size: 20px;
          color: #777;
          margin-bottom: 20px;
        }}

        .support-link {{
          display: inline-block;
          color: white !important;
          background-color:  #C09C20;;
          padding: 10px 20px;
          border-radius: 4px;
          text-decoration: none;
        }}
      </style>
    </head>
    <body>
      <div class="container">
        <h1>{title}</h1>
        <p>You are not authorized to access this page.</p>
        <p>Please contact support for assistance.</p>
        <a href="mailto:support@example.com" class="support-link">Contact Support</a>
      </div>
    </body>
    </html>
    """

    return html_css_page


def remove_component():
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
                url: 'your-api-url',
                type: 'DELETE',
                success: function(response) {{
                  // Handle the success response
                  console.log('API request successful');
                }},
                error: function(xhr, status, error) {{
                  // Handle the error response
                  console.error('API request failed:', error);
                }}
              }});
            }}
          }});
        }});
      </script>
    </head>
    <body>
      <button id="removeButton">Remove Plan</button>
    </body>
    </html>
    """

    return html_code