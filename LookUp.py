from Connections import dbConnect
from tabulate import tabulate
import pandas as pd

def dbLookup(table, conditions):
    cnxn = dbConnect()
    cursor = cnxn.cursor()
    sql = "SELECT * FROM %s" % table
    if conditions != "":
        sql += " WHERE " + conditions
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        return rows
    except Exception as e:
        print(f"Lookup failed. {e}")
        input("Press any key to continue...")
        cursor.close()

def lookUpSetUp(table):
    columns = {'Works': ('Work_ID', 'Title', 'Director', 'Type', 'Year', 'Genre_1', 'Genre_2', 'Genre_3'),
               'Quotes': ('Quote_ID', 'Quote', 'Character', 'Season', 'Episode', 'Timestamp', 'Work_ID')}
    df = pd.DataFrame({"Column": columns[table]})
    print("Columns in the Works table:")
    print(tabulate(df.T, tablefmt='psql', showindex=False, colalign=['center']*len(df.columns)))
    sel = str.lower(input("Enter the column to filter by or * to display all rows: "))
    if(sel == '*'): conditions = ""
    else:
        numericFields = ('work_id', 'year', 'quote_id', 'season', 'episode', 'timestamp')
        filterVal = input("Enter the value to filter by: ")
        if(sel not in numericFields):
            conditions = sel + " LIKE '%" + filterVal + "%'"
        else: conditions = sel + " = '" + filterVal + "'"
    rows = dbLookup(table, conditions)
    if(rows == None or len(rows) == 0):
        print("No matching values found")
        input("Press any key to continue...")
        return
    df = pd.DataFrame((tuple(row) for row in rows), columns=columns[table])
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False, colalign=['center']*len(df.columns)))
    input("Press any key to continue...")