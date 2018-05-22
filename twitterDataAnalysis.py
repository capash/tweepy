#Import the necessary methods from tweepy library
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import config
from datetime import datetime, date, time, timedelta
import sys
import time as systime
import json
import pandas as pd
from pandas import ExcelWriter
import xlsxwriter
import csv
from pandas.io.json import json_normalize
import flatten_json
import pandas as pd
from pandas import read_csv
import numpy as np
import ast
import objectpath

#Variables  
access_token=config.access_token
access_token_secret=config.access_token_secret
consumer_key=config.consumer_key
consumer_secret=config.consumer_secret

#Tweet output.
class StdOutListener(StreamListener):

    def on_data(self, data):
        
        saveMe=data
        output = open('output.txt','a')
        output.write(saveMe)
        output.close()
        #print(data)
        return True

    def on_error(self, status):
        #print(status)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

start_date = datetime.utcnow()
end_date = datetime.utcnow() - timedelta(days=10)

api = tweepy.API(auth)
tweets = api.user_timeline(config.screen_name)
for tweet in tweets:
    if end_date < tweet.created_at:
        print("End date:")
        print(end_date)
        print("created_at date:")
        print(tweet.created_at)
        print(1)
        l = StdOutListener()
        stream = Stream(auth, l)
        stream.filter(track=['NewYork', 'LosAngeles', 'SanFrancisco'])
        


tweets_data_path = 'C:/Blank/R/TwitterAnalysis/output.txt'
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
print(len(tweets_data))

df = pd.DataFrame(tweets_data)

flat_data = json_normalize(tweets_data)

df = pd.DataFrame(flat_data, columns = ['user.name', 'retweeted', 'retweet_count', 'favorite_count', 'entities.hashtags'])
print(df.head(1))

xls_name = "C:/Blank/R/TwitterAnalysis/" + "output.xlsx"
w = pd.ExcelWriter(xls_name, engine='xlsxwriter')
df.to_excel(w)
w.save()


