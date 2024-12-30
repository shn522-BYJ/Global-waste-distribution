
# Data Visualization Script

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load preprocessed data
city_data = pd.read_csv("data/processed_city_data.csv")
country_data = pd.read_csv("data/processed_country_data.csv")

# Visualization: City population distribution
sns.histplot(city_data['population_population_number_of_people'], kde=True)
plt.title('City Population Distribution')
plt.show()

# Waste treatment by income group (city)
city_data.groupby('income_id')[
    ['waste_treatment_open_dump_percent', 'waste_treatment_recycling_percent']
].mean().plot(kind='bar')
plt.title('Waste Treatment by Income Group (City)')
plt.show()

# Regional waste treatment using Plotly (city)
fig = px.bar(city_data, x='region_id', y='waste_treatment_open_dump_percent', color='income_id')
fig.show()

# Visualization: Country population distribution
sns.histplot(country_data['population_population_number_of_people'], kde=True)
plt.title('Country Population Distribution')
plt.show()

# Waste treatment by income group (country)
country_data.groupby('income_id')[
    ['waste_treatment_open_dump_percent', 'waste_treatment_recycling_percent']
].mean().plot(kind='bar')
plt.title('Waste Treatment by Income Group (Country)')
plt.show()

# Regional waste treatment using Plotly (country)
fig = px.bar(country_data, x='region_id', y='waste_treatment_open_dump_percent', color='income_id')
fig.show()
