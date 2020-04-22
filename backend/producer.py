#!/usr/bin/python

import tweepy
import kafka
from json import dumps
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer, KafkaClient, SimpleProducer


print("created producers")
tproducer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
                         
kafka = KafkaClient("localhost:9092") 
producer = SimpleProducer(kafka)
                         
#amd_producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: 
#                          dumps(x).encode('utf-8'))
#                         
#apple_producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: 
#                         dumps(x).encode('utf-8'))
                         
#  splunk_producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: 
#                          dumps(x).encode('utf-8'))

api_secret_key = '4n84JSQuX4qnZFt1jBVYOSbl8eA6mvOwSMbbtOjlpYX1cQQ6y0'
api_key = 'HFozqhWZcH3P2cUXsyBSZrf6P'
access_token = '341961921-uZrcljPNobyBflSXuZSYrnNZZLZ5r37FZbE6gmMX'
access_token_secret = 'fXKPY5rQLbXYTRCYVJPsDUEBqCr5lt3wKZiMBbE4F2i8W'

# attempt authentication
# try:
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#call to twitter api and read to kafka
tesla_tweets = api.search(q = "tesla", count = 100, lang = "en", result_type = "recent") 
for tweet in tesla_tweets:
  print(tweet.text)
  try:
    producer.send('TSLA', value = tweet)
  except:
    print("failed")
tproducer.flush()

# amd_tweets = api.search(q = "amd OR amd microchip OR Nvidia", count = 1000, lang = "en", result_type = "recent") 

# apple_tweets = api.search(q = "apple OR iphone OR ipad OR apple music OR mac OR apple tv", count = 1000, lang = "en", result_type = "recent") 
                       
#splunk_tweets = api.search(q = "splunk OR victorops OR big data OR data mining", count = 1000, lang = "en", result_type = "recent") 

# tesla_producer.send('TSLA', tesla_tweets)
# tesla_producer.flush()

# amd_producer.send('AMD', amd_tweets)
# amd_producer.flush()

# splunk_producer.send('SPLK', splunk_tweets)
#  splunk_producer.flush()

# apple_producer.send('AAPL', apple_tweets)
# apple_producer.flush()
print("added to kafka")
        