from flask import Flask, render_template, request
from flask_cors import CORS
import yfinance as yf
import tweepy
from tweepy.parsers import JSONParser
from tweepy.streaming import StreamListener
import json

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/tweepy')
def get_tweepy():
	api_secret_key = '4n84JSQuX4qnZFt1jBVYOSbl8eA6mvOwSMbbtOjlpYX1cQQ6y0'
	api_key = 'HFozqhWZcH3P2cUXsyBSZrf6P'
	access_token = '341961921-uZrcljPNobyBflSXuZSYrnNZZLZ5r37FZbE6gmMX'
	access_token_secret = 'fXKPY5rQLbXYTRCYVJPsDUEBqCr5lt3wKZiMBbE4F2i8W'

	auth = tweepy.OAuthHandler(api_key, api_secret_key)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth, parser = JSONParser())
	
	search = request.args.get('q')
	print(search)
	public_tweets = api.user_timeline(search)
	print(public_tweets)
	return json.dumps(public_tweets)

@app.route('/message')
def get_message():
  return 'Hello Stonks'

@app.route('/stock_data')
def get_stock_data():
	msft = yf.Ticker("MSFT")
	print(msft.info)

app.run(host='0.0.0.0')
