from Connections import dbConnect
from tabulate import tabulate
import pandas as pd
import LookUp

def dbDelete(table, conditions):
    cnxn = dbConnect()
    cursor = cnxn.cursor()
    rows = LookUp.dbLookup(table, conditions)
    if(rows == None or len(rows) == 0):
        print("No matching values found")
        input("Press any key to continue...")
        return
    columns = {'Works': ('Work_ID', 'Title', 'Director', 'Type', 'Year', 'Genre_1', 'Genre_2', 'Genre_3'),
               'Quotes': ('Quote_ID', 'Quote', 'Character', 'Season', 'Episode', 'Timestamp', 'Work_ID')}
    print("The following rows will be deleted:")
    df = pd.DataFrame((tuple(row) for row in rows), columns=columns[table])
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False, colalign=['center']*len(df.columns)))
    sel = str.lower(input("Continue? (y/n): "))
    if(sel != 'y'): return
    sql = "DELETE FROM %s WHERE %s" % (table, conditions)
    try:
        cursor.execute(sql)
        cnxn.commit()
        cursor.close()
        print("Delete successful")
        input("Press any key to continue...")
    except Exception as e:
        print(f"Delete failed. {e}")
        input("Press any key to continue...")
        cursor.close()

def deleteSetUp(table):
    ids = input("Enter the IDs of the works to delete, separated by spaces (0 to return to main menu): ").split()
    if(ids[0] == '0'): return
    if table == "Works": conditions = "Work_ID IN ('" + "', '".join(ids) + "')"
    else: conditions = "Quote_ID IN (" + ", ".join(ids) + ")"
    dbDelete(table, conditions)