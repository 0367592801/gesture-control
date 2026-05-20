# ✋ Gesture Control

> Điều khiển máy tính bằng ngón tay — không chạm bàn phím, không chạm chuột.

Bạn đang xem phim, ngả lưng ra ghế, tay với không tới bàn phím — chỉ để bấm Space tạm dừng.  
**Gesture Control** giải quyết đúng vấn đề đó. Giơ tay lên, ra hiệu, xong.

---

## Demo

| Cử chỉ | Lệnh |
|--------|------|
| ✌️ Chữ V | Space — Play / Pause |
| ☝️ 1 ngón trỏ | → Tua tới 5 giây |
| 🖕 Ngón giữa | ← Tua lùi 5 giây |
| 👍 Ngón cái | F5 — Refresh trang |
| 3 ngón (trỏ + giữa + áp út) | ↑ Volume tăng |
| 🤙 Ngón út | ↓ Volume giảm |
| 🤙 Shaka (cái + út) | ⏭ Bài tiếp theo |
| ✊ Nắm tay | Tắt nhận lệnh |
| ✋ Mở tay | Bật lại |

---

## Cài đặt & Chạy

**Yêu cầu:** Python 3.10+ · Windows · Webcam

```bash
git clone https://github.com/your-username/gesture-control.git
cd gesture-control
```

Double-click `run.bat` — script tự lo phần còn lại:
- Tạo virtual environment
- Cài dependencies
- Download model MediaPipe
- Chạy app

> Lần đầu mất ~1 phút. Lần sau khởi động trong vài giây.

---

## Tùy chỉnh

Sửa `config.yaml` để đổi phím tắt theo ý muốn:

```yaml
gestures:
  peace:          # ✌️ V sign
    key: space
    description: "Play / Pause"

  point_up:       # ☝️ 1 finger
    key: right
    description: "Seek forward"
```

Danh sách tên phím: [pyautogui keyboard docs](https://pyautogui.readthedocs.io/en/latest/keyboard.html)

---

## Stack

- [MediaPipe](https://mediapipe.dev/) — nhận diện 21 điểm landmark trên bàn tay
- [OpenCV](https://opencv.org/) — capture webcam
- [PyAutoGUI](https://pyautogui.readthedocs.io/) — giả lập phím tắt

---

## Cấu trúc

```
gesture-control/
├── main.py              # Vòng lặp chính
├── detector.py          # MediaPipe → tên cử chỉ
├── executor.py          # Tên cử chỉ → nhấn phím
├── config.yaml          # Mapping cử chỉ ↔ phím
├── hand_landmarker.task # Model file (tự download khi chạy run.bat)
└── run.bat              # Chạy 1 click
```

---

## License

MIT — dùng thoải mái, fork thoải mái.
