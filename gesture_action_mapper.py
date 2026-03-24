import time

last_action_time = 0
COOLDOWN = 2

def map_gesture_to_action(gesture):
    global last_action_time
    current_time = time.time()
    
    if current_time - last_action_time < COOLDOWN:
        print("Please wait")
        return
    
    if gesture == "fist":
        print("Volume Muted")
    
    elif gesture == "peace":
        print("Volume Down")
    
    elif gesture == "thumbs_up":
        print("Play Pause")
    
    elif gesture == "open_hand":
        print("Next Slide")
    
    elif gesture == "point":
        print("Volume Up")
    
    else:
        print("Unknown gesture")
    
    last_action_time = time.time()

print("Gesture Mapping Test")
print("--------------------")
map_gesture_to_action("fist")
time.sleep(2)
map_gesture_to_action("peace")
time.sleep(2)
map_gesture_to_action("thumbs_up")
time.sleep(2)
map_gesture_to_action("open_hand")
time.sleep(2)
map_gesture_to_action("point")
print("--------------------")
print("Testing complete")