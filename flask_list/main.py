from flask import Flask, jsonify, request
from list_work import addTask, delete_task, list_item
app = Flask(__name__)

@app.route('/list/', methods=['GET', 'POST'])
def getList():
    list_items= list_item()
    return jsonify(list_items)


@app.route('/remove/', methods=['GET', 'POST'])
def removeItem():
    list_items= delete_task()
    return jsonify(list_items)



@app.route("/add/<string:item>", methods=['GET', 'POST'])
def additem(item:str):
    list_items= addTask(item)
    return jsonify(list_items)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)