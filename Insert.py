import pandas as pd
from Connections import driverConnect, dbConnect
from bs4 import BeautifulSoup
from tabulate import tabulate
import LookUp

def dbInsert(table, values):
    cnxn = dbConnect()
    cursor = cnxn.cursor()
    print(values)
    df = pd.DataFrame(data=values, index=[0])
    print("Are you sure you want to insert the following values into the " + table + " table?\n" + tabulate(df, headers='keys', tablefmt='psql', showindex=False, colalign=['center']*len(df.columns)))
    if(input("Enter y to confirm or n to cancel: ") == 'n'): return
    for index, rows in df.iterrows():
        sql = "INSERT INTO " + table + " VALUES"
        sql += "("
        for i in range(len(rows)): sql+= "?, "
        sql = sql[:-2] + ")"
        params = rows.tolist()
        try:
            cursor.execute(sql, params)
            cnxn.commit()
        except Exception as e:
            print(f"Failed to insert row {index}: {e}")
            input("Press any key to continue...")
    cursor.close()
    input("End of insertions. Press any key to continue...")

def insertCinematographicWork():
    imdb = 'https://www.imdb.com/title/tt'
    title_info = ['span', {"class":"sc-afe43def-1 fDTGTb"}]
    director_info = ['ul', {"class":"ipc-metadata-list ipc-metadata-list--dividers-all title-pc-list ipc-metadata-list--baseAlt"}]
    type_info = ['li', {"class": "ipc-inline-list__item"}]
    year_info = ['a', {"class": "ipc-link ipc-link--baseAlt ipc-link--inherit-color"}]
    genre_info = ['span', {"class": "ipc-chip__text"}]
    id = input("Enter a list of space separated IMDb IDs of the cinematographic works or 0 to go back to the main menu: ")
    if(id == '0'): return
    idList = id.split()
    vals = {"work_id": [], "title": [], "director": [], "type": [], "year": [], "genre_1": [], "genre_2": [], "genre_3": []}
    for id in idList:
        try:
            driver = driverConnect()
            driver.get(imdb + str(id))
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            title = soup.find(title_info[0], title_info[1]).text
            director = soup.find(director_info[0], director_info[1]).find('a').text
            year = 0
            type = "Movie"
            for element in soup.find_all(type_info[0], type_info[1]):
                if('TV' in element.text):
                    type = element.text
                    break
            for element in soup.find_all(year_info[0], year_info[1]):
                yearRange = element.text.split('–')
                if(yearRange[0].isdigit()):
                    year = yearRange[0]
                    break
            genre = [None, None, None]
            count = 0
            for element in soup.find_all(genre_info[0], genre_info[1]):
                if(count==3 or element.text == 'Back to top' or element.text.isdigit()): break
                genre[count] = element.text
                count+=1
        except Exception as e:
            print(f"Error: {e}")
            input("Press any key to continue...")
            return
        vals['work_id'].append(id)
        vals['title'].append(title)
        vals['director'].append(director)
        vals['year'].append(year)
        vals['type'].append(type)
        vals['genre_1'].append(genre[0])
        vals['genre_2'].append(genre[1])
        vals['genre_3'].append(genre[2])
    dbInsert("Works", vals)

def insertQuote():
    lookUpVal = input("Enter the title or ID of the cinematographic work to insert to (0 to return to main menu): ")
    if(lookUpVal == '0'): return
    rows = LookUp.dbLookup("Works", "title LIKE '%" + lookUpVal + "%' or work_id LIKE '%" + lookUpVal + "%'")
    if(rows==None or len(rows) == 0):
        print("No cinematographic works found with that title or ID.")
        input("Press any key to continue...")
        return
    else:
        cols = ['Work_ID', 'Title', 'Director', 'Type', 'Year', 'Genre_1', 'Genre_2', 'Genre_3']
        id_sel = 0
        if len(rows)>2:
            df = pd.DataFrame((tuple(row) for row in rows), columns=cols)
            print(tabulate(df, headers='keys', tablefmt='psql', showindex=True, colalign=['center']*len(df.columns)))
            id_sel = input("Multiple cinematographic works found with that title. Please enter the index of the correct one from the list above: ")
        work_id = rows[int(id_sel)][0]
    quote = input("Enter the quote or 0 to go back to the main menu: ")
    if(quote == '0'): return
    character = input("Enter the character who said the quote or 0 to go back to the main menu: ")
    if(character == '0'): return
    season = int(input("Enter the season and episode the quote is from or -1 to skip this step: "))
    if(season == -1):
        season = None
        episode = None
    else: episode = int(input())
    timestamp = input("Enter the timestamp (HH:MM:SS) of the quote or -1 to skip this step: ")
    if(timestamp == '-1'): timestamp = None
    vals = {
        'quote': quote, 'character': character, 'season': season,
        'episode': episode, 'timestamp': timestamp, 'work_id': work_id
    }
    dbInsert("Quotes", vals)

