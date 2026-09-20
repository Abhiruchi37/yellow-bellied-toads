# LabelMe Annotations

This folder contains the original LabelMe annotation files created manually for the combined belly + throat region.

A total of 100 images were annotated using polygon annotations.

Each JSON file stores the manually marked polygon coordinates for the `belly_throat` region together with the image information required by LabelMe.

These annotations were converted into YOLO segmentation format using `convert_labelme_yolo.py`.

The converted YOLO labels are available in the `../yolo_labels/` folder.

The corresponding original image files are not duplicated in this repository.
