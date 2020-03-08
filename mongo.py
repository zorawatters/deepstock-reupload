from flask import Flask, jsonify, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
import json
import yfinance as yf

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'vueloginreg'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/DeepStock'
app.config['JWT_SECRET_KEY'] = 'secret'

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

CORS(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'You want path: %s' % path

@app.route('/users/register', methods=['POST'])
def register():
    users = mongo.db.users
    first_name = request.get_json()['first_name']
    last_name = request.get_json()['last_name']
    email = request.get_json()['email']
    password = bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')
    created = datetime.utcnow()

    user_id = users.insert({
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
        'created': created
    })

    new_user = users.find_one({'_id': user_id})

    result = {'email': new_user['email'] + ' registered'}

    return jsonify({'result' : result})

@app.route('/users/login', methods=['POST'])
def login():
    users = mongo.db.users
    email = request.get_json()['email']
    password = request.get_json()['password']
    result = ""

    response = users.find_one({'email': email})

    if response:
        if bcrypt.check_password_hash(response['password'], password):
            access_token = create_access_token(identity = {
                'first_name': response['first_name'],
                'last_name': response['last_name'],
                'email': response['email']
            })
            result = jsonify({"token": access_token})
        else:
            result = jsonify({"error": "Invalid username and password"})
    else:
        result = jsonify({"result": "No results found"})
    return result


'''
  Storing stock data api

  Gets json data from response body and stores it into database
'''

@app.route('/users/store_data', methods=['POST'])
def insert_document():
    req_data = request.get_json()
    collection_stock = mongo.db.stocks
    collection_stock.insert_one(req_data).inserted_id
    return ('', 204)


'''
  Diplaying stock data api

  Gets all the sotored data in the database and retruns a json file
'''


@app.route('/users/historical_data/<string:company>', methods=['PUT'])
def update_historical_data(company):
    msft = yf.Ticker("MSFT")

    data = msft.info

    return json.dumps(data)



@app.route('/users/display_data')
def get_documents():
    collection_stock = mongo.db.stocks
    documents = collection_stock.find()
    response = []

    for doc in documents:
        doc['_id'] = str(doc['_id'])
        response.append(doc)

    return json.dumps(response)


if __name__ == '__main__':
    app.run(debug=True)
