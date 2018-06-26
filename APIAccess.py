import tweepy

# --------------------------------------------------------BUSHFRIES----------------------------------------------------
try:
    get_consumer_key = 'lZKHiGxzaac9eApuedZ8FuBlR'
    get_consumer_secret = 'QBo2RJob1Jz9QUg67S47cGPg3enQRwnQHii1r9Al1ikDxcQLG5'
    get_access_token = '834452681355882496-aCwWCJ3ynIP15j5afgM9e5KrPKXUjQp'
    get_access_token_secret = 'VTe2Hd9Rki4JxBJYk9siJf7hxXmiAPpn8FKCHtJh6oFss'

    get_auth = tweepy.OAuthHandler(get_consumer_key,
                                   get_consumer_secret)
    get_auth.set_access_token(get_access_token,
                              get_access_token_secret)
    get_api = tweepy.API(get_auth)
except tweepy.error.TweepError:
    print("Invalid API")

# --------------------------------------------------------BOTFRIES----------------------------------------------------
try:
    post_consumer_key = 'drwRd4caSmINAvTC1A7tx7xA2'
    post_consumer_secret = 'XPVTGkclLB4HeXEQx9pfbg3twWlMfthj5EDaLlElJUMvvTclk9'
    post_access_token = '974810262401363968-GddtODwIvoytzgTj3gZmDIk6QK3aBB4'
    post_access_token_secret = 'awqFqQ1o7XPuKfHpyUrLEOBgMBDfB7sAtvzhzYenCyUWW'

    post_auth = tweepy.OAuthHandler(post_consumer_key,
                                    post_consumer_secret)
    post_auth.set_access_token(post_access_token,
                               post_access_token_secret)
    post_api = tweepy.API(post_auth)
except tweepy.error.TweepError:
    print("Invalid API")