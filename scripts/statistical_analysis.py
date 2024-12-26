#!/usr/bin/env python
# coding: utf-8

# In[5]:


from google.colab import drive; drive.mount('/content/drive')


# In[ ]:


# Load datasets
import pandas as pd
city_data = pd.read_csv("/content/city_level_data_0_0.csv", encoding='cp1252')
# Added encoding='latin-1' to handle the different file encoding
city_codebook = pd.read_csv("/content/city_level_codebook_0.csv", encoding='latin-1')


# In[ ]:


city_data


# In[ ]:


# Check for missing values
print(city_data.isnull().sum())


# In[ ]:


city_Newdata = city_data[["iso3c","region_id","country_name","city_name","income_id","population_population_number_of_people","total_msw_total_msw_generated_tons_year","waste_treatment_open_dump_percent","waste_treatment_recycling_percent"]].copy()
# Changed the tuple of column names to a list by enclosing it in square brackets []
# This will correctly select the desired columns and create a copy in city_Newdata
city_Newdata


# In[ ]:


# Check for missing values
print(city_Newdata.isnull().sum())


# In[ ]:


waste_summary = city_Newdata.groupby('region_id')[['waste_treatment_open_dump_percent', 'waste_treatment_recycling_percent']].mean()
print(waste_summary)


# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns

# Population distribution
sns.histplot(city_Newdata['population_population_number_of_people'], kde=True)
plt.title('City Population Distribution')
plt.show()

# Waste treatment percentages by income group
waste_cols = ['waste_treatment_open_dump_percent', 'waste_treatment_recycling_percent']
city_Newdata.groupby('income_id')[waste_cols].mean().plot(kind='bar')
plt.title('Waste Treatment by Income Group')
plt.show()


# In[ ]:


import plotly.express as px

# Example: Regional Waste Treatment Visualization
fig = px.bar(city_Newdata, x='region_id', y='waste_treatment_open_dump_percent', color='income_id')
fig.show()


# In[ ]:


import plotly.express as px

# Example: Regional Waste Treatment Visualization
#fig = px.bar(city_Newdata, x='city_name', y='waste_treatment_open_dump_percent', color='income_id')
#fig.show()


# In[ ]:


import plotly.express as px

# Sort the data by 'waste_treatment_recycling_percent' in descending order
sorted_data = city_Newdata.sort_values(by='waste_treatment_open_dump_percent', ascending=False)

# Select the top 10 cities
top_10_cities = sorted_data.head(10)

# Create the bar chart
fig = px.bar(
    top_10_cities,
    x='city_name',
    y='waste_treatment_open_dump_percent',
    color='income_id',
    title='Top 10 Cities by Waste Treatment Open dump Percentage',
    labels={'waste_treatment_open_dump_percent': 'Open dump (%)'},
)

# Customize the layout
fig.update_layout(
    xaxis_title="City Name",
    yaxis_title="Open dump (%)",
    xaxis=dict(tickangle=45, categoryorder='total descending'),  # Ensure sorted order is preserved
    showlegend=True,
    template="plotly_white"
)

# Show the figure
fig.show()


# In[ ]:


import plotly.express as px

# Example: Regional Waste Treatment Visualization
fig = px.bar(city_Newdata, x='region_id', y='waste_treatment_recycling_percent', color='income_id')
fig.show()


# In[ ]:


import plotly.express as px

# Example: Regional Waste Treatment Visualization
#fig = px.bar(city_Newdata, x='city_name', y='waste_treatment_recycling_percent', color='income_id')
#fig.show()


# In[ ]:


import plotly.express as px

# Sort the data by 'waste_treatment_recycling_percent' in descending order
sorted_data = city_Newdata.sort_values(by='waste_treatment_recycling_percent', ascending=False)

# Select the top 10 cities
top_10_cities = sorted_data.head(10)

# Create the bar chart
fig = px.bar(
    top_10_cities,
    x='city_name',
    y='waste_treatment_recycling_percent',
    color='income_id',
    title='Top 10 Cities by Waste Treatment Recycling Percentage',
    labels={'waste_treatment_recycling_percent': 'Recycling Percentage (%)'},
)

# Customize the layout
fig.update_layout(
    xaxis_title="City Name",
    yaxis_title="Recycling Percentage (%)",
    xaxis=dict(tickangle=45, categoryorder='total descending'),  # Ensure sorted order is preserved
    showlegend=True,
    template="plotly_white"
)

# Show the figure
fig.show()


# In[ ]:


city_Newdata1 = city_data[["iso3c","region_id","country_name","city_name","income_id","population_population_number_of_people","total_msw_total_msw_generated_tons_year","waste_treatment_open_dump_percent","waste_treatment_recycling_percent"]].copy()
# Changed the tuple of column names to a list by enclosing it in square brackets []
# This will correctly select the desired columns and create a copy in city_Newdata
city_Newdata1


