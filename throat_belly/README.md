# Throat + Belly Photo-Identification Pipeline

## Overview

This folder contains the combined **throat + belly photo-identification workflow** for the Yellow-Bellied Toad project.

The workflow uses the combined ventral belly + throat region for individual identification. It includes manual annotation, YOLO segmentation, crop generation, feature matching using SuperPoint + LightGlue, and comparison with Wild-ID.

## Workflow

The complete workflow is:

**Original Images → LabelMe Annotation → YOLO Segmentation Dataset → YOLOv8 Segmentation → Belly + Throat Crops → SuperPoint + LightGlue Matching → Candidate Matches → Manual Verification**

Wild-ID was additionally used as a comparison method using the cropped belly + throat images.

## Project Structure

```text
throat_belly/
├── crop/
│   ├── model/
│   │   ├── README.md
│   │   └── best.pt
│   │
│   ├── training_results/
│   │   ├── README.md
│   │   ├── results.csv
│   │   ├── results.png
│   │   ├── confusion_matrix.png
│   │   ├── confusion_matrix_normalized.png
│   │   ├── MaskF1_curve.png
│   │   ├── MaskPR_curve.png
│   │   ├── MaskP_curve.png
│   │   └── MaskR_curve.png
│   │
│   ├── prediction_examples/
│   │   ├── README.md
│   │   └── selected prediction images
│   │
│   ├── crop_examples/
│   │   ├── README.md
│   │   └── selected belly + throat crops
│   │
│   ├── data.yaml
│   └── README.md
│
├── data/
│   ├── labelme_annotations/
│   │   ├── README.md
│   │   └── LabelMe JSON annotations
│   │
│   ├── yolo_labels/
│   │   ├── train/
│   │   ├── val/
│   │   └── README.md
│   │
│   └── README.md
│
├── identification/
│   ├── results/
│   │   ├── README.md
│   │   ├── all_pair_scores.csv
│   │   ├── top5_candidates.csv
│   │   └── manual_verification.csv
│   │
│   ├── wild_id/
│   │   ├── README.md
│   │   └── confirmed-matches.txt
│   │
│   └── README.md
│
├── scripts/
│   ├── convert_labelme_yolo.py
│   ├── check_yolo_labels.py
│   ├── train_yolo.py
│   ├── predict_yolo.py
│   ├── crop_belly_throat.py
│   ├── crop_identification_images.py
│   ├── Belly_Throat_SuperPoint_LightGlue_Identification.ipynb
│   └── README.md
│
└── README.md
```

## 1. Annotation and Dataset Preparation

A total of **100 images** were manually annotated using LabelMe.

For each image, the combined belly + throat region was marked using a polygon annotation with the class:

```text
belly_throat
```

The original LabelMe annotations are stored in:

```text
data/labelme_annotations/
```

The LabelMe annotations were converted into YOLO segmentation format using:

```text
scripts/convert_labelme_yolo.py
```

The dataset was divided into:

- **80 training images**
- **20 validation images**

A fixed random seed of **42** was used for the train/validation split.

The converted YOLO segmentation labels are available in:

```text
data/yolo_labels/
```

The complete original image dataset is not duplicated in this repository.

## 2. YOLO Segmentation

A **YOLOv8n segmentation model** was trained to detect the combined belly + throat region.

The main training configuration was:

| Parameter | Value |
|---|---|
| Model | YOLOv8n segmentation |
| Segmentation class | `belly_throat` |
| Epochs | 50 |
| Image size | 640 |
| Batch size | 8 |
| Training images | 80 |
| Validation images | 20 |

The dataset configuration is available at:

```text
crop/data.yaml
```

The best model checkpoint obtained during training is stored at:

```text
crop/model/best.pt
```

The main training outputs, including training metrics, confusion matrices and segmentation-mask evaluation curves, are available in:

```text
crop/training_results/
```

## 3. Prediction and Crop Generation

The trained YOLO segmentation model was applied to test images and identification images.

A confidence threshold of:

