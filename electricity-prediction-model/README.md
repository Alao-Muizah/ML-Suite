# Household Electricity Consumption Prediction

## Overview
This project is a **Streamlit web application** that predicts household **Global Active Power** based on user inputs and derived features.  
It performs **feature engineering**, including cyclical encoding of time features, lagged and rolling target variables, and uses a **LightGBM machine learning model** for accurate electricity consumption forecasting.  
The app allows users to input real-world electricity readings in an easy-to-understand format and get instant predictions.

## Technologies Used
- **Python**: pandas, numpy, scikit-learn, lightgbm, joblib, matplotlib  
- **Web App**: Streamlit  
- **IDE**: Spyder  

## Approach & Methodology
- **Data Preprocessing & Feature Engineering**:  
  - Cyclical encoding of time features (hour, day, month)  
  - Creation of lagged variables and rolling averages for Global Active Power  
- **Modeling**:  
  - Evaluated **Ridge Regression**, **Random Forest**, and **LightGBM**  
  - LightGBM selected as final model due to superior performance and stability  
- **Deployment**:  
  - Saved model using `joblib`  
  - Streamlit web app for interactive predictions  

## Model Evaluation

| Model          | MAE      | MSE      | RMSE     |
|----------------|----------|----------|----------|
| Ridge          | 0.029119 | 0.002210 | 0.047005 |
| Random Forest  | 0.022944 | 0.003844 | 0.062004 |
| LightGBM       | 0.012732 | 0.000556 | 0.023583 |

> **LightGBM consistently outperformed Ridge Regression and Random Forest**, with a significantly lower RMSE, indicating stable predictions with fewer large errors.

## Usage

1.  [Access the deployed streamlit app here](https://household-electricity-consumption-prediction-haziumxyzqr.streamlit.app/)
2.  [Download Dataset here](https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption)
3.  [Clone the Repo here](<https://github.com/Alao-Muizah/Household-Electricity-Consumption-Prediction/tree/Electricity-Branch>)
