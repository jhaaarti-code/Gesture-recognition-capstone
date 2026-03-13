# Gesture-recognition-capstone

## ABHINAV JHA - Hand Detection
Uses MediaPipe to detect the hand through webcam and extract 21 landmark points (finger joints). This is the foundation — all other modules depend on it. Work involves: setting up the camera, running MediaPipe, extracting coordinates, drawing skeleton on screen.

## AARTI JHA - Gesture Recognition
Takes the 21 landmark points from Member 1 and figures out which gesture the user is making (fist, peace sign, thumbs up, etc.). Work involves: checking which fingers are up/down, classifying 10 gestures, adding a stability filter so gestures don't flicker.

## ADITI JHA - Gesture-to-Action Mapping
Takes the recognized gesture from Member 2 and actually does something on the computer — volume up/down, play/pause, take screenshot, next slide, etc. Uses PyAutoGUI and pycaw libraries. Work involves: mapping gestures to keyboard/system actions and adding a cooldown timer.

## ASHUTOSH JHA - UI/Visual Overlay
Designs everything the user sees on screen — the gesture name display, finger state indicators (which fingers are up), volume bar, FPS counter, cooldown arc, gesture history. All drawn on the webcam feed using OpenCV drawing functions.

## PRIYAKRITI JHA - System Integration & Testing
Combines all 4 modules into one working application (main.py). Also writes the config file, folder structure, unit tests, and gesture logger. This is the "glue" of the project.
