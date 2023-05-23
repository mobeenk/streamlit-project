import base64
import json
import pandas as pd
import streamlit as st
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


