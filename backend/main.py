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

# @app.route('/tweepy')
# def get_tweepy():
#     api_secret_key = '4n84JSQuX4qnZFt1jBVYOSbl8eA6mvOwSMbbtOjlpYX1cQQ6y0'
#     api_key = 'HFozqhWZcH3P2cUXsyBSZrf6P'
#     access_token = '341961921-uZrcljPNobyBflSXuZSYrnNZZLZ5r37FZbE6gmMX'
#     access_token_secret = 'fXKPY5rQLbXYTRCYVJPsDUEBqCr5lt3wKZiMBbE4F2i8W'
#     auth = tweepy.OAuthHandler(api_key, api_secret_key)
#     auth.set_access_token(access_token, access_token_secret)
#     api = tweepy.API(auth, parser = JSONParser())
#     tweets = []
#     f = open('companies.json',) 
#     data = json.load(f) 
#     for i in data['companies']:
#         # make call to tweepy api here and store in mongodb for each company
#         public_tweets = api.search(i, count = 3)
#         for tweet in public_tweets['statuses']:
#             tweet_json_string = {"ticker": '', "text": '', "id": ''}
#             tweet_json_dump = json.dumps(tweet_json_string)
#             tweet_json_object = json.loads(tweet_json_dump)
#             tweet_json_object["ticker"] = i;
#             tweet_json_object["text"] = tweet["text"];
#             tweet_json_object["id"] = tweet["id_str"];
#             tweets.append(tweet_json_object)
          
#     f.close() 

#     return json.dumps(tweets)

@app.route('/tweepy', methods=['GET'])
def get_tweepy():
    # api_secret_key = '4n84JSQuX4qnZFt1jBVYOSbl8eA6mvOwSMbbtOjlpYX1cQQ6y0'
    # api_key = 'HFozqhWZcH3P2cUXsyBSZrf6P'
    # access_token = '341961921-uZrcljPNobyBflSXuZSYrnNZZLZ5r37FZbE6gmMX'
    # access_token_secret = 'fXKPY5rQLbXYTRCYVJPsDUEBqCr5lt3wKZiMBbE4F2i8W'

    # auth = tweepy.OAuthHandler(api_key, api_secret_key)
    # auth.set_access_token(access_token, access_token_secret)
  # api = tweepy.API(auth, parser = JSONParser())

  # # search = request.args.get('q')
  # # print(search)
  # # public_tweets = api.user_timeline(search)
  # # print(public_tweets)
  # #creating a stream of tweets through tweepy
  # tweetStreamListener = TweetListener()
  # tweetStream = tweepy.Stream(auth = auth, listener = tweetStreamListener)
  # tweetStream.filter(track = ['tesla stocks']) #looking for tweets about tesla
  # return "got it"
  # creating object of TwitterClient Class 
  print("b4")
  api = TwitterClient()
  print("got api")
  # calling function to get tweets 
  tweets = api.get_tweets(query = 'TSLA', count = 200) 

  # picking positive tweets from tweets 
  ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
  # percentage of positive tweets 
  print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))) 
  # picking negative tweets from tweets 
  ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
  # percentage of negative tweets 
  print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets))) 
  # percentage of neutral tweets 
 # print("Neutral tweets percentage: {} %".format(100*len(tweets - ntweets - ptweets)/len(tweets))) 

  # printing first 5 positive tweets 
  print("\n\nPositive tweets:") 
  for tweet in ptweets[:10]: 
    print(tweet['text']) 

  #  printing first 5 negative tweets 
  print("\n\nNegative tweets:") 
  for tweet in ntweets[:10]: 
    print(tweet['text']) 

  # add to mongodb 

  return ntweets[0]


if os.getenv('environment') == 'dev':
    app.run(host='0.0.0.0')
elif __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)