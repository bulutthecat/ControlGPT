import os
from HAL9000inputoutput import defget
from HAL9000inputoutput import get_password_and_gmail
import speech_recognition as sr
import font
from HAL9000inputoutput import say
import sys
from HAL9000inputoutput import make_sound
import json
global overridechat, wakes, setup, setup2
overridechat=False
def get_audio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""
            try:
                said = r.recognize_google(audio)
            except Exception as e:
                print("Exception: " + str(e))
        return said.lower()

SHUTDOWN = "process exit"
#WAKES=["hey google","ok google","google activate"] - Works better, but its a knockoff so I refuse to use it
# keys for activating stuff

def get_settings():
    default_data = {
        "wakes": ["hey how", "ok how", "how activate", "hey Hal", "ok Hal", "Hal activate", "hey house", "Hey House", "hey House", "ok house", "hey hal", "ok hal"],
        "setup": "how setup",
        "setup2": "how set up"
    }

    try:
        with open('settings.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        # File does not exist, return default data
        return default_data

    # File exists, return data from the file
    return data["wakes"], data["setup"], data["setup2"]

wakes, setup, setup2 = get_settings()

print(f"wakes = {wakes}")
print(f"setup = {setup}")
print(f"setup2 = {setup2}")

#cmd:finaly no more legecy junk
exited=0
noteid=0
while True:
    try:
        print("Listening")
        if(overridechat==False):
         text = get_audio().lower()
        else:
         text=input()
        x=0
        if(text==setup or text==setup2):
            make_sound(200,10)
            make_sound(150,10)
            make_sound(100,10)
            make_sound(50,10)
            
            say("are you sure?")
            font.gen("Y / N")
            text = get_audio()
            text=text.replace("i am ","im ")
            text=text.replace("im ","i ")
            text=text.replace("i sure","")
            text=text.replace("sure","y")
            text=text.replace("yes","y")
            text=text.replace("no","n")
            text=text.replace("dont","n")
            if(text=="y"):
                os.system("del /f data.json")
                get_password_and_gmail()
        while(x<len(wakes)):
            WAKE=wakes[x]
            x=x+1
            if text.startswith(WAKE):
                if text==WAKE:
                    print ("detecting:")
                    make_sound(500,200)
                    if(overridechat==False):
                     text = get_audio().lower()
                    else:
                     text=input()
                elif text.startswith(WAKE):
                    text=text.split(WAKE)[1]
                resp,noteid=defget(text,noteid)
        if text.count(SHUTDOWN) > 0:
            make_sound(500,200)
            make_sound(200,200)
            exited=1
            exit()
        print(text)
    except Exception as e:
        font.gen("error")
        print(e)
        os.execv(sys.executable, [sys.executable] + sys.argv)
if(exited==0):input()
#pause on crash
