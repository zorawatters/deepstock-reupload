from flask import Flask
from flask_cors import CORS
from alpha_vantage.timeseries import TimeSeries
from flask import request
from flask_pymongo import pymongo
from pymongo import MongoClient
import yfinance as yf
from alpha_vantage.timeseries import TimeSeries
import json
import tweepy
from tweepy.parsers import JSONParser
from tweepy.streaming import StreamListener
from twitter import TwitterClient
from flask_jsonpify import jsonpify
from datetime import datetime
# from dotenv import Dotenv
# dotenv = Dotenv('./.env')
# print(dotenv)

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

    return json.dumps(intraday_data)



@app.route('/users/display_data')
def get_documents():

    documents = collection.find()

    response = []

    for doc in documents:
        doc['_id'] = str(doc['_id'])
        response.append(doc)

    return json.dumps(response)

@app.route('/tweepy/<string:ticker>', methods=['GET'])
def get_tweepy(ticker):
  api = TwitterClient()

  # calling function to get tweets 
  tweets = api.get_tweets(query = ticker, count = 500) 

  # store in mongodb
  for tweet in tweets:
    # might need to write condition to make sure tweets with same unique ID aren't duplicated

    # get date from iso datetime string
    tweet_date = datetime.strptime(tweet['date'], "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d")

    #check if there is already a date object for tweet_date
    tweet_array = collection.find_one({"ticker" : ticker })["tweets"]
    tweet_date_exists = any(x for x in tweet_array if x["date"] == tweet_date)

    # if date object doesn't exist yet, add it 
    if not tweet_date_exists:
        collection.update({"ticker" : ticker}, {'$push': {'tweets': {'date':tweet_date, 'day_sentiment': 0, 'tweets':[]}}})

    # add tweet to tweets array
    collection.update({"ticker" : ticker, "tweets.date": tweet_date}, {'$push': {'tweets.$.tweets': tweet}} )

    # recalculate day sentiment avg for each tweet added
    day_object = next((x for x in tweet_array if x["date"] == tweet_date), None)

    if day_object is None:
        avg_day_sentiment = 0
        updated_avg_day_sentiment = tweet["scaled_sentiment"]
    else:
        avg_day_sentiment = day_object["day_sentiment"]
        updated_avg_day_sentiment = ((avg_day_sentiment * len(day_object["tweets"])) + tweet["scaled_sentiment"])/(len(day_object["tweets"]) + 1)


    # calculate new average
    print(updated_avg_day_sentiment)

    # update daily sentiment
    collection.update({"ticker" : ticker, "tweets.date": tweet_date}, {'$set': {'tweets.$.day_sentiment': updated_avg_day_sentiment}} )

  return json.dumps(tweets, 200)

# this deletes all tweets in database for a specified company
@app.route('/cleartweets/<string:ticker>', methods=['GET'])
def clear_tweets(ticker):
    collection.update({"ticker" : ticker}, { "$set": {"tweets": []}})

    return "cleared tweets for " + ticker


if os.getenv('environment') == 'dev':
    app.run(host='0.0.0.0')
elif __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)