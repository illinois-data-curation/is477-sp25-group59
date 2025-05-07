import logging
import os
import json
import kaggle
import pandas as pd
import fastf1
from urllib.request import urlopen

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.getLogger('fastf1').setLevel(logging.CRITICAL)  # Use logging.INFO or logging.WARNING for more information

def download_data():
    logging.info("Downloading data...")

    # Create 'data' directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    # Set Kaggle API credentials using environment variables
    os.environ['KAGGLE_USERNAME'] = 'your_kaggle_username'
    os.environ['KAGGLE_KEY'] = 'your_kaggle_key'

    # Downloading lap times data from Kaggle
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files('rohanrao/formula-1-world-championship-1950-2020', path='data', unzip=True)

    logging.info("Downloaded lap times data from Kaggle.")

    # Attempt to download weather data using fastf1
    logging.info("Attempting to download weather data using fastf1...")

    try:
        years = [2018, 2019, 2020, 2021, 2022, 2023]
        num_races = [22, 22, 18, 22, 23, 23]

        weather = pd.DataFrame()

        for year, num_race in zip(years, num_races):
            df = pd.DataFrame()
            
            for x in range(1, num_race + 1):  # Adjusted to include the last race
                race_session = fastf1.get_session(year, x, 'R').event
                df = pd.concat([df, pd.DataFrame([race_session])], ignore_index=True)
            
            for track in df['Location']:
                race_session = fastf1.get_session(year, track, 'R')
                race_session.load()  # Load the data before accessing it
                weather_data = race_session.weather_data
                round_number = df.loc[df['Location'] == track, 'RoundNumber'].values[0]  # Get the round number for the race
                weather_data['Round Number'] = round_number
                weather_data['Year'] = year
                weather = pd.concat([weather, weather_data])
                print(f"{track}, Year: {year}")

        if not os.path.exists('data'):
            os.makedirs('data')
        weather.to_csv('data/f1-weather-dataset-2018-2023.csv', encoding='utf-8', index=False)

        logging.info("Weather data for Formula 1 races in 2018-2023 has been saved to 'data/F1_Weather_2018-2023.csv'")

    except Exception as e:
        logging.error(f"Failed to download weather data using fastf1: {e}")
        logging.info("Downloading weather data from Kaggle as a fallback...")

        # Downloading weather data from Kaggle as a fallback
        kaggle.api.dataset_download_files('quantumkaze/f1-weather-dataset-2018-2023', path='data', unzip=True)
        logging.info("Downloaded weather data from Kaggle.")


        # Rename the downloaded file to match the expected output
        downloaded_file = 'data/F1 Weather(2023-2018).csv'
        expected_file = 'data/f1-weather-dataset-2018-2023.csv'
        if os.path.exists(downloaded_file):
            os.rename(downloaded_file, expected_file)
            logging.info(f"Renamed {downloaded_file} to {expected_file}")


if __name__ == "__main__":
    download_data()