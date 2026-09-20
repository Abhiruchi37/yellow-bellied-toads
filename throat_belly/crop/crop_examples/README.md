# Belly + Throat Crop Examples

This folder contains selected examples of the combined belly + throat regions extracted using the trained YOLO segmentation model.

For each image, the segmentation mask predicted by YOLO was used to keep the detected belly + throat region. The detected region was then cropped to its bounding rectangle.

The filenames correspond to the prediction examples available in the `../prediction_examples/` folder.

These crops represent the output of the YOLO cropping stage before the SuperPoint + LightGlue identification stage.
