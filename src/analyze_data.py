import logging
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_data():
    logging.info("Analyzing data...")

    # Load cleaned data
    lap_times_data = pd.read_csv('data/clean_lap_times.csv')
    races_data = pd.read_csv('data/clean_races.csv')
    weather_data = pd.read_csv('data/clean_weather.csv')

    # Clean 'time' column and convert to numeric (milliseconds)
    logging.info("Cleaning 'time' column...")
    lap_times_data['time'] = lap_times_data['time'].str.replace(':', '').str.replace('.', '').astype(float)

    # Reduce the amount of data in clean_lap_times.csv by keeping the fastest lap time of each race
    logging.info("Reducing lap times data...")
    fastest_lap_times = lap_times_data.loc[lap_times_data.groupby('raceId')['time'].idxmin()]

    # Identify and remove outliers with lap time over 250000
    logging.info("Removing outliers...")
    outliers = fastest_lap_times[fastest_lap_times['time'] > 250000]
    logging.info(f"Identified outliers:\n{outliers}")
    fastest_lap_times = fastest_lap_times[fastest_lap_times['time'] <= 250000]

    # Merge datasets using raceId
    logging.info("Merging datasets...")
    merged_data = pd.merge(fastest_lap_times, races_data, on='raceId')
    merged_data = pd.merge(merged_data, weather_data, on=['year', 'round'])

    # Log the columns of the merged dataset
    logging.info(f"Columns in merged data: {merged_data.columns.tolist()}")

    # Keep only the specified columns, using 'time_x' for lap times
    merged_data = merged_data[['raceId', 'year', 'round', 'circuitId', 'name', 'driverId', 'lap', 'position', 'time_x', 'AirTemp', 'Humidity', 'Pressure', 'TrackTemp', 'WindDirection', 'WindSpeed', 'Rainfall']]
    merged_data.rename(columns={'time_x': 'time'}, inplace=True)

    # Data profiling and quality assessment
    logging.info("Profiling data...")
    logging.info(f"Number of rows in merged data: {merged_data.shape[0]}")
    logging.info(f"Number of columns in merged data: {merged_data.shape[1]}")
    logging.info(f"Missing values in merged data:\n{merged_data.isnull().sum()}")

    # Save merged data
    merged_data.to_csv('data/merged_data.csv', index=False)
    logging.info("Data analysis done.")

    # Create directories for visualizations if they don't exist
    weather_visualizations_folder = 'visualizations/weather'
    circuit_visualizations_folder = 'visualizations/circuit_laptime_evolution'
    
    if not os.path.exists(weather_visualizations_folder):
        os.makedirs(weather_visualizations_folder)
    
    if not os.path.exists(circuit_visualizations_folder):
        os.makedirs(circuit_visualizations_folder)

    # Visualizations for weather-related data
    weather_columns = ['AirTemp', 'Humidity', 'Pressure', 'TrackTemp', 'WindDirection', 'WindSpeed']

    for column in weather_columns:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=merged_data, x=column, y='time')
        plt.title(f'Relationship between {column} and Lap Time')
        plt.xlabel(column)
        plt.ylabel('Lap Time (milliseconds)')
        plt.savefig(os.path.join(weather_visualizations_folder, f'{column.lower()}_vs_laptime.png'))
        logging.info(f"Saved visualization: {column.lower()}_vs_laptime.png")

    # Visualization for circuit lap time evolution over time
    circuits = merged_data['circuitId'].unique()
    
    for circuit in circuits:
        circuit_data = merged_data[merged_data['circuitId'] == circuit]
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=circuit_data, x='year', y='time')
        plt.title(f'Lap Time Evolution for Circuit {circuit}')
        plt.xlabel('Year')
        plt.ylabel('Lap Time (milliseconds)')
        plt.savefig(os.path.join(circuit_visualizations_folder, f'circuit_{circuit}_laptime_evolution.png'))
        logging.info(f"Saved visualization: circuit_{circuit}_laptime_evolution.png")

if __name__ == "__main__":
    analyze_data()