import os, requests
import psycopg2
from dotenv import load_dotenv
import jwt

load_dotenv()

dbUrl = os.environ.get("POSTGRES_URL")
dbName = os.environ.get("POSTGRES_DB")
dbPassword = os.environ.get("POSTGRES_DB_PASSWORD")
dbUsersTable = os.environ.get("POSTGRES_USER_TABLE")
connection = psycopg2.connect(database=dbName, host="localhost", port="5432", user="postgres", password=dbPassword)
print("Successfully connected to database: " + dbName)

def login(request):
    auth = request.authorization
    if not auth:
        return None, ("missing credentials", 401)
    
    # check postgres for username and password
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT email, password FROM {dbUsersTable} WHERE email=%s", (auth.username,))
        userRow = cursor.fetchone()
        email = userRow[0]
        password = userRow[1]

        if auth.username != email or auth.password != password:
            return None, ("invalid credentials", 401)
        else:
            # TODO: create JWT token
            pass
            


# TODO: create JWT encoder function