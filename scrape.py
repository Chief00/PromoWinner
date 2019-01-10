import tweepy
import requests
import os

# All the access keys to authenticate
API_Key = "ZOXLUeZrRxZA2Z9Q5b3UaNpbh"
API_Secret_Key = "nEW3yCXzC0DSPp3fSEG74fkztB4jOsxtrXw9r07OSOWql1Ii4n"
Access_Token = "308574125-vDu3m6myZRUBA6vmjJCmEE2n2hzQS9hGRLSpRtIj"
Access_Token_Secret = "2bAoI8yIdbgVyIEQfGptSYJ6eNtKMRheE7rcx1a2RdxV9"

# Authenticating and creatign the api variable for use
auth = tweepy.OAuthHandler(API_Key, API_Secret_Key)
auth.set_access_token(Access_Token, Access_Token_Secret)
API = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


def userTweets(user, ntweets):
    # Getting last tweet from user
    userTweet = API.user_timeline(user, count=ntweets)[0]
    return userTweet


# Inputs tweet into variable creates variable oldTweetID

oldTweetID = '1083198705275002880'
OCRLooper = True
mailLoop = True

while mailLoop:
    # Gets tweet from twitter
    tweet = userTweets("sam_beckman", 1)
    print("Tweet Collected")
    # Checks to see if its a new tweet
    if tweet["id"] != oldTweetID:
        oldTweetID = tweet["id"]
        print("New Tweet")

        # Creates variable of the text in tweet
        tweetText = tweet["text"]

        # Checks if text is about KLCK promo code and downloads the image
        if "promo" and "KLCK" in tweetText:
            tweetImageURL = tweetText["entities"]["media"][0]["media_url"]
            twitterImage = requests.get(tweetImageURL)
            open("PromoCodes.jpg", 'wb').write(twitterImage.content)

            # Runs tesseract
            os.system("tesseract PromoCodes.jpg PromoCodesText")

            # Waits for the text file to be created
            while OCRLooper:
                if os.path.isfile("Promocodes.txt"):
                    PromoCodesText = open(
                        "PromoCodesText.txt", 'r').read().split()
                    # loops through items in list and send a notification
                    for i in range(2, len(PromoCodesText) - 1):
                        os.system(
                            "curl -u o.HKHTPzhnlx9AsQuDtOicBXAlqaZAkseV:poppy12 https://api.pushbullet.com/v2/pushes -d type=note -d title=\"Promo Codes\" -d body=" + str(PromoCodesText[i]))
                OCRLooper = False
                mailLoop = False
