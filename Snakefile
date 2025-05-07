rule all:
    input:
        "data/clean_circuits.csv",
        "data/clean_lap_times.csv",
        "data/clean_races.csv",
        "data/clean_weather.csv",
        "data/merged_data.csv",
        "visualizations/weather/airtemp_vs_laptime.png",
        "visualizations/weather/humidity_vs_laptime.png",
        "visualizations/weather/pressure_vs_laptime.png",
        "visualizations/weather/tracktemp_vs_laptime.png",
        "visualizations/weather/winddirection_vs_laptime.png",
        "visualizations/weather/windspeed_vs_laptime.png",
        expand("visualizations/circuit_laptime_evolution/circuit_{circuit}_laptime_evolution.png", circuit=[9, 6, 13, 14, 11, 18])

rule download_data:
    output:
        "data/formula-1-world-championship-1950-2020.zip",
        "data/f1-weather-dataset-2018-2023.zip"
    script:
        "src/download_data.py"

rule clean_data:
    input:
        "data/formula-1-world-championship-1950-2020.zip",
        "data/f1-weather-dataset-2018-2023.zip"
    output:
        "data/clean_circuits.csv",
        "data/clean_lap_times.csv",
        "data/clean_races.csv",
        "data/clean_weather.csv"
    script:
        "src/clean_data.py"

rule analyze_data:
    input:
        "data/clean_circuits.csv",
        "data/clean_lap_times.csv",
        "data/clean_races.csv",
        "data/clean_weather.csv"
    output:
        "data/merged_data.csv",
        "visualizations/weather/airtemp_vs_laptime.png",
        "visualizations/weather/humidity_vs_laptime.png",
        "visualizations/weather/pressure_vs_laptime.png",
        "visualizations/weather/tracktemp_vs_laptime.png",
        "visualizations/weather/winddirection_vs_laptime.png",
        "visualizations/weather/windspeed_vs_laptime.png",
        expand("visualizations/circuit_laptime_evolution/circuit_{circuit}_laptime_evolution.png", circuit=[9, 6, 13, 14, 11, 18])
    script:
        "src/analyze_data.py"