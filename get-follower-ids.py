import tweepy
import json
import time

# Consumer keys and access tokens, used for OAuth

consumer_key = '9VipAibfwycvY0CpZ5zHlYCsP'
consumer_secret = 'MlXdeAkkIua8PqkqHG9QFaH9jz4fzg8EaLDwm9cMAKVBPMaU4V'
access_token = '740569772908285953-8AiclxVg8BUySx27j4JIWLFBWYh6uf3'
access_token_secret = 'S03gPewlYtVHnG2r3xNgIrZnFOJOFMAYs5sCDX6Epfiub'


# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)


f= open('comedy-followers-ids-100.json', 'w')
movieinfo = open('comedy-movie-screenname-100.json')


to_check = json.load(movieinfo)
ids = []
jsonList = []
results = []

sleep_count = 0
for i in to_check:
	for a in i:
		sn = a['screen_name']
		print sn
		
		sleep_count = sleep_count +1
		if sleep_count%15 == 0:
			time.sleep(60*17)       #sleep for 17 mins after every 15 calls (one movie per call)
		
		ids = api.followers_ids(screen_name = sn, count = 1000)    #up to 5000 ids each call, 15 calls per 15mins
		print len(ids), "followers' ids have been gathered from", sn 
		jsonList.append(ids)  #jsonList contains 100 sublists
for i in jsonList:
	for num in i:
		results.append(num)     # put all ids into one list
json.dump(results, f, indent = 4)


'''

	for id in ids:
		user = api.get_user(user_id=id)    #up to 100 users per call, 180 calls per 15mins
		print user.profile_image_url
'''
'''
	users = api.get_user(user_id=ids) #ieterates through the list of users and prints them
	for u in users:
		print u.screen_name
'''


	#image_url = [user.profile_image_url for user in api.lookup_users(user_ids=ids)]
	#jsonList.append(image_url._json)
	#json.dump(jsonList, f, indent = 4)

