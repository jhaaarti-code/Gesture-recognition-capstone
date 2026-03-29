import cv2
import time
import hand_detection
import gesture_recognition 
import UI 
import gesture_action_mapper

cap = cv2.VideoCapture(0)
last_action_time = 0
cooldown_time = 1.00

while hands==true:
    sucess, image - cap.read()