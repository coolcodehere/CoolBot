from APIAccess import api
tweetCount = 1000
tweets = api.user_timeline(screen_name='Bushfries', count=tweetCount, include_rts=True)


def getTweets():
    cleanTweet = []
    for status in tweets:
        tweet = status.text
        tweet = tweet.split(" ")
        text = list(filter(lambda word: "https" not in word.lower() and "@" not in word.lower(), tweet))
        for word in text:
            cleanTweet.append(word)
    return cleanTweet


def deleteContent(file):
    file.seek(0)
    file.truncate()


def saveFile(file, wordBase):
    writeString = ""
    for word in wordBase:
        try:
            file.write(word + "\n")
        except UnicodeEncodeError:
            print("Can't encode special char")
    file.close()

wordFile = open('words.txt', 'r+')
deleteContent(wordFile)
wordBase = getTweets()
saveFile(wordFile, wordBase)


