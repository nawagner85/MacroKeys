import keyboard
import pygetwindow as gw

# Define key mappings for different applications
key_mappings = {
    'Spyder': {
        'button1': 'win+shift+j',
        'button2': 'f5',
        'button3': 'ctrl+s',
        'knob_press': 'ctrl+1',
        'knob_cw': 'down',
        'knob_ccw': 'up'
    },
    # Add more applications and their key mappings here
}

def get_active_window():
    """Get the title of the currently active window."""
    window = gw.getActiveWindow()
    return window.title if window else None

def send_key_combination(key_combination):
    """Send a key combination using the keyboard library."""
    keyboard.send(key_combination)

def handle_keypress(key):
    """Handle keypress events and send the appropriate key combination."""
    print(f"Key pressed: {key}")
    active_window = get_active_window()
    for app_name, mappings in key_mappings.items():
        if app_name in active_window:
            if key in mappings:
                send_key_combination(mappings[key])
                break

# Set up key listeners
keyboard.add_hotkey('f1', lambda: (print("Lambda for button1 executed"), handle_keypress('button1')))
keyboard.add_hotkey('f2', lambda: (print("Lambda for button2 executed"), handle_keypress('button2')))
keyboard.add_hotkey('f3', lambda: (print("Lambda for button3 executed"), handle_keypress('button3')))
keyboard.add_hotkey('space', lambda: (print("Lambda for knob_press executed"), handle_keypress('knob_press')))
keyboard.add_hotkey('right', lambda: (print("Lambda for knob_cw executed"), handle_keypress('knob_cw')))
keyboard.add_hotkey('left', lambda: (print("Lambda for knob_ccw executed"), handle_keypress('knob_ccw')))

# Keep the script running
keyboard.wait()
