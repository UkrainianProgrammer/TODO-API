from flask import Flask, request, jsonify

from auth import access

server = Flask(__name__)

@server.route("/", methods=[""])
def index():
    return render_template('index.html')

@server.route("/regiser", methods=["POST"])
def register():
    pass

@server.route("/login", methods=["POST"])
def login():
    token, err = access.login(request)

    if not err:
        return token
    else:
        return err

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