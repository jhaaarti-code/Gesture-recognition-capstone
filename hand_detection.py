import mediapipe as mp
import cv2

class HandDetector:
    def __init__(self, model_path='hand_landmarker.task'):
        BaseOptions = mp.tasks.BaseOptions
        HandLandmarker = mp.tasks.vision.HandLandmarker
        HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
        VisionRunningMode = mp.tasks.vision.RunningMode

        self.options = HandLandmarkerOptions(
            base_options=BaseOptions(model_asset_path=model_path),
            running_mode=VisionRunningMode.VIDEO
        )
        self.detector = HandLandmarker.create_from_options(self.options)

    def find_hands(self, frame, timestamp_ms):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
        
        result = self.detector.detect_for_video(mp_image, timestamp_ms)
        
        lmList = []
        handedness = "None"
        
        if result.hand_landmarks:
            hand_landmarks = result.hand_landmarks[0]
            handedness = result.handedness[0][0].category_name
            
            h, w, _ = frame.shape
            for id, lm in enumerate(hand_landmarks):
                lmList.append([id, int(lm.x * w), int(lm.y * h)])
        
        return lmList, handedness

    def close(self):
        self.detector.close()
