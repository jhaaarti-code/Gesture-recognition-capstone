import time
import pyautogui

def map_gesture_to_action(gesture):
    
    if gesture == "Fist":
        pyautogui.press("volumemute")
        print("Volume Muted")
        return("Volume Muted")
    
    
    elif gesture == "Peace":
        pyautogui.press("volumedown")
        print("Volume Down")
        return("Volume Down")
    
    elif gesture == "Thumbs Up":
        pyautogui.press("space")
        print("Play Pause")
        return("Play Pause")
    
    elif gesture == "Open Hand":
        pyautogui.press("right")
        print("Next Slide")
        return("Next Slide")
    
    elif gesture == "Pointing Up":
        pyautogui.press("volumeup")
        print("Volume Up")
        return("Volume Up")
    
    else:
        return("Unknown Gesture")
    
    
    
if __name__ == "__main__":
    print("Gesture Mapping Test")
    print("--------------------")
    print (map_gesture_to_action("Fist"))
    time.sleep(2)
    print (map_gesture_to_action("Peace"))
    time.sleep(2)
    print (map_gesture_to_action("Thumbs Up"))
    time.sleep(2)
    print (map_gesture_to_action("Open Hand"))
    time.sleep(2)
    print (map_gesture_to_action("Pointing Up"))

    print("--------------------")
    print("Testing complete")
    

