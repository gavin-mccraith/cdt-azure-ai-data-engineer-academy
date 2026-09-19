import pyodbc

connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost,1433;"
    "DATABASE=GreenLeafRetail;"
    "UID=sa;"
    "PWD=GIZMOBraxmawn5$;"
    "TrustServerCertificate=yes;"
)

try:

    connection = pyodbc.connect(connection_string)

    print("Connected successfully!")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM DailySales")

    for row in cursor.fetchall():
        print(row)

    row = cursor.fetchone()

    print(row[0])

    connection.close()

except Exception as ex:

    print(ex)
