import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

myConn = mysql.connector.connect(
    host = os.getenv("DB_HOST"),
    username = os.getenv("DB_USERNAME"),
    passwd = os.getenv("DB_PASSWORD"),
    database = os.getenv("DB_DATABASE")
)

myCursor = myConn.cursor()
