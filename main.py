import cv2
import time
from hand_detection import HandDetector
import gesture_recognition
import gesture_action_mapper
import UI

detector = HandDetector(model_path='hand_landmarker.task')
cap = cv2.VideoCapture(0)
last_action_time = 0
COOLDOWN = 0.6 

print("System Active. Exit keys: 'q', 'Esc', or 'Backspace'")

while cap.isOpened():
    success, frame = cap.read()
    if not success: break
    
    frame = cv2.flip(frame, 1)
    timestamp = int(time.time() * 1000)

    lmList, handedness = detector.find_hands(frame, timestamp)
    gesture = gesture_recognition.recognize_gesture(lmList, handedness)

    if time.time() - last_action_time > COOLDOWN:
        gesture_action_mapper.perform_action(gesture)
        last_action_time = time.time()

    frame = UI.apply_ui(frame, gesture, handedness, lmList)
    
    cv2.imshow("Gesture Control Hub", frame)

    key = cv2.waitKey(1) & 0xFF
    if key in [ord('q'), 27, 8]:
        break

cap.release()
cv2.destroyAllWindows()
detector.close()
