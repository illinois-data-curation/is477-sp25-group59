import argparse
import logging
import requests
import pandas as pd
import json
import sys
import os

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_data():
    logging.info("Downloading data...")

    # Create 'data' directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    # Downloading lap times and race circuit data from Kaggle
    lap_times_url = "https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020/download"
    performance_url = "https://openf1.org/api/v1/races"
    
    # Manually download the CSV file and place it in the data directory
    lap_times_data = pd.read_csv('data/formula-1-world-championship.csv', error_bad_lines=False)
    performance_data = requests.get(performance_url).json()
    
    lap_times_data.to_csv('data/lap_times_data.csv', index=False)
    with open('data/performance_data.json', 'w') as f:
        json.dump(performance_data, f)
    
    logging.info("Data download done.")

def clean_data():
    logging.info("Cleaning data...")
    # Cleaning lap times data
    lap_times_data = pd.read_csv('data/lap_times_data.csv')
    performance_data = pd.read_json('data/performance_data.json')
    
    # Drop missing values
    lap_times_data.dropna(inplace=True)
    performance_data.dropna(inplace=True)
    
    lap_times_data.to_csv('data/clean_lap_times_data.csv', index=False)
    performance_data.to_json('data/clean_performance_data.json')
    
    logging.info("Data cleaning done.")

def merge_data():
    logging.info("Merging data...")
    # Merging lap times and performance data
    lap_times_data = pd.read_csv('data/clean_lap_times_data.csv')
    performance_data = pd.read_json('data/clean_performance_data.json')
    
    # Merge datasets on team and season
    merged_data = pd.merge(lap_times_data, performance_data, on=['team', 'season'])
    
    merged_data.to_csv('data/merged_data.csv', index=False)
    
    logging.info("Data merging done.")

def analyze_data():
    logging.info("Analyzing data...")
    # Analyzing merged data
    merged_data = pd.read_csv('data/merged_data.csv')
    
    # Group by circuit and year to calculate mean lap times
    analysis_results = merged_data.groupby(['circuit', 'year']).agg({'lap_time': 'mean'})
    
    analysis_results.to_csv('data/analysis_results.csv', index=False)
    
    logging.info("Data analysis done.")

def main():
    parser = argparse.ArgumentParser(description="Formula 1 Lap Times Evolution Analysis Pipeline")
    parser.add_argument('--download', action='store_true', help="Download data")
    parser.add_argument('--clean', action='store_true', help="Clean data")
    parser.add_argument('--merge', action='store_true', help="Merge data")
    parser.add_argument('--analyze', action='store_true', help="Analyze data")
    
    # To handle Jupyter notebook arguments
    if 'ipykernel_launcher' in sys.argv[0]:
        sys.argv = sys.argv[:1]
    
    args = parser.parse_args()
    
    if args.download:
        download_data()
    if args.clean:
        clean_data()
    if args.merge:
        merge_data()
    if args.analyze:
        analyze_data()

if __name__ == "__main__":
    main()