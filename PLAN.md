# Gesture Control — Điều khiển media bằng cử chỉ ngón tay

## Vấn đề

Xem phim, ngả ghế ra sau, xa bàn phím → phải ngồi dậy chỉ để Space/F5. Không cần làm vậy.

## Giải pháp

Camera laptop theo dõi ngón tay → nhận diện cử chỉ → giả lập phím tắt.

```
[Webcam] → [MediaPipe detect hand] → [Nhận diện cử chỉ] → [pyautogui gõ phím]
```

Chạy nền. Không cần chuột, không cần bàn phím.

---

## Cử chỉ & lệnh

| Cử chỉ | Phím | Tác dụng |
|--------|------|----------|
| ✌️ 2 ngón (V) | `Space` | Play / Pause |
| ☝️ 1 ngón giơ lên | `→` (5 giây) | Tua tới |
| 🤙 1 ngón giơ xuống (ngón cái) | `←` (5 giây) | Tua lùi |
| 👍 Ngón cái lên | `F5` | Refresh trang |
| 👊 Nắm tay | *(dừng nhận lệnh)* | Tắt chế độ gesture |
| ✋ Mở tay | *(bật nhận lệnh)* | Bật lại |

> Tùy chỉnh thêm trong `config.yaml`.

---

## Tech Stack

```
Python 3.11+
├── opencv-python    # Webcam feed
├── mediapipe        # 21 landmark ngón tay
└── pyautogui        # Giả lập phím
```

3 thư viện. Không server, không mạng, không database.

---

## Cấu trúc

```
gesture-control/
├── main.py          # Entry point — chạy vòng lặp chính
├── detector.py      # MediaPipe wrapper → trả gesture name
├── executor.py      # gesture name → pyautogui action
├── config.yaml      # Mapping cử chỉ → phím (tùy chỉnh)
└── requirements.txt
```

---

## Phases

### Phase 1 — Chạy được (1 tuần)
- [ ] Detect bàn tay trong webcam feed
- [ ] Nhận diện 3 cử chỉ: V (pause), 1 ngón (seek), nắm tay (stop)
- [ ] Gửi `Space` / `→` / `←` bằng pyautogui
- [ ] Debounce: mỗi lệnh cách nhau ≥ 800ms (tránh spam)

**Verify:** Ngồi cách 1.5m, giơ V → YouTube pause.

### Phase 2 — Dùng được hàng ngày (1 tuần)
- [ ] Chạy nền, không hiện cửa sổ lớn (hoặc thu nhỏ)
- [ ] Activation zone: chỉ nhận lệnh khi tay ở vùng trên màn hình
- [ ] Hiển thị gesture đang nhận trong góc nhỏ (overlay)
- [ ] Config từ `config.yaml` — không cần sửa code

### Phase 3 — Tùy chọn
- [ ] System tray icon (bật/tắt nhanh)
- [ ] Thêm cử chỉ: volume up/down, tab switch
- [ ] Tự start khi bật máy

---

## Tiêu chí thành công

- [ ] Hoạt động cách camera 1–2m
- [ ] Phản hồi < 500ms từ khi giơ tay đến khi phím được nhấn
- [ ] Không trigger nhầm khi tay để tự nhiên trên bàn

---

## Bắt đầu

```bash
cd gesture-control
python -m venv venv
venv\Scripts\activate
pip install opencv-python mediapipe pyautogui
python main.py
```
