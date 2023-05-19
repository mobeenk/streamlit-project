import duckdb
import pandas as pd

# create a connection to a new, in-memory database
con = duckdb.connect()

# create a pandas dataframe with some data
# data = {'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']}
csv_data = pd.read_csv('student.csv')
df = pd.DataFrame(csv_data)

# write the dataframe to the database
con.register('mytable', df)

# run a SQL query on the table
result = con.execute("SELECT * FROM mytable WHERE name LIKE 'A%'")

# convert the query results to a pandas dataframe
df_result = result.fetchdf()

# print the query results
print(df_result)
