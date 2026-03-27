import cv2
import numpy as np
from ultralytics import YOLO
from playsound import playsound
import threading

model = YOLO('models/yolov8n.pt')

def play_alert():
    try:
        playsound('alert.wav')
    except:
        pass

def enhance_frame(frame):
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    l = clahe.apply(l)
    enhanced = cv2.merge([l, a, b])
    enhanced = cv2.cvtColor(enhanced, cv2.COLOR_LAB2BGR)
    return enhanced

video_path = 'data/videos/test.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file")
    exit()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

print(f"Video loaded: {width}x{height} at {fps}fps")

out = cv2.VideoWriter('output/result.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))

frame_count = 0
alert_count = 0
alert_playing = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    enhanced = enhance_frame(frame)
    results = model(enhanced, classes=[19], conf=0.3, verbose=False)
    annotated = results[0].plot()
    cattle_detected = len(results[0].boxes) > 0
    cattle_in_frame = len(results[0].boxes)

    if cattle_detected:
        alert_count += 1
        cv2.rectangle(annotated, (0, 0), (width, height), (0, 0, 255), 8)
        cv2.putText(annotated, '⚠ CATTLE ON ROAD - SLOW DOWN!', (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
        if not alert_playing:
            alert_playing = True
            threading.Thread(target=play_alert).start()
    else:
        alert_playing = False
        cv2.putText(annotated, 'Road Clear', (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

    cv2.putText(annotated, 'CATTLE ALERT SYSTEM', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.putText(annotated, f'Cattle in frame: {cattle_in_frame}', (10, height - 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
    cv2.putText(annotated, f'Total alerts: {alert_count}', (10, height - 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

    out.write(annotated)
    frame_count += 1

    if frame_count % 10 == 0:
        print(f"Processing frame {frame_count}...")

cap.release()
out.release()
cv2.destroyAllWindows()
print(f"Done! Total frames: {frame_count} | Alert frames: {alert_count}")
print("Check output/result.avi")