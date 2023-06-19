import webbrowser
import time

username = input("enter the sepcific username to see the info: ")
inputURL = 'https://api.github.com/users/' + username
openwebbrowser = webbrowser.open(inputURL, new=2)
time.sleep(2)
repoornot = input("do you want to see the information about their repositories(y/n): ")


def choose():
    if repoornot == "y" or "Y":
        InputURL = 'https://api.github.com/users/' + username + '/repos'
        openwebbrowser = webbrowser.open(InputURL, new=2)
        time.sleep(10)

    if repoornot == "n" or "N":
        print("terminating process")
        time.sleep(5)

    else:
        print("enter y or n only")
        choose()


choose()
