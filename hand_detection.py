from gesture_recognition import recognize_gesture
import cv2
import mediapipe as mp

# Load model
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path="hand_landmarker.task"),
    running_mode=VisionRunningMode.VIDEO
)

landmarker = HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)
timestamp = 0

while True:
    success, frame = cap.read()
    if not success:
        break

    # Convert image
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    result = landmarker.detect_for_video(mp_image, timestamp)
    timestamp += 1

    lmList = []

    if result.hand_landmarks:
        for hand in result.hand_landmarks:
            for id, lm in enumerate(hand):
                h, w, _ = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                
        if len(lmList) == 21:
            gesture = recognize_gesture(lmList)
            print("Gesture:", gesture)
            
            cv2.putText(frame, gesture, (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)



    cv2.imshow("Hand Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()