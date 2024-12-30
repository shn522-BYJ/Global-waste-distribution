
# Refactored data analysis script

# Import necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Define the data directory
data_dir = "data"

# Function to check directory write access
def check_write_access(path):
    directory = os.path.dirname(path) or "."
    if not os.access(directory, os.W_OK):
        raise IOError(f"Save directory '{directory}' is not writable.")
    if os.path.exists(path):
        print(f"Warning: {path} already exists and will be overwritten.")

# Function to preprocess data
def preprocess_data(data):
    data.fillna({
        "population_population_number_of_people": data["population_population_number_of_people"].median(),
        "total_msw_total_msw_generated_tons_year": data["total_msw_total_msw_generated_tons_year"].mean(),
        "waste_treatment_open_dump_percent": 0,
        "waste_treatment_recycling_percent": 0
    }, inplace=True)
    return data

# Function to save data with backup mechanism
def save_with_backup(data, path):
    check_write_access(path)
    if os.path.exists(path):
        backup_path = path.replace(".csv", "_backup.csv")
        os.rename(path, backup_path)
        print(f"Existing file renamed to backup: {backup_path}")
    data.to_csv(path, index=False)
    print(f"Data saved to '{path}'.")

# Load datasets (ensure the files are in the data directory)
try:
    city_data_path = os.path.join(data_dir, "city_level_data_0_0.csv")
    city_codebook_path = os.path.join(data_dir, "city_level_codebook_0.csv")
    country_data_path = os.path.join(data_dir, "country_level_data.csv")
    country_codebook_path = os.path.join(data_dir, "country_level_codebook.csv")
    city_data = pd.read_csv(city_data_path, encoding='cp1252')
    city_codebook = pd.read_csv(city_codebook_path, encoding='latin-1')
    country_data = pd.read_csv(country_data_path, encoding='cp1252')
    country_codebook = pd.read_csv(country_codebook_path, encoding='latin-1')
except FileNotFoundError as e:
    raise FileNotFoundError(f"Required file is missing: {e}")

# Display the city data
print(city_data.head())

# Preprocess city data
city_data = preprocess_data(city_data)

# Select and copy relevant columns from city data
city_Newdata = city_data[[
    "iso3c", "region_id", "country_name", "city_name", "income_id",
    "population_population_number_of_people",
    "total_msw_total_msw_generated_tons_year",
    "waste_treatment_open_dump_percent",
    "waste_treatment_recycling_percent"
]].copy()

# Check for missing values
print(city_Newdata.isnull().sum())

# Summary statistics for waste treatment in city data
waste_summary = city_Newdata.groupby('region_id')[
    ['waste_treatment_open_dump_percent', 'waste_treatment_recycling_percent']
].agg(['mean', 'std', 'min', 'max', 'median'])
print(waste_summary)

# Export waste summary for external analysis
waste_summary.to_csv("waste_summary_city.csv")
print("Waste summary for city data saved as 'waste_summary_city.csv'.")

# Visualization: City population distribution
quantile_threshold = 0.99
city_population_tolerance = city_Newdata['population_population_number_of_people'].quantile(quantile_threshold)
filtered_city_data = city_Newdata[city_Newdata['population_population_number_of_people'] <= city_population_tolerance]

sns.histplot(filtered_city_data['population_population_number_of_people'], kde=True)
plt.title('City Population Distribution')
plt.show()

# Waste treatment percentages by income group (city)
waste_cols = ['waste_treatment_open_dump_percent', 'waste_treatment_recycling_percent']
city_Newdata.groupby('income_id')[waste_cols].mean().plot(kind='bar')
plt.title('Waste Treatment by Income Group (City)')
plt.show()

# Visualization: Regional waste treatment using Plotly (city)
fig = px.bar(city_Newdata, x='region_id', y='waste_treatment_open_dump_percent', color='income_id')
fig.show()

# Preprocess country data
country_data = preprocess_data(country_data)

# Select and copy relevant columns from country data
country_Newdata = country_data[[
    "iso3c", "region_id", "country_name", "income_id",
    "gdp", "population_population_number_of_people",
    "total_msw_total_msw_generated_tons_year",
    "waste_treatment_open_dump_percent",
    "waste_treatment_recycling_percent"
]].copy()

# Summary statistics for waste treatment in country data
country_waste_summary = country_Newdata.groupby('region_id')[
    ['waste_treatment_open_dump_percent', 'waste_treatment_recycling_percent']
].agg(['mean', 'std', 'min', 'max', 'median'])
print(country_waste_summary)

# Export country waste summary for external analysis
country_waste_summary.to_csv("waste_summary_country.csv")
print("Waste summary for country data saved as 'waste_summary_country.csv'.")

# Visualization: Country population distribution
country_population_tolerance = country_Newdata['population_population_number_of_people'].quantile(quantile_threshold)
filtered_country_data = country_Newdata[country_Newdata['population_population_number_of_people'] <= country_population_tolerance]

sns.histplot(filtered_country_data['population_population_number_of_people'], kde=True)
plt.title('Country Population Distribution')
plt.show()

# Waste treatment percentages by income group (country)
country_Newdata.groupby('income_id')[waste_cols].mean().plot(kind='bar')
plt.title('Waste Treatment by Income Group (Country)')
plt.show()

# Visualization: Regional waste treatment using Plotly (country)
fig = px.bar(country_Newdata, x='region_id', y='waste_treatment_open_dump_percent', color='income_id')
fig.show()

# Save processed city data to CSV
save_city_path = "processed_city_data.csv"
try:
    save_with_backup(city_Newdata, save_city_path)
except IOError as e:
    raise IOError(f"Failed to save processed city data: {e}")

# Save processed country data to CSV
save_country_path = "processed_country_data.csv"
try:
    save_with_backup(country_Newdata, save_country_path)
except IOError as e:
    raise IOError(f"Failed to save processed country data: {e}")
