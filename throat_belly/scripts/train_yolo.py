from ultralytics import YOLO

DATA_YAML = r"C:\Users\lawan\Desktop\yellow belly toads\Bappa\dataset_yolo\data.yaml"

model = YOLO("yolov8n-seg.pt")

model.train(
    data=DATA_YAML,
    epochs=50,
    imgsz=640,
    batch=8,
    project=r"C:\Users\lawan\Desktop\yellow belly toads\Bappa\runs",
    name="belly_throat_model"
)