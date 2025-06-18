# 🎯 Object Detection with YOLOv8 and Gradio

## 📌 Project Overview

This project implements real-time object detection using **Ultralytics' YOLOv8** models, integrated into a simple **Gradio web interface**.  
It detects and labels objects in uploaded images using various YOLOv8 model variants and returns both annotated images and object count summaries.

✅ Ideal for:
- Surveillance  
- Visual inspection  
- Automated labeling tasks

---

## 📊 Dataset

This app does **not rely on a fixed dataset**. Instead, users can upload custom images.

All YOLOv8 models used here are pre-trained on the **COCO dataset**, which includes 80+ object categories such as:

- Person  
- Car  
- Animal  
- Electronics  
- Furniture  
- ...and many more

---

## 🧹 Data Handling

Since the app accepts user-uploaded images:
- Images are converted into **NumPy arrays**.
- Internally normalized and resized by the YOLOv8 model.
- No manual preprocessing required.

---

## 🧠 Steps Involved

### 1. Model Selection
Users can choose from these pre-trained YOLOv8 variants:
- YOLOv8n (Nano)
- YOLOv8s (Small)
- YOLOv8m (Medium)
- YOLOv8l (Large)
- YOLOv8x (Extra Large)

### 2. Image Upload
Upload any image through the Gradio interface.

### 3. Object Detection
- Image is processed by the selected YOLO model.
- Detected objects are shown with bounding boxes and class labels.
- Object classes are counted and summarized.

### 4. Visualization
- Output includes an annotated image.
- A textbox displays object count summary.

---

## 🖼️ Inference Output

Each detection produces:
- **✅ Annotated Image** — Bounding boxes with class labels
- **✅ Object Count Summary** — Text summary listing object types and quantities

---

## ⚙️ How to Run the Code

### 1. Clone the repository

```bash
git clone <your_repo_url>
cd <your_repo_folder>
2. Install dependencies
bash
Copy
Edit
pip install ultralytics gradio numpy
3. Run the application
bash
Copy
Edit
python object_detection_app.py
Replace object_detection_app.py with your actual filename.

🧩 Dependencies
Python 3.x

Ultralytics

Gradio

NumPy

📊 Visualizations
Annotated images with labeled bounding boxes

Text summary of detected objects displayed beside the image

📄 License
This project is licensed under the MIT License
