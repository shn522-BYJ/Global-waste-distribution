
# Advanced Data Analysis Script

import os
import pandas as pd

# Function to save with backup
def save_with_backup(data, path):
    if os.path.exists(path):
        backup_path = path.replace(".csv", "_backup.csv")
        os.rename(path, backup_path)
    data.to_csv(path, index=False)

# Load datasets
city_data = pd.read_csv("data/processed_city_data.csv")
country_data = pd.read_csv("data/processed_country_data.csv")

# Save backups of processed data
save_with_backup(city_data, "data/processed_city_data.csv")
save_with_backup(country_data, "data/processed_country_data.csv")
