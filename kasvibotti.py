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
consumer_key = "hnawz3FtbulfqNldgUROu2nfD"
consumer_secret = "qp1JuM3JrtMg7y0EvtBiqQSdolFO0oU1khITkUjbWgOYtYcXxp"
access_token = "1431700356707323906-VICQVoJAD3yKpb27c0aOGG72fr3lUW"
access_token_secret = "penb6MgM5Lqwlwq8wLN2M66RPpREfKR0PVBceOm8HDiWQ"

# ID of the recipient
recipient_id = 1249304815

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)

# calling the api
api = tweepy.API(auth)


def sendMessage(text):

    # sending the direct message
    direct_message = api.send_direct_message(recipient_id, text)

    # printing the text of the sent direct message
    print(direct_message.message_create['message_data']['text'])



# infinite loop
while True:
        time.sleep(1)
