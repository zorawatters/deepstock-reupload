from flask import Flask
from flask_cors import CORS
from alpha_vantage.timeseries import TimeSeries
from flask import request
from flask_pymongo import pymongo
from pymongo import MongoClient
import yfinance as yf
from alpha_vantage.timeseries import TimeSeries
import json
from flask_jsonpify import jsonpify
import datetime


from dotenv import load_dotenv
load_dotenv()
import os


app = Flask(__name__)

CONNECTION_STRING = "mongodb://deep-stock-cu:deep2020stock@deep-stock-cluster-shard-00-00-bwk5a.gcp.mongodb.net:27017,deep-stock-cluster-shard-00-01-bwk5a.gcp.mongodb.net:27017,deep-stock-cluster-shard-00-02-bwk5a.gcp.mongodb.net:27017/test?ssl=true&replicaSet=deep-stock-cluster-shard-0&authSource=admin&retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('deep-stock')
collection = db['companies']

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/message')
def get_message():
  return 'Hello Stonks'

@app.route('/stock_data')
def get_stock_data():
	msft = yf.Ticker("MSFT")

	dataframe = msft.history(period="1")
	print(dataframe)
	#dataframe['Date'] = dataframe['Date'].dt.strftime('%Y-%m-%d')
	return dataframe.reset_index().to_json(orient='records', date_format='iso')


@app.route("/<string:company>/tweets", methods=['PUT'])
def addTweet(company):
    new_tweet = request.get_json()
    collection.update({"ticker" : company}, {'$push': {'tweets': new_tweet}})


'''
  Storing stock data api

  Gets json data from response body and stores it into database
'''

@app.route('/users/store_data', methods=['POST'])
def insert_document():
    req_data = request.get_json()

    collection.insert_one(req_data).inserted_id
    return ('', 204)


'''
  Diplaying stock data api

  Gets all the sotored data in the database and retruns a json file
'''


@app.route('/<string:company>/intraday', methods=['GET'])
def get_intraday(company):


    key = 'CYNCL6X4FUN4SE0K'

    ts = TimeSeries(key= key)

    intraday_data, data_info = ts.get_intraday(symbol=company, outputsize='compact', interval='5min')


    daily_data = {}
    days_list = []
    convert_daytime = 0
    day = 0

    # Convert string dates to datetime format and append to list
    for key, value in intraday_data.items():
        convert_daytime = datetime.datetime.strptime(key, "%Y-%m-%d %H:%M:%S")
        days_list.append(convert_daytime.day)


    # Get latest day
    latest_day = max(days_list)

    # Add filtered data to new dictionary
    for key, value in intraday_data.items():
        convert_daytime = datetime.datetime.strptime(key, "%Y-%m-%d %H:%M:%S")
        day = convert_daytime.day

        if day == latest_day:
            if key not in daily_data:
                daily_data[key] = []
            daily_data[key].append(value)

    return json.dumps(daily_data)


@app.route('/users/display_data')
def get_documents():

    documents = collection.find()

    response = []

    for doc in documents:
        doc['_id'] = str(doc['_id'])
        response.append(doc)

    return json.dumps(response)


if __name__ == '__main__':
    if os.getenv('environment') == 'dev':
        app.run(host='0.0.0.0')
    else:
        app.run(host='0.0.0.0', port=8080, debug=True)
