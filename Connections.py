import pyodbc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import config # config.py file contains the database credentials

def dbConnect():
    # Connect to the database and open the Chrome driver
    try:
        # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+config.db["server"]+';DATABASE='+config.db["dbName"]+';UID='+config.db["username"]+';PWD='+ config.db["password"])
        return cnxn
    except Exception as e:
        print(f"Error: {e}")
        input("Press any key to continue...")
        exit()

def driverConnect():
    # Connect to the database and open the Chrome driver
    try:
        # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
        options = webdriver.ChromeOptions()
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument('--headless')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver
    except Exception as e:
        print(f"Error: {e}")
        input("Press any key to continue...")
        exit()