import random
from APIAccess import api

"""
TODO:

Add if statement so tweet doesn't surpass character limit
Add length limit and increase word length
    -Decrease chance for new line
Add post class later
Add spaces randomly 
"""

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
        if random.randint(0, 100) == 0:
            tweet += "\n" + str.rstrip(word[random.randint(0, (wordCount - 1))])
        else:
            tweet += str.rstrip(word[random.randint(0, (wordCount - 1))]) + " "
    return tweet


def postPost(post):
    api.update_status(post)


def getTweets():
    api.user_timeline()


words = open("words.txt", "r")
createdPost = createPost(words, file_len(words))
print(createdPost)
print(len(createdPost))
postPost(createdPost)
