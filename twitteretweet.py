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


#retweet tweet from a specific category
search = ["Python", "Java", "C/C++", "JavaScript", "PHP", "coding", "programming", "code", "software", "engineer", "developer", "freelancer"]
nrTweets = 10

random_num = random.choice(search)

def retweet():
    random_word = random.choice(search)
    print(random_word)
    for tweet in tweepy.Cursor(api.search_tweets, random_word).items(nrTweets):
        if tweet.user.id != "freelancerchamp":
            if not tweet.retweeted:
                try:
                    tweet_analysis = TextBlob(tweet.text)
                    tweet_analysis_score = tweet_analysis.sentiment.polarity
                    print(f"Tweet has polarity score of {tweet_analysis_score}")
                    if tweet_analysis_score > 0.5:
                        api.retweet(tweet.id)
                        print(f"Retweeted {tweet.user.name}")
                        time.sleep(3600*6)
                except tweepy.errors.TweepyException as e:
                    print(e)

while(True):
    retweet()