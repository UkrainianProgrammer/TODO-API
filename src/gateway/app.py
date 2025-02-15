from flask import Flask, request, jsonify, session, render_template, make_response
import psycopg2
from flask_pymongo import MongoClient
import os
from dotenv import load_dotenv

from auth import access, registration
from todo import todos

load_dotenv()
server = Flask(__name__)

# POSTGRES
postgreDbUrl = os.environ.get("POSTGRES_URL")
postgreDbName = os.environ.get("POSTGRES_DB")
postgresDbPassword = os.environ.get("POSTGRES_DB_PASSWORD")
postgresDbUsersTable = os.environ.get("POSTGRES_USER_TABLE")
jwtSecret = os.environ.get("JWT_SECRET")
postgresConnection = psycopg2.connect(database=postgreDbName, host="localhost", port="5432", user="postgres", password=postgresDbPassword)
print("Successfully connected to Postgres database: " + postgreDbName)

# MONGODB
MONGO_URI = os.environ.get("MONGO_URI")
MONGO_DB = os.environ.get("MONGO_DB")
MONGO_COLLECTION = os.environ.get("MONGO_DB_COLLECTION")

mongoClient = MongoClient(MONGO_URI)
mongoDb = mongoClient[MONGO_DB]
mongoCollection = mongoDb[MONGO_COLLECTION]
mongoDb.command("ping") # Check connection by sending a ping command
print("Successfully connected to MongoDB database: " + MONGO_DB)

@server.route("/", methods=["POST"])
def index():
    return render_template('index.html')

@server.route("/register", methods=["POST"])
def register():
    msg, statusCode = registration.register(request, postgresConnection)
    print(msg, statusCode)

    return jsonify(msg, statusCode)

@server.route("/login", methods=["POST"])
def login():
    msg, statusCode = access.login(request, postgresConnection)
    print(msg, statusCode)

    return jsonify(msg, statusCode)


@server.route('/logout', methods=["DELETE"])
def logout():
    if request.method == "DELETE":
        session['user_id'] = None
        response = make_response('', 204)
        return jsonify(response)

@server.route("/todos", methods=["POST"])
def todos():
    msg, statusCode = access.validateUser(request)
    print(msg)

    if statusCode != 200:
        return jsonify(msg, statusCode)

    # TODO: finish the request
    msg, statusCode = todos.createItem(request, mongoCollection)

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