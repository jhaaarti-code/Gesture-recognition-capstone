import cv2
from time import time
import hand_detection
import gesture_recognition 
import UI 
import gesture_action_mapper

cap = cv2.VideoCapture(0)

last_action_time = 0
cooldown_time = 1.0

EXIT_KEY = 27  # ESC key
print("System is Activated. Press 'esc' to quit.")

detector = hand_detection.HandDetector(model_path='hand_landmarker.task')

while True:
    success, image = cap.read()
    if not success:
        print("Error: Camera not found!")
        break
    
    flip_image = cv2.flip(image, 1)

    lmList = detector.find_hands(flip_image)

    if lmList:
        gesture = gesture_recognition.recognize_gesture(lmList)
        UI.draw_ui(flip_image, gesture)

        current_time = time()

        if gesture != "Unknown" and (current_time - last_action_time > cooldown_time):
            gesture_action_mapper.perform_action(gesture)
            last_action_time = current_time

    cv2.imshow("GestureX", flip_image)

    key = cv2.waitKey(1) & 0xFF
    if key == EXIT_KEY:
        break

cap.release()
cv2.destroyAllWindows()

print("GestureX Closed Successfully!")