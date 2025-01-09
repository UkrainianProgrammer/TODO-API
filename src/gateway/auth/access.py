import os, requests, datetime
from dotenv import load_dotenv
import jwt

load_dotenv()

dbUsersTable = os.environ.get("POSTGRES_USER_TABLE")
jwtSecret = os.environ.get("JWT_SECRET")

def login(request, connection):
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
            return createJWT(auth.username, jwtSecret, True)
            


def createJWT(username, secret, authz):
    return jwt.encode(
        {
            "username": username,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc)
                + datetime.timedelta(days=1),
            "iat": datetime.datetime.now(tz=datetime.timezone.utc),
            "admin": authz,
        },
        secret,
        algorithm="HS256",
    )
