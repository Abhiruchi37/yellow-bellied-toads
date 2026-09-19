# Yellow-Bellied Toad Photo-Identification

This repository contains code and experimental material for a photo-identification project on the Yellow-Bellied Toad (*Bombina variegata*).

The project investigates whether ventral body patterns can support individual re-identification from photographs. Three anatomical image configurations are studied so that the usefulness of each region can be evaluated separately and in combination.

## Team

This project was carried out as part of the RCS project at Trier University.

### Team Members
- **Tenzin Nyidon Tenzin Nyidon** – Subgular Throat
- **Ridhima Kishor Lawane** – Subgular Throat and Ventral Abdomen
- **Abhiruchi Sanjaykumar Bharambe** – Ventral Abdomen
- 
### Supervisor
- **Prof. Dr. Henning Fernau**
- **Prof. Dr. Michael Veith**

## Project Sections

### 1. Belly only
The belly pipeline uses YOLO segmentation to isolate the ventral belly pattern and create standardized crops. The extracted crops are then evaluated using BioCLIP 2, ALIKED + MNN + RANSAC, MiewID-msv3, and Wild-ID.

See **[belly/](belly/)** for the completed belly pipeline, methodology, and results.

### 2. Throat only
This section investigates whether the throat pattern alone can support individual photo-identification.

See **[throat/](throat/)**. The final notebook and results will be added by the group member responsible for this part.

### 3. Throat + belly
This section investigates whether using the throat and belly together improves re-identification, especially when one anatomical region is partly unclear or unavailable.

See **[throat_belly/](throat_belly/)**. The final notebook and results will be added by the group member responsible for this part.

## General Workflow

```text
Original photographs
        ↓
Anatomical region annotation
        ↓
YOLO segmentation
        ↓
Region extraction
        ↓
Standardized crops
        ↓
Re-identification
        ↓
Candidate ranking
        ↓
Reference / manual evaluation
```

## Repository Structure

```text
belly/          Belly-only pipeline
throat/         Throat-only pipeline
throat_belly/   Combined throat + belly pipeline
docs/           Project documentation
```

## Data

The complete original research image dataset is not included in this repository. Only derived results and selected example images should be added where sharing is permitted.

## Evaluation Note

Candidate-ranking results should not automatically be interpreted as independent biological identification accuracy. The evaluation protocol and the origin of the reference matches are documented in the README for each completed experiment.
