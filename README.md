# 🦅 Eagle-Eye-AI

## End-to-End AI-Powered Video Intelligence Platform

Eagle-Eye-AI is an intelligent real-time video analytics platform designed to analyze CCTV/video streams using Artificial Intelligence and Computer Vision.

The system aims to provide real-time object detection, anomaly detection, intelligent alert generation, and scalable video monitoring capabilities using modern AI engineering technologies.

The project is being developed incrementally, starting with real-time object detection and expanding toward a complete AI surveillance platform.

---

# 🚀 Project Vision

Traditional CCTV systems only record video and require humans to continuously monitor screens.

Eagle-Eye-AI aims to create an intelligent monitoring system that can:

- Detect objects in real-time
- Identify unusual activities
- Analyze video streams automatically
- Generate intelligent alerts
- Provide a real-time monitoring dashboard
- Scale to multiple camera streams

---

# ✨ Features

## Current Features (Phase 1)

✅ Real-time video processing using OpenCV  
✅ YOLO-based object detection  
✅ Detection of objects from video streams  
✅ Bounding box visualization  
✅ Confidence score display  
✅ FPS monitoring for performance analysis  


## Planned Features

### Phase 2 — Custom Object Detection
- Custom YOLO model training
- CCTV-specific object detection
- Improved detection accuracy


### Phase 3 — AI Anomaly Detection
- Autoencoder-based anomaly detection
- Abnormal activity recognition
- Anomaly scoring system


### Phase 4 — AI Decision Engine
- Combine object detection and anomaly detection
- Risk assessment
- Intelligent alert generation


### Phase 5 — Backend System
- FastAPI REST API
- WebSocket real-time communication
- Camera management
- Alert management


### Phase 6 — Frontend Dashboard
- React dashboard
- Live video monitoring
- Real-time alerts
- Analytics visualization


### Phase 7 — Scalable Infrastructure
- Kafka video streaming pipeline
- Redis alert caching
- FFmpeg video processing


### Phase 8 — Production Deployment
- Docker containerization
- NVIDIA Triton inference server
- Model monitoring and optimization

---

# 🏗️ System Architecture

Future architecture:
CCTV / Video Source
|
v
FFmpeg
|
v
Kafka
|
v
AI Processing Pipeline
|
+----+----+
| |
v v
YOLO Autoencoder
| |
+----+----+
|
v
Alert Management
|
+-----+-----+
| |
v v
Redis Database
|
v
FastAPI Backend
|
v
React Dashboard


---

# 🛠️ Technology Stack

## Artificial Intelligence
- Python
- PyTorch
- YOLO
- Autoencoders
- Computer Vision

## Computer Vision
- OpenCV
- FFmpeg

## Backend
- FastAPI
- WebSocket
- REST API

## Frontend
- React
- TypeScript
- Tailwind CSS

## Infrastructure
- Apache Kafka
- Redis
- Docker
- NVIDIA Triton Inference Server

---

# 📂 Project Structure
Eagle-Eye-AI/

│
├── src/
│ ├── detection/
│ ├── video_processing/
│ ├── models/
│ └── utils/
│
├── models/
│
├── screenshots/
│
├── requirements.txt
│
├── README.md
│
└── .gitignore

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/Eagle-Eye-AI.git
Navigate to project:

cd Eagle-Eye-AI
Create Virtual Environment
python -m venv venv

Activate:

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
---
▶️ Usage

Run the application:

python src/main.py

The system will:

Capture video input
Process frames
Run AI detection
Display detected objects
Show confidence scores
---
📸 Demo
Example:
screenshots/
 ├── detection-result.png
 └── realtime-demo.png
---
📊 Current Progress
Component	Status
Video Processing	✅ Completed
YOLO Object Detection	✅ Completed
Custom Model Training	⏳ Planned
Anomaly Detection	⏳ Planned
FastAPI Backend	⏳ Planned
React Dashboard	⏳ Planned
Kafka Pipeline	⏳ Planned
Docker Deployment	⏳ Planned
Triton Serving	⏳ Planned
---
🎯 Learning Goals

This project explores:

Computer Vision
Deep Learning
AI Model Deployment
Real-Time Systems
Backend Engineering
Full-Stack AI Applications
MLOps Concepts
---
🤝 Future Improvements

Possible improvements:

Multiple camera support
Cloud deployment
Mobile notifications
Face recognition integration
Advanced behavior analysis
Model performance monitoring
---
👨‍💻 Author

Dilshan Aishcharya Wijayawardhane

Software Engineering Undergraduate
Interested in AI Engineering, Machine Learning, and Computer Vision.
---

⭐ Acknowledgements

Technologies and frameworks used:

Ultralytics YOLO
OpenCV
PyTorch
FastAPI
React
---
⭐ If you find this project interesting, consider giving it a star!

This README is designed so that:
- **Today:** it correctly represents Phase 1
- **Later:** you only update progress checkboxes
- **For recruiters:** it looks like a planned AI Engineering product, not just a small YOLO demo.
