from ultralytics import YOLO
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
    "runs"
)

model = YOLO(MODEL_PATH)

model.predict(
    source=SOURCE_DIR,
    conf=0.5,
    save=True,
    project=OUTPUT_DIR,
    name="belly_throat_predictions"
)

print("Prediction completed")