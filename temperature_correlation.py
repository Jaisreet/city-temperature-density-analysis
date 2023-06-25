#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the weather station data
stations_file = "stations.json.gz"
stations = pd.read_json(stations_file, lines=True)

# Read the city data
city_data_file = "city_data.csv"
cities = pd.read_csv(city_data_file)

# Remove cities with missing area or population
cities = cities.dropna(subset=["area", "population"])

# Convert city area from m² to km²
cities["area"] = cities["area"] / 1000000

# Exclude cities with area greater than 10000 km²
cities = cities[cities["area"] <= 10000]

# Function to calculate the distance between a city and all weather stations
def distance(city, stations):
    lat_diff = np.radians(stations["latitude"]) - np.radians(city["latitude"])
    lon_diff = np.radians(stations["longitude"]) - np.radians(city["longitude"])
    a = np.sin(lat_diff / 2) ** 2 + np.cos(np.radians(city["latitude"])) * np.cos(np.radians(stations["latitude"])) * np.sin(lon_diff / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    distance = 6371 * c  # Earth's radius is approximately 6371 km
    return distance

# Function to find the best 'avg_tmax' value for a city from the list of weather stations
def best_tmax(city, stations):
    city_distance = distance(city, stations)
    best_station_index = np.argmin(city_distance)
    return stations.loc[best_station_index, "avg_tmax"] / 10

# Calculate the best 'avg_tmax' value for each city
cities["avg_tmax"] = cities.apply(best_tmax, stations=stations, axis=1)

# Create the scatter plot
plt.scatter(cities["population"] / cities["area"], cities["avg_tmax"])
plt.xlabel("Population Density (people/km²)")
plt.ylabel("Avg Max Temperature (°C)")
plt.title("Correlation between Population Density and Temperature")
plt.savefig("output.svg")

