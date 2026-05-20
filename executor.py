import sys
import os
import time
import pyautogui
import yaml


def _resource(filename):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, filename)


class GestureExecutor:
    def __init__(self, config_path=None):
        config_path = config_path or _resource("config.yaml")
        with open(config_path, encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
        self._mapping = cfg.get("gestures", {})
        self._debounce = cfg.get("debounce_ms", 800) / 1000.0
        self._last_time = 0.0
        self.active = True

    def execute(self, gesture: str | None):
        if gesture == "open":
            self.active = True
            return
        if gesture == "fist":
            self.active = False
            return
        if not self.active or gesture is None:
            return

        now = time.monotonic()
        if now - self._last_time < self._debounce:
            return

        entry = self._mapping.get(gesture)
        if entry:
            pyautogui.press(entry["key"])
            self._last_time = now
