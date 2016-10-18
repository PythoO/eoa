import tweepy
import config
import re

WORDS = {
    'read_tweet': {'groups': [['read', 'tweet'], ['get', 'tweet']]},
    'send_tweet': {'groups': [['send', 'tweet'], ['write', 'tweet']]},
}

auth = tweepy.OAuthHandler(config.data['twi_consumer_key'], config.data['twi_consumer_secret'])
auth.set_access_token(config.data['twi_access_token'], config.data['twi_access_token_secret'])
api = tweepy.API(auth)


def read_tweet():
    return api.home_timeline(count=7)


def send_tweet():
    # TODO: make it.
    api.update_status('msg test')
