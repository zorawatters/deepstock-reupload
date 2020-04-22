#!/usr/bin/python

import tweepy
import kafka

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient


class TweetListener(StreamListener):
    def on_data(self, data):
        producer.send_messages('test2', data.encode('utf-8'))
        print (data)
        return True
    def on_error(self, status):
        print (status)

api_secret_key = '4n84JSQuX4qnZFt1jBVYOSbl8eA6mvOwSMbbtOjlpYX1cQQ6y0'
api_key = 'HFozqhWZcH3P2cUXsyBSZrf6P'
access_token = '341961921-uZrcljPNobyBflSXuZSYrnNZZLZ5r37FZbE6gmMX'
access_token_secret = 'fXKPY5rQLbXYTRCYVJPsDUEBqCr5lt3wKZiMBbE4F2i8W'

# attempt authentication 
# try: 
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
dapi = tweepy.API(auth)

kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)
l = TweetListener()

stream = Stream(auth, l)
stream.filter(track=["trump"])