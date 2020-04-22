import tweepy
import kafka
import re
from json import loads
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from textblob import TextBlob
from tweepy.parsers import JSONParser
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient
from kafka import KafkaConsumer

#from read-tweets import


class TeslaListener(StreamListener):
    def on_data(self, data):
        print("sending")
        producer.send_messages('test2', data.encode('utf-8'))
        return True
    def on_error(self, status):
        print (status)

class AMDListener(StreamListener):
    def on_data(self, data):
        producer.send_messages('amd', data.encode('utf-8'))
        print (data)
        return True
    def on_error(self, status):
        print (status)

class SplunkListener(StreamListener):
    def on_data(self, data):
        producer.send_messages('splunk', data.encode('utf-8'))
        print (data)
        return True
    def on_error(self, status):
        print (status)

class AppleListener(StreamListener):
    def on_data(self, data):
        producer.send_messages('apple', data.encode('utf-8'))
        print (data)
        return True
    def on_error(self, status):
        print (status)


class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        api_secret_key = '4n84JSQuX4qnZFt1jBVYOSbl8eA6mvOwSMbbtOjlpYX1cQQ6y0'
        api_key = 'HFozqhWZcH3P2cUXsyBSZrf6P'
        access_token = '341961921-uZrcljPNobyBflSXuZSYrnNZZLZ5r37FZbE6gmMX'
        access_token_secret = 'fXKPY5rQLbXYTRCYVJPsDUEBqCr5lt3wKZiMBbE4F2i8W'

        # attempt authentication
       # try:
        self.auth = tweepy.OAuthHandler(api_key, api_secret_key)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)
        
        producer = SimpleProducer(kafka)
        
        self.t = TeslaListener()
        self.s = SplunkListener()
        self.a = AMDListener()
        self.ap = AppleListener()
        

        # except:
        #     print("Error: Authentication Failed")
        
        
    def stream(self, topic):
      #if topic == 'amd':
       # amd_stream = Stream(self.auth, self.a)
        #amd_stream.filter(track=["amd", 'amd microchip', 'Nvidia'])      
      #elif topic == 'tesla':
      tesla_stream = Stream(self.auth, self.t)
      tesla_stream.filter(track=["zoradearr"])
        #tesla_stream.filter(track=["tesla","electric car", "spacex", "elon musk", "self driving cars", "model x", "model s"])
     # elif topic == 'apple':
     #   apple_stream = Stream(self.auth, self.ap)
     #   apple_stream.filter(track=["apple", 'iphone', 'ipad', 'apple music', 'mac', 'apple tv'])
      #elif topic == 'splunk':
      #  splunk_stream = Stream(self.auth, self.s)
      #  splunk_stream.filter(track=["splunk", "victorops", "big data", "data mining"], languages = ['en'])

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) (\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        consumer = KafkaConsumer(
            'tesla',
             bootstrap_servers=['localhost:9092'],
             auto_offset_reset='earliest',
             enable_auto_commit=True,
             group_id='companies',
             value_deserializer=lambda x: loads(x.decode('utf-8')) 
             )
        print('created consumer')
        tweets = []

        try:
            # call twitter api to fetch tweets
            #fetched_tweets = self.api.search(q = query, count = count)
            print('getting tweets')
            n = 0
            # parsing tweets one by one
            for message in consumer:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                tweet = message.value
                #print(tweet)
                parsed_tweet['text'] = tweet['text']
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet['text'])

                # appending parsed tweet to tweets list
                if tweet['retweet_count'] > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
                print('added tweet')
                n += 1
                if n < count:
                  break
                

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))
