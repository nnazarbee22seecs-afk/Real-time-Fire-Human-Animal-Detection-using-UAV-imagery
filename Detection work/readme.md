# 🔥 Real-time Smoke & Fire Detection using YOLOv12



Multi-Platform Deployment: Colab, Local, and NVIDIA Orin Nano

An advanced real-time detection system built with YOLOv12 for identifying smoke and fire across diverse computing environments from cloud based prototyping with Google Colab to power efficient, real world inference on the NVIDIA Jetson Orin edge device.
---

## 🎯 Project Overview

This repository demonstrates a **deep learning-based fire and smoke detection system** that uses the YOLOv12 model for real-time inference. 
This project implements a full-stack deep learning pipeline for a critical safety application. It's not just a model but a complete workflow that validates the system's performance in three key environments, ensuring robustness from development to deployment.
Core Architecture: YOLOv12 (Attention-Centric Design) → Ultralytics Framework → Platform-Specific Optimization
The system can be used for early fire detection through surveillance UAV's,safety, and smart cities.

---

## ⚙️ Features

- 🔍 **YOLOv12 model** for accurate smoke/fire detection  
- 🎥 Works on both **images and videos**
- 🚀 Real-time detection on webcam or video files  
- 📊 Supports visualization and confidence score display  
- 💾 Lightweight and easy to deploy  

---


## 🧠 Model

The detection model is based on **YOLOv12**, trained on a custom dataset of smoke and fire images.  
You can fine tune or retrain it using the training notebook provided.

--

## ⚡ Installation

```bash
git clone https://github.com/<your-username>/Smoke-Fire-Detection-YOLOv12.git
cd Smoke-Fire-Detection-YOLOv12
pip install -r requirements.txt
```

---

## 🧩 Usage

1. Open `app.ipynb` to run the live detection demo.  
2. Or run `smoke-fire-detection-yolo-v12.ipynb` to test on your dataset or videos.  
3. Place your input video inside the project folder and update the path in the notebook.

---

## 📊 Example Results

| Input | Detection |
|:------:|:----------:|
| ![Fire](Screenshots/sample_result.jpg) | ✅ Fire detected with confidence 0.92 |

---

## 🧾 Requirements

Listed in `requirements.txt`.

---

## 🌐 Future Improvements

- Integration with IoT alert system  
- Web app interface using Streamlit or Flask  

---


