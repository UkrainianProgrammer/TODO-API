import os, requests, datetime
from flask import jsonify
from dotenv import load_dotenv
import jwt

import messages

load_dotenv()

dbUsersTable = os.environ.get("POSTGRES_USER_TABLE")
jwtSecret = os.environ.get("JWT_SECRET")

def login(request, connection):
    auth = request.authorization
    if not auth:
        return messages.errorMissingCredentials, 401
    
    # check postgres for username and password
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT email, password FROM {dbUsersTable} WHERE email=%s", (auth.username,))
        userRow = cursor.fetchone()
        email = userRow[0]
        password = userRow[1]

        if auth.username != email or auth.password != password:
            return messages.errorInvalidCredentials, 500
        else:
            return createJWT(auth.username, jwtSecret, True), 201

def validateUser(request):
    if not "Authorization" in request.headers:
        return messages.errorMissingCredentials, 401

    encodedToken = request.headers["Authorization"]
    if not encodedToken:
        return messages.errorInvalidCredentials, 401
    
    encodedToken = encodedToken.split(" ")[1]

    try:
        decoded = jwt.decode(encodedToken, jwtSecret, algorithms=["HS256"])
    except:
        return messages.errorUserNotAuthorized, 403

    return decoded, 200

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
