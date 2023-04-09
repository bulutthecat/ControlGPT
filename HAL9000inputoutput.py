import datetime
import os
from revChatGPT.V1 import Chatbot as ChatGPT
import random
import speech_recognition as sr
import json
import font
import webbrowser
import time
import keyring
import gkeepapi
from redmail import gmail # Not working, needs modification
import pyttsx3
from pynput.keyboard import Key, Controller # required to search local computer through windows search
import time
#imports

global newconv, storegmail, storepassword, variable_pairs, chatgptflag, loading, loadingtext, command, threading, noteid, app_password, sayoutput, overridechat, rules, keyboard

#set globals
overridechat=False # You shouldnt need to touch any of these, but as a breif overview. overridechat allows you to override voice commands, usefull if you are testing a new feature
app_password="" # just ignore this, idk what it is, I forgot what I was planning to do with it.
noteid=0
verson="2.0" # Version number, printed at the start if the program
has_been_called = False # Sendrules 
# Define a function to send a string of characters to the active window

keyboard = Controller()

def send_string(string):
    for char in string:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

# Define a function to search for a string in the Windows search bar
def windows_search(search_string):
    # Simulate Windows key press to open search bar
    keyboard.press(Key.cmd)
    keyboard.release(Key.cmd)
    time.sleep(0.5)

    # Send the search string to the search bar and press Enter to initiate search
    send_string(search_string)
    time.sleep(1)
def say(text): # call the TTS engine for your OS
    #the current tts engine
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def clear():
    os.system("cls")

def loading_animation(loading_text): # Loading animation, is not used after switching from webscraping (PyChatGPT, we had to wait to load the website) to on demmand results using revChatGPT API
    while loading:
        for frame in [" .", "  >", " ' ", " <"]:
            clear()
            font.gen(loading_text + frame) # You can use Font.get to generate font using our font engine 
            time.sleep(0.25) # Time between frames
    clear()

def incode(a): # Incodes the text, making plain Json files harder to decode and read (anybody that has acess to the plane json has acess to your ChatGPT account and possibly your Gmail)
    b = a + "#"
    c = "".join([b[x+1] + b[x] for x in range(0, len(a), 2)])
    return c.replace("#ThiSiSTheEnd", "").replace("ThiSiSTheEnd", "")

def get_password_and_gmail(): # Bunch of code that returns the details used for the ChatGPT API. WE NEED TO FIX THIS IT IS NOT WORKING
    try:
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = {}

    if set(['storepassword', 'storeid']) - set(data.keys()):
        say("Welcome to the HAL engine")
        font.gen(" <setup> ")

        data.update({
            'storepassword': incode(input('Please enter your password: ')),
            'storeid': input('Please enter your conversation ID: '),
            'sayoutput': "True",
            "username": incode(os.environ.get('username'))
        })

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)
    else:
        if data["username"] != incode(os.environ.get('username')):
            os.system("del data.json")
            return get_password_and_gmail()

    return (incode(data['storepassword']),
            data['storeid'],
            True)

password, conversation_id, sayoutput = get_password_and_gmail()



string_acess_token = str(password) #this is because if I directly write acess token it dosent work, for some reason.
chatbot = ChatGPT(config={
    "access_token": string_acess_token,
    "conversation_id": conversation_id
})
print("clearing chat")
say("clearing chat")
chatbot.clear_conversations()
with open("rules.txt", "r") as file:
    rules = file.read()
chatbot.ask(prompt=rules)
chatgpt_flag = True
loading=False
clear()
font.gen("hal engine")
font.gen(verson)
CMD = "0000"
DOOR1 = "0005"
LIGHT1 = "0001"
LIGHT2 = "0002"
LIGHT3 = "0003"
LIGHT4 = "0004"



def execute_command(command):
    if command.startswith("COMmand-"): # Run local CMD commands
        command = command.replace("COMmand-", "").replace("%username%", r"\%username%").split("Please note that")[0]
        print(command)
        os.system('echo hello')
        os.system(command)
    elif command.startswith("URL-"): # Open web pages
        webpage = command.split("Please note that")[0].split("RL-")[1]
        if not webpage.startswith("http"): webpage = "http://" + webpage
        webbrowser.open(webpage)
    elif command.startswith("PY-"): # Run generated python scripts
        code = command.split("Please note that")[0].replace("\nPY-", "\n").split("PY-")[1]
        print(code)
        exec(code)
    elif command.startswith("Search-"): # Search and run local programs
        search = command.replace("Search-", "")
        print("searching for " + search)
        windows_search(search)
        print("finished")
    # Other command cases go here
    return command

def defget(userinput, noteid):
    global resp, has_been_called
    resp = "ERROR"
    if userinput in ["hi", "hello"]:
        resp = "hello"
        say(resp)
    else:
        try:
            noteid2 = noteid + 1
            notetochat = [f"the time is {datetime.datetime.now()}", f"my username is {os.environ.get('username')}"]
            if not overridechat:
                if not has_been_called:
                    print("inside send rules")
                    with open('rules.txt', 'r') as f:
                        rules = f.read()
                    for data in chatbot.ask(str(rules)):
                        print('sent rules')
                    has_been_called = True
                for data in chatbot.ask(prompt=str(f"{userinput},note {notetochat[noteid]}")):
                    resp = data.get('message')
                say(resp)
                command = resp
            else:
                command = input()
            if noteid2 == len(notetochat): noteid2 = 0
            iscom = 0
            if command.count(CMD) == 1:
                iscom = 1
                os.system('start cmd.exe')
            else:
                command = execute_command(command)

            if iscom == 0 and sayoutput == "True":
                say(command)
            elif sayoutput != "True":
                print(command)

        except Exception as e:
            print("error")
            print(e)

    return command, noteid2