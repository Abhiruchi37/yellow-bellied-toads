# YOLO Training Results

This folder contains the main results from training the YOLOv8n segmentation model for the combined belly + throat region.

The model was trained for 50 epochs using 80 training images and evaluated using 20 validation images.

## Files

- `results.csv` - contains the training and validation metrics recorded for each epoch.
- `results.png` - shows the development of the main training and validation metrics across the training epochs.
- `confusion_matrix.png` - confusion matrix generated during model evaluation.
- `confusion_matrix_normalized.png` - normalized version of the confusion matrix.
- `MaskF1_curve.png` - F1 score curve for the segmentation mask.
- `MaskPR_curve.png` - precision-recall curve for the segmentation mask.
- `MaskP_curve.png` - precision curve for the segmentation mask.
- `MaskR_curve.png` - recall curve for the segmentation mask.

These results are used to evaluate the performance of the trained belly + throat segmentation model.
