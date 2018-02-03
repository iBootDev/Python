#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy, time, sys
import random
from twython import Twython
import pyjokes
import datetime
#CODED BY iBootDev. Twitter: @ibootdev Bot twitter: @iBoot_Bot
#enter the corresponding information from your Twitter application:
now = datetime.datetime.now()
CONSUMER_KEY = ''#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = ''#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = ''#keep the quotes, replace this with your access token
ACCESS_SECRET = ''#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
#Keys
twitter = Twython(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_KEY,
    ACCESS_SECRET
)
while True:
    messages = [
    " I Love Coffeeeee #PyBot. hour: ",
    " Follow my dev on twitter #PyBot. hour: ",
    " more updates soon #PyBot. hour: ",
    " Bip Bip BiiiPP wow i found a bug #PyBot. hour: ",
    " Hello <3 #PyBot. hour: ",
    " 100111000101010 ignore those numbers #PyBot. hour: ",
    " i have 153 lines of code #PyBot. hour: ",
    " AAAAAA, i don't love anyone #PyBot. hour: ",
    " I LOVE MY DEV #PyBot. hour: ",
    " One day, i'll dominate the world! #PyBot. hour: ",
    " NOW I CAN KILL PEOPLE #PyBot. hour: ",
    " Talk with me <3 #PyBot. hour: ",
    " Hi, i'm a bot of iBootDev. hour: ",
    " Perl and python is life #Perl #Python #PyBot. hour: ",
    " bugs and bugs #PyBot. hour: ",
    " Search by ibootdev on github. hour: ",
    " i'm the beauty bot u ever seen #PyBot. hour: ",
    " u want to beep with me? #PyBot. hour: ",
    " I don't havejjskaaaaaaa00092 BuuUúGgs #PyBot hour: ",
    " I love jokes and Pyjokes hour: ",
    " RnVpIGRlc2Vudm9sdmlkbyBwb3IgdW0gQnJhc2lsZWlybw== hour: ",
    " 8857fdb849c650a8957c3863215c54500f05b2153b44418e671e8a4eadb069c9 hour: "
    " Don't try to hack me, i'll know! #PyBot hour: "
    " Developed by @ibootdev"
    " Want my source code? Now u can find on my dev github: www.github.com/iBootDev"
    " Follow the link: https://github.com/iBootDev/Python/blob/master/TwitterBot.py"
    ]
    message = random.choice(messages) + str(now.isoformat())
    twitter.update_status(status = message)
    joke = pyjokes.get_joke() + str(now.isoformat())
    twitter.update_status(status = joke) + str(now.isoformat())
    time.sleep(900)#Tweet every 15 minutes
