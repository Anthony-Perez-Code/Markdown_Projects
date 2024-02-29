#Import the necessary modules to retrieve data from URLs and to change the string that is retrieved into a Python List.

import urllib.request
import ssl
import json

#Ignore any certification requirements

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Connect to the URL and retrieve the requested data

url = "https://jsonplaceholder.typicode.com/comments"
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()

#Convert retrieved data (a string) into a Python List for easy navigating

info = json.loads(data)

#Begin User Interface with introduction of the application

print("\nWelcome to the Latin Phrase Repository, where students can post comments about something in Latin. Follow the following instructions to practice your Latin comprehension. If at anytime you wish to quit, just type \"quit\".")

#Begin a loop that prompts for input and quits if requested

while (True):
    x = input("\nTo retrieve a post, please enter a number from 1-500. Along with the post, you'll also retrieve the email address of the student who posted it if you'd like to practice with someone.")
    if x == "quit":
        break
    x = int(x)
    if (x - 1) not in range(0,500):
        print("Your input is invalid. Ensure that your input follows the instructions given.")
        continue
    print("\nHere's the comment you requested.\n")
    print("The title of the post is \"",info[x - 1]['name'],"\"")
    print("The post is \"", info[x - 1]['body'],"\"")
    print("The email address of the poster is \"", info[x -1]['email'], "\"\n")