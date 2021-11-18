# Scarpe twitter
#  Objective: Download tweets for Kenyan agricultural firms and banks.
#  Clean the tweets, extract the required information and store it
#  in excel.From excel import the data into stata for statistical analysis.
# The text of the tweet is used for sentiment analysis, which was performed
# using the LIWC software.

import json
import requests
import tweepy
import csv
import re
import string
import pandas as pd
import numpy as np
Access_Token = 'xyz'
Access_Token_Secret = 'pqr'
Consumer_Key = 'abc'
Consumer_Secret = 'efg'

# Authenticate to twitter
auth = tweepy.OAuthHandler(Consumer_Key, Consumer_Secret)
auth.set_access_token(Access_Token, Access_Token_Secret)

# Create a tweepy object
api = tweepy.API(auth)
alltweets = [] # initialize a list to hold all tweets


# make initial request for most recent tweets
# (200 is the maximum allowed count)

new_tweets = api.user_timeline(id="@kenyaseed",count= 200,
                               include_entities="true",include_rts= "true",
                               include_my_retweet = "true")

#save most recent tweets
alltweets.extend(new_tweets)

#save the id of the oldest tweet less one
oldest = alltweets[-1].id - 1


#keep grabbing tweets until there are no tweets left to grab
while len(new_tweets) > 0:
   print("getting tweets before %s" % (oldest))
   #all subsiquent requests use the max_id param to prevent duplicates
   new_tweets = api.user_timeline(id = "@kenyaseed",count= 200,
                                  include_entities="true",include_rts= "true",
                                  include_my_retweet = "true", max_id=oldest)
   #save most recent tweets
   alltweets.extend(new_tweets)

   #update the id of the oldest tweet less one
   oldest = alltweets[-1].id - 1
   print("...%s tweets downloaded so far" % (len(alltweets)))


# convert every single item of the list into a json object.
jalltweets = map(lambda x: x._json, alltweets)

# from JSON object to JSON string
json.dumps(jalltweets[0])
pdf = pd.DataFrame(jalltweets)

############ TOTAL NUMBER OF RETWEETS #####################
###Retweet ---- calculated via the API
# 0 = not a retweet &&& 1 = a retweet


###Manual Retweet
# Function: tracks the presence of 'RT' in the column (Name of the column is text)
# Note: The text column contains the tweets in text format
def trace_rt(text):
    z = re.findall('RT',text)
    if 'RT' in text:
        return 1
    else:
        return 0

# Calling the function to check the presence of RT in the column(name of the column is text)
pdf['text_RT'] = pdf['text'].apply(trace_rt)
pdf ['Retweet_total'] = pdf['text_RT'] + pdf['retweet_count']


# Calculate how many users are mentioned
pdf["User_names_trial"] = pdf['entities'].map(lambda x: x['user_mentions'])
pdf["Usermention_api"] = pdf["User_names_trial"].map(lambda lst: map(lambda x: x["name"], lst))

# Calculate how many hashtags are used
pdf["Hashtags_trial"] = pdf['entities'].map(lambda x: x['hashtags'])
pdf["Hashtags_api"] = pdf["Hashtags_trial"].map(lambda lst: map(lambda x: x["text"], lst))

# Calculate how many Urls are used
pdf["Urls_trial"] = pdf['entities'].map(lambda x: x['urls'])
pdf["Urls_api"] = pdf["Urls_trial"].map(lambda lst: map(lambda x: x["expanded_url"], lst))

# Hashtag from text ---- Informal
# Function: tracks the presence of # in the column (Name of the column is text) and extract hashtag words
def trace_hashtag(text):
    store = set([i for i in text.split() if i.startswith("#")])
    return list(store)
pdf['Hashtag_informal'] = pdf['text'].apply(trace_hashtag)

# '@' from text ---- Informal mention of user
# Function: tracks the presence of @ in the column (Name of the column is text) and extract words written with @
def trace_informal_usermention(text):
    store = set([i for i in text.split() if i.startswith("@")])
    return list(store)
pdf['usermention_informal'] = pdf['text'].apply(trace_informal_usermention)


# Function: Count the number of hastag (informal)/ username, etc present in a tweet
def estimate_size(Hashtag_detail):
    value = len(Hashtag_detail)
    return value

### Counting formal & informal hashtag
pdf['Hashtag_informal_count'] = pdf['Hashtag_informal'].apply(estimate_size)
pdf['Hashtag_api_count'] = pdf["Hashtags_api"].apply(estimate_size)

### Counting formal & informal usage of '@'
pdf['usermention_informal_count'] = pdf['usermention_informal'].apply(estimate_size)
pdf['Usermention_api_count'] = pdf ['Usermention_api'].apply(estimate_size)

### Counting number of urls
pdf['Urls_api_count']= pdf['Urls_api'].apply(estimate_size)

# If the represented tweet is a reply, this field will contain screen name of the original tweet author. Hence,
# If the value is '1' it means a reply.
pdf['In_reply_tweet_binary'] = pdf['in_reply_to_screen_name'].isnull().map(lambda x: int(not x))

############### CLEANING THE TEXT ######################
def rmtags(inStr):
    rex1 = re.compile("([#@].*?[$\W]+)|(RT[\s$])|(http(s?)://.*?[$\s]+)")
    return rex1.sub("", inStr+" ").strip()

pdf["text_Clean"] = pdf["text"].map(rmtags)

### Everything
pdf.to_excel('@kenyaseed__19thFeb_Entire_not_clean.xls',  encoding='utf-8')

pdf.dtypes

# For rest of the firms
columnsNeeded = ["created_at","favorite_count","id","retweet_count","Manual_RT","Retweet_total",
               "Hashtag_informal_count", "Hashtag_api_count", "usermention_informal_count", "Usermention_api_count",
               "Urls_api_count", "In_reply_tweet_binary"]

pdf2 = pdf[columnsNeeded]

# Required for analysis
pdf2.to_excel('@kenyaseed_19thFeb_stata.xls',  encoding='utf-8')
