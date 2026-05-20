# Gesture Control

Python app dùng MediaPipe để nhận diện cử chỉ tay qua webcam và gửi phím tắt.

## Stack

- Python 3.x + OpenCV + MediaPipe + PyAutoGUI + PyYAML
- Build: PyInstaller (tạo `.exe`)
- Config: `config.yaml` — map gesture → pyautogui key

## Files

| File | Mục đích |
|------|----------|
| `main.py` | Entry point, vòng lặp camera |
| `detector.py` | `HandDetector` — nhận diện gesture từ frame |
| `executor.py` | `GestureExecutor` — gửi phím, debounce, on/off |
| `config.yaml` | Gesture-key mapping, debounce_ms, camera_index |
| `hand_landmarker.task` | MediaPipe model file (binary, không sửa) |
| `*.spec` | PyInstaller spec (GestureControl, 2, 3) |

## Run

```bash
python main.py
```

## Build exe

```bash
pyinstaller GestureControl.spec
```

Output: `dist/GestureControl/GestureControl.exe`

## Gestures

| Gesture | Phím | Mô tả |
|---------|------|--------|
| ✌️ peace | space | Play/Pause |
| ☝️ point_up | right | Tua tới |
| 🖕 middle_up | left | Tua lùi |
| 👍 thumb_up | f5 | Refresh |
| 3 ngón | up | Volume tăng |
| 🤙 pinky_up | down | Volume giảm |
| shaka | nexttrack | Bài tiếp |
| 👊 fist | — | Tắt detection |
| ✋ open | — | Bật detection |

## Notes

- `venv/` không commit
- `build/` và `dist/` không commit
- `hand_landmarker.task` cần có trong thư mục khi chạy source; PyInstaller bundle tự gộp
