# Belly Extraction and Re-Identification Results

This folder contains the final outputs from the belly extraction and re-identification stages of the pipeline.

## Extraction Results

The `extraction/` folder contains the extraction results generated when the final YOLO segmentation model was applied to the A-pond images.

The `extraction_results.csv` file records the extraction status for each input image.

- Total input images: 199
- Successful belly extractions: 192
- No detection: 7
- Extraction success rate: 96.48%

The successfully extracted belly images were used as input for the subsequent re-identification experiments.

## Re-Identification Results

The `reidentification/` folder contains the results obtained from the different methods evaluated for individual identification using the extracted belly patterns.

The evaluated methods include:

- Wild-ID
- MiewID-msv3
- BioCLIP 2
- ALIKED + MNN + RANSAC

The experiments were evaluated using the same set of 62 manually confirmed Wild-ID reference pairs to allow comparison between the different approaches.

The result folders contain the available ranking outputs, similarity scores, evaluation tables, plots, and other method-specific files.

## Candidate-Ranking Performance

| Method | Rank-1 | Top-5 | Top-10 | Top-20 |
|---|---:|---:|---:|---:|
| Wild-ID | 91.94% | 95.16% | 96.77% | 100.00% |
| MiewID-msv3 | 66.13% | 83.87% | 88.71% | 93.55% |
| BioCLIP 2 | 11.29% | 24.19% | 30.65% | 38.71% |
| ALIKED + MNN + RANSAC | 16.13% | 22.58% | 24.19% | 27.42% |

Wild-ID is used as the established semi-automated baseline, while MiewID-msv3 was selected as the final new automated re-identification approach evaluated in this work.

## Evaluation Note

The 62 reference pairs were derived from manually confirmed Wild-ID matches and therefore do not represent a completely independent biological ground-truth dataset.

The reported values should be interpreted as candidate-ranking performance on these confirmed reference pairs rather than as overall individual-identification accuracy.

For the complete implementation and evaluation workflow, see:

`../belly_pipeline.ipynb`
