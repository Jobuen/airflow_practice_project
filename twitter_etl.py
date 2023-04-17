import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs
import constants


def run_twitter_etl():
    # Keys, stored in a separate file
    api_key = constants.API_KEY
    secret_key = constants.API_KEY_SECRET
    access_key = constants.ACCESS_TOKEN
    access_secret = constants.ACCESS_TOKEN_SECRET

    # Twitter handle TODO:
    # Create functionality to pass in a twitter handle
    twitter_handle = 'placeholder'

    # Twitter aut
    auth = tweepy.OAuthHandler(api_key, secret_key)
    auth.set_access_token(access_key, access_secret)

    # Creating an API object
    api = tweepy.API(auth)

    # Get tweet-data
    tweets = api.user_timeline(screen_name=twitter_handle,
                                count=200, # max allowed
                                include_rts=False,
                                tweet_mode='extended')

    # Clean tweet-data
    tweet_list = []
    for tweet in tweets:
        text = tweet._json['full_text']

        refined_tweet = {"user": tweet.user.screen_name,
                        "text": text,
                        "favorite_count": tweet.favorite_count,
                        "retweet_count": tweet.retweet_count,
                        "created_at": tweet.created_at}
        tweet_list.append(refined_tweet)

    # Save tweet-data to csv
    df = pd.DataFrame(tweet_list)
    df.to_csv(f'{twitter_handle}_twitter_data.csv', index=False)
