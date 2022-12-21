#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import tweepy
 
#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
        if GPIO.input(channel):

                text = "Water Detected!"
                print(text)
                sendMessage(text)
                
        else:
                text = "No Water Detected!"
                print(text)
                sendMessage(text)

 
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
 
# assign the values accordingly
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# ID of the recipient
recipient_id = 1249304815

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)

# calling the api
api = tweepy.API(auth)

previous_dm = ""

# send the message
def sendMessage(text)
    
    # sending the direct message
    if (previous_dm != text):
        direct_message = api.send_direct_message(recipient_id, text)
        previous_dm = text

    # print the text, can be used for debugging
    # print(direct_message.message_create['message_data']['text'])



# infinite loop
while True:
        time.sleep(1)
