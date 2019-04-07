
# coding: utf-8

# ### importing Twitter API

# In[1]:


from TwitterAPI import TwitterAPI, TwitterPager


# In[2]:


SCREEN_NAME = 'Twitter username Here'


# In[4]:


ConsumerKey = 'Your ConsumerKey Here'
ConsumerSecret = 'Your ConsumerSecret Here'
# AccessToken = 'Your AccessToken Here'
# AccessTokenSecret = 'Your AccessTokenSecret Here'
API = TwitterAPI(ConsumerKey,ConsumerSecret,auth_type='oAuth2')
pager = TwitterPager(API,'statuses/user_timeline',{'screen_name':SCREEN_NAME, 'count':200})


# In[5]:


Tweets = []


# In[6]:


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

