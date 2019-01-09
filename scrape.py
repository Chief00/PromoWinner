import tweepy
import re
import requests

# All the access keys to authenticate
API_Key = "ZOXLUeZrRxZA2Z9Q5b3UaNpbh"
API_Secret_Key = "nEW3yCXzC0DSPp3fSEG74fkztB4jOsxtrXw9r07OSOWql1Ii4n"
Access_Token = "308574125-vDu3m6myZRUBA6vmjJCmEE2n2hzQS9hGRLSpRtIj"
Access_Token_Secret = "2bAoI8yIdbgVyIEQfGptSYJ6eNtKMRheE7rcx1a2RdxV9"

# Authenticating and creatign the api variable for use
auth = tweepy.OAuthHandler(API_Key, API_Secret_Key)
auth.set_access_token(Access_Token, Access_Token_Secret)
API = tweepy.API(auth)


def userTweets(user, ntweets):
    # Getting last tweet from user
    userTweet = API.user_timeline(user, count=ntweets)[0].text
    return userTweet


tweetString = userTweets("sam_beckman", 1)

# Regex tweet link
tweetLinkRE = re.compile('https://t.co/\w+')


if "promo" and "KLCK" in tweetString:
    print(tweetLinkRE.search(tweetString).group())
