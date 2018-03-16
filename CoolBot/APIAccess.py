import tweepy

try:
    consumer_key = 'lZKHiGxzaac9eApuedZ8FuBlR'
    consumer_secret = 'QBo2RJob1Jz9QUg67S47cGPg3enQRwnQHii1r9Al1ikDxcQLG5'
    access_token = '834452681355882496-aCwWCJ3ynIP15j5afgM9e5KrPKXUjQp'
    access_token_secret = 'VTe2Hd9Rki4JxBJYk9siJf7hxXmiAPpn8FKCHtJh6oFss'

    auth = tweepy.OAuthHandler(consumer_key,
                               consumer_secret)
    auth.set_access_token(access_token,
                          access_token_secret)
    api = tweepy.API(auth)

except tweepy.error.TweepError:
    print("Invalid API")
