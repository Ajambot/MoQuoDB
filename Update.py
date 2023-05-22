from Connections import dbConnect
from tabulate import tabulate
import pandas as pd
import LookUp

def dbUpdate(table, newVals, conditions):
    cnxn = dbConnect()
    cursor = cnxn.cursor()
    rows = LookUp.dbLookup(table, conditions)
    columns = {'Works': ('Work_ID', 'Title', 'Director', 'Type', 'Year', 'Genre_1', 'Genre_2', 'Genre_3'),
               'Quotes': ('Quote_ID', 'Quote', 'Character', 'Season', 'Episode', 'Timestamp', 'Work_ID')}
    print("The following rows will be updated:")
    df = pd.DataFrame((tuple(row) for row in rows), columns=columns[table])
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False, colalign=['center']*len(df.columns)))
    sel = str.lower(input("Continue? (y/n): "))
    if(sel != 'y'): return
    sql = "UPDATE %s SET %s WHERE %s" % (table, newVals, conditions)
    try:
        cursor.execute(sql)
        cnxn.commit()
        cursor.close()
        print("Update successful")
        input("Press any key to continue...")
    except Exception as e:
        print(f"Update failed. {e}")
        input("Press any key to continue...")
        cursor.close()

def updateSetUp(table):
    ids = input("Enter the IDs of the " + table.lower() + " to update, separated by spaces (0 to return to main menu): ").split()
    if(ids[0] == '0'): return
    columns = {'Works': ('Work_ID', 'Title', 'Director', 'Type', 'Year', 'Genre_1', 'Genre_2', 'Genre_3'),
               'Quotes': ('Quote_ID', 'Quote', 'Character', 'Season', 'Episode', 'Timestamp', 'Work_ID')}
    df = pd.DataFrame({"Column": columns[table]})
    print("Columns in the Works table:")
    print(tabulate(df.T, tablefmt='psql', showindex=False, colalign=['center']*len(df.columns)))
    newVals = input("Enter the columns to update and the new values in the format (column1=numValue1, column2='strValue', etc.): ")
    if table == "Works": conditions = "Work_ID IN ('" + "', '".join(ids) + "')"
    else: conditions = "Quote_ID IN (" + ", ".join(ids) + ")"
    dbUpdate(table, newVals, conditions)