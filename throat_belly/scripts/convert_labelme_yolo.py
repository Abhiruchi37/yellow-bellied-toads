import os
import json
import random
import shutil

PROJECT_DIR = r"C:\Users\lawan\Desktop\yellow belly toads\Bappa"

SOURCE_DIR = os.path.join(PROJECT_DIR, "original_images")
YOLO_DIR = os.path.join(PROJECT_DIR, "dataset_yolo")

TRAIN_RATIO = 0.8
SEED = 42

random.seed(SEED)

train_images_dir = os.path.join(YOLO_DIR, "images", "train")
val_images_dir = os.path.join(YOLO_DIR, "images", "val")

train_labels_dir = os.path.join(YOLO_DIR, "labels", "train")
val_labels_dir = os.path.join(YOLO_DIR, "labels", "val")

for folder in [
    train_images_dir,
    val_images_dir,
    train_labels_dir,
    val_labels_dir
]:
    os.makedirs(folder, exist_ok=True)

json_files = [
    f for f in os.listdir(SOURCE_DIR)
    if f.lower().endswith(".json")
]

random.shuffle(json_files)

split_index = int(len(json_files) * TRAIN_RATIO)

train_files = json_files[:split_index]
val_files = json_files[split_index:]


def convert_file(json_file, split):

    json_path = os.path.join(SOURCE_DIR, json_file)

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    image_height = data["imageHeight"]
    image_width = data["imageWidth"]

    image_filename = data["imagePath"]
    image_filename = os.path.basename(image_filename)

    image_path = os.path.join(SOURCE_DIR, image_filename)

    if split == "train":
        dest_image_dir = train_images_dir
        dest_label_dir = train_labels_dir
    else:
        dest_image_dir = val_images_dir
        dest_label_dir = val_labels_dir

    shutil.copy2(
        image_path,
        os.path.join(dest_image_dir, image_filename)
    )

    txt_filename = os.path.splitext(image_filename)[0] + ".txt"

    txt_path = os.path.join(dest_label_dir, txt_filename)

    with open(txt_path, "w") as txt_file:

        for shape in data["shapes"]:

            if shape["label"] != "belly_throat":
                continue

            points = shape["points"]

            yolo_points = []

            for x, y in points:

                x_norm = x / image_width
                y_norm = y / image_height

                yolo_points.append(f"{x_norm:.6f}")
                yolo_points.append(f"{y_norm:.6f}")

            line = "0 " + " ".join(yolo_points)

            txt_file.write(line + "\n")


for f in train_files:
    convert_file(f, "train")

for f in val_files:
    convert_file(f, "val")


print("Conversion completed")
print("Total images:", len(json_files))
print("Training images:", len(train_files))
print("Validation images:", len(val_files))