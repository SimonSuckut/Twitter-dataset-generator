#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import sys
import os
import time

#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


def get_user_tweets(screen_name):
	
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	# check if the user exists
	try:
		u=api.get_user(screen_name)
	except tweepy.RateLimitError as e:
		return False		
	except tweepy.TweepError:
		return True
	
	alltweets = []	
	
	success = False		
	while (not success) :
		success = True
		try:
			tweets = api.user_timeline(screen_name = screen_name,count=200)
		except tweepy.RateLimitError as e:
			print("Limit exeeded. Waiting 5 minutes...")
			time.sleep(60*5)
			success = False		
		except tweepy.TweepError:
			print(e)
			success = False
		
	if len(new_tweets) == 0:
		return True

	alltweets.extend(tweets)
	oldest = alltweets[-1].id - 1

	while len(tweets) > 0:
		print("getting tweets before ", (oldest))
		
		success = False	
		while (not success) :
			success = True
			try:
				tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
			except tweepy.RateLimitError as e:
				# API limit exeeded. Wait for 5 minutes
				print("Limit exeeded. Waiting 5 minutes...")
				time.sleep(60*5)
				success = False		
			except tweepy.TweepError:
				print(e)
				success = False
		
		alltweets.extend(tweets)
		
		oldest = alltweets[-1].id - 1
	
	alltweets = [[tweet.user.id, tweet.user.screen_name, tweet.id, tweet.text] for tweet in alltweets if not tweet.retweeted]

	with open('output/%s_tweets.csv' % screen_name, 'w', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerow(["user_id", "screen_name", "id", "text"])
		writer.writerows(alltweets)
	
	return True


if __name__ == '__main__':
	#pass in the username of the account you want to download
	f = open("../accounts", 'r')
	accounts = f.read().splitlines()
	f.close() 

	if os.path.exists("output") :
		for root, dirs, files in os.walk("output", topdown=False):
			for name in files:
				os.remove(os.path.join(root, name))
			for name in dirs:
				os.rmdir(os.path.join(root, name))		
	else :
		os.mkdir("output")

	for acc in accounts:
		print(acc)
		while(not get_user_tweets(acc)): 
			print("Retry...")
