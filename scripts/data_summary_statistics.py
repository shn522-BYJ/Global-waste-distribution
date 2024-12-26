# Load datasets
import pandas as pd

def load_data(data/city_level_data_0_0.csv):
    """Load data from a CSV file."""
    return pd.read_csv("data/city_level_data_0_0.csv", encoding='cp1252')
    
print(city_data)

def check_missing_values(city_data):
    """Print the count of missing values for each column."""
    print("Missing Values:\n", city_data.isnull().sum())
    
# Changed the tuple of column names to a list by enclosing it in square brackets []    
def group(city_data, iso3c,region_id,country_name,city_name,income_id,population_population_number_of_people,total_msw_total_msw_generated_tons_year,waste_treatment_open_dump_percent,waste_treatment_recycling_percent):
city_Newdata = city_data["iso3c","region_id","country_name","city_name","income_id","population_population_number_of_people","total_msw_total_msw_generated_tons_year","waste_treatment_open_dump_percent","waste_treatment_recycling_percent"].drop_duplicates()
print(city_Newdata)
return city_Newdata


# Check for missing values
def check_missing_values(city_Newdata):
print(city_Newdata.isnull().sum())

def group_and_average(city_Newdata, waste_treatment_open_dump_percent, waste_treatment_recycling_percent, region_id):
waste_summary = city_Newdata.groupby('region_id')['waste_treatment_open_dump_percent', 'waste_treatment_recycling_percent'].mean()
print(waste_summary)
return waste_summary

def group_and_size(city_Newdata, region_id):
city_counts = city_Newdata.groupby("region_id").size()
print(city_counts)
return city_counts

def?
city_total_data = city_Newdata.dropna(subset=["total_msw_total_msw_generated_tons_year"], inplace=False)
# This will drop rows where "total_msw_total_msw_generated_tons_year" has missing values
print(city_total_data)
return city_total_data

def?
city_total_data["total_msw_total_msw_generated_tons_year"] = pd.to_numeric(city_total_data["total_msw_total_msw_generated_tons_year"], errors='coerce')
city_total_data["population_population_number_of_people"] = pd.to_numeric(city_total_data["population_population_number_of_people"], errors='coerce')
city_total_data["msw per capita"] = city_total_data["total_msw_total_msw_generated_tons_year"] / city_total_data["population_population_number_of_people"]
print(city_total_data)
return city_total_data

# Check for missing values
def check_missing_values(city_total_data):
print(city_total_data.isnull().sum())

city_total_data = city_total_data.dropna(subset=["total_msw_total_msw_generated_tons_year"], inplace=False)
# This will drop rows where "total_msw_total_msw_generated_tons_year" has missing values
print(city_total_data)
return city_total_data

# Check for missing values
def check_missing_values(city_total_data):
print(city_total_data.isnull().sum())

def load_data(data/city_level_codebook_0.csv):
    """Load data from a CSV file."""
    return pd.read_csv("data/city_level_codebook_0.csv",encoding='latin-1')

city_Newcodebook = city_codebook.iloc[:,0:8]
city_Year_codebook = city_Newcodebook.dropna(subset=["year"])
tonnes_data = city_Year_codebook[city_Year_codebook['units'] == 'tonnes/year']
city_Year_codebook['year'] = city_Year_codebook['year'].astype(int)
tonnes_data

import pandas as pd

# Example: Rename columns in `tonnes_data` to match `city_com_data`
tonnes_data.rename(columns={
    "regionID": "region_id",
    "incomeID": "income_id"
}, inplace=True)

# Perform the merge on common columns
merged_data = pd.merge(
    city_total_data,
    tonnes_data[["city_name", "year"]],  # Only keep necessary columns from tonnes_data
    how="left",  # Left join to keep all rows from city_com_data
    on="city_name"  # Merge on city_name
)

# Check the resulting table
merged_data

# Check for missing values
print(merged_data.isnull().sum())

# Drop rows with missing 'year'
city_com = merged_data.dropna(subset=["year","total_msw_total_msw_generated_tons_year"],inplace=False)

# Check the size of the resulting DataFrame
print(f"Original data size: {merged_data.shape}")
print(f"Filtered data size: {city_com.shape}")

# Verify if all 'year' values are now valid
print(city_com["year"].isnull().sum())  # Should print 0

# Check for missing values
print(city_com.isnull().sum())

# Drop rows where "year" is NaN
city_com_codebook = city_com.dropna(subset=["year"])

# Convert the "year" column to integers
city_com_codebook['year'] = city_com_codebook['year'].astype(int)
city_com_codebook

# Load datasets
country_data = pd.read_csv("/content/country_level_data.csv", encoding='cp1252')
# Added encoding='latin-1' to handle the different file encoding
country_codebook = pd.read_csv("/content/country_level_codebook.csv", encoding='latin-1')

