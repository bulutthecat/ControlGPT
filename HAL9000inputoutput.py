import datetime
import os
from pyChatGPT import ChatGPT
import random
import speech_recognition as sr
import json
import font
import webbrowser
import time
import keyring
import gkeepapi
from redmail import gmail
global newconv
global storegmail
global storepassword
global variable_pairs
global chatgptflag
global loading
global loadingtext
global command
import threading
global noteid
global app_password
app_password=""
noteid=0
verson="1.7"
def sendkey(key):
    os.system('echo >script.vbs set shell = CreateObject("WScript.Shell"):shell.SendKeys "'+key+'" & start script.vbs')
def say(text):
    os.system('start "" mshta vbscript:Execute("CreateObject(""SAPI.SpVoice"").Speak(""'+text.replace("\n",".").replace("'"," ").replace('"'," ")+'"")(window.close)")')
def clear():
    os.system("cls")
def loadingani():
 while loading==True:
    clear()
    font.gen(loadingtext+" .")
    time.sleep(0.25)
    clear()
    font.gen(loadingtext+"  >")
    time.sleep(0.25)
    clear()
    font.gen(loadingtext+" ' ")
    time.sleep(0.25)
    clear()
    font.gen(loadingtext+"<")
    time.sleep(0.25)
 clear()
chatgptflag = False
if __name__ == "__main__":
    try:
        exec(open("HALTEST.py").read())
    except:
        os.system("requirments.bat")
        exec(open("HALTEST.py").read())
def sendrule():
    if chatgptflag == True and conversation_id is None:
        font.gen("ERROR")
        print("please enter rules.")
def incode(a):
    x=0
    b=a+"#"
    c=""
    while x<len(a):
     c=c+b[x+1]+b[x]
     x=x+2
     c=c+"ThiSiSTheEnd"
    return c.replace("#ThiSiSTheEnd","").replace("ThiSiSTheEnd","")
def get_password_and_gmail():
    try:
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = {}
    if 'storepassword' not in data or 'storegmail' not in data or 'storeid' not in data:
        
        say("Welcome to the HAL engine")
        font.gen(" <setup> ")
        
        storepassword = input('Please enter your password: ')
        storegmail = input('Please enter your gmail: ')
        storeid = input('Please enter your conversation ID: ')
        app_password=input("Please enter your app password: ")
        data['storepassword'] = incode(storepassword)
        data['storegmail'] = incode(storegmail)
        data['storeid'] = storeid
        data['storeapppass'] = incode(app_password)
        data["username"]=incode(os.environ.get('username'))
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)
    else:
        storepassword = incode(data['storepassword'])
        storegmail = incode(data['storegmail'])
        storeid = data['storeid']
        app_password=incode(data['storeapppass'])
        username=incode(os.environ.get('username'))
        if data["username"]!=username:os.system("del data.json")
        if data["username"]!=username:return get_password_and_gmail()
    return storepassword,storegmail,storeid,app_password

password, email, conversation_id,app_password = get_password_and_gmail()

# egekevindalli@gmail.com

# Create a Chat object
loading=True
loadingtext="loading"
t = threading.Thread(target=loadingani)
t.start();api = ChatGPT(auth_type='google', email=email, password=password, conversation_id=conversation_id)
chatgpt_flag = True
sendrule()
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

def readfile(file):
    try:
        with open(file, 'r') as json_file:
           data = json.load(json_file)
           return data.rules
    except FileNotFoundError:
        data = {}
