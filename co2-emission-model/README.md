# Overview
Built a high-performance regression model to predict vehicle CO₂ emissions (g/km) using engine and fuel consumption features.
The project focuses on handling multicollinearity and producing stable, interpretable predictions.

---

## Live Dashboard
Access all deployed projects from a single interface: 
 [![CO2 Prediction](https://img.shields.io/badge/CO2-Emission_Prediction-00B894?logo=leaflet)](https://c02-emission-model-haziumxyz.streamlit.app)

---
# Dataset
This dataset captures the details of how CO2 emissions by a vehicle can vary with the different features. The dataset has been taken from Canada Government official open data website. This is a compiled version. This contains data over a period of 7 years. There are a total of 7385 rows and 12 columns. 

# Tools & Libraries
Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

## Approach & Methodology

- **Data Preprocessing**
  - Cleaned and processed the dataset using **NumPy** and **Pandas**.
  - Standardized numerical features to ensure fair scaling for the model.

- **Exploratory Data Analysis (EDA)**
  - Explored feature distributions and relationships with CO₂ emissions.
  - Performed correlation analysis using a heatmap to identify strong inter-feature relationships.
  - Detected multicollinearity among fuel consumption and engine-related features.

- **Model Selection**
  - Selected **Ridge Regression (L2 regularization)** to stabilize coefficients and improve generalization.

- **Training & Testing**
  - Split the dataset into training and testing sets.
  - Trained the model on the training set.

- **Evaluation**
  - Assessed model performance using **R²**, **MAE**, and **RMSE**.
  - Ensured accurate and consistent predictions across the dataset.
# Model Evaluation
R² = 0.99 → Explains 99.2% of emission variability

MAE ≈ 2.77 g/km → Very low average prediction error

RMSE ≈ 4.41 g/km → Strong consistency with minimal outliers

Typical vehicle CO₂ emissions range from 100–400 g/km, making these errors very small.

# Dataset 
[C02-Emission-Model/CO2 Emissions_Canada.csv](https://github.com/Alao-Muizah/C02-Emission-Model/blob/CO2Branch/CO2%20Emissions_Canada.csv)

