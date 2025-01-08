from flask import Flask, request, jsonify, session, render_template, make_response
import psycopg2
import os
from dotenv import load_dotenv

from auth import access

load_dotenv()

dbUrl = os.environ.get("POSTGRES_URL")
dbName = os.environ.get("POSTGRES_DB")
dbPassword = os.environ.get("POSTGRES_DB_PASSWORD")
dbUsersTable = os.environ.get("POSTGRES_USER_TABLE")
jwtSecret = os.environ.get("JWT_SECRET")
connection = psycopg2.connect(database=dbName, host="localhost", port="5432", user="postgres", password=dbPassword)
print("Successfully connected to database: " + dbName)

server = Flask(__name__)

@server.route("/", methods=[""])
def index():
    return render_template('index.html')

@server.route("/register", methods=["POST"])
def register():
    pass

@server.route("/login", methods=["POST"])
def login():
    token, err = access.login(request, connection)

    if not err:
        return token
    else:
        return err


@server.route('/logout', methods=["DELETE"])
def logout():
    if request.method == "DELETE":
        session['user_id'] = None
        response = make_response('', 204)
        return response

@server.route("/todos", methods=["POST"])
def todos():
    pass

@server.route("/todos/<int:arg1>", methods=["PATCH", "POST"])
def updateTodo(arg1=None):
    pass

@server.route("/todos/<int:arg1>", methods=["DELETE", "POST"])
def removeTodo(arg1=None):
    pass

#TODO: figure out how to write route with question mark ?
@server.route("/todos/?<string:arg1>&<string:arg2>", methods=["GET", "POST"])
def getTodo():
    pass


if __name__ == '__main__':
    server.run(debug=True)