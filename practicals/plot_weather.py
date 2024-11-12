import pandas as pd
import matplotlib.pyplot as plt
import os

# Define the path to the data directory
data_dir = 'data/practical_data'

# List of CSV files to read
csv_files = ['weather_2001.csv', 'weather_2003.csv', 'weather_2007.csv']

# Initialize a dictionary to store the data
data = {}

# Read each CSV file into a pandas DataFrame
for csv_file in csv_files:
    file_path = os.path.join(data_dir, csv_file)
    df = pd.read_csv(file_path, comment='#', header=None, names=['STN', 'YYYYMMDD', 'TG', 'SQ', 'Q'])
    data[csv_file] = df

# Plot the data
plt.figure(figsize=(15, 10))

# Plot daily mean temperature (TG)
plt.subplot(3, 1, 1)
for csv_file, df in data.items():
    plt.plot(df['YYYYMMDD'], df['TG'], label=csv_file)
plt.title('Daily Mean Temperature (TG)')
plt.xlabel('Date')
plt.ylabel('Temperature (0.1 °C)')
plt.legend()

# Plot sunshine duration (SQ)
plt.subplot(3, 1, 2)
for csv_file, df in data.items():
    plt.plot(df['YYYYMMDD'], df['SQ'], label=csv_file)
plt.title('Sunshine Duration (SQ)')
plt.xlabel('Date')
plt.ylabel('Sunshine Duration (0.1 hour)')
plt.legend()

# Plot global radiation (Q)
plt.subplot(3, 1, 3)
for csv_file, df in data.items():
    plt.plot(df['YYYYMMDD'], df['Q'], label=csv_file)
plt.title('Global Radiation (Q)')
plt.xlabel('Date')
plt.ylabel('Global Radiation (J/cm²)')
plt.legend()

# Adjust layout and show the plot
plt.tight_layout()
plt.show()