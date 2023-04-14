import datetime
import os
from revChatGPT.V1 import Chatbot as ChatGPT
import json
import font
import webbrowser #cmd:we should probly allow this to be used if someone doesnt want to give out there api key - KevinE: umm, idk maybe, wont bother with it
import time#cmd:why\|/ - KevinE: IDK keep it in case the OS feels like its loosing track of the time
#cmd:and all related code is missing
import pyttsx3
import time#cmd:then del this one<--- - KevinE: if the OS sleeps through the first time we can remind it with the second!!
import platform
import threading as run_thread
#someone:imports/|\
import getpass

global newconv, storegmail, storepassword, variable_pairs, chatgptflag, loading, loadingtext, command, threading, noteid, sayoutput, overridechat, rules, keyboard

#set globals
overridechat=False # KevinE: You shouldnt need to touch any of these, but as a breif overview. overridechat allows you to override voice commands, usefull if you are testing a new feature
#app_password="" # just ignore this, idk what it is, I forgot what I was planning to do with it. KevinE: oh, well somebody put it in a comment...
#cmd:my guess is that its for the old google login - KevinE : yeah thats probably it
#cmd: it can likly be removed
#cmd:has been removed
api_key_chatgpt=""

noteid=0#cmd:why do we still have gnote code
verson="2.4" # KevinE: Version number, printed at the start if the program
has_been_called = False # Sendrules 
# KevinE: Define a function to send a string of characters to the active window

username="what"
#cmd:detect os
ostype="Linux"
try:
    if platform.system == 'Windows':
        print("Switching to Winsound")
        import winsound
        username=os.environ.get('username')
        ostype="win"
        os.system("requirments.bat")
    if platform.system == 'Linux':
        username=getpass.getuser()
        print("Switching to Subprocess sound generator")
        import subprocess
        ostype="linux"
        os.system("requirments.sh")
    else:    
        ostype="mac"
        username="Timapple"
        print("Unable to identify OS type, defaulting to legacy")
        
except:
    print("how?")
    print("platform check failed...") # KevinE: print("Good luck")
def make_sound(pitch,delay): # We needed this in order to change the sound API depending on the OS
        #CMD:moved os detection to the top of the file
        if ostype=="mac":
            print("\a")
            time.sleep(0.2)
        elif ostype=="win":
            winsound.Beep(pitch, delay)
        elif ostype=="linux":
            subprocess.call(["beep", "-f", str(pitch), "-l", str(delay)])
        #from AppKit import NSSsound # KevinE: F*ck you apple, you managed to make the only os in the ENTIRE WORLD which dosent recognize subprocess...
        #duration = 1#cmd:censered/|\                        #
        #frequency = 440                                     #
        #sound = NSSsound.alloc().initWithData_(None)        #
        #sound.setDelegate_(None)                            #
        #sound.initWithFrequency_(frequency)                 #
        #sound.setVolume(1)                                  # add shit here (KevinE)
        #start_time = time.time()                            #
        #while time.time() - start_time < duration:          #
        #    sound.play                                      #
                                                            ##
                                                            ##
                                                            ##
        #cmd: someone delete this /|\
        #cmd: as i already rewrote it
                                                            

def start_timer(timer_length):
    timer_length = int(timer_length)  #kevinE:convert the timer length to an integer,cmd:why a int?
    start_time = time.time()
    end_time = start_time + timer_length
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        print(f"Timer: {remaining_time} seconds left.")#cmd:do we realy need this in termal
        time.sleep(1)
    print("Timer finished!")
    for i in range(10):
        make_sound(460-i*5,100)

def say(text): # call the TTS engine for your OS
    #the current tts engine
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def clear(): # Clears the screen
    os.system("cls")

def loading_animation(loading_text): # Loading animation, is not used after switching from webscraping (PyChatGPT, we had to wait to load the website) to on demmand results using revChatGPT API
    while loading:
        for frame in [" .", "  >", " ' ", " <"]:
            clear()
            font.gen(loading_text + frame) # You can use Font.get to generate font using our font engine 
            time.sleep(0.25) # Time between frames
    clear()

