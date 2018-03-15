import sys
import twitter
import random
"""
TODO:

Add api variables
Add if statement so tweet doesn't surpass character limit
Add length limit and increase word length
    -Decrease chance for new line
Add post class later
Add spaces randomly 
"""

api = twitter.Api(consumer_key='Jtg3dIWeT7adpv9l4YM3AVDSY',
                  consumer_secret='uclNdS6Vgod5EPh5v3Z8teJAb6C1eu8nCaSDIf7qbX9zednuib',
                  access_token_key='834452681355882496-aCwWCJ3ynIP15j5afgM9e5KrPKXUjQp',
                  access_token_secret='VTe2Hd9Rki4JxBJYk9siJf7hxXmiAPpn8FKCHtJh6oFss')
try:
    print("Valid API \n", api.VerifyCredentials())
except twitter.error.TwitterError:
    print("Invalid API")
    sys.exit()


def file_len(words):
    sum = 0
    for line in open("words.txt", "r"):
        sum += 1
    return sum


def createPost(file, wordCount):
    word = file.readlines()
    length = 280
    tweetLen = random.randint(1, 50)
    tweet = ""
    for x in range(0,tweetLen):
        if random.randint(0, 5) == 0:
            tweet += "\n"
        else:
            tweet += " " + str.rstrip(word[random.randint(0, (wordCount - 1))])
    return tweet


def postPost(post):
    api.PostUpdate(post)

words = open("words.txt", "r")
createdPost = createPost(words, file_len(words))
postPost(createdPost)