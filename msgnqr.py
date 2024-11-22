import mouse
import pyautogui
import pyperclip
import time
from module1.textclip import clipcopy as clipcopy
x, y = pyautogui.locateCenterOnScreen ("C:\Users\mukun\OneDrive\Desktop\msg\chrome.png")
mouse.move(x, y, duration = 0.3)
mouse.click('left')
# chrome location
mouse.move(643, 1066, duration = 0.3)
mouse.click('left')
# whatsapp location
mouse.move(517, 1066, duration = 0.3)
mouse.click('left')
# chrome location
mouse.move(643, 1066, duration = 0.3)
mouse.click('left')
# no. of customer
mouse.move(113, 850, duration = 0.6)
mouse.click('left')
for y in range(2):
    ad = clipcopy()
    time.sleep(0.2)

mouse.move(113, 850, duration = 0.3)
print (ad)
for x in range(int(ad)):
    print (x)
    # right arrow location  
    mouse.move(713, 727, duration = 0.3)
    mouse.click('left')
    # whatsapp location
    mouse.move(517, 1066, duration = 0.4)
    pyautogui.hotkey("alt","tab")
    # search bar location
    mouse.move(167, 125, duration = 0.2)
    mouse.move(167, 125, duration = 0.3)
    mouse.click('left')
    mouse.move(167, 125, duration = 0.1)
    mouse.click('left')
    mouse.move(167, 125, duration = 0.5)
    pyautogui.hotkey("ctrl","a")
    mouse.move(167, 125, duration = 0.1)
    pyautogui.hotkey("backspace")
    mouse.move(167, 125, duration = 0.2)
    pyautogui.hotkey("ctrl","v")
    
    # customer
    mouse.move(201, 205, duration = 0.2)
    mouse.move(201, 205, duration = 2.6)
    mouse.click('left')
    mouse.click('left')

# --------image copy new------------------------

    # mouse.move(500, 1012, duration = 0.1)
    # mouse.move(500, 1012, duration = 0.8)
    # mouse.click('left')
    # mouse.move(500, 813, duration = 0.8)
    # # mouse.move(500, 813, duration = 0.8)
    # # mouse.move(500, 781, duration = 0.8)
    # mouse.click('left')
    # mouse.click('left')
    # mouse.move(500, 813, duration = 1.4)
    # pyautogui.typewrite("bob")
    # mouse.move(500, 813, duration = 0.2)
    # pyautogui.hotkey("down")
    # mouse.move(500, 813, duration = 0.2)
    # pyautogui.hotkey("Enter")





    
# --------image copy old------------------------
    # # desktop offer
    # mouse.move(1919, 1079, duration = 0.2)
    # mouse.click('left')
    # mouse.move(1870, 940, duration = 0.5)
    # mouse.click('left')
    # mouse.move(1870, 940, duration = 0.3)
    # pyautogui.hotkey("ctrl","c")
    # # whatsapp location
    # mouse.move(510, 1066, duration = 0.1)
    # mouse.click('left')

    # # text 
    # mouse.move(740, 1000, duration = 0.5)
    # mouse.click('left')
    # mouse.move(740, 1000, duration = 0.3)
    # pyautogui.hotkey("ctrl","v")
    # mouse.move(740, 1000, duration = 1.0)

# ----------------------------------------------

    # chrome location
    mouse.move(650, 1066, duration = 0.4)
    pyautogui.hotkey("alt","tab")
    # copy location
    mouse.move(772, 795, duration = 0.1)
    mouse.move(772, 795, duration = 0.4)
    mouse.click('left')
    # whatsapp location
    mouse.move(510, 1066, duration = 0.2)    
    pyautogui.hotkey("alt","tab")
    # mouse.move(510, 1066, duration = 0.2)
    # mouse.click('left')
    # media text 
    
    mouse.move(563, 935, duration = 0.7)
    mouse.click('left')
    mouse.move(740, 1000, duration = 0.5)
    pyautogui.hotkey("ctrl","v")
    mouse.move(740, 1000, duration = 0.6)

    pyautogui.hotkey("Enter")
    mouse.move(740, 1000, duration = 0.3)
    # chrome location
    mouse.move(643, 1066, duration = 0.3)
    pyautogui.hotkey("alt","tab")
    


# pyautogui.hotkey("Enter")
# # right arrow location
# mouse.move(713, 727)
# mouse.click('left')
# # search bar location
# mouse.move(167, 125)
# mouse.click('left')
# # right arrow location
# mouse.move(713, 727)
# mouse.click('left')
# # whatsapp location
# mouse.move(552, 1066)
# # chrome location
# mouse.move(514, 1066)
# # copy location
# mouse.move(772, 795)
# mouse.click('left')