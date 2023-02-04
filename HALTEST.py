import os
os.system("requirments.bat")
from HAL9000inputoutput import defget
from HAL9000inputoutput import get_password_and_gmail
import speech_recognition as sr
import font
from HAL9000inputoutput import say
import sys
import winsound
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
#WAKES=["hey google","ok google","google activate"]
WAKES=["hey how","ok how","how activate","hey hal","ok hal","hal activate"]
SETUP = "how setup"
SETUP2 = "how set up"
# keys for activating stuff
CMD = "0000"
DOOR1 = "0005"
LIGHT1 = "0001"
LIGHT2 = "0002"
LIGHT3 = "0003"
LIGHT4 = "0004"
exited=0
noteid=0
while True:
    try:
        print("Listening")
        text = get_audio().lower()
        x=0
        if(text==SETUP or text==SETUP2):
            winsound.Beep(200,10)
            winsound.Beep(150,10)
            winsound.Beep(100,10)
            winsound.Beep(50,10)
            
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
        while(x<len(WAKES)):
            WAKE=WAKES[x]
            x=x+1
            if text.startswith(WAKE):
                if text==WAKE:
                    print ("detecting:")
                    winsound.Beep(500,200)
                    text = get_audio()
                elif text.startswith(WAKE):
                    text=text.split(WAKE)[1]
                resp,noteid=defget(text,noteid)
        if text.count(SHUTDOWN) > 0:
            winsound.Beep(500,200);winsound.Beep(200,200)
            exited=1
            exit()
        print(text)
    except Exception as e:
        font.gen("error")
        print(e)
        os.execv(sys.executable, [sys.executable] + sys.argv)
if(exited==0):input()
#pause on crash
