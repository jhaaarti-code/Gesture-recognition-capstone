from gesture_recognition import recognize_gesture
from gesture_action_mapper import map_gesture_to_action
import cv2
import mediapipe as mp
import time

cv2.setUseOptimized(True)

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

pTime = 0  # FPS

prev_gesture = ""
action = "No Action"

while True:
    if not cap.isOpened():
        break
    success, frame = cap.read()
    
    if not success or frame is None:
        print("Camera error")
        break

    frame = cv2.flip(frame, 1)  # mirror view

    # Convert image
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    result = landmarker.detect_for_video(mp_image, timestamp)
    timestamp += 1

    lmList = []
    gesture = "No Hand"

    if result.hand_landmarks: 
        for hand in result.hand_landmarks:
            for id, lm in enumerate(hand):
                h, w, _ = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                
        if len(lmList) == 21:
            gesture = recognize_gesture(lmList)
            
            
        if gesture != prev_gesture:
            action = map_gesture_to_action(gesture)
            prev_gesture = gesture
        


        # ✅ Draw landmarks
        for lm in lmList:
            cv2.circle(frame, (lm[1], lm[2]), 4, (0, 255, 0), cv2.FILLED)

        # ✅ Draw connections (hand skeleton)
        connections = [(0,1),(1,2),(2,3),(3,4),
                       (0,5),(5,6),(6,7),(7,8),
                       (5,9),(9,10),(10,11),(11,12),
                       (9,13),(13,14),(14,15),(15,16),
                       (13,17),(17,18),(18,19),(19,20)]

        if len(lmList) == 21:
            for con in connections:
                x1, y1 = lmList[con[0]][1:]
                x2, y2 = lmList[con[1]][1:]
                cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 255), 2)

        # 🟢 Highlight index finger tip
        x, y = lmList[8][1], lmList[8][2]
        cv2.circle(frame, (x, y), 10, (0, 255, 255), cv2.FILLED)

        # 🔳 Bounding box
        xList = [lm[1] for lm in lmList]
        yList = [lm[2] for lm in lmList]

        xmin, xmax = min(xList), max(xList)
        ymin, ymax = min(yList), max(yList)

        cv2.rectangle(frame, (xmin-20, ymin-20), (xmax+20, ymax+20),
                      (255, 0, 255), 2)

    # ================= 🎨 AESTHETIC UI ================= #

    # Transparent panel
    overlay = frame.copy()
    cv2.rectangle(overlay, (10, 10), (350, 120), (20, 20, 20), -1)
    frame = cv2.addWeighted(overlay, 0.6, frame, 0.4, 0)

    # Gesture text
    cv2.putText(frame, "Gesture:", (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (200, 200, 200), 2)

    cv2.putText(frame, gesture, (20, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 255), 3)
    
    cv2.putText(frame, action,(20,130),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                (255, 255, 255), 2)

    # 🎯 Gesture feedback messages
    if gesture == "Fist":
        cv2.putText(frame, "✊ LOCK MODE", (200, 200),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 0, 255), 3)

    elif gesture == "Peace":
        cv2.putText(frame, "✌️ PEACE MODE", (200, 200),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (255, 0, 255), 3)

    elif gesture == "Thumbs Up":
        cv2.putText(frame, "👍 LIKE!", (200, 200),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 255, 0), 3)

    elif gesture == "Open Hand":
        cv2.putText(frame, "🖐 READY", (200, 200),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (255, 255, 255), 3)

    # ================= FPS ================= #

    cTime = time.time()
    fps = 1 / (cTime - pTime) if (cTime - pTime) != 0 else 0
    pTime = cTime

    cv2.putText(frame, f'FPS: {int(fps)}', (500, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                (255, 255, 0), 2)

    # ================================================= #
    if frame is not None:
        cv2.imshow("Virtual Gesture UI", frame)
    try:
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    except:
        pass

       
cap.release()
cv2.destroyAllWindows()
