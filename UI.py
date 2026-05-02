import cv2

CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),
    (0, 5), (5, 6), (6, 7), (7, 8),
    (9, 10), (10, 11), (11, 12),     
    (13, 14), (14, 15), (15, 16),
    (17, 18), (18, 19), (19, 20),
    (0, 17), (5, 9), (9, 13), (13, 17) 
]

def apply_ui(frame, gesture, handedness, lmList):
    
    overlay = frame.copy()
    cv2.rectangle(overlay, (0, 0), (frame.shape[1], 65), (40, 40, 40), -1)
    cv2.addWeighted(overlay, 0.7, frame, 0.3, 0, frame)

    status_text = f"Hand: {handedness} | Gesture: {gesture}"
    cv2.putText(frame, status_text, (20, 42), 
                cv2.FONT_HERSHEY_DUPLEX, 0.9, (0, 255, 0), 1)
    if lmList:
        for pair in CONNECTIONS:
            pt1 = (lmList[pair[0]][1], lmList[pair[0]][2])
            pt2 = (lmList[pair[1]][1], lmList[pair[1]][2])
            cv2.line(frame, pt1, pt2, (255, 255, 255), 2)

        for id, x, y in lmList:
            color = (0, 0, 255) if id in [4, 8, 12, 16, 20] else (0, 255, 255)
            cv2.circle(frame, (x, y), 5, color, -1)
            
    return frame
