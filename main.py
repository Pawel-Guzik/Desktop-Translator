import pyperclip
from deep_translator import GoogleTranslator
from pynput import keyboard
from gui import Gui

COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='X')}
]
COMBINATION = {keyboard.Key.shift, keyboard.KeyCode(char='X')}
current = set()


def execute():
    toTranslate = pyperclip.paste()
    translated = GoogleTranslator(source='auto', target='pl').translate(toTranslate)
    current.clear()
    translateGui = Gui(toTranslate, translated)
    translateGui.root.mainloop()


def on_press(key):
    if any([key in combo for combo in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()


def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        try:
            current.clear()
        except:
            pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
