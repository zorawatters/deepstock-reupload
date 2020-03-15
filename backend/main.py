from flask import Flask, render_template, request
from flask_cors import CORS
import yfinance as yf
import tweepy
from tweepy.parsers import JSONParser
from tweepy.streaming import StreamListener
import json
from twitter import TwitterClient

app = Flask(__name__)

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
  print("got api")
  # calling function to get tweets 
  tweets = api.get_tweets(query = 'Donald Trump', count = 200) 

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
	print(msft.info)

app.run(host='0.0.0.0')
