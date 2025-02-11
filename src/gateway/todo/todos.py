from flask import jsonify

import messages

# creates a new todo item and inserts it into MongoDB
def createItem(request, mongoCollection):
    try:
        data = request.get_json()
        
        # TODO: check if this request already exists in db

        if not data:
            return jsonify({"ErrorInfo": messages.errorMissingDataInRequest.format("todos")}), 400

        res = mongoCollection.insert_one(data)

        if res.inserted_id:
            return jsonify({"MessageInfo": messages.todoInserted, "inserted_id": str(res.inserted_id)}), 201
        else:
            return jsonify({"ErrorInfo": messages.errorProcessingRequest.format("failed to insert data into MongoDB")}), 500

    except Exception as e:
        return jsonify({"ErrorInfo": messages.errorFailedToInsertTodoData}), 500

def updateItem():
    pass

def deleteItem():
    pass

def getItem():
    pass