# TalkGPT - An AI Voice Assistant

TalkGPT is an advanced AI voice assistant built on ChatGPT. It enables users to interact with their devices through voice commands. With TalkGPT, you can open web pages, execute commands, run python scripts, and even control household appliances with just your voice.

# Capabilities

TalkGPT provides access to the following functions:

   1. Chat with ChatGPT using speech recognition and Microsoft Bob
   2. Open web pages with simple queries such as, "Hey Hal, open a video streaming website."
   3. Create, edit, and manage files and system applications through voice commands such as, "Hey Hal, create a text file on my desktop."
   4. Run ChatGPT generated one-liner python scripts such as easy as, "Hey Hal, make a sound out of my speakers using python."
   5. Search for system-wide applications and files using your voice, "Hey Hal, search locally for Firefox."
   6. Send emails through Gmail with a command like, "Hey Hal, send an email to dev@gmail.com with the text 'Hi, how are you.'"
   7. Control household appliances like smart plugs and bulbs.

# How it works

TalkGPT uses the unofficial python wrapper for ChatGPT and logs in using your Gmail account on startup. When you make a voice request, TalkGPT sends the text after the catchphrase to the ChatGPT engine. The engine is preconfigured to respond to your request based on the ruleset outlined in the quick start guide.

The response from ChatGPT is then checked for the necessary parameters to execute the command. If the response includes "Mail-," for example, the mail function is executed, and the details about the recipient and the message are obtained from the rest of the response.

The entire program relies on ChatGPT, which can be advantageous. If you provide a vague argument, ChatGPT will do its best to understand what you mean and deliver a good result. For instance, if you say "search the system for a web browser," it might output "SEARCH-Chrome," which would find and launch Chrome, even if you didn't mention the specific name of the browser.

Some things to note:
1. ChatGPT will remember what you said if you specified a conversation ID, even after a full restart; meaning that if you have a preferance it will remember it.
2. ChatGPT has acess to local Command line, meaning it can cause damage if you are not carefull, although if you tell it to do something like delete system32 it will tell you that that is a bad idea, and not execute the command.
3. Only works on windows, unless somebody else wants to port it to linux (Wine is not tested and will not be supported officually in the near future)

# Quick Start Guide
You can find the guide in the Wiki section above.
Or here:
[https://github.com/bulutthecat/TalkGPT/wiki](https://github.com/bulutthecat/TalkGPT/wiki/Basic-Usage---Quick-Start)
