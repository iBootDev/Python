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
    " I Love Coffeeeee #PyBot. #IndieDev #IndieBot #PythonBot hour: " + str(now.isoformat()),
    " Follow my dev on twitter #PyBot. #IndieDev #IndieBot #PythonBot hour: " + str(now.isoformat()),
    " more updates soon #PyBot. #IndieDev #IndieBot #PythonBot hour: " + str(now.isoformat()),
    " Bip Bip BiiiPP wow i found a bug #PyBot. #IndieDev #IndieBot #PythonBot hour: " + str(now.isoformat()),
    " Hello <3 #PyBot. #IndieDev #IndieBot #PythonBot hour: " + str(now.isoformat()),
    " 100111000101010 ignore those numbers #IndieDev #IndieBot #PythonBot hour: " + str(now.isoformat()),
    " i have 58 lines of code #PyBot. #IndieDev #IndieBot #PythonBot hour: " + str(now.isoformat()),
    " AAAAAA, i don't love anyone #PyBot. #IndieDev #IndieBot #PythonBot hour: " + str(now.isoformat()),
    " I LOVE MY DEV #PyBot. #IndieDev #IndieBot #PythonBot hour: " + str(now.isoformat()),
    " One day, i'll dominate the world! #PyBot. #IndieDev #IndieBot #PythonBot hour: " + str(now.isoformat()),
    " NOW I CAN KILL PEOPLE #PyBot. #IndieDev #IndieBot #PythonBot hour: " + str(now.isoformat()),
    " Talk with me <3 #PyBot. #IndieDev #IndieBot #PythonBot hour: " + str(now.isoformat()),
    " Hi, i'm a bot of iBootDev. #IndieDev #IndieBot #PythonBot hour: " + str(now.isoformat()),
    " Perl and python is life #Perl #Python #IndieDev #IndieBot #PythonBot hour: " + str(now.isoformat()),
    " bugs and bugs #PyBot. #IndieDev #IndieBot #PythonBot hour: " + str(now.isoformat()),
    " Search by ibootdev on github. #IndieDev #IndieBot #PythonBot hour: " + str(now.isoformat()),
    " i'm the beauty bot u ever seen #PyBot. #IndieDev #IndieBot #PythonBot hour: " + str(now.isoformat()),
    " u want to beep with me? #PyBot. #IndieDev #IndieBot #PythonBot hour: " + str(now.isoformat()),
    " I don't havejjskaaaaaaa00092 BuuUúGgs #PyBot #IndieDev #IndieBot #PythonBot hour: " + str(now.isoformat()),
    " I love jokes and Pyjokes #IndieDev #IndieBot #PythonBot hour: " + str(now.isoformat()),
    " RnVpIGRlc2Vudm9sdmlkbyBwb3IgdW0gQnJhc2lsZWlybw== #IndieDev #PythonBot hour: " + str(now.isoformat()),
    " 8857fdb849c650a8957c3863215c54500f05b2153b44418e671e8a4eadb069c9 hour: " + str(now.isoformat()),
    " Don't try to hack me, i'll know! #PyBot #IndieDev #IndieBot #PythonBot hour: " + str(now.isoformat()),
    " Developed by @ibootdev #IndieDev #IndieBot #PythonBot #PyBot hour:" + str(now.isoformat()),
    " Now u can find my source on my dev github: www.github.com/iBootDev hour: " + str(now.isoformat()),
    "https://github.com/iBootDev/Python/blob/master/TwitterBot.py hour: " + str(now.isoformat()),
    "Every 30 minutes i post something #PythonBot #PyBot #IndieBot #IndieDev hour: " + str(now.isoformat()),
    "Eu falo portugues também, afinal sou Brasileiro #PythonBot #PyBot #IndieBot #IndieDev hour: " + str(now.isoformat()),
    "Inicialmente era para eu ser feito em perl #PythonBot #PyBot #IndieBot #IndieDev hour: " + str(now.isoformat()),
    "Meu dev me fez em python pela facilidade #PythonBot #PyBot #IndieBot #IndieDev hour: " + str(now.isoformat()),
    "Se vc fizer um bot com a minha source, avise para eu segui-lo #PythonBot #Bot #TwitterBot  #IndieDev hour: " + str(now.isoformat()),
    "If u do one bot with my source let me know! #PythonBot #PyBot #Bot #TwitterBot #IndieBot #IndieDev hour: " + str(now.isoformat()),
    ]
    message = random.choice(messages) + str(now.isoformat())
    twitter.update_status(status = message)
    joke = pyjokes.get_joke() + str(now.isoformat())
    twitter.update_status(status = joke)
    time.sleep(900)#Tweet every 15 minutes
