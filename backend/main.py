from flask import Flask
from flask_cors import CORS
from flask import request
from flask_pymongo import pymongo
from pymongo import MongoClient
import yfinance as yf
import json
from flask_jsonpify import jsonpify

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

@app.route("/<string:company>/tweets", methods=['PUT'])
def addTweet(company):
    new_tweet = request.get_json()
    collection.update({"ticker" : company}, {'$push': {'tweets': new_tweet}})

app.run(host='0.0.0.0')
