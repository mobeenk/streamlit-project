import pyodbc


def execute_stored_procedure(server, database, username, password, procedure_name, params=None):
    # params = ['field1','f2','f3']
    # Set up the connection parameters
    driver = '{ODBC Driver 17 for SQL Server}'  # Driver name may vary based on your system

    # Establish the connection
    connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    conn = pyodbc.connect(connection_string)

    # Create a cursor object
    cursor = conn.cursor()

    try:
        # Prepare the parameter string for the stored procedure
        param_string = ', '.join([f'@{param}' for param in params]) if params else ''

        # Prepare the SQL statement with the parameter placeholders
        sql = f"EXEC {procedure_name} {param_string}"

        # Execute the stored procedure
        cursor.execute(sql)

        # Get the return value
        return_value = cursor.fetchval()

        # Return the value
        return return_value

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()
