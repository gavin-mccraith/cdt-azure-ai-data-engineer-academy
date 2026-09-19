import csv
import logging
import shutil
import pyodbc

from config import *

logging.basicConfig(
    filename="logs/import.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

connection = None

try:
    connection_string = (
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={SQL_SERVER};"
        f"DATABASE={SQL_DATABASE};"
        f"UID={SQL_USERNAME};"
        f"PWD={SQL_PASSWORD};"
        "TrustServerCertificate=yes;"
    )

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    with open(
        "daily-sales.csv",
        newline="",
        encoding="utf-8-sig"
    ) as csv_file:

        reader = csv.DictReader(csv_file)

        for row in reader:

            if not row["StoreName"]:
                continue

            if int(row["Quantity"]) <= 0:
                continue

            cursor.execute(
                """
                INSERT INTO DailySales
                (StoreName, Product, Quantity, SaleDate)
                VALUES (?, ?, ?, ?)
                """,
                row["StoreName"],
                row["Product"],
                int(row["Quantity"]),
                row["SaleDate"]
            )

    connection.commit()

    shutil.move(
        "daily-sales.csv",
        "archive/daily-sales.csv"
    )

    logging.info("Import completed successfully.")
    print("Import Complete")

except Exception as ex:
    logging.error("Import failed: %s", ex)
    print(f"Import failed: {ex}")

finally:
    if connection is not None:
        connection.close()
