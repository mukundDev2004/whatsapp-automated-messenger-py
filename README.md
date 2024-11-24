Automation Script: Version 1
This is an automation script designed to interact with WhatsApp Desktop and a web page (main.html) to perform repetitive tasks. The script automates actions like switching between applications, copying data, and interacting with user interfaces.

Prerequisites
Before running the script, ensure the following prerequisites are met:

WhatsApp Desktop:

Make sure the WhatsApp Desktop application is installed and logged in with the required account.
main.html File:

The file main.html should already be open and running in a Chrome browser.
The required Excel file must be uploaded in main.html.
Python:

Install Python (version 3.7 or above).
Python Libraries:

Install the required Python libraries by running:
bash
Copy code
pip install -r requirements.txt
The script uses the following libraries:

pyautogui
mouse
pynput
Verify Dependencies:

Ensure the system display and scaling settings allow accurate detection of screen elements by pyautogui.
Installation
Clone or download this repository to your local machine.
Navigate to the folder containing the script.
Usage
Prepare the Environment:

Open WhatsApp Desktop.
Open main.html in Chrome and ensure the required Excel file is uploaded.
Make sure no other programs or elements overlap with the required screen elements.
Run the Script:

Open a terminal in the folder where the script is located.
Run the following command:
bash
Copy code
python v1.py
Script Workflow:

The script performs the following actions:
Interacts with WhatsApp Desktop to search and interact with contacts.
Switches to Chrome to fetch data from the uploaded Excel file.
Automates tasks like sending messages, copying, and pasting.
Fail-Safe:

Press the ESC key at any time to immediately stop the script.
Troubleshooting
Screen Element Not Found:

Ensure all elements (like WhatsApp and Chrome) are visible on the screen.
Adjust screen scaling to 100% if detection fails.
Space Key Not Working:

If pressing the space key does not activate the required functionality in Chrome, ensure the browser window is in focus.
ModuleNotFoundError:

If you encounter errors like ModuleNotFoundError, make sure the required libraries are installed using pip.
Note
This is Version 1 of the script. Future versions may include enhancements such as error handling, dynamic scaling support, and better compatibility across systems.