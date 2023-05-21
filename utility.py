import json

import pandas as pd


class Person:
    def __init__(self, name, title):
        self.name = name
        self.title = title


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