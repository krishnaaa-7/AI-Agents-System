import cv2

def crop_regions(image_path, regions):
    """
    regions = [
      {"label": "TABLE", "bbox": [x1, y1, x2, y2]}
    ]
    """
    img = cv2.imread(image_path)
    crops = []

    for i, r in enumerate(regions):
        x1, y1, x2, y2 = r["bbox"]
        crop = img[y1:y2, x1:x2]
        crop_path = f"outputs/crop_{i}.png"
        cv2.imwrite(crop_path, crop)
        crops.append({
            "label": r["label"],
            "path": crop_path
        })

    return crops
