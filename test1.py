import mouse
import pyautogui
import pyperclip
import time

screen_width, screen_height = pyautogui.size()
taskbar_height = 40  # Adjust this based on your taskbar size
taskbar_region = (0, screen_height - taskbar_height, screen_width, taskbar_height)

# Locate the center of an image in the taskbar region
image_path = "chrome2.png"
center = pyautogui.locateCenterOnScreen(image_path, region=taskbar_region, confidence=0.8)


if center:
    print(f"Found at: {center}")
    pyautogui.click(center)
else:
    print("Image not found in the selected area. Taking alternative action...")
    # Example alternative action: moving mouse to a default position
    pyautogui.moveTo(screen_width // 2, screen_height // 2)

# chrome_x, chrome_y = pyautogui.locateCenterOnScreen ("chrome1.png", confidence = 0.8)
# mouse.move(chrome_x, chrome_y, duration = 0.3)
# mouse.click('left')

whatsapp= pyautogui.locateCenterOnScreen ("whatsapp.png", confidence = 0.8)
mouse.move(whatsapp.x, whatsapp.y, duration = 0.3)
mouse.click('left')
