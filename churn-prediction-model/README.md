# Overview
This project builds a machine learning classification model to predict customer churn in the telecom industry. By analyzing customer demographics, service usage, and account information, the model identifies customers who are likely to leave, enabling businesses to take proactive retention actions.

---

## Live Dashboard

Access all deployed projects from a single interface: 
 [![Churn Prediction](https://img.shields.io/badge/Customer-Churn_Prediction-E17055?logo=databricks)](https://churn-prediction-model-haziumxyz.streamlit.app/)

---
# Problem
Customer churn leads to significant revenue loss for telecom companies.
The challenge is to accurately identify high-risk customers early using historical customer data.
Tech stack: 

# Tools 
Python, pandas, NumPy, scikit-learn, matplotlib, seaborn, LightGBM, pickle 

## Approach & Methodology

- **Exploratory Data Analysis (EDA)**
  - Analyzed customer demographics, service usage, and contract details.
  - Identified patterns and trends relevant to churn behavior.

- **Data Preprocessing**
  - Handled missing values and encoded categorical features.
  - Prepared data for modeling while ensuring consistency and accuracy.

- **Modeling**
  - Trained a **LightGBM Classifier** optimized for performance and scalability.
  - Tuned hyperparameters to improve predictive accuracy.

- **Evaluation**
  - Evaluated model performance using **ROC-AUC**, suitable for imbalanced classification problems.
  - Ensured the model reliably distinguishes churners from non-churners.

- **Deployment**
  - Saved the trained model using **pickle**.
  - Built a **Streamlit web app** to interactively predict customer churn.

# Results

ROC AUC Score: 0.834
Indicates strong ability to distinguish between churned and non-churned customers.

The model successfully identified high-risk customers, enabling targeted retention strategies.

# Business Impact
By identifying customers likely to churn, businesses can:

Launch targeted retention campaigns

Improve customer satisfaction

Reduce revenue loss

# Project Branch
About: The Telco customer churn data contains information about a fictional telco company that provided home phone and Internet services to 7043 customers in California in Q3. It indicates which customers have left, stayed, or signed up for their service. Multiple important demographics are included for each customer, as well as a Satisfaction Score, Churn Score, and Customer Lifetime Value (CLTV) index.

# Datatset
[Download Dataset here](https://github.com/Alao-Muizah/Churn-Prediction-Model/blob/ChurnBranch/WA_Fn-UseC_-Telco-Customer-Churn.csv)


