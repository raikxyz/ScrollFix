import keyboard
import pyautogui

def checkScrollUp(key):
    if key.name == '[':
        pyautogui.scroll(100)

def checkScrollDown(key):
    if key.name == ']':
        pyautogui.scroll(-100)

keyboard.hook(checkScrollUp)
keyboard.hook(checkScrollDown)

keyboard.wait()