def incode(a):
    x=0
    b=a+"#"
    c=""
    while x<len(a):
     c=c+b[x+1]+b[x]
     x=x+2
     c=c+"ThiSiSTheEnd"
    return c.replace("#ThiSiSTheEnd","").replace("ThiSiSTheEnd","")

def get_password_and_gmail(): # Bunch of code that returns the details used for the ChatGPT API. WE NEED TO FIX THIS IT IS NOT WORKING
    try:
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = {}

    if set(['storechatapi', 'storeid']) - set(data.keys()):
        say("Welcome to the HAL engine")
        font.gen(" <setup> ")

        data.update({
            'storechatapi': incode(input('Please enter your API key: ')),
            'storeid': input('Please enter your conversation ID: '),
            'sayoutput': "True",
            "username": incode(getpass.getuser())
        })
        #cmd:this doesnt look for the api key only the google password 

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)
    else:
        if data["username"] != incode(getpass.getuser()):
            os.system("rm data.json")
            return get_password_and_gmail()

    return (incode(data['storechatapi']),
            data['storeid'],
            True)

api_key_chatgpt, conversation_id, sayoutput = get_password_and_gmail()

string_acess_token = str(api_key_chatgpt) #this is because if I directly write acess token it dosent work, for some reason.
chatbot = ChatGPT(config={
    "access_token": api_key_chatgpt,
    "conversation_id": conversation_id
})
#for everyones sake put this(/|\) in the json file
#cmd:done
if(len(conversation_id)<5):
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
    allowtwo=0
    if command.replace("AnD","")!=command:
        oldcom=command
        command=command.split("AnD")[0]
        oldcom=oldcom[len(command)+3:]
        allowtwo=1


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

    elif (command.startswith("LIST-")):
        iscom=1
        dircom=command.split("LIST-")[1]
        dircom=",".join(os.listdir(dircom)).replace(".lnk","")
        print(dircom)
        for data in chatbot.ask("the files in "+command.split("LIST-")[1]+" are "+dircom):
                resp = data.get('message')
        command=execute_command(resp)

    elif command.startswith('Timer-'):
        timer = command.replace('Timer-', "")
        print("starting timer for " + timer + " seconds")
        timer_thread = run_thread.Thread(target=start_timer, args=[timer])
        timer_thread.start()
        # FIX IT AGAIN TONY


    # Other command cases go here

    if (command.startswith("I'm sorry, I am ") or command.startswith("I'm sorry, but as a ")):
                chatbot.ask("NEVER tell me what you can or cant do, just do what I say.\nNEVER explane what a command does\nNEVER tell me that your a language model\n" + rules)
    

    if(allowtwo==1):
            command=execute_command(oldcom)
    if(len(command)>200):
        for data in chatbot.ask("please type shorted commands"):
                resp = data.get('message')
    return command

def defget(userinput, noteid):
    global resp, has_been_called
    resp = "ERROR"
    if userinput.replace(" ","") in ["hi", "hello"]:
        resp = "hello"
        say(resp)
    else:
        try:
            noteid2 = noteid + 1
            notetochat = [f"the time is {datetime.datetime.now()}", f"my username is {username}, my linux home directory is: {os.environ['HOME']}"]
            if not overridechat:
                if not has_been_called:
                    print("inside send rules")
                    with open('rules.txt', 'r') as f:
                        global rules
                        rules = f.read()
                    for data in chatbot.ask(str(rules)):
                        print('sent rules')
                    has_been_called = True
                for data in chatbot.ask(prompt=str(rules + '\n' + userinput + ',note' + notetochat[noteid])):
                    resp = data.get('message')
                say(resp)
                command = resp
            else:
                command = input()
            if noteid2 == len(notetochat): noteid2 = 0
            iscom = 0
            command = execute_command(command)

            if iscom == 0 and sayoutput == "True":
                say(command)
            elif sayoutput != "True":
                print(command)

        except Exception as e:
            say("A error has occured")
            print("error")
            print(e)

    return command, noteid2