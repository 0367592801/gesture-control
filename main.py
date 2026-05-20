import sys
import os
import cv2
import yaml
from detector import HandDetector
from executor import GestureExecutor


def _resource(filename):
    """Resolve path for both source runs and PyInstaller bundles."""
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, filename)


def main():
    with open(_resource("config.yaml"), encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    cap = cv2.VideoCapture(cfg.get("camera_index", 0))
    if not cap.isOpened():
        print("Cannot open camera.")
        return

    detector = HandDetector()
    executor = GestureExecutor()

    print("Gesture Control running. Press Q to quit.")
    print("  ✌️  V sign   → Space (Play/Pause)")
    print("  ☝️  1 finger → → (Seek forward)")
    print("  👍 Thumb up  → F5 (Refresh)")
    print("  👊 Fist      → Pause gesture detection")
    print("  ✋ Open hand → Resume gesture detection")

    prev_gesture = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        gesture = detector.get_gesture(frame)

        if gesture != prev_gesture:
            executor.execute(gesture)
            prev_gesture = gesture

        # Overlay
        status = "ON " if executor.active else "OFF"
        color = (0, 220, 0) if executor.active else (0, 0, 220)
        label = f"[{status}]  {gesture or '---'}"
        cv2.putText(frame, label, (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.1, color, 2, cv2.LINE_AA)

        cv2.imshow("Gesture Control  (Q = quit)", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
