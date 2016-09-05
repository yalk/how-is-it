import tweepy
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#single_tweet = 'This has been posted by the #TwitterAPI :)'
#api.update_status(single_tweet)
#print "successfully Updated"

query = 'wolf'
max_tweets = 2
'''searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]

for tweet in searched_tweets:
	print tweet[0]
'''

newlist= api.search(q='wolf', count='1')
print newlist
