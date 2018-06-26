import random
import time
from APIAccess import get_api, post_api

# So the bot doesn't exceed the character limit.
word_limit = 20
# Minute = 60, Hour = 3600, Day = 86400.
wait_time = 3600
# How far back into tweets the bot should look.
tweetCount = 500
tweets = get_api.user_timeline(screen_name='Bushfries', count=tweetCount, include_rts=True)


# A function to fetch my tweets
def get_tweets():
    clean_tweet = []
    for status in tweets:
        tweet = status.text
        tweet = tweet.split(" ")
        # Filters out all links/twitter symbols so no one gets tagged and nothing gets linked
        text = list(filter(lambda word: "https" not in word.lower() and "@" not in word.lower()
                                        and "\s" not in word.lower(), tweet))
        for word in text:
            clean_tweet.append(word)
    return clean_tweet


# Creates a string for the bot to post
def create_string(tweets, word_limit, tweet_count):

    tweet_string = ""
    while True:
        for x in range(0, word_limit):
            tweet_string += str.rstrip(tweets[random.randint(0, (tweet_count - 1))]) + " "
        if len(tweet_string) < 240:
            return tweet_string


def post_tweet(post):
    post_api.update_status(post)
    return post


while True:
    print(post_tweet(create_string(get_tweets(), word_limit, tweetCount)))
    time.sleep(wait_time)



