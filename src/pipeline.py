import argparse
import logging
import requests
import pandas as pd
import json
import sys

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_data():
    logging.info("Downloading data...")
    # Downloading sponsorship data from Kaggle
    sponsorship_url = "https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020/download"
    performance_url = "https://openf1.org/api/v1/races"
    
    sponsorship_data = pd.read_csv(sponsorship_url)
    performance_data = requests.get(performance_url).json()
    
    sponsorship_data.to_csv('data/sponsorship_data.csv', index=False)
    with open('data/performance_data.json', 'w') as f:
        json.dump(performance_data, f)
    
    logging.info("Data download done.")

def clean_data():
    logging.info("Cleaning data...")
    # Cleaning sponsorship data
    sponsorship_data = pd.read_csv('data/sponsorship_data.csv')
    performance_data = pd.read_json('data/performance_data.json')
    
    # Drop missing values
    sponsorship_data.dropna(inplace=True)
    performance_data.dropna(inplace=True)
    
    sponsorship_data.to_csv('data/clean_sponsorship_data.csv', index=False)
    performance_data.to_json('data/clean_performance_data.json')
    
    logging.info("Data cleaning done.")

def merge_data():
    logging.info("Merging data...")
    # Merging sponsorship and performance data
    sponsorship_data = pd.read_csv('data/clean_sponsorship_data.csv')
    performance_data = pd.read_json('data/clean_performance_data.json')
    
    # Merge datasets on team and season
    merged_data = pd.merge(sponsorship_data, performance_data, on=['team', 'season'])
    
    merged_data.to_csv('data/merged_data.csv', index=False)
    
    logging.info("Data merging done.")

def analyze_data():
    logging.info("Analyzing data...")
    # Analyzing merged data
    merged_data = pd.read_csv('data/merged_data.csv')
    
    # Group by team and calculate sum of deal values and mean of points
    analysis_results = merged_data.groupby('team').agg({'deal_value': 'sum', 'points': 'mean'})
    
    analysis_results.to_csv('data/analysis_results.csv', index=False)
    
    logging.info("Data analysis done.")

def main():
    parser = argparse.ArgumentParser(description="Formula 1 Sponsorship and Performance Analysis Pipeline")
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
