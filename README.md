# TalkGPT - An AI Voice Assistant

TalkGPT is an advanced AI voice assistant built on ChatGPT. It enables users to interact with their devices through voice commands. With TalkGPT, you can open web pages, execute commands, run python scripts, and even control household appliances with just your voice.

# Capabilities

TalkGPT provides access to the following functions:

   1. Chat with ChatGPT using speech recognition and Microsoft Bob
   2. Open web pages with simple queries such as, "Hey Hal, open a video streaming website."
   3. Create, edit, and manage files and system applications through voice commands such as, "Hey Hal, create a text file on my desktop."
   4. Run ChatGPT generated one-liner python scripts such as, "Hey Hal, make a sound out of my speakers using python."
   5. Search for system-wide applications and files using your voice, "Hey Hal, search locally for Firefox."
   6. Send emails through Gmail with a command like, "Hey Hal, send an email to dev@gmail.com with the text 'Hi, how are you.'"
   7. Control household appliances like smart plugs and bulbs.

# How it works

TalkGPT uses the unofficial python wrapper for ChatGPT and logs in using your Gmail account on startup. When you make a voice request, TalkGPT sends the text after the catchphrase to the ChatGPT engine. The engine is preconfigured to respond to your request based on the ruleset outlined in the quick start guide.

The response from ChatGPT is then checked for the necessary parameters to execute the command. If the response includes "Mail-," for example, the mail function is executed, and the details about the recipient and the message are obtained from the rest of the response.

The entire program relies on ChatGPT, which can be advantageous. If you provide a vague argument, ChatGPT will do its best to understand what you mean and deliver a good result. For instance, if you say "search the system for a web browser," it might output "SEARCH-Chrome," which would find and launch Chrome, even if you didn't mention the specific name of the browser.

# Quick Start Guide