# In[ ]:


# Check for missing values
print(city_Newdata1.isnull().sum())


# In[ ]:


city_total_data = city_Newdata1.dropna(subset=["total_msw_total_msw_generated_tons_year"], inplace=False)
# Changed the first argument to subset=["total_msw_total_msw_generated_tons_year"]
# This will drop rows where "total_msw_total_msw_generated_tons_year" has missing values
city_total_data


# In[ ]:


city_total_data["total_msw_total_msw_generated_tons_year"] = pd.to_numeric(city_total_data["total_msw_total_msw_generated_tons_year"], errors='coerce')
city_total_data["population_population_number_of_people"] = pd.to_numeric(city_total_data["population_population_number_of_people"], errors='coerce')
city_total_data["msw per capita"] = city_total_data["total_msw_total_msw_generated_tons_year"] / city_total_data["population_population_number_of_people"]
city_total_data


# In[ ]:


# Check for missing values
print(city_total_data.isnull().sum())


# In[ ]:


city_total_data = city_total_data.dropna(subset=["total_msw_total_msw_generated_tons_year"], inplace=False)
# Changed the first argument to subset=["total_msw_total_msw_generated_tons_year"]
# This will drop rows where "total_msw_total_msw_generated_tons_year" has missing values
city_total_data


# In[ ]:


# Check for missing values
print(city_total_data.isnull().sum())


# In[ ]:


import matplotlib.pyplot as plt
import pandas as pd
# Convert the 'total_msw_total_msw_generated_tons_year' column to numeric type before using nlargest
city_total_data["total_msw_total_msw_generated_tons_year"] = pd.to_numeric(city_total_data["total_msw_total_msw_generated_tons_year"], errors='coerce')

# Filter the top 10 cities based on total waste generated
#cities = city_total_data.nlargest(326, "total_msw_total_msw_generated_tons_year")
top_cities = city_total_data.nlargest(10, "total_msw_total_msw_generated_tons_year")
# Dynamically adjust the figure size based on the number of cities
plt.figure(figsize=(max(15, len(top_cities) / 2), 8))  # Adjust width dynamically

# Plot the bar chart
plt.bar(top_cities["city_name"], top_cities["total_msw_total_msw_generated_tons_year"], color='orange')

# Customize the plot
plt.xticks(rotation=90, fontsize=10)  # Rotate X-axis labels for better readability
plt.xlabel("City Name", fontsize=14)
plt.ylabel("Total MSW Generated (tons/Year)", fontsize=14)
plt.title("Waste Generated by Top 10 Cities", fontsize=16)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()


# In[ ]:


import matplotlib.pyplot as plt
import pandas as pd
# Convert the 'total_msw_total_msw_generated_tons_year' column to numeric type before using nlargest
city_total_data["msw per capita"] = pd.to_numeric(city_total_data["msw per capita"], errors='coerce')

# Filter the top 10 cities based on total waste generated
#cities = city_total_data.nlargest(326, "total_msw_total_msw_generated_tons_year")
top_cities = city_total_data.nlargest(10, "msw per capita")
# Dynamically adjust the figure size based on the number of cities
plt.figure(figsize=(max(15, len(top_cities) / 2), 8))  # Adjust width dynamically

# Plot the bar chart
plt.bar(top_cities["city_name"], top_cities["msw per capita"], color='grey')

# Customize the plot
plt.xticks(rotation=90, fontsize=10)  # Rotate X-axis labels for better readability
plt.xlabel("City Name", fontsize=14)
plt.ylabel("MSW per capita (tons/Year)", fontsize=14)
plt.title("Waste per capita Generated by Top 10 Cities", fontsize=16)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()


# In[ ]:


city_codebook


# In[ ]:


city_Newcodebook = city_codebook.iloc[:,0:8]
city_Year_codebook = city_Newcodebook.dropna(subset=["year"])
tonnes_data = city_Year_codebook[city_Year_codebook['units'] == 'tonnes/year']
city_Year_codebook['year'] = city_Year_codebook['year'].astype(int)
tonnes_data


# 

# In[6]:


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


# In[ ]:


# Check for missing values
print(merged_data.isnull().sum())


# In[ ]:


# Drop rows with missing 'year'
city_com = merged_data.dropna(subset=["year","total_msw_total_msw_generated_tons_year"],inplace=False)

# Check the size of the resulting DataFrame
print(f"Original data size: {merged_data.shape}")
print(f"Filtered data size: {city_com.shape}")

# Verify if all 'year' values are now valid
print(city_com["year"].isnull().sum())  # Should print 0


