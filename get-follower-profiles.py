import tweepy
import json
import time

# Consumer keys and access tokens, used for OAuth
consumer_key = 'oEQBMb01E8gilQCblUU2Jkx4d'
consumer_secret = '3WP1k9CGyNBys0sasGAbIXFikkkTFZZplRkzfyIBUYHSgFlQGJ'
access_token = '802744359238193153-7gaKxjF5jXrhSbfDaXnhKgYVKUob9mv'
access_token_secret = 'TFunSHbWM62kyYC9tX7ik2R0DiE6PXKH2XKtVhzELq3Dv'


# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)


f= open('comedy-followers-profiles-65k-85k.json', 'w')  
#m = open('comedy-followers-count-1.json', 'w')  
#n = open('comedy-followers-description-1.json', 'w')  
follower_ids = open('comedy-followers-ids-65k-85k.json')    #input ids of followers
to_check = json.load(follower_ids)

profiles = []
jsonList1 = []    #store profiles
#jsonList2 = []    #store follower count
#jsonList3 = []    #store description

sleep_count = 0

for ids in to_check:
	sleep_count = sleep_count +1
	if sleep_count%860 == 0:
		print sleep_count/860,"waiting"
		time.sleep(60*17) 
		print "next"
	try:
		profiles = api.get_user(user_id=ids)
	except tweepy.TweepError:
		continue
	#profiles = api.get_user(user_id=ids)   #up to 900 per 15mins
	#print profiles.profile_image_url
	print ids
	jsonList1.append(profiles._json)
	#jsonList2.append(profiles.followers_count)
	#jsonList3.append(profiles.description)

json.dump(jsonList1,f,indent=4)
#json.dump(jsonList2,m,indent=4)
#json.dump(jsonList3,n,indent=4)




