import tweepy

keys = [line.rstrip('\n') for line in open('AccessKeys.txt')]
consumer_key = keys[0]
consumer_secret = keys[1]

access_token = keys[2]
access_token_secret = keys[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = api.user_timeline(screen_name="big_ben_clock", count="25")
for tweet in tweets:
    print(tweet.text)
