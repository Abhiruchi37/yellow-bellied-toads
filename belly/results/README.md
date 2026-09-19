# Belly Extraction and Re-Identification Results

This folder contains the final outputs from the belly extraction and re-identification stages of the belly-pattern identification pipeline.

## Folder Structure

The results are organised into three main components:

- `extraction_results.csv` – summary of the belly extraction results
- `wildid/` – Wild-ID matching and manually confirmed reference matches
- `reidentification/` – results from the automated re-identification methods

---

## Belly Extraction Results

The `extraction_results.csv` file contains the results obtained when the final YOLO segmentation model was applied to the A-pond images.

A total of **199 images** were processed.

- Successful belly extractions: **192**
- No detection: **7**
- Extraction success rate: **96.48%**

The 192 successfully extracted belly crops were subsequently used as input for the re-identification experiments.

---

## Wild-ID Results

The Wild-ID results are stored separately in the `wildid/` folder.

Wild-ID was used as the established semi-automated identification method. It produces a ranked list of candidate images, after which the user manually confirms or rejects the proposed matches.

The folder contains the manually confirmed match information together with the associated Wild-ID `test/` outputs.

A total of **62 pairwise matches** were manually confirmed using Wild-ID.

These confirmed pairs were subsequently used as the reference set for evaluating the automated re-identification approaches.

### Wild-ID Test Output

The `test/` folder contains the available files and logs generated during the Wild-ID experiment.

The complete `match_info` output is not included in this GitHub repository because of its large size. It is available separately on Google Drive:

[match_info - Google Drive](https://drive.google.com/drive/u/0/folders/1OnlE-AyhsJsfuNTN04oxDlrWgIpERbUg)

---

## Automated Re-Identification Results

The `reidentification/` folder contains the outputs from the automated methods evaluated using the extracted belly crops.

The evaluated approaches include:

- **MiewID-msv3**
- **BioCLIP 2**
- **ALIKED + MNN + RANSAC**

Additional MiewID experiments are also included where applicable.

The individual result folders contain the available ranking outputs, similarity scores, evaluation tables, plots, and other method-specific files.

---

## Candidate-Ranking Performance

The methods were evaluated using the same set of 62 manually confirmed Wild-ID reference pairs.

| Method | Rank-1 | Top-5 | Top-10 | Top-20 |
|---|---:|---:|---:|---:|
| Wild-ID | 91.94% | 95.16% | 96.77% | 100.00% |
| MiewID-msv3 | 66.13% | 83.87% | 88.71% | 93.55% |
| BioCLIP 2 | 11.29% | 24.19% | 30.65% | 38.71% |
| ALIKED + MNN + RANSAC | 16.13% | 22.58% | 24.19% | 27.42% |

Wild-ID serves as the established semi-automated baseline.

Among the newly evaluated automated approaches, **MiewID-msv3** produced the strongest candidate-ranking performance and was selected as the final automated re-identification method for the belly pipeline.

---

## Evaluation Note

The 62 reference pairs were obtained from manually confirmed Wild-ID matches. Therefore, they do not represent a completely independent biological ground-truth dataset.

The reported values should be interpreted as **candidate-ranking performance on the confirmed reference pairs**, rather than as overall individual-identification accuracy.

---

## Complete Pipeline

The complete implementation of belly segmentation, extraction, re-identification, and evaluation is available in:

`../belly_pipeline.ipynb`
