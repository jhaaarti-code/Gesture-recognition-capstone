import time
import pyautogui

last_action_time = 0
COOLDOWN = 2

def map_gesture_to_action(gesture):
    global last_action_time
    current_time = time.time()
    
    if current_time - last_action_time < COOLDOWN:
        print("Please wait")
        return
    
    if gesture == "Fist":
        pyautogui.press("volumemute")
        print("Volume Muted")
    
    elif gesture == "Peace":
        pyautogui.press("volumedown")
        print("Volume Down")
    
    elif gesture == "Thumbs up":
        print("Play Pause")
    
    elif gesture == "Open Hand":
        print("Next Slide")
    
    elif gesture == "Point":
        print("Volume Up")
    
    else:
        print("Unknown gesture")
    
    last_action_time = time.time()

print("Gesture Mapping Test")
print("--------------------")
map_gesture_to_action("Fist")
time.sleep(2)
map_gesture_to_action("Peace")
time.sleep(2)
map_gesture_to_action("Thumbs up")
time.sleep(2)
map_gesture_to_action("Open Hand")
time.sleep(2)
map_gesture_to_action("Point")
print("--------------------")
print("Testing complete")
