import cv2
import mediapipe as mp
import pyautogui
import math
import threading

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands(max_num_hands=1)
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()

pyautogui.FAILSAFE = False

running = True

def virtual_mouse():
    global running
    
    while running:
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

                index_tip = landmarks[8]
                thumb_tip = landmarks[4]

                index_x = int(index_tip.x * frame_width)
                index_y = int(index_tip.y * frame_height)
                thumb_x = int(thumb_tip.x * frame_width)
                thumb_y = int(thumb_tip.y * frame_height)

                cv2.circle(frame, (index_x, index_y), 10, (0, 255, 255), -1)
                cv2.circle(frame, (thumb_x, thumb_y), 10, (0, 255, 255), -1)

                screen_x = screen_width / frame_width * index_x
                screen_y = screen_height / frame_height * index_y
                pyautogui.moveTo(screen_x, screen_y)

                distance = math.hypot(index_x - thumb_x, index_y - thumb_y)
                if distance < 30:
                    pyautogui.click()
                    cv2.waitKey(200)

        cv2.imshow("Virtual Mouse", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            running = False

    cap.release()
    cv2.destroyAllWindows()

# Run thread
thread = threading.Thread(target=virtual_mouse)
thread.start()
thread.join()
