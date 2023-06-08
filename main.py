import pandas as pd

data = {
    'ID': [11, 22, 33],
    'Name': ["Ahmad Sammer", "Jonny b", "Omar c"]
}

df = pd.DataFrame(data)

# Print the DataFrame
print(df)

# Create a list of dictionaries with integer keys and name values
records_list = [{row['ID']: row['Name']} for _, row in df.iterrows()]

# Print the records list
print(records_list)
