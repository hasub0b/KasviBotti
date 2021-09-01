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
consumer_key = "YOURVALUEHERE"
consumer_secret = "YOURVALUEHERE"
access_token = "YOURVALUEHERE"
access_token_secret = "YOURVALUEHERE"

# ID of the recipient
recipient_id = "YOURVALUEHERE"

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)

# calling the api
api = tweepy.API(auth)

# send the message
def sendMessage(text):

    # check previous DM to prevent unnecessary spam
    previous_messages = api.sent_direct_messages
    prevoius_dm = previous_messages[0].message_create['message_data']['text']
    
    # sending the direct message
    if (previous_dm != text):
        direct_message = api.send_direct_message(recipient_id, text)

    # print the text, can be used for debugging
    # print(direct_message.message_create['message_data']['text'])



# infinite loop
while True:
        time.sleep(1)
