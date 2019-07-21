import tweepy
consumer_key = "ypWAv9QvDwyuYoA03ysNFpwaL" 
consumer_secret = "3nsGriPliwAlNKXc0m7HYZ64ZUEXt4jVmaJaUxbqIeJhyPQotx"
access_key = "1328561335-bEeA5T5kDindRC2QhAQpwJSl11zVenDhQVXKqZX"
access_secret = "UYmfF64acAkglBuRkH4OZdJTGiz3oaSfc0kbUn6gN8zeW"
  
# Function to extract tweets 

def get_tweets(username): 
          
        # Authorization to consumer key and consumer secret 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        # Access to user's access key and access secret 
        auth.set_access_token(access_key, access_secret) 
  
        # Calling api 
        api = tweepy.API(auth) 
        userobj = api.get_user(username)
        print("User'Name :" +userobj.name)
        print(" Screen Name: "+userobj.screen_name)
        print(" User's Location: " +userobj.location)
        userobj.description = userobj.description.replace("\n", "");
        print(" User's Description: "+userobj.description)
        print(" Followers count:"+str(userobj.followers_count))
        print(" Friends Count:"+str(userobj.friends_count))  
        print("\n\n")

        # 200 tweets to be extracted 
        number_of_tweets=200
        tweets = api.user_timeline(screen_name=username) 
  
        # Empty Array     
        tmp=[]  
  
        # create array of tweet information: username,  
        # tweet id, date/time, text 
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
        for j in tweets_for_csv: 
  
            # Appending tweets to the empty array tmp 
            tmp.append(j)  
  
        # Printing the tweets 
        print(tmp) 
  
  
# Driver code 
if __name__ == '__main__': 
  
    # Here goes the twitter handle for the user 
    # whose tweets are to be extracted. 
    get_tweets("elonmusk")
     