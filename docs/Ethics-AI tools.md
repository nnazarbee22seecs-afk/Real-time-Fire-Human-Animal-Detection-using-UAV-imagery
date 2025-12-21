You're absolutely right! Thank you for the correction. Here's the fixed version with **YOLOv12** instead of YOLOv8:

---

# 🤖 **Ethics & AI Tool Documentation**

## **Project Title**  
Real-time Fire Detection using UAV Imagery

## **Team Members**
| Name | CMS ID | Role |
|------|--------|------|
| Ayesha Hussain | 404215 | Simulation & Algorithms |
| Arbaaz Alam | 411425 | Research & Documentation |
| Bushra | 429427 | Research & Documentation |
| Nayab | 414017 | Embedded Systems |

---

## **1. Project Overview**
This project focuses on developing a real-time fire detection system using UAV imagery for emergency response scenarios. The system builds upon our previous FireLite-Seg segmentation work and implements two complementary detection methods optimized for edge deployment on NVIDIA Jetson platforms.

---

## **2. Previous Work Summary**
The following components from prior research were utilized:
- **FireLite-Seg:** Lightweight fire segmentation model (96.85% accuracy, 11.6 FPS on Jetson Nano)
- **Corsican Fire Dataset:** Dataset preprocessing and augmentation techniques
- **Edge Deployment Pipeline:** Jetson Nano optimization strategies
- **Evaluation Metrics:** Standard computer vision metrics for performance validation

---

## **3. New Objectives**
- **Fire Detection:** Real-time identification of fire and smoke using dual-method approach
- **Edge Optimization:** Target 15-25 FPS on Jetson Nano with minimal accuracy trade-off
- **Emergency Integration:** Framework for potential search and rescue system integration

---

## **4. Ethical Considerations**

### **4.1 Human Safety & Privacy**
- System designed exclusively for fire detection and emergency response
- No personal identification, facial recognition, or biometric tracking
- UAV imagery processed only for object detection purposes

### **4.2 Data Usage & Consent**
- Publicly available datasets used (Corsican Fire Dataset, VisDrone)
- No private or personally identifiable data collected
- Academic research compliance maintained throughout

### **4.3 Bias & Fairness**
- Training data includes diverse fire scenarios (indoor/outdoor, day/night)
- Focus on environmental conditions rather than demographic factors
- Regular evaluation to minimize false positives/negatives

### **4.4 Safety-Critical Reliability**
- Confidence thresholds implemented (0.25-0.5 range)
- System serves as decision-support tool only
- Human verification required for critical alerts

### **4.5 Environmental Considerations**
- UAV operations designed to minimize wildlife disruption
- System intended for protective, not invasive, applications

---

## **5. Use of AI & Development Tools**

### **5.1 AI-Assisted Development Tools**
The following AI coding assistants were used during development:

| Tool | Purpose | Extent of Use |
|------|---------|--------------|
| **DeepSeek AI Assistant** | Code generation, debugging, documentation, README creation | Extensive - Used for Python script development, error troubleshooting, and project documentation |
| **ChatGPT (OpenAI)** | Algorithm explanation, research paper summaries, technical concept clarification | Moderate - Used for understanding complex computer vision concepts and model architectures |
| **GitHub Copilot** | Code completion, boilerplate code generation, syntax suggestions | Moderate - Integrated in IDE for faster development |
| **Claude AI** | Ethical framework development, documentation structuring, academic writing | Limited - Used for structuring ethics documentation and academic writing guidance |

### **5.2 AI & Machine Learning Frameworks**
| Framework | Purpose | Version |
|-----------|---------|---------|
| **PyTorch** | Deep learning model development | 2.0+ |
| **Ultralytics YOLOv12** | Object detection implementation | Latest |
| **OpenCV** | Image processing and visualization | 4.8.0+ |
| **TensorRT** | Inference optimization for Jetson | 8.5.0+ |

### **5.3 Hardware & Deployment Tools**
| Tool | Purpose |
|------|---------|
| **NVIDIA Jetson Nano** | Primary edge deployment platform |
| **NVIDIA Jetson Orin** | Secondary testing platform |
| **NVIDIA JetPack SDK** | Operating system and driver package |
| **CUDA** | GPU acceleration for deep learning |

