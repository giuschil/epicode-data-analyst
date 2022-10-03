import tweepy

def main():
    twitter_auth_keys = {
        "consumer_key": "ILdHmJcxixtwNAPdZLHkjSW8e",
        "consumer_secret": "TnMJiXJqEqFdS3HdcEBwRHRv2crtDXXqPwYBz4sTcKRo39dgTe",
        "access_token": "1576293965963436032-bHRdDjbCV8aJcAt0wIr4R2udhOQEJ6",
        "access_token_secret": "XnXq9lcHWdi2dAnz4lGEmzXwNWS54TqXlGLl9lTNhlkmCT"
    }

    auth = tweepy.OAuthHandler(
        twitter_auth_keys['consumer_key'],
        twitter_auth_keys['consumer_secret']
    )
    auth.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_token_secret']
    )
    api = tweepy.API(auth)

    tweet = "Another day, another #scifi #book and a cup of #coffee"
    status = api.update_status(status=tweet)


if __name__ == "__main__":
    main()