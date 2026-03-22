import cv2
import mediapipe as mp
import pyautogui
import math # Imported for distance calculation

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands(max_num_hands=1) # Recommended: limit to 1 hand to avoid cursor jumping
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()

# Optional: Add a smooth factor to prevent the cursor from being jittery
pyautogui.FAILSAFE = False 

while True:
    success, frame = cap.read()
    if not success:
        break
        
    frame = cv2.flip(frame, 1) 
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            
            # 1. Directly grab the index and thumb landmarks
            index_tip = landmarks[8]
            thumb_tip = landmarks[4]

            # 2. Convert to pixel coordinates on the frame
            index_x = int(index_tip.x * frame_width)
            index_y = int(index_tip.y * frame_height)
            thumb_x = int(thumb_tip.x * frame_width)
            thumb_y = int(thumb_tip.y * frame_height)

            # Draw circles on the tips
            cv2.circle(img=frame, center=(index_x, index_y), radius=10, color=(0, 255, 255), thickness=-1)
            cv2.circle(img=frame, center=(thumb_x, thumb_y), radius=10, color=(0, 255, 255), thickness=-1)

            # 3. Move the mouse based on the index finger
            screen_index_x = screen_width / frame_width * index_x
            screen_index_y = screen_height / frame_height * index_y
            pyautogui.moveTo(screen_index_x, screen_index_y)

            # 4. Calculate actual Euclidean distance between thumb and index
            distance = math.hypot(index_x - thumb_x, index_y - thumb_y)
            
            # 5. Click logic
            if distance < 30: # 30 pixels on the camera frame (adjust as needed)
                pyautogui.click()
                
                # Replaced sleep(1) with waitKey to prevent freezing the webcam feed entirely, 
                # though building a time.time() cooldown is even better for production.
                cv2.waitKey(200) 

    cv2.imshow('Virtual Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()