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
└── README                                    # Document
```
---

### **Description**
This project contains scripts for analyzing and visualizing data. The programs included are designed to process input data, perform statistical summaries and data visualizations to understand key trends.

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
You can install all packages using the following command:

```bash
pip install pandas numpy matplotlib plotly seaborn jupyterlab



1. **Clone this repository to your local machine**  
   Run the following command in your terminal to clone the data repository:
   ```bash
   git clone --depth 1 https://github.com/


2. **Navigate to the directory**  
   cd your-repository

3. **Ensure all required packages are installed**  

4. **Open the Jupyter Notebook in JupyterLab or Jupyter Notebook**
    ```bash
    ```jupyter lab data_analysis.ipynb

   ```

---

### **4. Testing and Code Review**
- Test your code locally before pushing changes.
- Review pull requests thoroughly before approving.

---

```

---

## **Project Setup**
1. Install required libraries:
   ```bash
   pip install pandas matplotlib
   ```

2. Run the analysis script:
   ```bash
   python scripts/covid_analysis.py
   ```

---

By following these rules, the team can work collaboratively, efficiently, and without conflicts. For any questions or issues, please open a **GitHub Issue** or reach out to the team.

---
