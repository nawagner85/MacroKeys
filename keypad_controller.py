from time import sleep
import keyboard
import pygetwindow as gw

# Define key mappings for different applications
key_mappings = {
    'Spyder': {
        'button1': 'ctrl+.',
        'button2': 'f5',
        'button3': 'ctrl+s',
        'knob_press': 'ctrl+1',
        'knob_cw': 'down',
        'knob_ccw': 'up'
    },
    'Chrome': {
        'button1': 'alt+left',
        'button2': 'f5',
        'button3': 'alt+right',
        'knob_press': 'end',
        'knob_cw': 'page down',
        'knob_ccw': 'page up'
    },
    # Add more applications and their key mappings here
}

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
                break

# Set up key listeners
keyboard.add_hotkey("ctrl+alt+f5", lambda: (handle_keypress('button1')), suppress=True, )
keyboard.add_hotkey("ctrl+alt+f6", lambda: (handle_keypress('button2')), suppress=True)
keyboard.add_hotkey("ctrl+alt+f7", lambda: (handle_keypress('button3')), suppress=True)
keyboard.add_hotkey("ctrl+alt+f8", lambda: (handle_keypress('knob_ccw')), suppress=True)
keyboard.add_hotkey("ctrl+alt+f9", lambda: (handle_keypress('knob_press')), suppress=True)
keyboard.add_hotkey("ctrl+alt+f3", lambda: (handle_keypress('knob_cw')), suppress=True)

# Keep Hthe script running
keyboard.wait()
