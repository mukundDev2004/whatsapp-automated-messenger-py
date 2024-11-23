import mouse
import pyautogui
import time
import pyperclip
import subprocess
import psutil
from module1.textclip import clipcopy as clipcopy
def is_process_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] and process_name.lower() in process.info['name'].lower():
            return True
    return False

def open_application_from_start_menu(app_name):
    """Open an application from the Start Menu."""
    print(f"Launching {app_name}...")
    pyautogui.press('win')  # Open the Start Menu
    time.sleep(1)  # Wait for the Start Menu to appear
    pyautogui.typewrite(app_name)  # Type the app name
    time.sleep(1)  # Wait for search results to appear
    pyautogui.press('enter')  # Press Enter to open the app
    time.sleep(3)  # Wait for the app to launch

# Ensure WhatsApp is running
if not is_process_running("WhatsApp.exe"):
    open_application_from_start_menu("WhatsApp")
else:
    print("WhatsApp is already running.")

# Ensure Chrome is running
if not is_process_running("chrome.exe"):
    open_application_from_start_menu("Google Chrome")
else:
    print("Chrome is already running.")

import pyautogui
import time

# Screen dimensions
screen_width, screen_height = pyautogui.size()
taskbar_height = 40  # Adjust based on your taskbar size
taskbar_region = (0, screen_height - taskbar_height, screen_width, taskbar_height)
wx, wy, cx, cy = 0, 0, 0, 0
# Dictionary to store found locations
img_lcsn = {}

def locate_and_click(img_path, confidence=0.8, region=None, fallback_position=None):
    """Locate an image on the screen and click its center if found.
    If not found, move to a fallback position or log the failure."""
    try:
        center = pyautogui.locateCenterOnScreen(img_path, region=region, confidence=confidence)
        if center:
            print(f"Image '{img_path}' found at: {center}")
            pyautogui.click(center)
            img_lcsn[img_path] = center  # Store location for later use
            return center  # Return the center coordinates
        else:
            raise pyautogui.ImageNotFoundException
    except pyautogui.ImageNotFoundException:
        print(f"Image '{img_path}' not found on the screen.")
        if fallback_position:
            print(f"Moving to fallback position: {fallback_position}")
            pyautogui.moveTo(*fallback_position)
        return None  # Return None if the image is not found

# Locate and click Chrome in the taskbar
crm = "chrome.png"
chrome_fallback = (screen_width // 2, screen_height // 2)  # Example fallback position
crm_lcsn = locate_and_click(crm, region=taskbar_region, fallback_position=chrome_fallback)

# Locate and click WhatsApp anywhere on the screen
wa_img = "whatsapp.png"
whatsapp_location = locate_and_click(wa_img, fallback_position=(screen_width // 2, screen_height // 2))

# Later in the program, use the stored locations
if crm in img_lcsn:
    cx, cy = img_lcsn[crm].x, img_lcsn[crm].y
    print(f"Chrome location saved: {img_lcsn[crm]}")
    mouse.move(cx,cy, duration = 0.6)
if wa_img in img_lcsn:
    wx, wy = img_lcsn[wa_img].x, img_lcsn[wa_img].y
    print(f"WhatsApp location saved: {img_lcsn[wa_img]}")
    mouse.move(wx,wy, duration = 0.6)

try:
    center = pyautogui.locateCenterOnScreen("whats-win.png", region=(0, 0, 460, 60), confidence=0.8)
    if center:
        print(f"'whats-win.png' found at: {center}")
        mouse.move(center.x, center.y, duration=0.6)
        mouse.click('left')  # Single click
    else:
        raise pyautogui.ImageNotFoundException  # Explicitly raise exception if not found
except (pyautogui.ImageNotFoundException, AttributeError):
    print("'whats-win.png' not found in the specified region. Searching the whole screen...")
    # Search for the image on the whole screen
    center = pyautogui.locateCenterOnScreen("whats-win.png", confidence=0.8)
    if center:
        print(f"'whats-win.png' found on the whole screen at: {center}")
        mouse.move(center.x, center.y, duration=0.6)
        mouse.double_click('left')  # Double click
    else:
        print("'whats-win.png' not found on the entire screen.")



mouse.move(cx,cy, duration = 0.6)
mouse.click('left')

def activate_chrome_and_find_tab(cx, cy, tab_title):
    """Move to Chrome, check for a tab with the given title, and perform an action if found."""
    # Step 1: Move to Chrome and click
    mouse.move(cx, cy, duration=0.6)
    mouse.click('left')
    time.sleep(1)  # Wait for Chrome to become active
    
    # Step 2: Check for a tab with the specified title
    try:
        tab_location = pyautogui.locateCenterOnScreen(f"{tab_title}.png", region=(0, 0, 1920, 60), confidence=0.8)
        if tab_location:
            print(f"Tab with title '{tab_title}' found at: {tab_location}")
            
            # Step 3: Move to the tab and click
            pyautogui.moveTo(tab_location.x, tab_location.y, duration=0.5)
            pyautogui.click()
            time.sleep(0.5)  # Wait for the tab to activate
            
            # Step 4: Press the Right Arrow key
            pyautogui.press('right')
            print(f"Switched to the tab '{tab_title}' and pressed the Right Arrow key.")
        else:
            print(f"Tab with title '{tab_title}' not found.")
    except pyautogui.ImageNotFoundException:
        print(f"Failed to locate the tab with title '{tab_title}'.")

# Example: Coordinates of Chrome
chrome_x, chrome_y = 200, 50  # Adjust these values based on Chrome's location
tab_title = "page title"  # Replace with your tab title

activate_chrome_and_find_tab(chrome_x, chrome_y, tab_title)
