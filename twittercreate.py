from multiprocessing.connection import wait
import time
import random
from unittest import result
from textblob import TextBlob
import pandas
import tweepy
import credentials

# Initialization
auth = tweepy.OAuth1UserHandler(credentials.API_KEY, credentials.API_SECRET_KEY, credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)


#Creating tweets from the quotes csv
df = pandas.read_csv('quotes_all.csv', sep=";");

index = 0;

with open('tweet_index.txt', 'r') as file:
    index = int(file.read())

def tweet():
    for idx, row in df.iterrows():
        if idx <= index:
            continue
        str1 = "'"
        str2 = "'"
        string = str1 + row[0] + str2 +  "\n\n" + row[1]
        if len(string) < 280:
            print(string)
            api.update_status(string)
            time.sleep(3600*6)

        with open('tweet_index.txt', 'w') as file:
            file.write(str(idx))
        
        

tweet()