# What a Waste Global Data Analysis

The dataset entitled What a Waste GLobal was provided by World Bank Data Catalog.

## **Data Source**
The original dataset can be found on https://datacatalog.worldbank.org/search/dataset/0039597/What-a-Waste-Global-Database

What a Waste is a global project to aggregate data on solid waste management from around the world. This database features the statistics collected. The information presented is the best available based on a study of current literature and limited conversations with waste agencies and authorities. While there may be variations in the definitions and quality of reporting for individual data points, general trends should reflect the global reality. All sources and any estimations are noted.

Geographical Coverage:   nearly all countries and over 330 cities

Metrics:        waste generation, composition, collection, disposal, user fees and financing, the 
                informal sector, administrative structures, public communication, and legal information.             

Temporal Coverage:       2010-2020

## Abbreviation of key metrics
iso3c:                 Country or region codes

region_id: 

      EAS: East Asia and Pacific
      ECS: Europe and Central Asia
      LCN: Latin America and the Caribbean
      MEA: Middle East and North Africa
      NAC: North America
      SAS: South Asia
      SSF: Sub-Saharan Africa
      
income_id/incomeID:      classification system for categorizing cities or countries based on their income levels

      LIC:   Low-Income Countries/Cities
      LMC:   Lower-Middle-Income Countries/Cities
      UMC:   Upper-Middle-Income Countries/Cities
      HIC:   High-Income Countries/Cities

total_msw_total_msw_generated_tons_year:  

     the total amount of municipal solid waste generated in a particular area (e.g., city, region, or country) measured in tons per year

waste_treatment_open_dump_percent:  
    
     the percentage of total waste in a given area (e.g., city, region, or country) that is disposed of using open dumping methods. 
    
     This is an important metric for evaluating the environmental and health implications of waste management practices and identifying areas needing improvement

waste_treatment_recycling_percent:   

     the percentage of total waste in a given area (e.g., city, region, or country) that is recycled
     
     This metric is often used to assess the efficiency and effectiveness of recycling programs, monitor progress toward sustainability goals, and identify opportunities for improvement in waste management systems.

---

## Data Analysis Project

### **Description**
This project analyzes city- and country-level data on waste management, which contains scripts for processing input data, performing statistical summaries and data visualizations to understand key trends.

### **Directory Structure**
Maintain this structure:
```
What a waste/
│
├── data/
   ├──city_level_codebook_0.csv
   ├──city_level_data_0_0.csv
   ├──country_level_codebook_0.csv
   ├──country_level_data_0_0.csv                        
├── scripts/                                  # Python analysis scripts
   ├──data_summary.py
   ├──data_visualizations.py             
   ├──statistical_analysis.py                 
├── notebooks/                                # Jupyter Notebooks
   ├──data_analysis.ipynb
├── requirements.txt                  # setting up the environment
└── README                            # Document
```
---

### **List of Programs**
1. **data_analysis.ipynb**
   
   This Jupyter Notebook connects to Google Drive to access datasets, performs data preprocessing, and generates visualizations. It also includes statistical summaries and data visualizations to understand key trends.

2. **data_summary.py**

   This script provides a concise overview of the dataset, calculates basic summary statistics (e.g., mean) and generates an overview of the data distribution to help understand the dataset's structure and key features.
   
3. **data_visualizations.py**
   
   This script generates various visualizations (e.g., bar charts, scatter plots) to represent data insights visually.
   
4. **statistical_analysis.py**

   This program analyze relationships between variables and draw meaningful conclusions from the data.

### **Python Packages**
To ensure the code runs smoothly, install the following Python packages:
- pandas
- numpy
- matplotlib.pyplot
- plotly.express
- seaborn
- jupyterlab

### **How to use**
1. You can install all packages using the following command:
```bash
pip install pandas numpy matplotlib plotly seaborn jupyterlab
```
2. Run the following command in your terminal to clone the data repository:
```bash
git clone --depth 1 https://github.com/shn522-BYJ/Global-waste-distribution.git
```
3. Navigate to the directory
```bash
    cd your-repository
```
4. Run the command to ensure all the required packages installed for your project.
```bash
   pip install -r requirements.txt
```
5. Run the script:
```bash
   python scripts/data_summary_statistics.py
```
6.Run the script:
```bash
   python scripts/data_visualization_statistics.py
```
7.Run the script:
```bash
   python scripts/data_advanced_analysis.py
```
---

Add a README. md file to your GitHub repository with instructions on how to run the code, including how to set up the environment (installing dependencies, setting up virtual environments, etc.).
   



4. **Open the Jupyter Notebook in JupyterLab or Jupyter Notebook**
    ```bash
    ```jupyter lab data_analysis.ipynb

---
