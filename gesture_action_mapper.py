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
    elif gesture == "Four fingers Up":
        pyautogui.press("left")
    elif gesture == "Zoom":
        pyautogui.hotkey("ctrl","=")
    elif gesture == "Zoom_2":
        pyautogui.hotkey("ctrl","-")
    elif gesture == "Three up":
        pyautogui.press("down")
    elif gesture == "Call":
        pyautogui.press("up")
    elif gesture == "Close Cam":
        pyautogui.press("q")    