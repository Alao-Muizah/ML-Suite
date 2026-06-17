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

loaded_model = pickle.load(open("Churn_model.sav", 'rb'))

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
    

    
def main():
     
    st.title("Customer churn prediction Web App")
    gender = st.text_input("Gender (Male/Female)").capitalize()
    SeniorCitizen = st.number_input("Is customer a Senior Citizen? (0 = No, 1 = Yes)")
    Partner = st.text_input("Does customer have a partner? (Yes/No)").capitalize()
    Dependents = st.text_input("Does customer have dependents? (Yes/No)").capitalize()
    tenure = st.number_input("Enter tenure (Number of months the customer has stayed)")
    PhoneService = st.text_input("Does customer have Phone Service? (Yes/No)").capitalize()
    MultipleLines = st.text_input("Multiple Lines (No, Yes, No phone service)").capitalize()
    InternetService = st.text_input("Internet Service Type (DSL, Fiber optic, No)").capitalize()
    OnlineSecurity = st.text_input("Online Security (Yes, No, No internet service)").capitalize()
    OnlineBackup = st.text_input("Online Backup (Yes, No, No internet service)").capitalize()
    DeviceProtection = st.text_input("Device Protection (Yes, No, No internet service)").capitalize()
    TechSupport = st.text_input("Tech Support (Yes, No, No internet service)").capitalize()
    StreamingTV = st.text_input("Streaming TV (Yes, No, No internet service)").capitalize()
    StreamingMovies = st.text_input("Streaming Movies (Yes, No, No internet service)").capitalize()
    Contract = st.text_input("Contract Type (Month-to-month, One year, Two year)").capitalize()
    PaperlessBilling = st.text_input("Paperless Billing (Yes/No)").capitalize()
    PaymentMethod = st.text_input("Payment Method (Electronic check, Mailed check, Bank transfer (automatic)r, Credit card (automatic)").capitalize()
    MonthlyCharges = st.number_input("Monthly Charges")
    TotalCharges = st.number_input("Total Charges")
    
                                   
                                  
    Churn = ''
    if st.button('Customer churn result'):                                  
        Churn = churn([gender, SeniorCitizen, Partner, Dependents, tenure,
        PhoneService, MultipleLines, InternetService, OnlineSecurity,
        OnlineBackup, DeviceProtection, TechSupport, StreamingTV,
        StreamingMovies, Contract, PaperlessBilling, PaymentMethod,
        MonthlyCharges, TotalCharges])

    st.success(Churn)
                                  

if __name__ == '__main__':
    main()
                            

                                  


