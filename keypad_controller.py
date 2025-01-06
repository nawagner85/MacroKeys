import keyboard
import pygetwindow as gw
import pyautogui
from time import sleep

# Define key mappings for different applications
key_mappings = {
    'Spyder': {
        'button1': 'control+.',
        'button2': 'f5',
        'button3': 'control+s',
        'knob_press': 'control+1',
        'knob_cw': 'down',
        'knob_ccw': 'up'
    },
    # Add more applications and their key mappings here
}

def get_active_window():
    """Get the title of the currently active window."""
    window = gw.getActiveWindow()
    print(f"Window: {window.title}")
    return window.title if window else None

def send_key_combination(key_combination):
    """Send a key combination using the keyboard library."""
    pyautogui.hotkey(*key_combination.split('+'))

def handle_keypress(key):
    """Handle keypress events and send the appropriate key combination."""
    # keycode_checker()
    print(f"Key pressed: {key}")
    active_window = get_active_window()
    for app_name, mappings in key_mappings.items():
        if app_name.lower() in active_window.lower():
            if key in mappings:
                send_key_combination(mappings[key])
                break

# Set up key listeners
keyboard.add_hotkey("shift+win+j", lambda: (print("Lambda for button1 executed"), handle_keypress('button1')), suppress=True, trigger_on_release=True)
keyboard.add_hotkey("shift+win+q", lambda: (print("Lambda for button2 executed"), handle_keypress('button2')), suppress=True, trigger_on_release=True)
keyboard.add_hotkey("shift+win+y", lambda: (print("Lambda for button3 executed"), handle_keypress('button3')), suppress=True, trigger_on_release=True)
keyboard.add_hotkey("shift+win+w", lambda: (print("Lambda for knob_press executed"), handle_keypress('knob_press')), suppress=True, trigger_on_release=True)
keyboard.add_hotkey("shift+win+k", lambda: (print("Lambda for knob_cw executed"), handle_keypress('knob_cw')), suppress=True, trigger_on_release=True)
keyboard.add_hotkey("shift+win+h", lambda: (print("Lambda for knob_ccw executed"), handle_keypress('knob_ccw')), suppress=True, trigger_on_release=True)

# Keep the script running
keyboard.wait()