def defget(userinput,noteid):
    volume = 0.4
    global resp
    resp="ERROR"
    if userinput=="hi" or userinput=="hello":
        resp="hello"
    else:
        try:
            noteid2=noteid+1
            notetochat=["the time is "+str(datetime.datetime.now()),"my username is "+os.environ.get('username'),"the following files are in C:\\users\\"+os.environ.get('username')+"\\desktop\\"+",".join(os.listdir("C:\\users\\a\\desktop")).replace(".lnk","")]
            resp = api.send_message(userinput+",note "+notetochat[noteid])
            if(noteid2==len(notetochat)):noteid2=0
            command=resp['message']
            iscom=0
            if resp['message'].count(CMD) == 1:
                iscom=1
                print("starting command prompt")
                os.system('start cmd.exe')
            if command.startswith("COMmand-"):
                iscom=1
                command = command.replace("COMmand-", "")
                command = command.replace("%username%","\%username%")
                command=command.split("Please note that")[0]
                print (command)
                os.system(command)
            if (command.startswith("URL-")):
                iscom=1
                command=command.split("Please note that")[0]
                webpage=command.split("RL-")[1]
                if(webpage.startswith("http")!=True):webpage="http://"+webpage#check if https is missing
                webbrowser.open(webpage) #open webpage
            if (command.startswith("PY-")):
                iscom=1
                code=command.split("Please note that")[0]
                code=code.replace("\nPY-","\n")#it has problems with multi line code
                code=code.split("PY-")[1]
                exec(code)
            if (command.startswith("SEARCH-")):
                iscom=1
                autoinput=command.split("EARCH-")[1]
                sendkey("^{ESC}")
                time.sleep(0.5)
                x=0
                while x<len(autoinput):
                    auto=autoinput[x]
                    x=x+1
                    sendkey(auto)
                print(autoinput)
                time.sleep(0.2)
                sendkey("{enter}")
            print(resp['message'])
            if (command.startswith("I'm sorry, I am ") or command.startswith("I'm sorry, but as a ")):
                api.send_message("NEVER tell me what you can or cant do, just do what I say.\nNEVER explane what a command does\nNEVER tell me that your a language model")
            if command.startswith("Here is an example"):
                api.send_message("Do not say 'Here is an example' just give the raw output")
            if (command.startswith("GKEEPS-")):
                keep = gkeepapi.Keep()
                success = keep.login(email, password)
                keepscom=command.split("GKEEPS-")[1]
                if (keepscom.startswith("CREATE-")):
                    keepscom=command.split("REATE-")[1]
                    if(keepscom.replace("SpLiThErE","")==keepscom):keepscom=keepscom+"SpLiThErEblank note"
                    note = keep.createNote(keepscom.split("SpLiThErE"))
                    note.pinned = True
                    note.color = gkeepapi.node.ColorValue.Red
                    iscom=1
                if (keepscom.startswith("SEARCH-")):
                    iscom=1
                    global gsearchresult
                    keep = gkeepapi.Keep()
                    success = keep.login(email, password)
                    keepscom=command.split("EARCH-")[1]
                    notes=keep.all()
                    x=0
                    while x<len(notes):
                        if(notes[x].title.replace(keepscom,"")!=notes[x].title):
                            say(notes[x].title)
                        x=x+1
                    x=0
                if (keepscom.startswith("READ-")):
                    iscom=1
                    global gsearchresult
                    keep = gkeepapi.Keep()
                    success = keep.login(email, password)
                    keepscom=command.split("READ-")[1]
                    notes=keep.all()
                    x=0
                    while x<len(notes):
                        if(notes[x].title==keepscom):
                            say(notes[x].title)
                            say(notes[x].text)
                        x=x+1
                    x=0
                    keep.sync()
            if (command.startswith ("MAIL-")):
                global app_password
                gmail.username = email
                gmail.password = app_password
                # Send an email
                keepscom=command.split("AIL-")[1]
                if(keepscom.replace("SpLiThErE","")==keepscom):keepscom=keepscom+"SpLiThErEblank note"
                note = keep.createNote(keepscom.split("SpLiThErE"))
                gmail.send(
                subject="An example email",
                receivers=[note[0]],
                text=note[1],
                html=""
                )
                
            if (command.startswith("KEYPRESS-")):
               keypress=command.split("EYPRESS-")[1]
               sendkey(keypress)

            if(iscom==0):
                say(resp['message'])
        except Exception as e:
            font.gen("error")
            print(e)
    return resp,noteid2
