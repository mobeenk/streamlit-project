import pyodbc
import pandas as pd


def call_stored_procedure_get(server, database, stored_procedure, *args):
    """
    Calls a stored procedure in a SQL Server database and returns the result as a pandas DataFrame.

    Args:
        server (str): The name or IP address of the SQL Server.
        database (str): The name of the database.
        stored_procedure (str): The name of the stored procedure to call.
        *args: Variable number of arguments to pass to the stored procedure.

    Returns:
        pandas.DataFrame: A DataFrame containing the result of the stored procedure.

    Raises:
        pyodbc.Error: If an error occurs while executing the stored procedure.

    Example:
        >>> server_name = 'localhost'
        >>> database_name = 'my_database'
        >>> procedure = 'get_customers'
        >>> status = 'active'
        >>> city = 'New York'
        >>> df = call_stored_procedure_get(server_name, database_name, procedure, status, city)
        >>> print(df)
           CustomerID     Name             Email
        0           1  John Doe  john.doe@example.com
        1           2  Jane Doe  jane.doe@example.com

    """
    # Establish a connection to the SQL Server using Windows authentication
    conn = pyodbc.connect(
        f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes"
    )
    # Create a cursor object to interact with the database
    cursor = conn.cursor()
    try:
        # Execute the stored procedure with the given arguments
        cursor.execute(f"EXEC {stored_procedure} {','.join(map(str, args))}")
        # Fetch all the rows returned by the stored procedure
        rows = cursor.fetchall()
        # Get the column names from the cursor's description
        columns = [column[0] for column in cursor.description]

        # Close the cursor and connection
        cursor.close()
        conn.close()

        # Create a list of dictionaries, each representing a row with column names
        result = []
        for row in rows:
            result_row = dict(zip(columns, row))
            result.append(result_row)

        # Create a DataFrame from the result
        df = pd.DataFrame(result)
        return df

    except pyodbc.Error as e:
        # Handle any errors that occur during execution
        cursor.close()
        conn.close()
        raise e


def execute_insert_procedure_master(server, database, procedure_name, inputs):
    """
    Executes an insert stored procedure in a SQL Server database and returns the new record ID.

    Args:
        server (str): The name or IP address of the SQL Server.
        database (str): The name of the database.
        procedure_name (str): The name of the insert stored procedure.
        inputs (tuple): The input parameters for the stored procedure.

    Returns:
        int: The ID of the newly inserted record.

    Raises:
        pyodbc.Error: If an error occurs while executing the stored procedure.

    Example:
        >>> server_name = 'localhost'
        >>> database_name = 'my_database'
        >>> procedure = 'insert_customer'
        >>> inputs = ('John Doe', 'john.doe@example.com')
        >>> new_record_id = execute_insert_procedure_master(server_name, database_name, procedure, inputs)
        >>> print(new_record_id)
        12345

    """
    # Connect to the SQL Server
    conn = pyodbc.connect(
        f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes"
    )

    # Create a cursor to execute SQL statements
    cursor = conn.cursor()

    try:
        # Define the parameters for the stored procedure
        params = (inputs,)

        # Execute the stored procedure with the provided name and parameters
        cursor.execute(f"{{CALL {procedure_name}(?)}}", params)

        # Fetch the new record ID
        new_record_id = cursor.fetchone()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        # Return the new record ID
        return new_record_id[0]

    except pyodbc.Error as e:
        # Handle any errors that occur during execution
        cursor.close()
        conn.close()
        raise e


def execute_insert_procedure_details(server, database, procedure_name, inputs):
    """
    Executes an insert procedure with multiple parameter sets in a SQL Server database.

    Args:
        server (str): The name or IP address of the SQL Server.
        database (str): The name of the database.
        procedure_name (str): The name of the insert procedure to execute.
        inputs (tuple): A tuple of parameter sets to pass to the stored procedure.

    Raises:
        pyodbc.Error: If an error occurs while executing the stored procedure.

    Example:
        >>> server_name = 'localhost'
        >>> database_name = 'my_database'
        >>> procedure = 'insert_order'
        >>> inputs = (
        ...     (1001, '2022-01-01', 'Product A', 2),
        ...     (1002, '2022-02-01', 'Product B', 5)
        ... )
        >>> execute_insert_procedure_details(server_name, database_name, procedure, inputs)

    """
    conn = pyodbc.connect(
        f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes"
    )
    cursor = conn.cursor()
    for params in inputs:
        # Execute the stored procedure with the provided name and parameters
        cursor.execute(f"{{CALL {procedure_name}({', '.join(['?'] * len(params))})}}", params)
    cursor.close()
    conn.close()


# USE [Northwind]
# GO
# /****** Object:  StoredProcedure [dbo].[InsertDrink]    Script Date: 6/7/2023 9:48:05 PM ******/
# SET ANSI_NULLS ON
# GO
# SET QUOTED_IDENTIFIER ON
# GO
# ALTER PROCEDURE [dbo].[InsertDrink]
#     @DrinkName VARCHAR(100),
#     @NewDrinkID INT OUTPUT
# AS
# BEGIN
#     SET NOCOUNT ON;
#
#     INSERT INTO Drinks (DrinkName)
#     VALUES (@DrinkName);
#
#     SET @NewDrinkID = SCOPE_IDENTITY();
#   SELECT @NewDrinkID AS NewDrinkID
# END
