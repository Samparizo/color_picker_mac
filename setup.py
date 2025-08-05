
from setuptools import setup

APP = ['color_picker.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'includes': ['PyQt6', 'mss', 'PIL.Image', 'pyperclip'],
    'packages': ['PyQt6', 'mss', 'Pillow', 'pyperclip'],
    'excludes': ['tkinter', 'zmq'],
    'optimize': 1,
    'plist': {
        'CFBundleName': 'ColorPickerBubble',
        'CFBundleDisplayName': 'Color Picker Bubble',
        'CFBundleIdentifier': 'com.samparizo.colorpicker',
        'CFBundleVersion': '0.1.0',
        'CFBundleShortVersionString': '0.1.0',
    }
}

setup(
    app=APP,
    name='ColorPickerBubble',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