# Check for missing values
print(country_data.isnull().sum())

# Drop rows with missing 'year'
country_Newdata = country_data[["iso3c","region_id","country_name","income_id","gdp","population_population_number_of_people","total_msw_total_msw_generated_tons_year","waste_treatment_open_dump_percent","waste_treatment_recycling_percent"]].copy()

country_Newdata

# Check for missing values
print(country_Newdata.isnull().sum())

country_total_data = country_Newdata.dropna(subset=["total_msw_total_msw_generated_tons_year", "country_name"],inplace=False)
# Changed the first argument to subset=["total_msw_total_msw_generated_tons_year"]
# This will drop rows where "total_msw_total_msw_generated_tons_year" has missing values
country_total_data
country_total_data

print(country_total_data.isnull().sum())

waste_summary = country_total_data.groupby('region_id')[['waste_treatment_open_dump_percent', 'waste_treatment_recycling_percent']].mean()
print(waste_summary)

# Convert the 'total_msw_total_msw_generated_tons_year' column to numeric type before using nlargest
country_total_data["total_msw_total_msw_generated_tons_year"] = pd.to_numeric(country_total_data["total_msw_total_msw_generated_tons_year"], errors='coerce')

# Filter the top 10 cities based on total waste generated
top_countries = country_total_data.nlargest(10, "total_msw_total_msw_generated_tons_year")



import pandas as pd

# Convert the 'total_msw_total_msw_generated_tons_year' column to numeric type before using nsmallest
country_total_data["total_msw_total_msw_generated_tons_year"] = pd.to_numeric(
    country_total_data["total_msw_total_msw_generated_tons_year"], errors="coerce"
)

# Filter the bottom 10 countries based on total waste generated
bottom_countries = country_total_data.nsmallest(10, "total_msw_total_msw_generated_tons_year")



country_total_data["gdp per capita"] = country_total_data["gdp"] / country_total_data["population_population_number_of_people"]
country_total_data["msw per capita"] = country_total_data["total_msw_total_msw_generated_tons_year"] / country_total_data["population_population_number_of_people"]
country_total_data

# Group data by income group and compute average metrics
grouped_metrics = country_total_data.groupby("income_id")[["msw per capita", "gdp per capita"]].mean() # Use column names with spaces

# Display the result
print("Average Metrics by Income Group:\n", grouped_metrics)



print(country_total_data.isnull().sum())

country_codebook

print(country_codebook.isnull().sum())

country_Newcodebook = country_codebook.dropna(subset=["country_name","year"], inplace=False)
# Changed the first argument to subset=["total_msw_total_msw_generated_tons_year"]
# This will drop rows where "total_msw_total_msw_generated_tons_year" has missing values
country_Newcodebook

country_finalcodebook = country_Newcodebook.iloc[:,0:7]
country_finalcodebook

# Drop rows with missing 'year' and "country_name"
country_Year_codebook = country_finalcodebook.dropna(subset=["year","country_name"],inplace=False)
country_Year_codebook

print(country_Year_codebook.isnull().sum())

# Convert the "year" column to integers
country_Year_codebook['year'] = country_Year_codebook['year'].astype(int)

country_Year_codebook

# Filter rows based on the "units" column
tonnes_data1 = country_Year_codebook[country_Year_codebook['measurement'] == 'total_msw_total_msw_generated_tons_year']
tonnes_data1

print(tonnes_data1.isnull().sum())

import pandas as pd

# Perform the merge on common columns
country_com_codebook = pd.merge(
    country_total_data,
    tonnes_data1[["country_name", "year"]],  # Only keep necessary columns from tonnes_data
    how="left",  # Left join to keep all rows from city_com_data
    on="country_name"  # Merge on city_name
)

# Check the resulting table
country_com_codebook

# Check for missing values
print(country_com_codebook.isnull().sum())

# Drop rows where "year" is NaN
country_com_codebook = country_com_codebook.dropna(subset=["year"])

# Convert the "year" column to integers
country_com_codebook['year'] = country_com_codebook['year'].astype(int)

country_com_codebook

# Check for missing values
print(country_com_codebook.isnull().sum())



# Save the file to Google Drive
#merged_total_data.to_csv('/content/drive/My Drive/merged_total_data.csv',encoding='cp1252',index=False)

city_com_codebook.head()

city_com_codebook1 = city_com_codebook.iloc[:,[2,3,9]]
city_com_codebook1

country_com_codebook.head()

country_com_codebook1 = country_com_codebook.iloc[:,[2,9]]
country_com_codebook1

import pandas as pd

# Ensure the 'country_name' column exists in both tables
# Merge the tables on the 'country_name' column
merged_table = pd.merge(city_com_codebook1, country_com_codebook1, on="country_name", how="inner")

# Display the result
merged_table

# Check for missing values
print(merged_table.isnull().sum())

