from ultralytics import YOLO
import gradio as gr  # Fixed line

import numpy as np
from collections import Counter

# Define available models
MODEL_OPTIONS = {
    "YOLOv8n (nano)": "yolov8n.pt",
    "YOLOv8s (small)": "yolov8s.pt",
    "YOLOv8m (medium)": "yolov8m.pt",
    "YOLOv8l (large)": "yolov8l.pt",
    "YOLOv8x (extra-large)": "yolov8x.pt"
}

# Load model based on user selection
def load_model(model_name):
    model_path = MODEL_OPTIONS[model_name]
    return YOLO(model_path)

# Define object detection function
def detect_objects(image, model_name):
    # Load the selected model
    model = load_model(model_name)

    # Convert image from PIL format (used by Gradio) to NumPy format
    image_np = np.array(image)

    # Perform object detection
    results = model(image_np)
    detections = results[0]

    # Retrieve bounding box and label information
    boxes = detections.boxes
    labels = [model.names[int(box.cls)] for box in boxes]

    # Count detected objects
    object_counts = Counter(labels)
    object_counts_text = "\n".join([f"{obj} - {count}" for obj, count in object_counts.items()])

    # Draw bounding boxes on the detected objects
    result_image = detections.plot()  # Annotated image with bounding boxes and labels

    return result_image, object_counts_text

# Create Gradio interface with model selection
iface = gr.Interface(
    fn=detect_objects,
    inputs=[
        gr.Image(type="pil"),
        gr.Dropdown(
            choices=list(MODEL_OPTIONS.keys()),
            label="Select YOLO Model",
            value="YOLOv8n (nano)"  # Default model
        )
    ],
    outputs=[gr.Image(type="pil"), gr.Textbox()],
    title="Real-Time Object Detection with YOLOv8",
    description="Upload an image, select a YOLO model, and detect objects."
)

# Launch the interface
iface.launch()
