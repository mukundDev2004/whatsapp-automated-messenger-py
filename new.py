    

import mouse
import pyautogui
import time

def func():
    mouse.move(643, 1066, duration = 0.3)
    pyautogui.hotkey("alt","tab")

    mouse.move(563, 935, duration = 0.7)
    mouse.click('left')
    time.sleep(0.2)
    pyautogui.hotkey("down")
    time.sleep(0.2)
    pyautogui.press("space")
func()