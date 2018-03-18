import random
from APIAccess import get_api
from APIAccess import post_api

"""
TODO:

Set a timer so the bot posts automatically
"""

tweetCount = 500
tweets = get_api.user_timeline(screen_name='Bushfries', count=tweetCount, include_rts=True)


def get_tweets():
    clean_tweet = []
    for status in tweets:
        tweet = status.text
        tweet = tweet.split(" ")
        text = list(filter(lambda word: "https" not in word.lower() and "@" not in word.lower()
                                        and "\s" not in word.lower(), tweet))
        for word in text:
            clean_tweet.append(word)
    return clean_tweet


def create_string(tweets, word_limit):
    tweet_string = ""
    for x in range(0, 8):
        tweet_string += str.rstrip(tweets[random.randint(0, (word_limit - 1))]) + " "
    return tweet_string


def post_tweet(post):
    post_api.update_status(post)

wordLimit = 50
pulled_tweets = get_tweets()
post = create_string(pulled_tweets, wordLimit)
print(post)
print(len(post))
#post_tweet(post)

