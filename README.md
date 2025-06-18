Object Detection with YOLOv8 and Gradio





📌 Project Overview
This project implements real-time object detection using Ultralytics' YOLOv8 models, integrated into a simple Gradio web interface. The goal is to detect and label objects in images using various YOLOv8 model variants, providing users with annotated results and object count summaries. This solution is suitable for tasks such as surveillance, visual inspection, and automated labeling.

📊 Dataset
This project does not rely on a fixed dataset. Instead, it allows users to upload custom images for object detection. The models used have been pre-trained on the COCO dataset, which includes a wide range of object classes such as:

Person

Car

Animal

Electronics

Furniture
...and many more (80+ categories).

🧹 Data Handling
Since the app works on uploaded images, no preprocessing or cleaning of static data is required. However, the uploaded image is:

Converted into NumPy format for model processing.

Normalized and resized internally by the YOLOv8 model.








🧠 Steps Involved
1. Model Selection:
Users can select from multiple pre-trained YOLOv8 models:

YOLOv8n (Nano)

YOLOv8s (Small)

YOLOv8m (Medium)

YOLOv8l (Large)

YOLOv8x (Extra Large)



2. Image Upload:
Users upload any image via the Gradio interface.



3. Object Detection:
YOLOv8 processes the image.

Detected objects are labeled and highlighted using bounding boxes.

Detected classes are counted and displayed in summary.



4. Visualization:
The output image contains drawn bounding boxes with labels.

A textbox displays a count of each detected object class.

🖼️ Inference Output
Each detection results in:

Annotated Image – Bounding boxes and labels drawn on original input.

Object Count Summary – Text summary listing object types and counts.






⚙️ How to Run the Code
Clone the repository:
bash
Copy
Edit
git clone <repo_url>
cd <repo_folder>
Install the required libraries:
bash
Copy
Edit
pip install ultralytics gradio numpy
Run the Python script:
bash
Copy
Edit
python object_detection_app.py
Replace object_detection_app.py with your actual file name.



🧩 Dependencies
Python 3.x

Ultralytics

Gradio

NumPy



📊 Visualizations
Annotated images with bounding boxes and labels.

Object count displayed alongside the result image.




📄 License
This project is licensed under the MIT License – see the LICENSE file for details.

