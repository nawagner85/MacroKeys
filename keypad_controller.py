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
    'Spotify': {
        'button1': 'previous track',
        'button2': 'play/pause media',
        'button3': 'next track',
        'knob_press': 'volume mute',
        'knob_cw': 'volume up',
        'knob_ccw': 'volume down'
    },
    'Chrome': {
        'button1': 'alt+left',
        'button2': 'f5',
        'button3': 'alt+right',
        'knob_press': 'end',
        'knob_cw': 'page down',
        'knob_ccw': 'page up'
    },
    '': {
        'button1': 'win',
        'button2': 'win+r',
        'button3': 'win+d',
        'knob_press': 'win+tab',
        'knob_cw': 'alt+tab',
        'knob_ccw': 'shift+alt+tab'
    },
    'Visual Studio Code': {
        'button1': 'ctrl+shift+p',
        'button2': 'ctrl+b',
        'button3': 'ctrl+`',
        'knob_press': 'ctrl+shift+e',
        'knob_cw': 'ctrl+tab',
        'knob_ccw': 'ctrl+shift+tab'
    },
    'Microsoft Word': {
        'button1': 'ctrl+n',
        'button2': 'ctrl+s',
        'button3': 'ctrl+p',
        'knob_press': 'ctrl+z',
        'knob_cw': 'ctrl+]',
        'knob_ccw': 'ctrl+['
    },
    'Microsoft Excel': {
        'button1': 'ctrl+n',
        'button2': 'ctrl+s',
        'button3': 'ctrl+p',
        'knob_press': 'ctrl+z',
        'knob_cw': 'ctrl+]',
        'knob_ccw': 'ctrl+['
    },
    'Microsoft PowerPoint': {
        'button1': 'ctrl+n',
        'button2': 'ctrl+s',
        'button3': 'ctrl+p',
        'knob_press': 'ctrl+z',
        'knob_cw': 'ctrl+]',
        'knob_ccw': 'ctrl+['
    },
    'Slack': {
        'button1': 'ctrl+k',
        'button2': 'ctrl+t',
        'button3': 'ctrl+shift+\\',
        'knob_press': 'ctrl+shift+space',
        'knob_cw': 'ctrl+tab',
        'knob_ccw': 'ctrl+shift+tab'
    },
    'Zoom': {
        'button1': 'alt+a',
        'button2': 'alt+v',
        'button3': 'alt+s',
        'knob_press': 'alt+h',
        'knob_cw': 'alt+u',
        'knob_ccw': 'alt+i'
    },
    'Adobe Photoshop': {
        'button1': 'ctrl+n',
        'button2': 'ctrl+s',
        'button3': 'ctrl+shift+s',
        'knob_press': 'ctrl+z',
        'knob_cw': 'ctrl+]',
        'knob_ccw': 'ctrl+['
    },
    'Adobe Illustrator': {
        'button1': 'ctrl+n',
        'button2': 'ctrl+s',
        'button3': 'ctrl+shift+s',
        'knob_press': 'ctrl+z',
        'knob_cw': 'ctrl+]',
        'knob_ccw': 'ctrl+['
    },
    'Notepad++': {
        'button1': 'ctrl+n',
        'button2': 'ctrl+s',
        'button3': 'ctrl+p',
        'knob_press': 'ctrl+z',
        'knob_cw': 'ctrl+tab',
        'knob_ccw': 'ctrl+shift+tab'
    },
    'File Explorer': {
        'button1': 'ctrl+n',
        'button2': 'ctrl+w',
        'button3': 'ctrl+e',
        'knob_press': 'alt+up',
        'knob_cw': 'alt+right',
        'knob_ccw': 'alt+left'
    }
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
