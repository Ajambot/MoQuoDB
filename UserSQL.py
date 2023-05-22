from Connections import dbConnect
from tabulate import tabulate
import pandas as pd

# Lets the user run a custom SQL query
def runQuery():
    cnxn = dbConnect()
    cursor = cnxn.cursor()
    while True:
        sql = input("Enter your SQL query or 0 to return to main menu: ")
        if sql == '0': break
        try:
            cursor.execute(sql)
            if sql[:6].lower() == "select":
                rows = cursor.fetchall()
                columns = [column[0] for column in cursor.description]
                df = pd.DataFrame((tuple(row) for row in rows), columns=columns)
                print(tabulate(df, headers='keys', tablefmt='psql', showindex=False, colalign=['center']*len(df.columns)))
        except Exception as e:
            print(f"Query failed. {e}")
            input("Press any key to continue...")
    cnxn.commit()
    cursor.close()