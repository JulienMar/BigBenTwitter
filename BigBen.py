import tweepy

keys = [line.rstrip('\n') for line in open('AccessKeys.txt')]
consumer_key = keys[0]
consumer_secret = keys[1]

access_token = keys[2]
access_token_secret = keys[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def get_tweets():
    tweets = api.user_timeline(screen_name="big_ben_clock", count="25")
    return tweets

tweets = get_tweets()

for tweet in tweets:
    print(tweet.text)
    print(str(tweet.created_at))
    print(tweet.retweet_count)
