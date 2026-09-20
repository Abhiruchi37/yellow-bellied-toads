# SuperPoint + LightGlue Identification Results

This folder contains the main result files produced during the belly + throat identification experiment using SuperPoint and LightGlue.

## Files

### `all_pair_scores.csv`

Contains the matching results for all unique pairs of the 200 belly + throat crop images.

A total of 19,900 unique image pairs were compared.

### `top5_candidates.csv`

Contains the top candidate matches selected from the pairwise comparison results.

These candidates were selected according to the matching scores produced by SuperPoint + LightGlue.

### `manual_verification.csv`

Contains the results used for manual verification of the generated candidate matches.

## Matching Score

The identification workflow uses the following combined matching score:

`Combined Score = Number of Matches × Average Match Confidence`

A higher combined score indicates that the image pair produced more feature matches and/or stronger matching confidence.
