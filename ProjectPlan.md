## Overview

The goal of this project is to analyze the evolution of lap times across different circuits in Formula 1. By integrating lap times and race circuit datasets, we aim to uncover patterns and insights that can help stakeholders understand how lap times have changed over the years.

Our objectives include:

- Identifying key trends in lap times across different circuits and seasons.
- Analyzing factors that may influence lap times, such as technological advancements and changes in regulations.
- Creating a fully reproducible, automated data pipeline to fetch, clean, integrate, and analyze data from two distinct sources.
- Packaging our work into a documented, shareable Python package with metadata and citation.


## Research Questions

1. How have lap times evolved over the years across different circuits?
2. Are there specific circuits where lap times have improved significantly?
3. What factors contribute to changes in lap times over the years?
4. Can we build a model to predict lap times based on historical data?

These questions will guide our data collection and analysis efforts throughout the project.


## Team

This is a solo project with responsibilities:

### Scott Abednego – Data Engineer, Data Analyst & Visualization
- Responsible for data acquisition from sponsorship and performance APIs
- Writing scripts for data retrieval, integrity checks, and logging
- Conducting data profiling, cleaning, and exploratory analysis
- Implementing visualization of sponsorship vs. performance trends
- Structuring and documenting the reproducible package
- Writing metadata and handling citation formats
- Setting up and managing the GitHub repository


## Datasets

We will use two datasets from completely different sources and formats:

### Dataset 1: Formula 1 Lap Time Data
- Source: Kaggle (Formula 1 World Championship dataset)
- Access Method: CSV download
- Content:  Lap times and race circuit details for Formula 1 teams
- URL: https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020
- License: Public domain
  - Notes: Data will be accessed using a script at runtime; integrity checks via SHA256 hash

### Dataset 2: Formula 1 Weather Data
- Source: Kaggle (F1 Weather dataset)
- Access Method: CSV download
- Content: Historical race weather data for each round
- URL: https://www.kaggle.com/datasets/quantumkaze/f1-weather-dataset-2018-2023
- License: Public domain
  - Notes: Data will be accessed using a script at runtime; integrity checks via SHA256 hash


## Timeline

### Week 8-9: Reproducible Package Setup
- Set up Python package structure (src/, docs/, tests/, etc.)
- Develop CLI script for end-to-end data pipeline
- Write README.md with install/setup instructions
- Add unit tests for core functions
  - Requirements: Reproducible structure, installable package, CLI-enabled

### Week 10-11: Workflow Automation
- Create Makefile and CLI wrapper for automated steps: download → clean → merge → analyze
- Add logging and error handling for reproducibility
- Test automation in a clean environment
- Refactor scripts based on test results
  - Requirements: End-to-end automation with robust testing

### Week 12: Metadata & Citations
- Create CITATION.md citing Kaggle, OpenF1, and key Python packages
- Add licensing files to GitHub
- Draft dataset metadata (YAML or JSON) including source, time range, units, fields
  - Requirements: Clear citations, licensing, metadata for data provenance

### Week 13-15: Final Archiving
- Archive final project using GitHub-Zenodo integration
- Add DOI and citation info to README.md and documentation
  - Requirements: Long-term archiving with persistent identifier (e.g., Zenodo DOI)

