import base64
import json
import pandas as pd
import streamlit as st
from jwt_generator  import  *
class Person:
    def __init__(self, name, title, department, phone):
        self.name = name
        self.title = title
        self.department = department
        self.phone = phone


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
        "title": person.title,
        "department": person.department,
        "phone": person.phone
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


def get_user_claims(token):
    isValid = is_valid_jwt(token, "your_secret_key")
    if isValid == True:
        user_id = read_jwt_token(token)[0]
        # token_expiry_date = datetime.fromtimestamp(read_jwt_token(token)[1])
        return user_id, read_jwt_token(token)[1]
    else:
        return None, None

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
