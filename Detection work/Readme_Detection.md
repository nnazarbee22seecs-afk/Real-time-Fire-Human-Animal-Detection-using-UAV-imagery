
# 🔥 Smoke & Fire Detection using YOLOv12

An advanced real-time **Smoke and Fire Detection System** built using **YOLOv12** for object detection.  
This project detects smoke and fire in video streams or live camera feeds with high accuracy and speed.

---

## 📋 Project Overview

This repository contains a **YOLOv12-based smoke and fire detection model** specifically designed for real-time detection using computer vision. The model is trained to detect two critical classes:
- **🔥 fire** (wildfires, building fires, etc.)
- **💨 smoke** (smoke plumes, early fire indicators)

The system can be used for early fire detection in surveillance cameras, industrial safety, and smart cities.

---

## 🚀 Quick Start

### **Method 1: Google Colab Testing**
Use the provided notebook for easy testing:

1. **Mount Google Drive** and load the model:
```python
from google.colab import drive
drive.mount('/content/drive')
model_path = '/content/drive/MyDrive/Smoke-Fire-Detection-YOLO-V12-main/Smoke Fire.pt'
```

2. **Test with uploaded images/videos** using `model_test_Smoke fire.ipynb`
3. **Get real-time results** with bounding boxes and confidence scores

---

## 🧠 Model Details

### **Model Specifications**
- **Architecture**: YOLOv12 (custom)
- **Classes**: 2 (fire, smoke)
- **Training Dataset**: Custom collected UAV/surveillance footage
- **Input Resolution**: 640x640
- **Training Epochs**: 100+
- **mAP@0.5**: >0.85
Model Architecture Description:
Backbone

The backbone consists of a sequence of stride-2 convolutional layers that progressively downsample the input while increasing the channel depth. Initial feature extraction is performed using standard Conv–BatchNorm–SiLU blocks to capture low-level spatial patterns.

To enhance feature representation with minimal computational overhead, the backbone incorporates multiple C3k2 blocks, which are lightweight cross-stage partial modules that improve gradient flow and promote feature reuse.

At deeper layers, A2C2f blocks are employed to integrate convolutional processing with attention-based feature modulation. These blocks utilize query–key–value projections, depthwise convolutional positional encoding, and compact MLP layers, enabling the network to emphasize spatially salient regions such as smoke dispersion patterns and flame structures.
Neck

The neck follows a Feature Pyramid Network (FPN) style architecture to enable effective multi-scale feature fusion. High-level semantic features are upsampled using nearest-neighbor interpolation and concatenated with lower-level spatial features through skip connections.

The fused features are further refined using additional A2C2f and C3k blocks, preserving both fine-grained spatial details required for early smoke detection and high-level contextual information essential for accurate fire localization.
Detection Head

The detection head operates across three feature scales, enabling robust detection of objects of varying sizes. Each detection branch includes:

A convolutional pathway for bounding box regression

A depthwise-separable convolutional pathway for classification

The model predicts two classes: fire and smoke, and employs a Distribution Focal Loss (DFL) layer for bounding box regression. DFL improves localization accuracy by modeling bounding box offsets as probability distributions rather than single scalar values.
### **Model Performance**
- **Real-time detection** (30+ FPS on GPU)
- **High accuracy** for both fire and smoke
- **Low false positive rate**
- **Works on various resolutions**

### **Detection Examples:**
```
✅ Wildfire smoke plumes
✅ Building fires
✅ Early smoke detection
✅ Indoor fire scenarios
```

---

## ⚡ Installation & Requirements

### **Dependencies**
All required packages are listed in `requirements.txt`:

```txt
ultralytics>=8.2.0
torch>=2.1.0
opencv-python
numpy
pandas
matplotlib
Pillow
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 🧩 Usage

### **Basic Inference with Python:**
```python
from ultralytics import YOLO

# Load model
model = YOLO('Smoke Fire.pt')

# Detect on image
results = model('test.jpg', conf=0.25)

# Access results
for result in results:
    boxes = result.boxes  # Bounding boxes
    classes = result.names  # Class names
    print(f"Detected {len(boxes)} objects")
```

### **Video Processing:**
```python
# Process video
results = model('fire_video.mp4', 
                save=True, 
                conf=0.25,
                project='results',
                name='video_detection')
```

### **Using Notebooks:**
1. Open `app.ipynb` to run the live detection demo  
2. Or run `smoke-fire-detection-yolo-v12.ipynb` to test on your dataset or videos  

---

## 📊 Example Results

Here are sample detections from the model showing both **fire** and **smoke** detection in various scenarios:

| Scenario | Detection Result |
|:----------:|:----------------:|
| **Indoor Fire Detection**<br>![Indoor Fire](results/fire%20detection2.png) | ✅ **Fire detected**<br>Confidence: 0.89 |
| **Multiple Fire Sources**<br>![Multiple Fires](results/fire%20detection3.png) | ✅ **Multiple fires detected**<br>Confidence: 0.87-0.91 |
| **Real Fire Scenario**<br>![Real Fire](results/real%20fire.png) | ✅ **Fire & smoke detected**<br>Confidence: 0.94 |

**Note**: The model successfully detects both fire and smoke in various lighting conditions and environments. Confidence scores may vary based on image quality and fire intensity.

---

## 🌐 Future Improvements

- Integration with IoT alert system  
- Web app interface using Streamlit or Flask  
- Add more training data
- Improve small object detection
- Reduce false positives
- Add distance estimation
- Create mobile app version

---

## 🚨 Important Notes

1. **Model is for detection only** - Not for fire suppression systems
2. **Use appropriate confidence thresholds** (0.25-0.5 recommended)
3. **For educational/research purposes** - Commercial use may require additional permissions

---

## 🤝 Contributing

Feel free to:
1. Report issues with detections
2. Suggest improvements
3. Share new training data
4. Create pull requests

---

## 🔗 Resources

- [Ultralytics YOLO Documentation](https://docs.ultralytics.com)
- [OpenCV Documentation](https://docs.opencv.org)
- [PyTorch Documentation](https://pytorch.org/docs)

---



**⚠️ Disclaimer**: This model is for detection purposes only. Always follow proper fire safety protocols and consult professionals for critical applications.
