# 🖐️ GestureX - Hand Gesture Recognition System

---

## 📌 Project Overview

This project implements a real-time hand gesture recognition system using a webcam.
It detects hand landmarks and identifies gestures based on finger positions.

**Built using:**
- Python
- OpenCV
- MediaPipe (Tasks API)

---

## 🎯 Objective

- Detect hand in real-time
- Extract 21 landmark points
- Recognize gestures using finger positions
- Display gesture output live

---

## ⚙️ Features

- Real-time hand tracking
- 21 landmark detection (`lmList`)
- Gesture recognition (Fist, Peace, Thumbs Up, etc.)
- Live gesture display on screen
- Modular code structure

---

## 🧠 Workflow

```
Camera → Hand Detection → Landmark Extraction → Gesture Recognition → Output
```

---

## 👥 Team Contributions

### 👤 Member 1 — Hand Detection
- Implemented hand detection using MediaPipe
- Generated 21 landmark points (`lmList`)
- Handled webcam input and frame processing

### 👤 Member 2 — Gesture Recognition
- Developed `recognize_gesture(lmList)`
- Implemented finger detection logic
- Defined gesture patterns (Fist, Peace, Thumbs Up, etc.)

### 👤 Member 3 — Gesture to Action Mapping
- Developed the gesture-to-action mapping module
- Mapped recognized gestures to specific system actions (e.g., volume control, play/pause, navigation)
- Implemented logic to trigger corresponding actions based on detected gestures
  
  

### 👤 Member 4 — UI / Output
- Displayed gesture on screen using OpenCV
- Managed visual output and user interaction

### 👤 Member 5 — Integration and Execution
- Integrated all modules including hand detection, gesture recognition, and action mapping into a single system
- Ensured smooth data flow between different components
- Managed overall execution of the system for real-time performance

---

## 🗂️ Project Structure

```
Gesture-recognition-capstone/
│
├── hand_detection.py        # Main file
├── gesture_recognition.py  # Gesture logic
├── hand_landmarker.task     # MediaPipe model file
└── README.md
```

---

## 🚀 How to Run

```bash
python hand_detection.py
```

---

## 🎮 Usage

1. Run the program
2. Show your hand in front of the webcam
3. Perform gestures — ✊ ✌️ 👍 ✋
4. Gesture name will be displayed on screen

---

## ⚠️ Errors & Fixes

| Error | Fix |
|-------|-----|
| MediaPipe `solutions` deprecated error | Switched to `mp.tasks` API |
| Virtual environment issues | Recreated `.venv` from scratch |
| Timestamp error in MediaPipe | Used strictly increasing timestamp |
| Gesture always showing "Unknown" | Fixed `tipIds` indexing logic |
| Gesture not displaying on screen | Integrated `recognize_gesture()` properly |
| Running wrong entry file | Used `hand_detection.py` as main file |

---

## 🧩 Technologies Used

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| OpenCV | Webcam input & visual output |
| MediaPipe | Hand landmark detection |

---

## 🔥 Conclusion

This project demonstrates real-time gesture recognition using hand tracking and computer vision, combining MediaPipe's landmark detection with custom gesture logic for a smooth, responsive experience.

---

## 📌 Future Scope

- Mouse control using gestures
- Support for more gesture types
- Improved recognition accuracy

---

## 🙌 Acknowledgement

Developed as part of a capstone project using **MediaPipe** and **OpenCV**.
