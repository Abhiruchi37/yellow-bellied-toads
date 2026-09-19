# Belly Segmentation Model Evaluation

This folder contains the datasets, trained model weights, and validation outputs for the two YOLO segmentation models developed for belly-region detection and extraction.

The segmentation stage was developed in two steps: an initial model trained on manually annotated images, followed by a final model trained using the expanded labelled dataset.

## Folder Contents

### First Model

The `first_model/` folder contains the files associated with the initial YOLO segmentation model.

The initial dataset was created from 100 manually annotated images selected from the A and H pond datasets. The images were annotated in CVAT using polygon masks around the belly region.

The initial model was trained using:

- 80 training images
- 20 validation images
- YOLO segmentation
- 100 epochs
- Image size: 640
- Batch size: 8

The validation results for the first model include training and validation plots, prediction examples, and segmentation metrics.

The best-performing trained model is stored as:

`best.pt`

### Final Model

The `final_model/` folder contains the files associated with the final belly segmentation model.

The initial model was used to generate labels for the remaining images. After combining the manually annotated images with the successfully generated labels, the final labelled dataset contained 341 image-label pairs.

The final dataset was divided into:

- 271 training images
- 70 validation images

The final model was then trained using the expanded dataset.

The best-performing trained model is stored as:

`best.pt`

## Final Model Performance

The final YOLO segmentation model achieved the following validation results:

| Metric | Result |
|---|---:|
| Mask Precision | 0.9849 |
| Mask Recall | 0.9330 |
| Mask mAP@0.5 | 0.9883 |
| Mask mAP@0.5:0.95 | 0.8475 |
| Box Precision | 0.9849 |
| Box Recall | 0.9330 |
| Box mAP@0.5 | 0.9883 |
| Box mAP@0.5:0.95 | 0.8331 |

The final model was subsequently used to extract belly regions from the A-pond dataset. It successfully produced belly crops for 192 of the 199 images.

## Validation Outputs

The validation folders may contain outputs generated during YOLO training and evaluation, including:

- Precision-recall curves
- Precision curves
- Recall curves
- F1-confidence curves
- Confusion matrices
- Validation labels
- Validation predictions
- Training metrics and plots

These files are retained to document and compare the performance of the initial and final segmentation models.

## Model Weights

The `best.pt` files contain the best-performing YOLO model weights selected during training.

The final model weight is the checkpoint used for the production belly-extraction stage of the pipeline.


## Related Files

The complete belly segmentation and re-identification workflow is available in:

`../belly_pipeline.ipynb`

The original image dataset is stored externally in Google Drive because of its size.
