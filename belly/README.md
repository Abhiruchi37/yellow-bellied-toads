# Belly-Only Pipeline

## Overview

This part of the project investigates whether the ventral belly pattern of Yellow-Bellied Toads can be used for individual photo-identification.

The belly contribution has two main stages:

1. **YOLO segmentation and belly crop extraction**
2. **Re-identification using the extracted belly crops**

The final re-identification experiments compared BioCLIP 2, ALIKED + MNN + RANSAC, MiewID-msv3, and Wild-ID.

## 1. Dataset Preparation

The belly dataset contained **349 original photographs**:

| Source | Images |
|---|---:|
| A pond | 199 |
| H pond | 150 |
| **Total** | **349** |

A bootstrap subset of **100 images** was manually annotated in CVAT using polygon masks:

- 50 A-pond images
- 50 H-pond images

The 100 manually labelled image-mask pairs were divided into **80 training** and **20 validation** images for the initial segmentation model.

## 2. Initial YOLO Segmentation Model

A pretrained **YOLO26n segmentation model** was fine-tuned for one class:

```text
toad_belly
```

Training settings included:

- image size: 640
- batch size: 8
- maximum epochs: 100
- early-stopping patience: 20
- GPU execution

Initial mask results:

| Metric | Initial model |
|---|---:|
| Mask Precision | 0.9029 |
| Mask Recall | 0.9303 |
| Mask mAP@0.5 | 0.9793 |
| Mask mAP@0.5:0.95 | 0.7822 |

## 3. Assisted Labelling and Final Dataset

The first YOLO model was applied to the remaining **249 photographs**.

- Successful automatic labels: **241**
- No detection: **8**

The 100 manually annotated pairs and 241 automatically generated pairs produced **341 labelled image-mask pairs**.

The final dataset was shuffled using a fixed random seed and divided into:

- **271 training pairs**
- **70 validation pairs**

The 241 generated labels are therefore treated as **pseudo-labels** in this workflow.

## 4. Final Belly Segmentation Model

The final segmentation model was initialized from the best checkpoint of the initial belly model and trained using the expanded dataset.

Final validation results:

| Metric | Final model |
|---|---:|
| Mask Precision | 0.9849 |
| Mask Recall | 0.9330 |
| Mask mAP@0.5 | 0.9883 |
| Mask mAP@0.5:0.95 | 0.8475 |
| Box mAP@0.5:0.95 | 0.8331 |

The value **0.9883 is a segmentation mAP@0.5 metric**, not individual-identification accuracy.

## 5. Production Belly Extraction

The final model was applied to all **199 A-pond photographs**.

For successful predictions, the highest-confidence segmentation mask was resized to the original image dimensions and thresholded. A tight crop was created around the mask with 3% padding. Pixels outside the belly polygon were removed, producing a belly-only JPG/JPEG crop while preserving the original colour and orientation.

Production results:

| Outcome | Count | Percentage |
|---|---:|---:|
| Successful belly crops | 192 | 96.48% |
| No detection | 7 | 3.52% |
| **Total** | **199** | **100%** |

The resulting **192 belly crops** formed the gallery for the re-identification experiments.

## 6. Re-Identification Experiments

### BioCLIP 2

BioCLIP 2 was evaluated as a pretrained biological image representation without species-specific fine-tuning. Each crop was represented by a **768-dimensional normalized embedding**, and cosine similarity was used for retrieval.

### ALIKED + MNN + RANSAC

ALIKED local features were extracted from the belly crops. Candidate correspondences were obtained using mutual nearest-neighbour matching and checked for geometric consistency using RANSAC.

The resulting score was used for **candidate ranking only** and was not interpreted as a probability of biological identity.

### MiewID-msv3

MiewID-msv3 was evaluated as the learned animal re-identification model. Each crop was resized to 440 × 440 pixels and converted to a **2,152-dimensional normalized embedding**.

Cosine similarity was used to rank the other belly photographs for each query. The twenty highest-ranked candidates were retained.

### Wild-ID

Wild-ID was retained as the established semi-automated photo-identification baseline. Its candidate lists were manually reviewed to confirm reference matches.

## 7. Candidate-Ranking Results

All methods were compared using the same **62 manually confirmed Wild-ID reference pairs**.

| Method | Rank-1 | Top-3 | Top-5 | Top-10 | Top-20 |
|---|---:|---:|---:|---:|---:|
| BioCLIP 2 | 11.29% | 20.97% | 24.19% | 30.65% | 38.71% |
| ALIKED + MNN + RANSAC | 16.13% | 20.97% | 22.58% | 24.19% | 27.42% |
| MiewID-msv3 | 66.13% | 80.65% | 83.87% | 88.71% | 93.55% |
| Wild-ID baseline | 91.94% | 95.16% | 95.16% | 96.77% | 100% |

Among the newly evaluated automated methods, **MiewID-msv3 provided the strongest candidate-ranking performance**.

### Important evaluation limitation

The 62 reference pairs originated from the manually confirmed Wild-ID workflow. They are not independent biological ground-truth identities. Therefore, these percentages describe **candidate-ranking agreement with the reference set**, not absolute individual-identification accuracy. The setup also naturally favours Wild-ID because the reference pairs originated from that workflow.

## 8. Main Issues Faced

Practical challenges included:

- differences in lighting, shadows, moisture, posture, and image angle;
- time required for manual polygon annotation;
- eight no detections during assisted labelling;
- seven no detections during final production extraction;
- changes in crop geometry and skin deformation affecting re-identification;
- lack of independent identity labels for all photographs.

## 9. Future Scope

Future work can include more photographs from different ponds, years, and field conditions; manual review of pseudo-labels; analysis of the seven production failures; and independent individual identities from field records.

MiewID could also be fine-tuned using a larger labelled Yellow-Bellied Toad dataset. Finally, belly results can be compared directly with the throat-only and throat+belly pipelines.

## Notebook

The final notebook for this section should be stored at:

```text
belly/belly_pipeline.ipynb
```

## Images and Original Dataset

Selected documentation images can be stored under [`images/`](images/), separated into original examples, annotations, final crops, and YOLO predictions.

The complete original image dataset is stored in the project [Google Drive folder](https://drive.google.com/drive/u/0/folders/1r_AQc_w7h_Xhkd9MLBpo8sZaRwaw9Mv-). The full dataset is not duplicated in this public repository. 

## Data Availability

The source dataset used for the belly experiment contained 349 photographs (199 A pond and 150 H pond). The Google Drive folder above is the project location for the original image files; GitHub is used for code, documentation, selected examples, and derived results.
