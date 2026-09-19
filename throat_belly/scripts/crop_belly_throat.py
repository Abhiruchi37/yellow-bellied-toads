from ultralytics import YOLO
import cv2
import numpy as np
import os

PROJECT_DIR = r"C:\Users\lawan\Desktop\yellow belly toads\Bappa"

MODEL_PATH = os.path.join(
    PROJECT_DIR,
    "runs",
    "belly_throat_model",
    "weights",
    "best.pt"
)

SOURCE_DIR = os.path.join(
    PROJECT_DIR,
    "test_images"
)

OUTPUT_DIR = os.path.join(
    PROJECT_DIR,
    "outputs",
    "raw_crops"
)

os.makedirs(OUTPUT_DIR, exist_ok=True)

model = YOLO(MODEL_PATH)

image_extensions = (".jpg", ".jpeg", ".png")

for filename in os.listdir(SOURCE_DIR):

    if not filename.lower().endswith(image_extensions):
        continue

    image_path = os.path.join(SOURCE_DIR, filename)

    image = cv2.imread(image_path)

    if image is None:
        print("Could not read:", filename)
        continue

    results = model.predict(
        source=image_path,
        conf=0.5,
        verbose=False
    )

    result = results[0]

    if result.masks is None or len(result.masks.xy) == 0:
        print("NO DETECTION:", filename)
        continue

    # Use detection with highest confidence
    confidences = result.boxes.conf.cpu().numpy()

    best_index = int(np.argmax(confidences))

    polygon = result.masks.xy[best_index]

    polygon = np.array(polygon, dtype=np.int32)

    mask = np.zeros(image.shape[:2], dtype=np.uint8)

    cv2.fillPoly(
        mask,
        [polygon],
        255
    )

    # Keep only belly + throat
    masked_image = cv2.bitwise_and(
        image,
        image,
        mask=mask
    )

    # Find crop boundary
    x, y, w, h = cv2.boundingRect(polygon)

    crop = masked_image[
        y:y+h,
        x:x+w
    ]

    output_path = os.path.join(
        OUTPUT_DIR,
        filename
    )

    cv2.imwrite(output_path, crop)

    print("Saved:", filename)

print("Finished cropping.")