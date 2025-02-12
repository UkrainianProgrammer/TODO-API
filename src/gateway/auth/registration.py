import os, requests, datetime
import messages
import bcrypt
from dotenv import load_dotenv

load_dotenv()

dbUrl = os.environ.get("POSTGRES_URL")
dbUsersTable = os.environ.get("POSTGRES_USER_TABLE")

def register(request, connection):
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # check if email already exists in the database
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT email FROM {dbUsersTable} WHERE email=%s", (email,))
        if cursor.fetchone():
            return messages.errorEmailExists, 409

    # hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    print(type(hashed_password))

    # insert new user into the database
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO {dbUsersTable} (email, password) VALUES (%s, %s)", (email, hashed_password))
        connection.commit()

    return messages.userCreatedSuccess.format(email), 201