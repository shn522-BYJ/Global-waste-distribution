
# Data Summary Statistics Script

import os
import pandas as pd

# Function to preprocess data
def preprocess_data(data):
    data.fillna({
        "population_population_number_of_people": data["population_population_number_of_people"].median(),
        "total_msw_total_msw_generated_tons_year": data["total_msw_total_msw_generated_tons_year"].mean(),
        "waste_treatment_open_dump_percent": 0,
        "waste_treatment_recycling_percent": 0
    }, inplace=True)
    return data

# Load datasets
# Ensure paths are dynamically constructed for portability
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "..", "data")  # Adjust to locate the data directory
try:
    city_data_path = os.path.join(data_dir, "city_level_data_0_0.csv")
    country_data_path = os.path.join(data_dir, "country_level_data.csv")
    city_data = pd.read_csv(city_data_path, encoding='cp1252')
    country_data = pd.read_csv(country_data_path, encoding='cp1252')
except FileNotFoundError as e:
    raise FileNotFoundError(f"Required file is missing: {e}")

# Preprocess data
city_data = preprocess_data(city_data)
country_data = preprocess_data(country_data)

# Compute summary statistics
city_summary = city_data.groupby('region_id')[
    ['waste_treatment_open_dump_percent', 'waste_treatment_recycling_percent']
].agg(['mean', 'std', 'min', 'max', 'median'])

country_summary = country_data.groupby('region_id')[
    ['waste_treatment_open_dump_percent', 'waste_treatment_recycling_percent']
].agg(['mean', 'std', 'min', 'max', 'median'])

# Save summaries in the same directory as the script
output_dir = base_dir
city_summary.to_csv(os.path.join(output_dir, "city_summary.csv"))
country_summary.to_csv(os.path.join(output_dir, "country_summary.csv"))
