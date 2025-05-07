import logging
import os
import pandas as pd

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_data():
    logging.info("Cleaning data...")

    # Rename the weather dataset
    data_folder = 'data'
    old_weather_filename = 'F1 Weather(2023-2018).csv'
    new_weather_filename = 'weather.csv'
    old_weather_filepath = os.path.join(data_folder, old_weather_filename)
    new_weather_filepath = os.path.join(data_folder, new_weather_filename)
    
    if os.path.exists(old_weather_filepath):
        os.rename(old_weather_filepath, new_weather_filepath)
        logging.info(f"Renamed {old_weather_filename} to {new_weather_filename}")
    else:
        logging.warning(f"{old_weather_filename} does not exist in the data folder")

    # Delete every CSV from the data folder except for circuits.csv, lap_data.csv, lap_times.csv, and races.csv
    exceptions = {'circuits.csv', 'weather.csv', 'lap_times.csv', 'races.csv'}
    
    for filename in os.listdir(data_folder):
        if filename.endswith('.csv') and filename not in exceptions:
            os.remove(os.path.join(data_folder, filename))
            logging.info(f"Deleted {filename}")

    # Cleaning specified CSV files
    csv_files = ['circuits.csv', 'lap_times.csv', 'races.csv']
    circuit_ids_to_keep = {9, 6, 13, 14, 11, 18}
    
    for filename in csv_files:
        file_path = os.path.join(data_folder, filename)
        data = pd.read_csv(file_path, on_bad_lines='skip')
        
        # Filter data based on circuit IDs
        if filename == 'circuits.csv':
            data = data[data['circuitId'].isin(circuit_ids_to_keep)]
        elif filename == 'races.csv':
            data = data[data['circuitId'].isin(circuit_ids_to_keep)]
        elif filename == 'lap_times.csv':
            race_ids_to_keep = pd.read_csv(os.path.join(data_folder, 'races.csv'))
            race_ids_to_keep = race_ids_to_keep[race_ids_to_keep['circuitId'].isin(circuit_ids_to_keep)]['raceId']
            data = data[data['raceId'].isin(race_ids_to_keep)]
        
        # Drop missing values
        data.dropna(inplace=True)
        
        # Save cleaned data
        cleaned_file_path = os.path.join(data_folder, f'clean_{filename}')
        data.to_csv(cleaned_file_path, index=False)
        logging.info(f"Cleaned {filename} and saved to {cleaned_file_path}")

    # Delete old CSV files
    for filename in csv_files:
        file_path = os.path.join(data_folder, filename)
        os.remove(file_path)
        logging.info(f"Deleted old file {filename}")

    # Clean weather data to only include rounds and years found in clean_races.csv
    clean_races_filepath = os.path.join(data_folder, 'clean_races.csv')
    clean_races_data = pd.read_csv(clean_races_filepath)
    
    if os.path.exists(new_weather_filepath):
        weather_data = pd.read_csv(new_weather_filepath)
        
        # Filter weather data based on rounds and years found in clean_races.csv
        filtered_weather_data = weather_data.merge(clean_races_data[['year', 'round']], left_on=['Year', 'Round Number'], right_on=['year', 'round'])
        
        # Average the values in columns AirTemp, Humidity, Pressure, TrackTemp, WindDirection, WindSpeed
        averaged_weather_data = filtered_weather_data.groupby(['year', 'round']).agg({
            'AirTemp': 'mean',
            'Humidity': 'mean',
            'Pressure': 'mean',
            'TrackTemp': 'mean',
            'WindDirection': 'mean',
            'WindSpeed': 'mean',
            'Rainfall': lambda x: x.any()
        }).reset_index()
        
        # Save cleaned weather data
        weather_filepath = os.path.join(data_folder, 'clean_weather.csv')
        averaged_weather_data.to_csv(weather_filepath, index=False)
        logging.info(f"Cleaned weather data and saved to {weather_filepath}")
        os.remove(new_weather_filepath)
    else:
        logging.warning(f"{new_weather_filename} does not exist in the data folder")

    logging.info("Data cleaning done.")

# Run the clean_data function
if __name__ == "__main__":
    clean_data()
