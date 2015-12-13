import requests
import json
import time

from requests_oauthlib import OAuth1

# authentication pieces
client_key    = ""
client_secret = ""
token         = ""
token_secret  = ""

# the base for all Twitter calls
base_twitter_url = "https://api.twitter.com/1.1/"

# setup authentication
oauth = OAuth1(client_key,client_secret,token,token_secret)


# https://api.twitter.com/1.1/users/show.json?screen_name=twitterdev


def convert_username(user,user_type):
    api_url = "https://api.twitter.com/1.1/users/show.json?"
    
    if user_type == "username":
        
        api_url += "screen_name=%s" % user
        
    else:
        
        api_url += "user_id=%d" % user
        

    response = requests.get(api_url,auth=oauth)
        
    time.sleep(3)
        
    if response.status_code == 200:
            
        result = json.loads(response.content)
            
        return result
    
    else: print "[*] Twitter API FAILED! %d" % response.status_code
        
    return None

result = convert_username("twitter handle","username")

print "Screen name [name]: ", result['name']
print "User Id: ", result['id']
