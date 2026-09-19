# Scripts

This folder contains the Python scripts used for the combined throat and belly segmentation and re-identification pipeline.

## Pipeline

The main workflow is:

1. Convert the manually created LabelMe annotations into YOLO segmentation format.
2. Check the converted YOLO labels visually.
3. Train the YOLO segmentation model for the combined throat and belly region.
4. Run the trained YOLO model on new images.
5. Extract the detected throat and belly regions as colour crops.
6. Use the extracted crops for re-identification with SuperPoint + LightGlue.

## Scripts

### `convert_labelme_yolo.py`

Converts the manually created LabelMe polygon annotations into YOLO segmentation format for model training.

### `check_yolo_labels.py`

Visualizes the converted YOLO labels on the images so that the annotations can be checked before training.

### `train_yolo.py`

Trains the YOLO segmentation model using the prepared throat and belly dataset.

The final dataset contained 100 manually annotated images, divided into 80 training images and 20 validation images.

### `predict_yolo.py`

Runs the trained YOLO segmentation model on images and generates predictions for the combined throat and belly region.

### `crop_belly_throat.py`

Uses the YOLO segmentation results to extract the combined throat and belly region from the original images.

### `crop_identification_images.py`

Applies the trained model to the images used for the identification experiment and saves the extracted throat and belly crops.

## Re-identification

The extracted colour crops were used for the re-identification stage with SuperPoint + LightGlue.

SuperPoint detects local image features, while LightGlue matches the detected features between pairs of images.

For the final set of 200 cropped images, all unique image pairs were compared:

200 × 199 / 2 = 19,900 image pairs.

The candidate ranking was based on:

Combined Score = Number of Matches × Average Matching Confidence

The final SuperPoint + LightGlue script is also included in this folder.

## Note

RANSAC is not part of the final implemented re-identification pipeline. It is considered only as a possible extension for future work.
