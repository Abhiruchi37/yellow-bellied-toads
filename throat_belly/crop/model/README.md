
# Trained YOLO Model

This folder contains the trained YOLOv8n segmentation model for the combined belly + throat region.

## `best.pt`

`best.pt` is the best model checkpoint obtained during the 50-epoch training process.

This model is used by the prediction and cropping scripts to detect and extract the combined belly + throat region from new images.

The model is applied with a confidence threshold of 0.5 during prediction and crop generation.
