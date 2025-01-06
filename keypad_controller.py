from time import sleep
import keyboard
import pygetwindow as gw
import yaml
from tkinter import Tk, Label, Entry, Button, Listbox, END, SINGLE

# Load key mappings from YAML file
def load_key_mappings():
    with open('key_mappings.yaml', 'r') as file:
        return yaml.safe_load(file)

key_mappings = load_key_mappings()

def get_active_window():
    """Get the title of the currenKtly active window."""
    window = gw.getActiveWindow()
    print(f"Window: {window.title}")
    return window.title if window else None

def send_key_combination(key_combination):
    """Send a key combination using the keyboard library."""
    sleep(0.1)
    keyboard.send(key_combination)

def handle_keypress(key):
    """Handle keypress events and send the appropriate key combination."""
    # keycode_checker()
    print(f"Key pressed: {key}")
    active_window = get_active_window()
    for app_name, mappings in key_mappings.items():
        if app_name.lower() in active_window.lower():
            if key in mappings:
                send_key_combination(mappings[key])
                return
    # Use default key mappings if no specific application is found
    default_mappings = key_mappings.get('', {})
    if key in default_mappings:
        send_key_combination(default_mappings[key])

# Set up key listeners
keyboard.add_hotkey("ctrl+alt+f5", lambda: (handle_keypress('button1')), suppress=True, )
keyboard.add_hotkey("ctrl+alt+f6", lambda: (handle_keypress('button2')), suppress=True)
keyboard.add_hotkey("ctrl+alt+f7", lambda: (handle_keypress('button3')), suppress=True)
keyboard.add_hotkey("ctrl+alt+f8", lambda: (handle_keypress('knob_ccw')), suppress=True)
keyboard.add_hotkey("ctrl+alt+f9", lambda: (handle_keypress('knob_press')), suppress=True)
keyboard.add_hotkey("ctrl+alt+f3", lambda: (handle_keypress('knob_cw')), suppress=True)

# Keep Hthe script running
keyboard.wait()
