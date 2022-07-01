from email import message
from flask import Flask, jsonify, request, render_template



app = Flask(__name__)

stores = [
    {
        'name':'My Wonderful Store',
        'items':[
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]


@app.route('/') #accessing a homepage
def home():
    return render_template('index.html')

@app.route('/store', methods=['POST'])
def createStore():
    requestData = request.get_json()
    newStore = {
        'name': requestData['name'],
        'items': []
    }
    stores.append(newStore)
    return jsonify(newStore)


@app.route('/store/<string:name>')
def getStore(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'Store not found'})


@app.route('/store')
def getStores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>/item', methods=['POST'])
def createItemInStore(name):
    requestData = request.get_json()
    for store in stores:
        if store['name'] == name:
            newItem = {
                'name': requestData['name'],
                'price': requestData['price']
            }
            store['items'].append(newItem)
            return jsonify(newItem)
    return jsonify({'message': 'Store not found'})

@app.route('/store/<string:name>/item')
def getItemsInStore(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'Store not found'})



app.run(port=5000)