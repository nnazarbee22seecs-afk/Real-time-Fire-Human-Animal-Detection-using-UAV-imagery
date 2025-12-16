# 🔥 Real-Time Fire Detection on Jetson Edge Devices

This folder contains a real-time fire detection system optimized for **NVIDIA Jetson Nano** and **Jetson Orin** platforms. The implementation provides immediate, low-latency fire detection directly from a USB webcam, making it ideal for standalone edge deployment.

---

## ⚡ Quick Start: Run in 1 Minute

**Step 1: Save the Script**
Create a new file called `fire_hybrid.py` on your Jetson Orin and paste in the entire script code:
```bash
nano fire_hybrid.py
```

**Step 2: Run the Detection**
```bash
python3 fire_hybrid.py
```

**Controls While Running:**
- **Press `q`** to quit
- **Press `s`** to save a screenshot

---

## 📋 Prerequisites Setup

### 1️⃣ Install NVIDIA JetPack OS
Your Jetson device requires the official NVIDIA software.

**📥 Download JetPack:**
- **Primary Source:** [NVIDIA Jetson Download Center](https://developer.nvidia.com/embedded/downloads)
- **Getting Started:** [Jetson Orin Nano Developer Kit Guide](https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit)

**Installation Steps:**
1. Download the correct JetPack SD card image for your Jetson model
2. Flash to microSD card using [Balena Etcher](https://www.balena.io/etcher/)
3. Insert into Jetson, boot up, and complete initial setup

### 2️⃣ Connect Your Webcam
Plug any USB webcam into your Jetson. Verify detection:
```bash
ls /dev/video*
# Should show: /dev/video0 or /dev/video1
```

---

## ⚙️ Complete Dependency Installation

### Step 1: Install System Packages
```bash
sudo apt update
sudo apt upgrade -y
sudo apt install python3-pip python3-dev libjpeg-dev libopenblas-dev -y
```

### Step 2: Install PyTorch for Jetson (Official)
```bash
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/jetson
```

### Step 3: Install Computer Vision Libraries
```bash
pip3 install numpy opencv-python-headless pillow matplotlib scikit-image
```

### Step 4: Verify All Installations
```bash
python3 -c "
import torch, cv2, numpy, PIL, matplotlib
print('✅ PyTorch:', torch.__version__)
print('✅ CUDA Available:', torch.cuda.is_available())
print('✅ OpenCV:', cv2.__version__)
print('✅ All libraries installed successfully!')
"
```

---

## 🚀 Running Fire Detection

### Step 1: Save the Script
Create `fire_hybrid.py` and paste your complete code:
```bash
nano fire_hybrid.py
# Paste your entire fire_hybrid.py code here
# Press CTRL+X, then Y, then Enter to save
```

### Step 2: Run Detection System
```bash
python3 fire_hybrid.py
```

### 🔧 Controls While Running:
- **Press `q`** → Quit application
- **Press `s`** → Save screenshot
- **Press `r`** → Reset counters

---

## 🛠️ Official Resources & Links

### Essential Documentation:
- **PyTorch for Jetson:** https://pytorch.org/get-started/locally/#jetson-nano
- **OpenCV Installation:** https://docs.opencv.org/4.x/d2/de6/tutorial_py_setup_in_ubuntu.html
- **Matplotlib Guide:** https://matplotlib.org/stable/users/installing/index.html

### Troubleshooting Forums:
- **NVIDIA Developer Forum:** https://forums.developer.nvidia.com/c/agx-autonomous-machines/jetson-embedded-systems/70

---

## ⚡ Quick Troubleshooting Guide

| Problem | Solution |
|---------|----------|
| **"No module named 'torch'"** | Reinstall: `pip3 install torch --extra-index-url https://download.pytorch.org/whl/jetson` |
| **"Cannot open webcam"** | Check with `ls /dev/video*`, try camera index 1 |
| **Low FPS** | Edit script lines 9-10 to lower resolution |
| **CUDA not available** | Verify JetPack installation: `nvcc --version` |

---

## ✅ Final Checklist

- [ ] JetPack OS installed and booted
- [ ] Webcam connected and detected (`/dev/video0`)
- [ ] All Python libraries installed (PyTorch, OpenCV, etc.)
- [ ] `fire_hybrid.py` file created with your code
- [ ] In the correct directory containing the script

---

## 🆘 Need Help?

1. Run verification command above to check installations
2. Ensure you're using Jetson-specific PyTorch wheels
3. Check webcam detection with: `nvgstcapture-1.0`
4. Visit NVIDIA forums with your error messages

---

**🎉 Ready to launch! Run:**
```bash
python3 fire_hybrid.py
```

*Part of Real-time-Fire-Human-Animal-Detection-using-UAV-imagery project*  
*Compatible with: NVIDIA Jetson Orin Series*  
*Requires: JetPack 5.1+, Python 3.8+*
