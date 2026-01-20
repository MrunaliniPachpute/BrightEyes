# main.py
import cv2
import pyttsx3
import pytesseract
import os
from text_coverage_check import text_coverage_percentage

# Configure pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# TTS engine for guidance
engine = pyttsx3.init()
engine.setProperty("rate", 160)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Camera URL
url = "http://192.168.31.23:8080/video"
cap = cv2.VideoCapture(url)

if not cap.isOpened():
    speak("Camera not accessible")
    exit()

ROTATION = cv2.ROTATE_90_CLOCKWISE
MAX_FRAMES = 4
captured_frames = []

speak("Camera opened. Press spacebar to capture a frame.")

while True:
    ret, frame = cap.read()
    if not ret:
        speak("Frame not received. Check camera connection.")
        break

    frame = cv2.rotate(frame, ROTATION)
    cv2.imshow("Camera View", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == 32:  # SPACE → capture
        coverage = text_coverage_percentage(frame)
        if coverage < 90:
            speak(f"Page not fully visible. Only {int(coverage)} percent covered. Move camera closer.")
            continue

        captured_frames.append(frame.copy())
        speak("Capture successful.")
        remaining = MAX_FRAMES - len(captured_frames)

        if remaining == 0:
            speak("Maximum frames captured. Proceeding to reading.")
            break
        else:
            speak(f"You can capture {remaining} more frames. Press SPACE to capture, ENTER to proceed.")

    elif key == 13:  # ENTER → proceed
        if len(captured_frames) == 0:
            speak("No frame captured yet. Capture at least one frame.")
        else:
            speak("Proceeding to reading captured frames.")
            break

    elif key == 27:  # ESC → exit
        speak("Exiting camera.")
        break

cap.release()
cv2.destroyAllWindows()

# Save captured frames
os.makedirs("frames", exist_ok=True)
for i, img in enumerate(captured_frames):
    cv2.imwrite(f"frames/frame_{i+1}.jpg", img)

# Optional: save OCR text here if you want to pass it to frontend
final_text = ""
for img in captured_frames:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(thresh)
    final_text += "\n" + text.strip()

with open("frames/final_text.txt", "w", encoding="utf-8") as f:
    f.write(final_text.strip())

speak("Capture complete. You can now open the frontend to view results and listen to text.")
