# 🐄 Cattle-on-Road Night Safety Alert System

A Computer Vision project that detects cattle on roads in real time and triggers a visual alert to prevent road accidents — built as part of the Computer Vision course at VIT Bhopal University.

**Made by:** Lavanya Karna  
**Institution:** VIT Bhopal University  

---

## 🚨 The Problem

A large number of road accidents in rural and semi-urban India happen at night due to stray cattle wandering onto highways and roads. Drivers often cannot see them in time to brake safely. This project addresses that problem using computer vision — automatically detecting cattle in road footage and alerting the driver before it is too late.

---

## 💡 What It Does

- Takes any road video as input
- Enhances low-light frames automatically using CLAHE (Contrast Limited Adaptive Histogram Equalization)
- Detects cattle in each frame using YOLOv8
- Displays a **red alert border** with "CATTLE ON ROAD - SLOW DOWN!" when cattle is detected
- Displays a **green "Road Clear"** message when no cattle is visible
- Shows live cattle count and alert count on screen
- Saves the fully annotated output video

---

## 🛠️ Tech Stack

- Python
- YOLOv8 (Ultralytics)
- OpenCV
- NumPy

---

## 📁 Folder Structure
```
cattle-alert/
├── data/
│   └── videos/        ← input video files
├── models/
│   └── yolov8n.pt     ← YOLOv8 model
├── output/            ← processed output videos saved here
├── detect.py          ← main detection script
├── create_sound.py    ← generates alert sound file
├── requirements.txt   ← dependencies
└── README.md
```

---

## ⚙️ Setup and Installation

**1. Clone the repository**
```
git clone https://github.com/yourusername/cattle-alert.git
cd cattle-alert
```

**2. Install dependencies**
```
pip install -r requirements.txt
```

**3. Add your video**

Place any road video inside `data/videos/` and name it `test.mp4`

**4. Run the detection**
```
python detect.py
```

**5. Check the output**

Your annotated video will be saved in the `output/` folder as `result.avi`

---

## 📊 How It Works

1. Each frame of the video is enhanced for low-light conditions using CLAHE
2. YOLOv8 runs object detection on the enhanced frame, filtering for class 19 (cow)
3. If cattle is detected, a red alert is overlaid on the frame
4. If no cattle is detected, a green "Road Clear" message is shown
5. The annotated frame is written to the output video

---

## 🌍 Real World Impact

This system can be integrated into dashcams or roadside cameras in rural India to automatically warn drivers of cattle on the road — potentially saving lives and reducing accidents on national and state highways.

---

## 📦 Requirements
```
ultralytics
opencv-python
numpy
playsound==1.2.2
```