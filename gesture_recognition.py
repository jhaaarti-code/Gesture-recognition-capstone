tipIds = [4,8,12,16,20]

def recognize_gesture(lmList):
    
    fingers = []
    # Thumb (x direction)
    if lmList[4][1] > lmList[3][1]:
        fingers.append(1)
    else:
        fingers.append(0)
        
    # other fingers (y direction)
    for i in range(1,5):
        print(f"checking finger {i}:tip = {lmList[tipIds[i]][2]}, joint = {lmList[tipIds[i]-2][2]}")
        if lmList[tipIds[i]][2] < lmList[tipIds[i]-2][2]:
            fingers.append(1)
        else:
            fingers.append(0)
        
    print("Fingers:", fingers)
            
    # Gesture recognition
    if fingers == [0,0,0,0,0]:
        return "Fist"
    
    elif fingers == [0,1,1,0,0]:
        return "Peace"
    
    elif fingers == [1,0,0,0,0]:
        return "Thumbs Up"
    
    elif fingers == [0,1,0,0,0]:
        return "Pointing Up"
    
    elif fingers == [1,1,1,1,1]:
        return "Open Hand"
    
    else:
        return "Unkown Gesture"
    
# TEST CODE

if __name__ == "__main__":
    lmList = [[i,0,0] for i in range(21)]
    
    #Thumb Down
    lmList[4][1] = 100
    lmList[3][1] = 200
    
    # Index Up
    lmList[8][2] = 50
    lmList[6][2] = 200
    
    # Middle Up
    lmList[12][2] = 50
    lmList[10][2] = 200
    
    # Ring Down
    lmList[16][2] = 300
    lmList[14][2] = 100
    
    # Pinky Down
    lmList[20][2] = 300
    lmList[18][2] = 100

    print("Index values:", lmList[8][2], lmList[6][2])
 
    
    print(recognize_gesture(lmList))
    gesture = recognize_gesture(lmList)
    print("Gesture",gesture)
    
    
    
    

    
        