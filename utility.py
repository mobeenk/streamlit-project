import base64
import json
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder
class Person:
    def __init__(self, name, title):
        self.name = name
        self.title = title
        # self.department = department
        # self.phone = phone


def person_to_dict(person):
    """
       Converts person class object to dictionary type in order to make it serializable for json.

       Parameters:
           person: Person class object

       Returns:
           return the object as dictionary.
       """
    return {
        "name": person.name,
        "title": person.title
        # "department": person.department,
        # "phone": person.phone
    }
def json_to_dataframe(json_data):
    """
           Converts any valid json to pandas dataframe, make sure the json passed is cohherent with no lists.

           Parameters:
               json_data: any json format type object

           Returns:
               return the json as dataframe for pandas.
           """
    # Load JSON data into a Python dictionary
    data_dict = json.loads(json_data)
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data_dict)
    return df

@st.cache_resource()
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()



def show_grid(addurl, editurl,  df, cellsytle_jscode):
    edit_column = df['id'].copy()
    edit_column.rename('edit', inplace=True)
    # df_new = pd.concat([new_column, df], axis=1)

    # remove_column = df['id'].copy()
    # remove_column.rename('remove', inplace=True)
    df_new = pd.concat([edit_column, df], axis=1)

    id_injectJs = InjectJSCode(addurl, "👁️")
    edit_injectJs = InjectJSCode(editurl, "️✏️")
    # remove_injectJs = InjectJSCode(removeurl, "️❌")

    gd = GridOptionsBuilder.from_dataframe(df_new)
    gd.configure_pagination(enabled=True, paginationAutoPageSize=False, paginationPageSize=10)
    gd.configure_column( "id", "View", cellRenderer=JsCode(id_injectJs))
    gd.configure_column("edit", "Edit", cellRenderer=JsCode(edit_injectJs))
    # gd.configure_column("remove", "Edit", cellRenderer=JsCode(remove_injectJs))
    gd.configure_column("status", cellStyle=cellsytle_jscode)
    gd.configure_side_bar(filters_panel=True)

    gd.configure_columns(df_new.columns, width=30)
    gd.configure_column("id", width=20)
    gd.configure_column("edit", width=20)
    # gd.configure_default_column(editable=True, groupable=True)
    # gd.configure_selection(selection_mode='multiple', use_checkbox=True)
    gdOptions = gd.build()
    # df = load_data()
    custom_css = {
        ".ag-row-hover": {"background-color": " #C09C20 !important"},
    }
    AgGrid(df_new
           , gridOptions=gdOptions
           , allow_unsafe_jscode=True
           , enable_enterprise_modules=True
           , theme="streamlit"
           , enable_quicksearch=True
           , reload_data=True
           , fit_columns_on_grid_load=True
           , custom_css=custom_css,
           )


#
def InjectJSCode(url, icon):
    injected_javascript = f"""
            class UrlCellRenderer {{
                init(params) {{
                    this.eGui = document.createElement('a');
                    this.eGui.innerText = "{icon}";
                    this.eGui.setAttribute('title', params.value);
                    this.eGui.setAttribute("href", "{url}" + params.value);
                    this.eGui.setAttribute('style', "text-decoration:underline");
                    this.eGui.setAttribute('style', "color:white");
                    this.eGui.setAttribute('target', "_blank");

                }}
                getGui() {{
                    return this.eGui;
                }}
            }}
        """
    return injected_javascript
