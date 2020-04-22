from flask import Flask, render_template, request
from flask_cors import CORS
from alpha_vantage.timeseries import TimeSeries
from flask import request
from flask_pymongo import pymongo
from pymongo import MongoClient
import yfinance as yf
import tweepy
from tweepy.parsers import JSONParser
from tweepy.streaming import StreamListener
import json
import twitter
from twitter import TwitterClient
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
  print('got') 
  # calling function to get tweets
  tweets = api.get_tweets(query = 'tesla', count = 200)

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

  return ntweets[0]

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



if os.getenv('environment') == 'dev':
    app.run(host='0.0.0.0')
elif __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
