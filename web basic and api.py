
#                                                                                 ---WEB BASIC AND API ---




# Q1:-  What is an access token? Generate your access token for any API.

'''

Access Tokens :- An access token is an object that describes the security context of a process or thread.
                        The information in a token includes the identity and privileges of the user account associated with the process or thread.
                        When a user logs on, the system verifies the user's password by comparing it with information stored in a security database.
                        If the password is authenticated, the system produces an access token.
                        Every process executed on behalf of this user has a copy of this access token.

API Key          :- AIzaSyAz9kfWWe0-i8xmYQo0SPkzQPIwLVqWtrQ

'''

####################


# Q2:- Get the IP address of some common sites like Google, Facebook by using DNS lookup.

'''

import socket
a=(socket.gethostbyname('google.com'))
print(" IP address of Google is ",a)
b=(socket.gethostbyname('facebook.com'))
print(" IP address of Google is ",b)

'''

########################


# Q3:-  Using google API

'''
import urllib.request
import json
url='https://maps.googleapis.com/maps/api/directions/json?'
api='AIzaSyARaUqq0lZgvvD6W6lUH1l0HEwm8kd5DHo'
origin=input("Tell me your location:").replace(' ','+')
destination=input("Where you want to go ? :").replace(' ','+')
nav_request='origin={}&destination={}&key={}'.format(origin,destination,api)
request=url+nav_request
response=urllib.request.urlopen(request).read().decode('utf-8')
directions=json.loads(response)
print(directions)


'''

###################



# Q4:- What is a difference between library and API . Figure it out with examples.

'''

library :- A library is a collection of functions/objects that serves one particular purpose. we could use a library in a variety of projects.
             ex. android.app.Activity library (Class with all code).
API     :- An API is an interface for other programs to interact with our program or library without having direct access.
             Android API to interact with hardware, like the front camera of an Android based device.
              ex. If your app needs to vibrate the phone, you must use the Android API method like vibratePhone.

'''

######################


# Q5:- Try to access Spotify API . Find out some library for it and play some music.

"""
Spotify is not avliable in india.

"""
############# END 
