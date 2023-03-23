import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs
import constants

# Keys, stored in a separate file
access_key = constants.ACCESS_KEY
secret_key = constants.SECRET_KEY
consumer_key = constants.CONSUMER_KEY
consumer_secret = constants.CONSUMER_SECRET

# Twitter aut
auth = tweepy.OAuthHandler(access_key, secret_key)
auth.set_access_token(consumer_key, consumer_secret)

api = tweepy.API(auth)
