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
    },
    'Outlook': {
        'button1': 'ctrl+shift+m',
        'button2': 'ctrl+enter',
        'button3': 'ctrl+r',
        'knob_press': 'ctrl+shift+k',
        'knob_cw': 'ctrl+]',
        'knob_ccw': 'ctrl+['
    },
    'OneNote': {
        'button1': 'ctrl+n',
        'button2': 'ctrl+s',
        'button3': 'ctrl+p',
        'knob_press': 'ctrl+z',
        'knob_cw': 'ctrl+]',
        'knob_ccw': 'ctrl+['
    },
    'Microsoft Teams': {
        'button1': 'ctrl+shift+m',
        'button2': 'ctrl+shift+o',
        'button3': 'ctrl+shift+k',
        'knob_press': 'ctrl+e',
        'knob_cw': 'ctrl+tab',
        'knob_ccw': 'ctrl+shift+tab'
    },
    'Skype': {
        'button1': 'ctrl+n',
        'button2': 'ctrl+s',
        'button3': 'ctrl+p',
        'knob_press': 'ctrl+z',
        'knob_cw': 'ctrl+]',
        'knob_ccw': 'ctrl+['
    },
    'GIMP': {
        'button1': 'ctrl+n',
        'button2': 'ctrl+s',
        'button3': 'ctrl+shift+s',
        'knob_press': 'ctrl+z',
        'knob_cw': 'ctrl+]',
        'knob_ccw': 'ctrl+['
    },
    'VLC Media Player': {
        'button1': 'space',
        'button2': 'f',
        'button3': 'ctrl+up',
        'knob_press': 'm',
        'knob_cw': 'ctrl+right',
        'knob_ccw': 'ctrl+left'
    },
    'iTunes': {
        'button1': 'ctrl+alt+left',
        'button2': 'ctrl+alt+space',
        'button3': 'ctrl+alt+right',
        'knob_press': 'ctrl+alt+m',
        'knob_cw': 'ctrl+alt+up',
        'knob_ccw': 'ctrl+alt+down'
    },
    'Thunderbird': {
        'button1': 'ctrl+n',
        'button2': 'ctrl+s',
        'button3': 'ctrl+p',
        'knob_press': 'ctrl+z',
        'knob_cw': 'ctrl+]',
        'knob_ccw': 'ctrl+['
    },
    'Firefox': {
        'button1': 'ctrl+t',
        'button2': 'ctrl+r',
        'button3': 'ctrl+w',
        'knob_press': 'ctrl+shift+p',
        'knob_cw': 'ctrl+tab',
        'knob_ccw': 'ctrl+shift+tab'
    },
    'Opera': {
        'button1': 'ctrl+t',
        'button2': 'ctrl+r',
        'button3': 'ctrl+w',
        'knob_press': 'ctrl+shift+n',
        'knob_cw': 'ctrl+tab',
        'knob_ccw': 'ctrl+shift+tab'
    },
    'Safari': {
        'button1': 'cmd+t',
        'button2': 'cmd+r',
        'button3': 'cmd+w',
        'knob_press': 'cmd+shift+n',
        'knob_cw': 'cmd+tab',
        'knob_ccw': 'cmd+shift+tab'
    },
    'Evernote': {
        'button1': 'ctrl+n',
        'button2': 'ctrl+s',
        'button3': 'ctrl+p',
        'knob_press': 'ctrl+z',
        'knob_cw': 'ctrl+]',
        'knob_ccw': 'ctrl+['
    },
    'Trello': {
        'button1': 'b',
        'button2': 'c',
        'button3': 'd',
        'knob_press': 'e',
        'knob_cw': 'f',
        'knob_ccw': 'g'
    },
    'Asana': {
        'button1': 'tab+q',
        'button2': 'tab+w',
        'button3': 'tab+e',
        'knob_press': 'tab+r',
        'knob_cw': 'tab+t',
        'knob_ccw': 'tab+y'
    },
    'Jira': {
        'button1': 'j',
        'button2': 'k',
        'button3': 'l',
        'knob_press': 'm',
        'knob_cw': 'n',
        'knob_ccw': 'o'
    },
    'GitHub Desktop': {
        'button1': 'ctrl+shift+a',
        'button2': 'ctrl+shift+c',
        'button3': 'ctrl+shift+d',
        'knob_press': 'ctrl+shift+e',
        'knob_cw': 'ctrl+shift+f',
        'knob_ccw': 'ctrl+shift+g'
    },
    'Discord': {
        'button1': 'ctrl+shift+u',
        'button2': 'ctrl+shift+i',
        'button3': 'ctrl+shift+o',
        'knob_press': 'ctrl+shift+p',
        'knob_cw': 'ctrl+shift+[',
        'knob_ccw': 'ctrl+shift+]'
    },
    'WhatsApp': {
        'button1': 'ctrl+shift+n',
        'button2': 'ctrl+shift+m',
        'button3': 'ctrl+shift+,',
        'knob_press': 'ctrl+shift+.',
        'knob_cw': 'ctrl+shift+/',
        'knob_ccw': 'ctrl+shift+\\'
    },
    'Telegram': {
        'button1': 'ctrl+shift+1',
        'button2': 'ctrl+shift+2',
        'button3': 'ctrl+shift+3',
        'knob_press': 'ctrl+shift+4',
        'knob_cw': 'ctrl+shift+5',
        'knob_ccw': 'ctrl+shift+6'
    },
    'Signal': {
        'button1': 'ctrl+shift+7',
        'button2': 'ctrl+shift+8',
        'button3': 'ctrl+shift+9',
        'knob_press': 'ctrl+shift+0',
        'knob_cw': 'ctrl+shift+-',
        'knob_ccw': 'ctrl+shift+='
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