# In[ ]:


# Check for missing values
print(city_com.isnull().sum())


# In[ ]:


# Drop rows where "year" is NaN
city_com_codebook = city_com.dropna(subset=["year"])

# Convert the "year" column to integers
city_com_codebook['year'] = city_com_codebook['year'].astype(int)
city_com_codebook


# In[ ]:


# Trend analysis for a specific metric
yearly_trend = city_com_codebook.groupby('year')['waste_treatment_open_dump_percent'].mean()
yearly_trend.plot()
plt.title('City Waste Treatment open_dump Trends Over Time')
plt.show()


# In[ ]:


# Trend analysis for a specific metric
yearly_trend = city_com_codebook.groupby('year')['waste_treatment_recycling_percent'].mean()
yearly_trend.plot()
plt.title('City Waste Treatment recycling Trends Over Time')
plt.show()


# In[ ]:


# Load datasets
country_data = pd.read_csv("/content/country_level_data.csv", encoding='cp1252')
# Added encoding='latin-1' to handle the different file encoding
country_codebook = pd.read_csv("/content/country_level_codebook.csv", encoding='latin-1')


# In[ ]:


# Check for missing values
print(country_data.isnull().sum())


# In[ ]:


# Drop rows with missing 'year'
country_Newdata = country_data[["iso3c","region_id","country_name","income_id","gdp","population_population_number_of_people","total_msw_total_msw_generated_tons_year","waste_treatment_open_dump_percent","waste_treatment_recycling_percent"]].copy()

country_Newdata


# In[ ]:


# Check for missing values
print(country_Newdata.isnull().sum())


# In[ ]:


country_total_data = country_Newdata.dropna(subset=["total_msw_total_msw_generated_tons_year", "country_name"],inplace=False)
# Changed the first argument to subset=["total_msw_total_msw_generated_tons_year"]
# This will drop rows where "total_msw_total_msw_generated_tons_year" has missing values
country_total_data
country_total_data


# In[ ]:


print(country_total_data.isnull().sum())


# In[ ]:


waste_summary = country_total_data.groupby('region_id')[['waste_treatment_open_dump_percent', 'waste_treatment_recycling_percent']].mean()
print(waste_summary)


# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns
# Load datasets
import pandas as pd
# Population distribution
sns.histplot(country_total_data['population_population_number_of_people'], kde=True)
plt.title('Country Population Distribution')
plt.show()

# Waste treatment percentages by income group
waste_cols = ['waste_treatment_open_dump_percent', 'waste_treatment_recycling_percent']
country_total_data.groupby('income_id')[waste_cols].mean().plot(kind='bar')
plt.title('Waste Treatment by Income Group')
plt.show()


# In[ ]:


import plotly.express as px

# Example: Regional Waste Treatment Visualization
fig = px.bar(country_total_data, x='region_id', y='waste_treatment_open_dump_percent', color='income_id')
fig.show()


# In[ ]:


import plotly.express as px

# Example: Regional Waste Treatment Visualization
fig = px.bar(country_total_data, x='region_id', y='waste_treatment_recycling_percent', color='income_id')
fig.show()


# In[ ]:


import plotly.express as px

# Example: Regional Waste Treatment Visualization
fig = px.bar(country_total_data, x='country_name', y='waste_treatment_recycling_percent', color='income_id')
fig.show()


# In[ ]:


# Convert the 'total_msw_total_msw_generated_tons_year' column to numeric type before using nlargest
country_total_data["total_msw_total_msw_generated_tons_year"] = pd.to_numeric(country_total_data["total_msw_total_msw_generated_tons_year"], errors='coerce')

# Filter the top 10 cities based on total waste generated
top_countries = country_total_data.nlargest(10, "total_msw_total_msw_generated_tons_year")

# Dynamically adjust the figure size based on the number of cities
plt.figure(figsize=(max(15, len(top_cities) / 2), 8))  # Adjust width dynamically

# Plot the bar chart
plt.bar(top_countries["country_name"], top_countries["total_msw_total_msw_generated_tons_year"], color='orange')

# Customize the plot
plt.xticks(rotation=90, fontsize=10)  # Rotate X-axis labels for better readability
plt.xlabel("Country Name", fontsize=14)
plt.ylabel("Total MSW Generated (tons/Year)", fontsize=14)
plt.title("Waste Generated by Top 10 Countries", fontsize=16)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()


# In[ ]:


import matplotlib.pyplot as plt
import pandas as pd

# Convert the 'total_msw_total_msw_generated_tons_year' column to numeric type before using nsmallest
country_total_data["total_msw_total_msw_generated_tons_year"] = pd.to_numeric(
    country_total_data["total_msw_total_msw_generated_tons_year"], errors="coerce"
)

