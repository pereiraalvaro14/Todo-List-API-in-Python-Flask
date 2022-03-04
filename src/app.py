from flask import Flask, jsonify, request
import json


app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False },
]

@app.route('/todos', methods=['GET'])
def home():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_data = request.data
    data = json.loads(request_data)
    todos.append(data)
    # print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    # print("This is the position to delete: ",position)
    return jsonify(todos)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
