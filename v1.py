import mouse
import pyautogui
import time
import pyperclip
import subprocess
import psutil
from module1.textclip import clipcopy as clipcopy
from pynput import keyboard

# Enable PyAutoGUI's built-in failsafe
pyautogui.FAILSAFE = True  # Moving the mouse to the top-left corner will stop the script

# Variable to control script execution
script_running = True

def on_press(key):
    """Stop the script when the Esc key is pressed."""
    global script_running
    if key == keyboard.Key.esc:
        print("Escape key pressed. Stopping the script...")
        script_running = False
        return False  # Stop the keyboard listener

# Start listening for the Esc key
listener = keyboard.Listener(on_press=on_press)
listener.start()

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
    time.sleep(1.2)
    center = pyautogui.locateCenterOnScreen("whats-win.png", region=(0, 0, 460, 60), confidence=0.8)
    if center:
        print(f"'whats-win.png' found at: {center}")
        
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
            pyautogui.press('up')
            print(f"Switched to the tab '{tab_title}' and pressed the Right Arrow key.")
        else:
            print(f"Tab with title '{tab_title}' not found.")
    except pyautogui.ImageNotFoundException:
        print(f"Failed to locate the tab with title '{tab_title}'.")

# Example: Coordinates of Chrome
tab_title = "page title"  # Replace with your tab title
ad = 0
activate_chrome_and_find_tab(cx, cy, tab_title)
for y in range(2):
    ad = clipcopy()
    time.sleep(0.2)

def move_and_click(x, y, duration=0.3, clicks=1):
    """Move the mouse to (x, y) and perform a click."""
    mouse.move(x, y, duration=duration)
    for _ in range(clicks):
        time.sleep(0.1)
        mouse.click('left')

def clear_and_paste_in_search_bar():
    """Clear the search bar and paste copied content."""
    move_and_click(167, 125, duration=0.3)
    time.sleep(0.2)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("backspace")
    pyautogui.hotkey("ctrl", "v")
    
    move_and_click(201, 205, duration=2.6, clicks=2)

def interact_with_chrome():
    """Perform actions within Chrome."""
    # Press the space key instead of clicking on the copy location
    time.sleep(0.2)
    pyautogui.press('down')
    time.sleep(0.2)
    pyautogui.press("down")

def check_whatsapp_window():
    """Check if WhatsApp window is open and bring it to focus."""
    # Check if WhatsApp window is found in the region (0, 0, 460, 60)
    time.sleep(0.3)
    if not pyautogui.locateCenterOnScreen("whats-win.png", region=(0, 0, 460, 60), confidence=0.8):
        print("WhatsApp window not found, clicking WhatsApp again to bring it to front.")
        go_to_whatsapp()

def go_to_whatsapp():
    # Switch to WhatsApp
    move_and_click(wx, wy, duration=0.3)
    check_whatsapp_window()

# Main loop
script_running = True  # Variable to control script execution
for x in range(int(ad)):
    if not script_running:
        break
    print(f"Iteration {x+1}")

    # Navigate to the right arrow location and press the right arrow key
    time.sleep(0.3)
    pyautogui.press("right")

    # Switch to WhatsApp and clear/paste in the search bar
    go_to_whatsapp()
    clear_and_paste_in_search_bar()

    # Switch to Chrome and press the space key
    move_and_click(cx, cy, duration=0.3)
    time.sleep(0.2)
    interact_with_chrome()

    # Switch back to WhatsApp
    move_and_click(wx, wy, duration=0.3)
    check_whatsapp_window()
    """Locate 'msg.png' 80px above the taskbar and click its center."""
    time.sleep(0.7)
    region = (0, screen_height- 120, screen_width, screen_height - 40)  # 80px above the taskbar
    
    # Locate the image within the defined region
    msg_location = pyautogui.locateCenterOnScreen("msg.png", region=region, confidence=0.8)
    if msg_location:
        print(f"'msg.png' found at {msg_location}")
        mouse.move(msg_location.x, msg_location.y, duration=0.3)
        mouse.click('left')
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.1)
        pyautogui.hotkey("Enter")
        time.sleep(0.3)
    else:
        print("'msg.png' not found in the specified region.")


    pyautogui.hotkey("Enter")
    mouse.move(740, 1000, duration = 0.3)
    # Switch to Chrome
    move_and_click(cx, cy, duration=0.3)

print("Script stopped.")