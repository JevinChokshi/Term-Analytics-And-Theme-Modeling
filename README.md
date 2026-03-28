# 📊 Text Analytics – Theme Modeling

## Overview

This project is an **end-to-end data analytics pipeline** designed to extract meaningful patterns from enrichment-based biological datasets.

It focuses on combining **clustering and NLP techniques** to group related signals and identify broader functional themes, enabling easier interpretation of complex, high-dimensional data.

---

## What this project does

* Processes enrichment outputs (e.g., functional terms and associated genes)
* Groups related terms using a **hybrid clustering approach**
* Uses **semantic modeling (transformers)** to understand contextual similarity
* Maps clusters to broader **interpretable themes**
* Generates **summary distributions and visualizations**

---

## Why this project

High-dimensional datasets often contain overlapping and noisy signals. This pipeline helps:

* Reduce complexity
* Improve interpretability
* Highlight dominant patterns across groups

---

## Project Structure

```id="fj5d7n"
Text-Analytics-Theme-Modeling/
│
├── main.py
├── requirements.txt
│
├── data/
│   ├── submodule_membership.csv
│   └── ORA_files/
│
├── outputs/
│   ├── sample_fraction_themes.csv
│   └── sample_plot.png
│
└── src/
    ├── config.py
    ├── pipeline.py
    ├── clustering.py
    ├── models.py
    ├── validator.py
    └── utils.py
```

---

## Installation

```id="q3q5l1"
pip install -r requirements.txt
```

---

## Usage

Run the pipeline:

```id="smwbbv"
python main.py
```

---

## Outputs

The pipeline generates:

* **Aggregated theme distribution** across groups
* **Visualization (stacked bar plot)** for quick comparison
* Structured output files for further analysis

---

## Approach (Simplified)

1. Load enrichment data and gene associations
2. Compute similarity
3. Perform clustering to group related terms
4. Assign clusters to broader themes
5. Aggregate and visualize results

---

## Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Sentence Transformers
* BERTopic
* Matplotlib, Seaborn

---

## Notes

* Sample outputs are included for demonstration
* The pipeline is modular and can be adapted to similar datasets
* Some domain-specific details have been abstracted for general use
* This pipeline is a submodule of a larger high-dimensional HIV research workflow. It focuses on a specific analytical task while the overarching project remains confidential.

---

## Author

Jevin Chokshi
