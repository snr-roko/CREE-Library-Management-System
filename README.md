# CREE-Library-Management-System

A simple Library Management Library System Using Python and SQL...

## Basic Steps:

- Clone this repo

- Create a branch to be working on

- create a virtual environment and activate

- install the packages in the `requirements.txt` file while virtual environment is active

- create a `.env` file to hold environment variables eg. database connection data

- include the `.env` and the virtual environment folder in the `.gitignore` file

### importing dotenv:

```py
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

connect = mysql.connector.connect(
    host = os.getenv("DB_HOST"),
    .
    .
    .
)

```

### dotenv connection data
```py
DB_HOST="localhost"
. 
.
. 
```
