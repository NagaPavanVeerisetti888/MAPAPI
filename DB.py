# import pandas as pd
# import pyodbc
# # Define your connection parameters
# server = 'lvdms-dev.database.windows.net'
# database = 'lvdms'
# username = 'nagaveerisetti@bftg.com'
# driver = '{ODBC Driver 17 for SQL Server}'
# # Connect to the database using interactive authentication
# try:
#     connection = pyodbc.connect(
#         f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};Authentication=ActiveDirectoryInteractive;'
#     )
#     # Fetch data into a DataFrame
#     df = pd.read_sql('SELECT * FROM MAP.User_Master', connection)
#     # Display the DataFrame
#     print(df)
# except Exception as e:
#     print("Error:", e)
# finally:
#     # Close the connection
#     connection.close()

import pyodbc

server = 'lvdms-dev.database.windows.net'
database = 'LVDMS'
username = 'saikrishna@bftg.com'
password = 'Floridasummer@11'

connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};Authentication=ActiveDirectoryPassword;'

try:
    connection = pyodbc.connect(connection_string)

    cursor = connection.cursor()

    cursor.execute('SELECT * FROM MAP.User_Master')

    rows = cursor.fetchall()
    for row in rows:
        print(row)

except Exception as e:
    print("Error:", e)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()