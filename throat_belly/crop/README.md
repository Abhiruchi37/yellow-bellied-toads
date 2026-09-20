# Crop and YOLO Segmentation

This folder contains the files and results from the YOLO segmentation and crop generation stage for the combined belly + throat region.

## Workflow

1. The combined belly + throat region was manually annotated as a polygon using LabelMe.
2. `convert_labelme_yolo.py` converted the LabelMe annotations into YOLO segmentation format.
3. The final annotated dataset contained 100 images.
4. The dataset was divided into 80 training images and 20 validation images using a random seed of 42.
5. A YOLOv8n segmentation model was trained for 50 epochs with an image size of 640 and batch size of 8.
6. The trained model was applied to test and identification images using a confidence threshold of 0.5.
7. For each image, the detection with the highest confidence was selected.
8. The segmentation mask was used to keep only the combined belly + throat region.
9. The detected region was cropped and saved as a new image.
10. These cropped images were later used for the identification stage.

## Files and Folders

### `data.yaml`

Contains the YOLO dataset configuration for the `belly_throat` segmentation class.

### `model/`

Contains the trained YOLO model used for prediction and cropping.

- `best.pt` - best model checkpoint obtained during training.

### `training_results/`

Contains the main results produced during YOLO training, including the training metrics, confusion matrices and mask evaluation curves.

### `prediction_examples/`

Contains selected examples of YOLO predictions on test images.

### `crop_examples/`

Contains the corresponding belly + throat crops produced from the YOLO segmentation masks.

## Dataset

The complete original image dataset, LabelMe annotations and YOLO training and validation dataset are not duplicated in this folder. They are handled separately as project data.

## Related Scripts

The scripts used for this stage are available in the `../scripts/` folder:

- `convert_labelme_yolo.py`
- `check_yolo_labels.py`
- `train_yolo.py`
- `predict_yolo.py`
- `crop_belly_throat.py`
- `crop_identification_images.py`
