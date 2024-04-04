import keyboard
import pyautogui


def check_scroll_up(key):
    if key.name == '[':
        pyautogui.scroll(100)


def check_scroll_down(key):
    if key.name == ']':
        pyautogui.scroll(-100)


keyboard.hook(check_scroll_up)
keyboard.hook(check_scroll_down)
keyboard.wait()
