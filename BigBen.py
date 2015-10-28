import tweepy

keys = [line.rstrip('\n') for line in open('AccessKeys.txt')]
consumer_key = keys[0]
consumer_secret = keys[1]

access_token = keys[2]
access_token_secret = keys[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
