#!/bin/bash

# Define the checkandfix function
checkandfix() {
    file="$1"
    isfound=0
    if test -e "$file"; then
        isfound=1
    fi
    if [ $isfound -eq 0 ]; then
        echo "${file} is not found"
    fi
    if [ $isfound -eq 0 ]; then
        if test -e "${file}.bak"; then
            mv "${file}.bak" "$file"
        fi
    fi
}

# Prompt the user to check for missing addons
echo "Check addons?"
echo "Check for missing Python addons (SpeechRecognition, pyaudio, pyautogui, revChatGPT) y/n"

# Input validation for the addons check
while true; do
    read -r varname
    if [ "$varname" == "y" ] || [ "$varname" == "n" ]; then
        break
    else
        echo "Invalid input. Please enter y or n."
    fi
done

if [ "$varname" == "y" ]; then
    # Install the required Python addons
    pip install SpeechRecognition pyaudio pyautogui revChatGPT SpeechRecognition
    sudo apt install espeak
fi

# Prompt the user to check for missing core files
echo "Checking for missing core files"
echo "Check for missing core files (font.py, data.json, build.bat, HALTEST.py, HAL9000inputoutput.py) y/n "

# Input validation for the core files check
while true; do
    read -r varname
    if [ "$varname" == "y" ] || [ "$varname" == "n" ]; then
        break
    else
        echo "Invalid input. Please enter y or n."
    fi
done

if [ "$varname" == "y" ]; then
    # Check and fix the core files
    checkandfix "font.py"
    checkandfix "data.json"
    checkandfix "build.bat"
    checkandfix "HALTEST.py"
    checkandfix "HAL9000inputoutput.py"
fi
