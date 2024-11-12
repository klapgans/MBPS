import pandas as pd
from matplotlib import pyplot as plt
import os


def transform_weather_data(data_dir, csv_files):
    data = {}
    for csv_file in csv_files:
        file_path = os.path.join(data_dir, csv_file)
        df = pd.read_csv(file_path, comment='#', header=None, names=['STN', 'YYYYMMDD', 'TG', 'SQ', 'Q'])
        data[csv_file] = df
    return data

def convert_units(data):
    for data_file, df in data.items():
        df['TG'] = df['TG'] * 0.1
        df['Q'] = df['Q'] * 10000*60*60*24
        df["date"] = pd.to_datetime(df["YYYYMMDD"], format='%Y%m%d')
        df["day_nr"] = df["date"].dt.dayofyear
        data[data_file] = df

    return data


def save_weather_data(data, output_dir):
    for data_file, df in data.items():
        output_file = os.path.join(output_dir, data_file)
        df.to_csv(output_file, index=False)
    return None


data = transform_weather_data('data/practical_data', ['weather_2001.csv', 'weather_2003.csv', 'weather_2007.csv'])

data = convert_units(data)

save_weather_data(data, 'data/practical_data/converted')