### **5.4 Data & Annotation Tools**
| Tool | Purpose |
|------|---------|
| **LabelImg** | Manual dataset annotation |
| **Roboflow** | Dataset management and augmentation |
| **Albumentations** | Programmatic data augmentation |

---

## **6. Technical Implementation Details**

### **6.1 Detection Methods Implemented**
1. **fire_hybrid.py** - Fast hybrid detection method (30+ FPS on Jetson Orin)
2. **fire_yolo.py** - YOLOv12-based accurate detection (89% mAP, 5-10 FPS)

### **6.2 Model Specifications**
- **Architecture:** YOLOv12 (custom implementation)
- **Classes:** Fire, Smoke (2 classes)
- **Input Resolution:** 640×640
- **Pre-trained Model:** `Smoke Fire.pt` (YOLOv12 weights)

### **6.3 Performance Metrics**
```
Method 1: fire_hybrid.py
├── Jetson Orin: 30+ FPS
├── Jetson Nano: 18 FPS
└── Accuracy: Good for small flames

Method 2: fire_yolo.py (YOLOv12)
├── Jetson Orin: 8-12 FPS
├── Jetson Nano: 5-7 FPS
└── Accuracy: 89% mAP
```

---

## **7. Responsible AI Practices & Transparency**

### **7.1 AI-Assistance Transparency**
- **Code Generation:** Approximately 40% of boilerplate code and utility functions were AI-assisted
- **Documentation:** 60% of README files and documentation were structured with AI assistance
- **Debugging:** AI tools used extensively for error diagnosis and solution generation
- **Learning:** AI tools served as educational resources for understanding complex topics

### **7.2 Human Oversight & Validation**
- All AI-generated code reviewed and validated by team members
- Technical decisions made by human team members based on AI-suggested options
- Final implementations tested and verified independently
- Critical system components developed manually

### **7.3 Academic Integrity Compliance**
- All AI assistance documented transparently
- Original thinking and problem-solving maintained in core algorithms
- Proper citations for referenced code and concepts
- Compliance with university policies on AI tool usage

### **7.4 Development Workflow with AI Tools**
```
1. Problem Analysis → Human
2. Solution Research → AI-Assisted + Human
3. Code Implementation → AI-Generated (reviewed by human)
4. Testing & Debugging → AI-Assisted + Human
5. Documentation → AI-Structured + Human Refined
6. Final Review → Human
```

---

## **8. Limitations & Risk Mitigation**

### **8.1 Technical Limitations**
- **Environmental Factors:** Smoke, lighting, altitude variations
- **Hardware Constraints:** Jetson Nano memory and processing limits
- **Model Complexity:** Trade-off between accuracy and speed

### **8.2 Mitigation Strategies**
- Dual-method approach (fast hybrid + YOLOv12 accurate)
- Confidence threshold tuning (0.25-0.5 range)
- Continuous performance monitoring
- Hardware-specific optimizations (TensorRT)

### **8.3 Ethical Risk Mitigation**
- Clear documentation of AI tool usage
- Human verification for critical detections
- Privacy-by-design implementation
- Academic transparency in all processes

---

## **9. Conclusion**
This project adheres to ethical AI development principles while transparently acknowledging the use of AI-assisted tools. The development process balanced automated assistance with human oversight, ensuring both technical quality and academic integrity. The system prioritizes safety, privacy, and responsible deployment in emergency response scenarios.

---

## **10. AI Tool Usage Declaration**
*This project utilized various AI coding assistants as learning and productivity tools. All final implementations, decisions, and validations were performed by human team members. AI tools served as collaborators in the development process, similar to consulting technical references or documentation. This transparent disclosure ensures academic integrity while acknowledging modern development practices.*

**AI-Assisted Development Percentage:** ~40% of code/documentation  
**Human Oversight & Original Work:** 100% of final decisions and validations  
**Primary AI Framework:** YOLOv12 for object detection  
**Edge Platform:** NVIDIA Jetson Series  

---

**Documentation Version:** 2.1  
**Last Updated:** 17 December 2025  
**Prepared By:** CS-477 Group 06  
**Review Status:** ✅ Approved for Submission
