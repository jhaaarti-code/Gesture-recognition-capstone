def recognize_gesture(lmList, handedness):
    if not lmList:
        return "No Hand"

    fingers = []

    if handedness == "Right":
        fingers.append(1 if lmList[4][1] > lmList[3][1] else 0)
    else:
        fingers.append(1 if lmList[4][1] < lmList[3][1] else 0)

    tipIds = [8, 12, 16, 20]
    for id in tipIds:
        if lmList[id][2] < lmList[id-2][2]:
            fingers.append(1)
        else:
            fingers.append(0)

    total = fingers.count(1)

    if total == 0: return "Fist"
    if total == 5: return "Open Hand"
    if fingers == [0, 1, 0, 0, 0]: return "Pointing Up"
    if fingers == [0, 1, 1, 0, 0]: return "Peace"
    if fingers == [1, 0, 0, 0, 0]: return "Thumbs Up"
    
    return "Neutral"
