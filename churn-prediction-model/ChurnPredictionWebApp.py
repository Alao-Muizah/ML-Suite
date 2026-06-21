# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 00:53:47 2025

@author: Muizzah
"""

import numpy as np
import pandas as pd
import streamlit as st
import sklearn
import pickle 
import lightgbm
import os 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "Churn_model.sav")

with open(model_path, "rb") as f:
    loaded_model = pickle.load(f)

def ContractServices(data):
    if data.InternetService == 'DSL' and data.Contract == 'Month-to-month':
        return 'Dmonth'
    elif data.InternetService == 'DSL' and data.Contract == 'One year':
        return  'D1year'        
    elif data.InternetService == 'DSL' and data.Contract == 'Two year':
        return  'D2years'	
    elif data.InternetService == 'Fiber optic' and data.Contract == 'Month-to-month':
        return  'Fmonth'
    elif data.InternetService == 'Fiber optic' and data.Contract == 'One year':
        return  'F1year'
    elif data.InternetService == 'Fiber optic' and data.Contract == 'Two year':
        return  'F2years'	
    elif data.InternetService == 'No' and data.Contract == 'Month-to-month':
        return  'Nmonth'
    elif data.InternetService == 'No' and data.Contract == 'One year': 
        return  'N1year'
    elif data.InternetService == 'No' and data.Contract == 'Two year':
        return  'N2years'	

st.set_page_config(layout="wide")

def churn(features):
    feature_names = ['gender','SeniorCitizen','Partner','Dependents','tenure','PhoneService','MultipleLines','InternetService',
                     'OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract',
                     'PaperlessBilling','PaymentMethod','MonthlyCharges','TotalCharges']
    features_dataframe = pd.DataFrame([features], columns=feature_names)
    features_dataframe['Ave_Charges'] = features_dataframe['TotalCharges'] / features_dataframe['MonthlyCharges']
    features_dataframe['ContractService'] =  features_dataframe.apply(ContractServices, axis=1)
    
    
    features_array = np.asarray(features)
    input_data_reshaped = features_array.reshape(1, -1)

    # y_prob = loaded_model.predict_proba(features_dataframe)[:, 1]
    # prediction = (y_prob >= 0.44).astype(int)
    prediction = loaded_model.predict(features_dataframe)
    print(prediction)
      
    if (prediction[0] == 0 ) :
        return "Customer will likely not churn"
    else:
        return "Customer will likely churn"
    
Senior_Citizen_mapping = {
    "yes": "1",
    "no ": "0"
}
Senior_Citizen_options = list(Senior_Citizen_mapping.keys())
    
def main():
     
    st.title("Customer Churn Prediction Web App")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

    with col2:
        SeniorCitizen_display = st.selectbox(
        "Senior Citizen",
        Senior_Citizen_options)
        SeniorCitizen = Senior_Citizen_mapping[SeniorCitizen_display]

    with col3:
        Partner = st.selectbox(
            "Partner",
            ["Yes", "No"]
        )

    with col4:
        Dependents = st.selectbox(
            "Dependents",
            ["Yes", "No"]
        )
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        tenure = st.number_input(
            "Tenure (Months)",
            min_value=0
        )

    with col2:
        PhoneService = st.selectbox(
            "Phone Service",
            ["Yes", "No"]
        )

    with col3:
        MultipleLines = st.selectbox(
            "Multiple Lines",
            ["Yes", "No", "No phone service"]
        )

    with col4:
        InternetService = st.selectbox(
            "Internet Service",
            ["DSL", "Fiber optic", "No"]
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        OnlineSecurity = st.selectbox(
            "Online Security",
            ["Yes", "No", "No internet service"]
        )

    with col2:
        OnlineBackup = st.selectbox(
            "Online Backup",
            ["Yes", "No", "No internet service"]
        )

    with col3:
        DeviceProtection = st.selectbox(
            "Device Protection",
            ["Yes", "No", "No internet service"]
        )           
    col1, col2, col3 = st.columns(3)

    with col1:
        TechSupport = st.selectbox(
            "Tech Support",
            ["Yes", "No", "No internet service"]
        )

    with col2:
        StreamingTV = st.selectbox(
            "Streaming TV",
            ["Yes", "No", "No internet service"]
        )

    with col3:
        StreamingMovies = st.selectbox(
            "Streaming Movies",
            ["Yes", "No", "No internet service"]
        )       

    col1, col2, col3 = st.columns(3)

    with col1:
        Contract = st.selectbox(
            "Contract",
            ["Month-to-month", "One year", "Two year"]
        )

    with col2:
        PaperlessBilling = st.selectbox(
            "Paperless Billing",
            ["Yes", "No"]
        )

    with col3:
        PaymentMethod = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        )             
    
    col1, col2 = st.columns(2)

    with col1:
        MonthlyCharges = st.number_input(
            "Monthly Charges",
            min_value=0.0,
            step=0.01
        )

    with col2:
        TotalCharges = st.number_input(
            "Total Charges",
            min_value=0.0,
            step=0.01
        )
    
    Churn = ''
    if st.button('Customer churn result',
                 use_container_width=True):                                  
        Churn = churn([gender, SeniorCitizen, Partner, Dependents, tenure,
        PhoneService, MultipleLines, InternetService, OnlineSecurity,
        OnlineBackup, DeviceProtection, TechSupport, StreamingTV,
        StreamingMovies, Contract, PaperlessBilling, PaymentMethod,
        MonthlyCharges, TotalCharges])

    st.success(Churn)
                                  

if __name__ == '__main__':
    main()
              
