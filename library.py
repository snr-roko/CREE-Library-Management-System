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
def search_books(title, mycursor):
  sql = "SELECT * FROM books WHERE title LIKE %s"
  val = (f"%{title}%",)
  mycursor.execute(sql, val)
  results = mycursor.fetchall()
  if results:
      print("Books found:")
      for book in results:
          print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, ISBN: {book[3]}")
  else:
      print("No books found.")

search_term = "NAZIS" 
search_books(search_term, myCursor)


