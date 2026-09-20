import os
import cv2
import random

PROJECT_DIR = r"C:\Users\lawan\Desktop\yellow belly toads\Bappa"

IMAGE_DIR = os.path.join(PROJECT_DIR, "dataset_yolo", "images", "train")
LABEL_DIR = os.path.join(PROJECT_DIR, "dataset_yolo", "labels", "train")

OUTPUT_DIR = os.path.join(PROJECT_DIR, "outputs", "label_check")
os.makedirs(OUTPUT_DIR, exist_ok=True)

image_files = [
    f for f in os.listdir(IMAGE_DIR)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
]

random.seed(42)
sample_files = random.sample(image_files, min(10, len(image_files)))

for image_file in sample_files:

    image_path = os.path.join(IMAGE_DIR, image_file)
    image = cv2.imread(image_path)

    h, w = image.shape[:2]

    label_file = os.path.splitext(image_file)[0] + ".txt"
    label_path = os.path.join(LABEL_DIR, label_file)

    if not os.path.exists(label_path):
        print("Missing label:", image_file)
        continue

    with open(label_path, "r") as f:
        lines = f.readlines()

    for line in lines:

        parts = line.strip().split()

        if len(parts) < 7:
            continue

        coords = list(map(float, parts[1:]))

        points = []

        for i in range(0, len(coords), 2):

            x = int(coords[i] * w)
            y = int(coords[i + 1] * h)

            points.append([x, y])

        import numpy as np

        pts = np.array(points, dtype=np.int32)

        cv2.polylines(
            image,
            [pts],
            isClosed=True,
            color=(0, 255, 0),
            thickness=3
        )

    output_path = os.path.join(OUTPUT_DIR, image_file)

    cv2.imwrite(output_path, image)

    print("Saved:", output_path)

print("Done")