#!/usr/bin/python

import tweepy
import kafka
from json import dumps
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer, KafkaClient

class KafkaListener(StreamListener):
    def on_data(self, data):
        print(data)
        producer.send('TSLA', data)
        producer.flush()
        return True
    def on_error(self, status):
        print (status)
        
        
#kafka = KafkaClient("localhost:9092") 
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))       
#producer = SimpleProducer(kafka)

# keys and tokens from the Twitter Dev Console
api_secret_key = '4n84JSQuX4qnZFt1jBVYOSbl8eA6mvOwSMbbtOjlpYX1cQQ6y0'
api_key = 'HFozqhWZcH3P2cUXsyBSZrf6P'
access_token = '341961921-uZrcljPNobyBflSXuZSYrnNZZLZ5r37FZbE6gmMX'
access_token_secret = 'fXKPY5rQLbXYTRCYVJPsDUEBqCr5lt3wKZiMBbE4F2i8W'

# attempt authentication
# try:
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

t = KafkaListener()
tesla_tweets = api.search(q = "tesla", count = 100, lang = "en", result_type = "recent") 
for tweet in tesla_tweets:
  print(tweet.text)
  try:
    producer.send('TSLA', value = tweet)
  except:
    print("failed")
  producer.flush()
#tesla_stream = Stream(auth, t)
#tesla_stream.filter(track=["tesla"], languages=["en"], is_async=True)