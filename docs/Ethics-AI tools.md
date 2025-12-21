# Ethics & AI Tool Documentation

## Project Title

**Real-time Fire, Human, and Animal Detection using UAV Imagery**

---

## Team Members

| Name           | CMS ID | Role                     |
| -------------- | ------ | ------------------------ |
| Ayesha Hussain | 404215 | Simulation & Algorithms  |
| Arbaaz Alam    | 411425 | Research & Documentation |
| Bushra         | 429427 | Research & Documentation |
| Nayab          | 414017 | Embedded Systems         |

---

## 1. Project Overview

This project focuses on the development of a **real-time, multi-class detection system** using UAV imagery to identify **fire, humans, and animals** during search and rescue operations. The system extends our previous work on **FireLite-Seg**, a lightweight fire segmentation model that achieved **96.85% accuracy** and **11.6 FPS on Jetson Nano**, by integrating additional detection classes to enhance situational awareness in emergency scenarios.

The solution aims to assist rescue teams by providing timely alerts, reducing response time, and improving decision-making in disaster-prone environments.

---

## 2. Previous Work Summary

The following components from prior research were reused and extended:

* **FireLite-Seg:** Lightweight fire segmentation model
* **Corsican Fire Dataset:** Dataset preprocessing and augmentation
* **Edge Deployment:** Jetson Nano deployment pipeline
* **Evaluation Metrics:** IoU (96.32%), Dice Score (97.45%), FPS analysis

---

## 3. New Objectives

* **Multi-Class Detection:** Simultaneous detection of fire, humans, and animals
* **Real-Time Performance:** Target inference speed of **15–25 FPS** on Jetson Nano
* **Search & Rescue Integration:** Automated alert generation for emergency response teams

---

## 4. Ethical Considerations

### 4.1 Human Safety & Privacy

* The system is designed strictly for **search and rescue operations**, not for surveillance or personal tracking.
* No personal identity recognition (face recognition or biometric identification) is performed.
* UAV imagery is processed solely for object detection and emergency response purposes.

### 4.2 Data Usage & Consent

* Publicly available and research-approved datasets are used.
* No private or personally identifiable datasets are included.
* Data collection aligns with ethical research standards and academic guidelines.

### 4.3 Bias & Fairness

* Training data includes diverse environmental conditions to reduce detection bias.
* The system avoids demographic profiling and focuses only on object presence.
* Continuous evaluation is planned to minimize false positives or missed detections.

### 4.4 Safety-Critical Reliability

* False detections could impact rescue decisions; therefore, confidence thresholds and validation checks are implemented.
* The system is intended as a **decision-support tool**, not a replacement for human judgment.

### 4.5 Environmental & Animal Welfare

* UAV operations are planned to minimize disturbance to wildlife.
* Animal detection is used for rescue and protection, not tracking or exploitation.

---

## 5. Use of AI Tools

### 5.1 AI & Machine Learning Frameworks

The following AI tools and frameworks were used during development:

* **Python** for implementation
* **PyTorch / TensorFlow** for deep learning model development
* **YOLO-based architectures** for multi-class object detection
* **OpenCV** for image processing and visualization

### 5.2 Hardware Acceleration Tools

* **NVIDIA Jetson Nano** for edge deployment
* **CUDA & TensorRT** (where applicable) for inference optimization

### 5.3 Data Processing Tools

* Data augmentation libraries to improve generalization
* Annotation tools for dataset labeling

---

## 6. Responsible AI Practices

* Model decisions are logged and evaluated using standard metrics.
* No autonomous lethal or harmful actions are triggered by the system.
* Alerts generated are advisory and require human verification.
* The system follows transparency, accountability, and safety principles.

---

## 7. Limitations & Risk Mitigation

* **Environmental Variability:** Smoke, lighting, and altitude may affect accuracy.
* **Hardware Constraints:** Jetson Nano limits model complexity.
* **Mitigation:** Use of lightweight models, continuous testing, and threshold tuning.

---

## 8. Conclusion

This project adheres to ethical AI development principles by prioritizing **human safety, privacy, fairness, and responsible deployment**. The use of AI tools is transparent, limited to research and rescue purposes, and aligned with academic and societal standards.

---



