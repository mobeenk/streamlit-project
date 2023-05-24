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

    html_css_page = f"""
    <!DOCTYPE html>
    <html>
    <head>
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
            font-size: 18px;
            font-weight: bold;
            padding: 15px;
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
                <div><i class="fas fa-star"></i>{token_expiry}</div>
           </div>
        </div>
    </body>
    </html>
    """
    return html_css_page
