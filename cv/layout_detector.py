from ultralytics import YOLO

_model = None

def get_model():
    global _model
    if _model is None:
        _model = YOLO("yolov8n.pt")
    return _model

def detect_layout(image):
    model = get_model()
    results = model(image)
    elements = []

    for r in results:
        for box in r.boxes:
            elements.append({
                "bbox": box.xyxy.tolist(),
                "confidence": float(box.conf),
                "class": int(box.cls)
            })
    return elements
