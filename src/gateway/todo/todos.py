from flask import jsonify

import messages

# creates a new todo item and inserts it into MongoDB
def createItem(request):
    try:
        data = request.get_json()
        # TODO: implement MongoDB connection
        # TODO: validate and sanitize data
        # TODO: insert into MongoDB

    except Exception as e:
        print(messages.errorProcessingRequest.format(e))  # Log the error for debugging
        return jsonify({"ErrorInfo": messages.errorProcessingRequest.format(e)}), 500

def updateItem():
    pass

def deleteItem():
    pass

def getItem():
    pass