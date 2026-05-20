import sys
import os
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


def _resource(filename):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, filename)


class HandDetector:
    def __init__(self):
        options = vision.HandLandmarkerOptions(
            base_options=python.BaseOptions(
                model_asset_path=_resource("hand_landmarker.task")
            ),
            num_hands=1,
            min_hand_detection_confidence=0.7,
            min_hand_presence_confidence=0.5,
            min_tracking_confidence=0.5,
            running_mode=vision.RunningMode.IMAGE,
        )
        self._detector = vision.HandLandmarker.create_from_options(options)

    def get_gesture(self, frame):
        """Process BGR frame, return gesture name string or None."""
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
        result = self._detector.detect(mp_image)

        if not result.hand_landmarks:
            return None

        lm = result.hand_landmarks[0]
        fingers = self._fingers_up(lm)
        return self._classify(fingers)

    def _fingers_up(self, lm):
        """Return [thumb, index, middle, ring, pinky] — True = extended."""
        index  = lm[8].y  < lm[6].y
        middle = lm[12].y < lm[10].y
        ring   = lm[16].y < lm[14].y
        pinky  = lm[20].y < lm[18].y
        thumb  = lm[4].y  < lm[2].y
        return [thumb, index, middle, ring, pinky]

    def _classify(self, f):
        """Map finger state list to gesture name. Thumb ignored unless required."""
        _, idx, mid, ring, pinky = f
        thumb = f[0]

        # Priority: most specific first
        if thumb and not idx and not mid and not ring and not pinky: return "thumb_up"      # 👍
        if not idx and not mid and not ring and not pinky:         return "fist"           # 👊
        if idx and mid and ring and pinky:                         return "open"           # ✋
        if idx and mid and not ring and not pinky:                 return "peace"          # ✌️
        if idx and not mid and not ring and not pinky:             return "point_up"       # ☝️
        if mid and not idx and not ring and not pinky:             return "middle_up"      # 🖕
        if idx and mid and ring and not pinky:                     return "three_up"       # 3 ngón
        if thumb and pinky and not idx and not mid and not ring:   return "shaka"          # shaka (before pinky_up)
        if pinky and not idx and not mid and not ring:             return "pinky_up"       # út
        return None
