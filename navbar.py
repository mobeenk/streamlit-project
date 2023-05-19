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
        menu_icon="cast", default_index=0, orientation="horizontal")
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