```text
0.5
```

was used during prediction and crop generation.

For each image, the detection with the highest confidence was selected.

The predicted segmentation mask was used to retain the combined belly + throat region. The detected region was then cropped to the bounding rectangle of the segmentation mask.

The crop-generation scripts are:

```text
scripts/crop_belly_throat.py
scripts/crop_identification_images.py
```

Selected YOLO prediction examples are available in:

```text
crop/prediction_examples/
```

The corresponding selected cropped regions are available in:

```text
crop/crop_examples/
```

The complete set of generated identification crops is not duplicated in this repository.

## 4. SuperPoint + LightGlue Identification

The generated belly + throat crops were used for individual photo-identification.

The identification method uses:

- **SuperPoint** for keypoint detection and local feature extraction.
- **LightGlue** for matching SuperPoint features between image pairs.

The identification dataset contained **200 cropped images**.

All unique pairs of the 200 images were compared:

```text
200 × 199 / 2 = 19,900 unique image pairs
```

For each image pair, a combined matching score was calculated as:

```text
Combined Score = Number of Matches × Average Match Confidence
```

This score combines the number of matched local features with the average confidence of the feature matches.

The SuperPoint + LightGlue identification workflow is implemented in:

```text
scripts/Belly_Throat_SuperPoint_LightGlue_Identification.ipynb
```

### Identification Results

The main identification result files are stored in:

```text
identification/results/
```

The files include:

- `all_pair_scores.csv` – pairwise matching results for the 19,900 unique image pairs.
- `top5_candidates.csv` – top candidate matches obtained from the pairwise matching results.
- `manual_verification.csv` – results used for manual verification of the generated candidate matches.

Additional details are available in:

```text
identification/results/README.md
```

## 5. Wild-ID Comparison

Wild-ID was used as an additional photo-identification method for comparison with the SuperPoint + LightGlue approach.

The belly + throat crops generated during the segmentation and cropping stage were used as input to Wild-ID.

Wild-ID calculates similarity scores between images and presents candidate matches for manual verification.

The retained Wild-ID result is stored in:

```text
identification/wild_id/confirmed-matches.txt
```

Additional information about the Wild-ID output is available in:

```text
identification/wild_id/README.md
```

The Wild-ID application, internal binary database files, logs and complete duplicate set of cropped input images are not included in this repository.

## 6. Scripts

The scripts required for the combined throat + belly workflow are located in:

```text
scripts/
```

### `convert_labelme_yolo.py`

Converts the manually created LabelMe polygon annotations into YOLO segmentation format and creates the training and validation split.

### `check_yolo_labels.py`

Used to inspect and verify the converted YOLO segmentation labels.

### `train_yolo.py`

Trains the YOLOv8n segmentation model for the combined belly + throat region.

### `predict_yolo.py`

Runs the trained segmentation model on test images.

### `crop_belly_throat.py`

Uses the predicted segmentation masks to generate belly + throat crops from the test images.

### `crop_identification_images.py`

Applies the trained segmentation model to the identification image dataset and generates the crops used for photo-identification.

### `Belly_Throat_SuperPoint_LightGlue_Identification.ipynb`

Performs the SuperPoint + LightGlue feature extraction, pairwise matching and candidate generation for individual identification.

More information about the scripts is available in:

```text
scripts/README.md
```

## Repository Data

The repository contains the main files used to document the combined throat + belly workflow, including:
- original LabelMe annotation files
- converted YOLO segmentation labels
- YOLO dataset configuration
- trained YOLO model
- main YOLO training results
- selected prediction examples
- selected crop examples
- SuperPoint + LightGlue identification code
- pairwise identification results
- candidate matching results
- manual verification results
- retained Wild-ID comparison result

The following large or duplicate files are intentionally not included:

- complete original image dataset
- duplicate YOLO training and validation images
- complete test image dataset
- complete identification image dataset
- complete generated identification crop dataset
- Wild-ID application files
- Wild-ID internal binary database files
- Wild-ID logs
