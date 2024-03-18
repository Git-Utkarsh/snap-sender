import time
import pyautogui

def send_snap(username):
    # Open Snapchat website in a new tab
    pyautogui.hotkey('ctrl', 't')
    pyautogui.write('https://www.snapchat.com/')
    pyautogui.press('enter')
    time.sleep(5)  # Wait for the website to load
    
    # Click on the login button
    pyautogui.click(x=100, y=100)  # Adjust coordinates according to your screen resolution
    time.sleep(2)  # Wait for the login page to load
    
    # Enter username and password
    pyautogui.write('your_username')
    pyautogui.press('tab')
    pyautogui.write('your_password')
    pyautogui.press('enter')
    time.sleep(10)  # Wait for the login to complete and page to load
    
    # Click on the camera icon to take a snap
    pyautogui.click(x=200, y=200)  # Adjust coordinates according to your screen resolution
    time.sleep(5)  # Wait for the camera to load
    
    # Take a snap
    pyautogui.press('space')
    time.sleep(3)  # Wait for the snap to be taken
    
    # Enter the username to send the snap
    pyautogui.write(username)
    time.sleep(2)  # Wait for the user to be selected
    
    # Click on the send button
    pyautogui.click(x=300, y=300)  # Adjust coordinates according to your screen resolution
    time.sleep(2)  # Wait for the snap to be sent

# Replace 'your_username' with your Snapchat username
send_snap('recipient_username')
