# Formula 1 Lap Time and Weather Analysis

## DOI
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15362042.svg)](https://doi.org/10.5281/zenodo.15362042)

## Contributors
Scott Abednego

## Summary
This project aims to analyze the evolution of lap times in specific circuits in Formula 1. By leveraging data science and machine learning techniques, we explore how various factors, such as weather, influence the speed of Formula 1 cars around a circuit.

## Data Profile
To support our analysis, we worked with multiple datasets, including lap times and weather data. These datasets were selected for their richness in relevant features and their potential for integration across different dimensions.

### Kaggle Formula 1 World Championship Dataset
- **Source:** Kaggle Formula 1 World Championship Dataset
- **License:** Community-shared
- **Format:** CSV
- **Size:** Multiple files with varying rows and columns
- **Key Fields:** lap times, race details, driver information

### F1 Weather Dataset
- **Source:** F1 Weather Dataset
- **License:** Community-shared
- **Format:** CSV
- **Size:** Multiple files with varying rows and columns
- **Key Fields:** weather conditions, race details

## Process
### Scripts
1. **download_data.py**
   - Downloads lap times and weather data from Kaggle and fastf1.
   - Saves the data in the `data` directory.

2. **clean_data.py**
   - Cleans the downloaded data.
   - Renames and removes unnecessary files.
   - Filters data based on specified criteria and saves cleaned data.

3. **analyze_data.py**
   - Analyzes the cleaned data.
   - Merges datasets and performs exploratory data analysis (EDA).
   - Generates visualizations and saves them in the `visualizations` directory.

4. **pipeline.py**
   - Provides a command-line interface (CLI) to run the entire pipeline.
   - Supports downloading, cleaning, and analyzing data through specific arguments.

### Running the Pipeline
To run the full pipeline, use the following commands:

1. **Download data**
   ```bash
   python pipeline.py --download
   ```

2. **Clean data**
   ```bash
   python pipeline.py --clean
   ```

3. **Analyze data**
   ```bash
   python pipeline.py --analyze
   ```

## Findings
Our analysis produced several key insights:
- **Lap Times:** Fastest lap times are influenced by weather conditions such as air temperature and track temperature.
- **Weather Impact:** Higher track temperatures generally correlate with faster lap times.

### EDA Visualizations
- Scatter plots showing the relationship between weather conditions and lap times.
- Line plots illustrating lap time evolution over the years for different circuits.

## Future Work
While our current project met its goals, we identified several areas for future improvement:
- **Data Expansion:** Incorporate more recent data and additional features such as tire types and pit stop strategies.
- **Advanced Modeling:** Implement machine learning models like Random Forests and XGBoost for better predictive performance.
- **Interactive Dashboards:** Develop user-facing applications to visualize data and predictions interactively.
- **Bias & Fairness Analysis:** Analyze the impact of team budget on team performance and ensure fairness in predictions.

## Reproducing
To reproduce our full analysis workflow, follow these steps:

1. **Clone the GitHub repository**
   ```bash
   git clone https://github.com/illinois-data-curation/is477-sp25-group59.git
   cd is477-sp25-group59
   ```

2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Set up Kaggle API credentials**
   - Place your `kaggle.json` file in the `~/.kaggle/` directory.

4. **Run the full workflow**
   ```bash
   python pipeline.py --download
   python pipeline.py --clean
   python pipeline.py --analyze
   ```

## References
- Kaggle Formula 1 World Championship Dataset: [Link](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020)
- F1 Weather Dataset: [Link](https://www.kaggle.com/datasets/quantumkaze/f1-weather-dataset-2018-2023)