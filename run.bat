@echo off
cd /d "%~dp0"

if not exist venv (
    echo Setting up environment...
    python -m venv venv
    venv\Scripts\pip install opencv-python mediapipe pyautogui pyyaml
)

if not exist hand_landmarker.task (
    echo Downloading hand model...
    venv\Scripts\python -c "import urllib.request; urllib.request.urlretrieve('https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task', 'hand_landmarker.task')"
)

venv\Scripts\python main.py
