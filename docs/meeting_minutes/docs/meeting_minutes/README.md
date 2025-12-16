# Minutes of Meeting (MoM)

**Project Title:** Real-Time Multi-Class Detection for UAV Search & Rescue
**Repository:** GitHub (Project Documentation)
**Meeting Type:** Project Kick-off & Planning
**Mode:** In-person / Online
**Date:** 20 November 2025
**Time:** 03:00 PM – 04:00 PM
**Location:** University Lab / Online (Team Coordination)

---

## 1. Attendees

| Name           | Registration No. | Role                     |
| -------------- | ---------------- | ------------------------ |
| Ayesha Hussain | 404215           | Simulation & Algorithms  |
| Arbaaz Alam    | 411425           | Research & Documentation |
| Bushra         | 429427           | Research & Documentation |
| Nayab          | 414017           | Embedded Systems         |

---

## 2. Meeting Objective

The objective of this meeting was to formally initiate the project, define the problem statement, finalize the project scope, assign roles and responsibilities, and agree on the initial technical roadmap for developing a **real-time multi-class detection system for UAV-based search and rescue operations**.

---

## 3. Project Overview

The project aims to design and implement a **real-time multi-class detection system** mounted on a **UAV (Unmanned Aerial Vehicle)** to assist in **search and rescue missions**. The system will be capable of detecting and classifying multiple object categories (e.g., humans, animals, obstacles, fire/smoke) from aerial imagery or video streams using computer vision and machine learning techniques. The solution emphasizes **real-time performance, accuracy, and practical deployment constraints**.

---

## 4. Agenda Items Discussed

* Understanding the problem statement and real-world use case
* Finalizing system architecture (UAV + processing pipeline)
* Selection of detection approach (traditional vs deep learning)
* Dataset requirements and sources
* Simulation and testing environment
* Hardware and embedded system considerations
* Documentation and reporting structure
* Task distribution among group members

---

## 5. Key Discussions & Decisions

### 5.1 Detection Approach

* The team agreed to use **deep learning–based object detection** for multi-class recognition due to better robustness and accuracy in aerial imagery.
* Lightweight models suitable for real-time inference (e.g., YOLO-based architectures) will be explored.

### 5.2 Simulation & Testing

* Initial development and validation will be carried out in a **simulation environment** before hardware deployment.
* Performance metrics such as **accuracy, precision, recall, FPS (frames per second), and latency** will be evaluated.

### 5.3 Embedded & UAV Integration

* Embedded system constraints (processing power, energy efficiency, and onboard deployment) were discussed.
* Possibility of edge computing versus ground-station processing was considered.

### 5.4 Documentation & Research

* Proper research papers, datasets, and benchmarks will be reviewed and cited.
* All progress, experiments, and results will be documented and pushed to GitHub regularly.

---

## 6. Roles & Responsibilities

### Ayesha Hussain – *Simulation & Algorithms*

* Design and implement detection algorithms
* Work on simulation models and algorithm optimization
* Evaluate model performance and tune parameters

### Arbaaz Alam – *Research & Documentation*

* Define problem statement, objectives, and methodology
* Maintain GitHub documentation and reports
* Prepare MoM, progress reports, and final documentation

### Bushra – *Research & Documentation*

* Conduct literature review and dataset research
* Assist in methodology design and result analysis
* Support documentation and presentation preparation

### Nayab – *Embedded Systems*

* Handle UAV and embedded system considerations
* Work on hardware feasibility and integration planning
* Optimize system for real-time and resource constraints

---

## 7. Action Items

| Task                                       | Assigned To    | Deadline         |
| ------------------------------------------ | -------------- | ---------------- |
| Literature review on UAV-based detection   | Bushra         | 20 November 2025 |
| Algorithm selection and simulation setup   | Ayesha Hussain | 20 November 2025 |
| Project documentation & GitHub structuring | Arbaaz Alam    | 20 November 2025 |
| Embedded system feasibility study          | Nayab          | 20 November 2025 |

---

## 8. Risks & Mitigation

* **Real-time performance limitations:** Use lightweight models and optimization techniques.
* **Hardware constraints:** Early consideration of embedded deployment.
* **Dataset mismatch with aerial views:** Use UAV-specific datasets and data augmentation.

---

## 9. Next Meeting

**Tentative Date:** 10 December 2025 (Final Project Submission)
**Agenda:** Review literature findings, finalize model selection, and discuss initial simulation results.

---

**Meeting Adjourned**


