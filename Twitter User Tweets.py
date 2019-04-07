# importing Twitter API
from TwitterAPI import TwitterAPI, TwitterPager

SCREEN_NAME = 'Twitter username Here'

ConsumerKey = 'Your ConsumerKey Here'
ConsumerSecret = 'Your ConsumerSecret Here'
# AccessToken = 'Your AccessToken Here'
# AccessTokenSecret = 'Your AccessTokenSecret Here'
API = TwitterAPI(ConsumerKey,ConsumerSecret,auth_type='oAuth2')
pager = TwitterPager(API,'statuses/user_timeline',{'screen_name':SCREEN_NAME, 'count':200})

Tweets = []

# Storing Tweets into LIST
count = 0
for item in pager.get_iterator(wait=2.5):
    if 'text' in item:
        count = count + 1
        Tweets.append(item['text'])
        # print(count, item['text'])
    elif 'message' in item:
        print(item['message'])
        break
