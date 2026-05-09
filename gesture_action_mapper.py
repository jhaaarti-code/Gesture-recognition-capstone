import pyautogui

def perform_action(gesture):

    if gesture == "Pointing Up":
        pyautogui.press("volumeup")
    elif gesture == "Peace":
        pyautogui.press("volumedown")
    elif gesture == "Thumbs Up":
        pyautogui.press("space")
    elif gesture == "Open Hand":
        pyautogui.press("right")
    elif gesture == "Fist":
        pyautogui.press("volumemute")