# Filter the bottom 10 countries based on total waste generated
bottom_countries = country_total_data.nsmallest(10, "total_msw_total_msw_generated_tons_year")

# Dynamically adjust the figure size based on the number of countries
plt.figure(figsize=(max(15, len(bottom_countries) / 2), 8))  # Adjust width dynamically

# Plot the bar chart
plt.bar(bottom_countries["country_name"], bottom_countries["total_msw_total_msw_generated_tons_year"], color="green")

# Customize the plot
plt.xticks(rotation=90, fontsize=10)  # Rotate X-axis labels for better readability
plt.xlabel("Country Name", fontsize=14)
plt.ylabel("Total MSW Generated (tons/Year)", fontsize=14)
plt.title("Waste Generated by Bottom 10 Countries", fontsize=16)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Display the plot
plt.show()


# In[ ]:


country_total_data["gdp per capita"] = country_total_data["gdp"] / country_total_data["population_population_number_of_people"]
country_total_data


# In[ ]:


print(country_total_data.isnull().sum())


# In[ ]:


country_codebook


# In[ ]:


print(country_codebook.isnull().sum())


# In[ ]:


country_Newcodebook = country_codebook.dropna(subset=["country_name","year"], inplace=False)
# Changed the first argument to subset=["total_msw_total_msw_generated_tons_year"]
# This will drop rows where "total_msw_total_msw_generated_tons_year" has missing values
country_Newcodebook


# In[ ]:





# In[ ]:


country_finalcodebook = country_Newcodebook.iloc[:,0:7]
country_finalcodebook


# In[ ]:


# Drop rows with missing 'year' and "country_name"
country_Year_codebook = country_finalcodebook.dropna(subset=["year","country_name"],inplace=False)
country_Year_codebook


# In[ ]:


print(country_Year_codebook.isnull().sum())


# In[ ]:


# Convert the "year" column to integers
country_Year_codebook['year'] = country_Year_codebook['year'].astype(int)

country_Year_codebook


# In[ ]:


# Filter rows based on the "units" column
tonnes_data1 = country_Year_codebook[country_Year_codebook['measurement'] == 'total_msw_total_msw_generated_tons_year']
tonnes_data1


# In[ ]:


print(tonnes_data1.isnull().sum())


# In[ ]:


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


# In[ ]:


# Check for missing values
print(country_com_codebook.isnull().sum())


# In[ ]:


# Drop rows where "year" is NaN
country_com_codebook = country_com_codebook.dropna(subset=["year"])

# Convert the "year" column to integers
country_com_codebook['year'] = country_com_codebook['year'].astype(int)

country_com_codebook


# In[ ]:


# Check for missing values
print(country_com_codebook.isnull().sum())


# In[ ]:


# Trend analysis for a specific metric
yearly_trend = country_com_codebook.groupby('year')['waste_treatment_open_dump_percent'].mean()
yearly_trend.plot()
plt.title('Country Waste Treatment open_dump Trends Over Time')
plt.show()


# In[ ]:


# Trend analysis for a specific metric
yearly_trend = country_com_codebook.groupby('year')['waste_treatment_recycling_percent'].mean()
yearly_trend.plot()
plt.title('Country Waste Treatment recycling Trends Over Time')
plt.show()


# In[ ]:


# Save the file to Google Drive
#merged_total_data.to_csv('/content/drive/My Drive/merged_total_data.csv',encoding='cp1252',index=False)


# In[ ]:


city_com_codebook.head()


# In[ ]:


city_com_codebook1 = city_com_codebook.iloc[:,[2,3,7]]
city_com_codebook1


# In[ ]:


country_com_codebook.head()


# In[ ]:


country_com_codebook1 = country_com_codebook.iloc[:,[2,9]]
country_com_codebook1


# In[ ]:


import pandas as pd

# Ensure the 'country_name' column exists in both tables
# Merge the tables on the 'country_name' column
merged_table = pd.merge(city_com_codebook1, country_com_codebook1, on="country_name", how="inner")

# Display the result
merged_table




# In[ ]:


# Check for missing values
print(merged_table.isnull().sum())


# In[ ]:


# Example Analysis: Correlation between GDP per capita and MSW per capita
correlation = merged_table["gdp per capita"].corr(merged_table["msw per capita"])
print(f"Correlation between GDP per capita and MSW per capita: {correlation}")

# Optional: Visualization
import matplotlib.pyplot as plt

plt.scatter(merged_table["gdp per capita"], merged_table["msw per capita"], color='gold')
plt.title("Correlation")
plt.xlabel("GDP per Capita")
plt.ylabel("MSW per Capita")
plt.grid()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




