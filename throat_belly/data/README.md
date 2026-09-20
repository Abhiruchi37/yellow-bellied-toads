# Data

This folder documents the image datasets used for the combined belly + throat segmentation and identification workflow.

## Original Annotated Dataset

A total of 100 images were manually annotated using LabelMe.

Each image contains a polygon annotation for the combined belly + throat region.

The LabelMe annotations were later converted into YOLO segmentation format using `convert_labelme_yolo.py`.

## YOLO Dataset

The 100 annotated images were divided into:

- 80 training images
- 20 validation images

The split was created using a fixed random seed of 42.

The YOLO dataset contains corresponding image and segmentation label folders for training and validation.

The YOLO dataset configuration is available in `../crop/data.yaml`.

## Test Images

A separate set of 20 images was used to test the trained YOLO segmentation model and generate belly + throat crops.

Selected prediction and crop examples are available in the `../crop/` folder.

## Identification Images

A set of 200 images was used for the identification experiment.

The trained YOLO model was applied to these images to extract the combined belly + throat region.

The resulting crops were used as input for the SuperPoint + LightGlue identification stage.

## Note

The complete image datasets are not duplicated in this GitHub repository. This folder documents the datasets and their use in the project.
