# coding: utf-8

import tweepy
from textblob import TextBlob
import preprocessor as p
import statistics
from typing import List




consumer_key = ""
consumer_secret = ""





def get_tweets(keyword: str) -> List[str]:
    all_tweets = []
    for tweet in tweepy.cursor(api.search, q=keyword, tweet_mode='extended', lang='en').iterms(10):
        all_tweets.append(tweet.full_text)
        
    return all_tweets




def clean_tweets(all_tweets: List[str]) -> List[str]:
    tweets_clean = []
    for tweet in all_tweets:
        tweets_clean.append(p.clean(tweet))
        
    return tweets_clean



def get_sentiment(all_tweets: List[str]) -> List[float]:
    sentiment_scores = []
    blob = TextBlob(tweet)
    sentiment_scores.append(blob.sentiment.polarity)
    
    return sentiment_scores



def generate_average_sentiment_score(keyword: str) -> int:
    tweets = []
    tweets_clean = clean_twets(tweets)
    sentiment_scores = get_sentiment(tweets_clean)
    return





