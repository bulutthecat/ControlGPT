from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

# Define a function to send a string of characters to the active window
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

# Example usage
search_string = "BeamNG"
windows_search(search_string)
