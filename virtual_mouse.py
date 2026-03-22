import cv2
import mediapipe as mp

print("Program started")

cap = cv2.VideoCapture(0)

# Initialize MediaPipe Tasks
mp_hands = mp.tasks.vision
base_options = mp.tasks.BaseOptions(model_asset_path=None)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)

    # For now, just display camera (to avoid complexity)
    cv2.imshow("Hand Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()