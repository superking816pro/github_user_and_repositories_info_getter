import webbrowser
import time
import os
import json
import requests

path = "/temp"
isExist = os.path.exists(path)
if isExist == False:
    os.mkdir("temp")

username = input("enter the sepcific username to see the info: ")
inputURL = 'https://api.github.com/users/' + username
openwebbrowser = webbrowser.open(inputURL, new=2)
time.sleep(2)
repoornot = input("do you want to see the information about their repositories(y/n): ")

request1 = requests.get(inputURL, allow_redirects=True)

with open('temp/superking816pro.json','r') as firstfile:
    for line in firstfile:
        jsonfile = line

loadjson = json.loads(jsonfile)

print("username:" + jsonfile["login"])
print("type:" + jsonfile["type"])
print("site admin:" + jsonfile["site_admin"])
print("name:" + jsonfile["name"])
print("company:" + jsonfile["company"])
print("blog:" + jsonfile["blog"])
print("location:" + jsonfile["location"])
print("email:" + jsonfile["email"])
print("hireable:" + jsonfile["hireable"])
print("bio:" + jsonfile["bio"])
print("twitter username:" + jsonfile["twitter_username"])
print("public repos:" + jsonfile["public_repos"])
print("public gists:" + jsonfile["public_gists"])
print("followers:" + jsonfile["followers"])
print("following:" + jsonfile["following"])
print("created at:" + jsonfile["created_at"])
print("updated at:" + jsonfile["updated_at"])


if repoornot == "y" or "Y":
    InputURL = 'https://api.github.com/users/' + username + '/repos'
    openwebbrowser = webbrowser.open(InputURL, new=2)
    time.sleep(10)

if repoornot == "n" or "N":
    print("terminating process")
    quit()

else:
    print("enter y or n only")
