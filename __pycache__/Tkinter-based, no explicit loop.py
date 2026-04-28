import cv2
import mediapipe as mp
import pyautogui
import math
import tkinter as tk

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands(max_num_hands=1)
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()

pyautogui.FAILSAFE = False

root = tk.Tk()
root.title("Virtual Mouse Controller")

def update_frame():
    success, frame = cap.read()
    if not success:
        return

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

            screen_x = screen_width / frame_width * index_x
            screen_y = screen_height / frame_height * index_y
            pyautogui.moveTo(screen_x, screen_y)

            distance = math.hypot(index_x - thumb_x, index_y - thumb_y)
            if distance < 30:
                pyautogui.click()

    cv2.imshow("Virtual Mouse", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        root.destroy()
        return

    # Schedule next frame (no loop!)
    root.after(10, update_frame)

# Start loop
update_frame()
root.mainloop()
