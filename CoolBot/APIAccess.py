import tweepy

# --------------------------------------------------------BUSHFRIES----------------------------------------------------
try:
    get_consumer_key = ''
    get_consumer_secret = ''
    get_access_token = ''
    get_access_token_secret = ''

    get_auth = tweepy.OAuthHandler(get_consumer_key,
                                   get_consumer_secret)
    get_auth.set_access_token(get_access_token,
                              get_access_token_secret)
    get_api = tweepy.API(get_auth)
except tweepy.error.TweepError:
    print("Invalid API")

# --------------------------------------------------------BOTFRIES----------------------------------------------------
try:
    post_consumer_key = ''
    post_consumer_secret = ''
    post_access_token = ''
    post_access_token_secret = ''

    post_auth = tweepy.OAuthHandler(post_consumer_key,
                                    post_consumer_secret)
    post_auth.set_access_token(post_access_token,
                               post_access_token_secret)
    post_api = tweepy.API(post_auth)
except tweepy.error.TweepError:
    print("Invalid API")
