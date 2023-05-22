import pandas as pd
import os
import Insert, LookUp, Update, Delete, UserSQL

pd.set_option('display.colheader_justify', 'center')

while True:
    sel = input(
        """Menu
           1. Look up a cinematographic work in the database
           2. Look up a quote in the database
           3. Insert a cinematographic work
           4. Insert a quote
           5. Update cinematographic works
           6. Update quotes
           7. Delete a cinematographic work
           8. Delete a quote
           9. Write your own SQL query (advanced)
           Enter your selection or 0 to exit: """)
    os.system('cls')
    match sel:
        case '0': os.system('cls'); break
        case '1': LookUp.lookUpSetUp("Works")
        case '2': LookUp.lookUpSetUp("Quotes")
        case '3': Insert.insertCinematographicWork()
        case '4': Insert.insertQuote()
        case '5': Update.updateSetUp("Works")
        case '6': Update.updateSetUp("Quotes")
        case '7': Delete.deleteSetUp("Works")
        case '8': Delete.deleteSetUp("Quotes")
        case '9': UserSQL.runQuery()
    os.system('cls')