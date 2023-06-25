## City Temperature-Density Analysis

This project aims to investigate the correlation between population density and average maximum temperature in cities. By combining weather station data with city information from Wikidata, we analyze the relationship between these two variables and visualize the results in a scatterplot.

### Problem Statement

The main question we seek to answer is whether there is any correlation between population density and temperature. To tackle this question, we need to match population density data with weather station data. The program, `temperature_correlation.py`, takes weather station and city data files as input and generates a scatterplot to visualize the correlation.

### Data Sources

The project utilizes two main data sources:

1. **Weather Station Data**: The weather station data is provided in a line-by-line JSON format, compressed in a gzip file (`stations.json.gz`). The data includes information such as latitude, longitude, and average maximum temperature ('avg_tmax').

2. **City Data**: The city data is available in a convenient CSV file (`city_data.csv`). It contains information about cities, including population and area. The population density is calculated by dividing the population by the area.

### Workflow

The project follows the following workflow to analyze the correlation:

1. **Data Preparation**: The weather station data is loaded from the JSON file using Pandas, and the 'avg_tmax' column is divided by 10 to convert it from °C×10 to °C. The city data is read from the CSV file, and cities with missing population or area information are filtered out. City area is converted from m² to km², and cities with an area greater than 10,000 km² are excluded.

2. **Entity Resolution**: Since the city and weather station data refer to different locations, we need to find the weather station closest to each city. A distance calculation function is implemented to determine the distance between a city and each weather station. Another function is created to find the best 'avg_tmax' value for each city by selecting the station with the minimum distance. These functions are applied across all cities using Pandas' `apply` function.

3. **Visualization**: The final step involves generating a scatterplot to visualize the correlation between average maximum temperature and population density. The scatterplot is saved as an SVG file specified in the command line arguments.

### Getting Started

To get started with the project, follow these steps:

1. Install the necessary dependencies: Pandas, NumPy, and Matplotlib.

2. Clone the repository:
   ```
   git clone https://github.com/jaisreet/city-temperature-density-analysis.git
   ```

3. Navigate to the project directory:
   ```
   cd city-temperature-density-analysis
   ```

4. Prepare the input files:
   - Obtain the weather station data file in the specified format and save it as `stations.json.gz` in the project directory.
   - Prepare the city data file in CSV format, ensuring it includes population and area information. Save it as `city_data.csv` in the project directory.

5. Run the program to analyze the correlation and generate the scatterplot:
   ```
   python3 temperature_correlation.py stations.json.gz city_data.csv output.svg
   ```

6. Once the program completes, you will find the scatterplot saved as `output.svg` in the project directory. Open this file to visualize and analyze the correlation between average maximum temperature and population density.

This project is licensed under the [MIT License](LICENSE).

### Contributing

Contributions are welcome!
