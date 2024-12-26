# Global-waste-distribution

This project uses What a Waste GLobal Database provided by World Bank Data Catalog.


## **Data Source**
The original dataset can be found on https://datacatalog.worldbank.org/search/dataset/0039597/What-a-Waste-Global-Database

### **How to Download the Data**

1. **Download directly from Data Source**  

2. **Clone the shn522-BYJ Repository**  
   Run the following command in your terminal to clone the data repository:
   ```bash
   git clone --depth 1 https://github.com/shn522-BYJ/Global-waste-distribution.git

3. **Move the dataset to Your Project**  
   Open `data` folder and copy 4 .csv files

4. **Remove the Original Repository** (Optional):
   ```bash
   rm -rf COVID-19
   ```

---
### **2. Directory Structure**
Maintain this structure:
```
What a waste/
│
├── data/
   ├──city_level_codebook_0.csv
   ├──city_level_data_0_0.csv
   ├──country_level_codebook_0.csv
   ├──country_level_data_0_0.csv                        
├── scripts/
   ├──data_summary.py
   ├──data_visualizations.py                  # Visualizations and plots
   ├──statistical_analysis.py                 # Python analysis scripts
├── notebooks/                                # Jupyter Notebooks
   ├──data_analysis.ipynb                                               
├── results/                                  # Output files
├── README.md                                 # Documentation
└── .gitignore                                # Ignore unnecessary files
```
---
### **3. Coding Standards**
- Follow **PEP 8** guidelines for Python.
- Use meaningful variable and function names.
- Add comments and docstrings:
   ```python
   def load_data(file_path):
       """
       Load a CSV file into a pandas DataFrame.

       Args:
           file_path (str): Path to the CSV file.

       Returns:
           pd.DataFrame: DataFrame containing the data.
       """
       return pd.read_csv(file_path)
   ```
---

### **4. Testing and Code Review**
- Test your code locally before pushing changes.
- Review pull requests thoroughly before approving.

---

### **5. .gitignore Rules**
To avoid committing unnecessary files, add the following to `.gitignore`:
```
__pycache__/
*.csv.zip
*.csv.tar
*.log
data/raw_data/
figures/temp/
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
