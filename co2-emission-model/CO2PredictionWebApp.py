
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 12:41:23 2025

@author: Muizzah
"""
import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
import streamlit as st
import cloudpickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "C02_model.sav")
DATA_PATH = os.path.join(BASE_DIR, "CO2 Emissions_Canada.csv")


with open(MODEL_PATH, "rb") as f:
    loaded_model = cloudpickle.load(f)


dataset = pd.read_csv(DATA_PATH)

make_options = sorted(dataset["Make"].unique().tolist())
model_options = sorted(dataset["Model"].unique().tolist())
vehicle_class_options = sorted(dataset["Vehicle Class"].unique().tolist())
transmission_mapping = {
    "Automatic 4-Speed": "A4",
    "Automatic 5-Speed": "A5",
    "Automatic 6-Speed": "A6",
    "Automatic 7-Speed": "A7",
    "Automatic 8-Speed": "A8",
    "Automated Manual 6-Speed": "AM6",
    "Automated Manual 7-Speed": "AM7",
    "Automatic Select Shift 5-Speed": "AS5",
    "Automatic Select Shift 6-Speed": "AS6",
    "Automatic Select Shift 8-Speed": "AS8",
    "Continuously Variable Transmission": "AV",
    "CVT 7-Speed": "AV7",
    "CVT 8-Speed": "AV8",
    "Manual 5-Speed": "M5",
    "Manual 6-Speed": "M6",
    "Manual 7-Speed": "M7"
}
transmission_option = list(transmission_mapping.keys())

fuel_type_mapping = {
    "Diesel": "D",
    "Ethanol (E85)": "E",
    "Natural Gas": "N",
    "Regular Gasoline": "X",
    "Premium Gasoline": "Z"
}
fuel_type_options = list(fuel_type_mapping.keys())


st.set_page_config(
    page_title="CO2 Emission Predictor",
    layout="wide"
)

# DARK THEME
st.markdown("""
<style>

.stApp{
    background-color:#0b1020;
}

h1,h2,h3,label,p{
    color:white !important;
}

div[data-baseweb="select"]{
    background-color:#151b2f;
}

input{
    background-color:#151b2f !important;
    color:white !important;
}

.stButton button{
    width:100%;
    height:50px;
    border-radius:10px;
}

.block-container{
    padding-top:2rem;
}

</style>
""", unsafe_allow_html=True)


def co2(features):

    feature_names = ['Make', 'Model', 'Vehicle Class', 'Engine Size(L)', 'Cylinders',
                    'Transmission', 'Fuel Type', 'Fuel Consumption City (L/100 km)',
                    'Fuel Consumption Hwy (L/100 km)', 'Fuel Consumption Comb (L/100 km)',
                    'Fuel Consumption Comb (mpg)']
    features_dataframe = pd.DataFrame([features], columns=feature_names)
    prediction = loaded_model.predict(features_dataframe)
    return prediction
     


def main():
     
    st.title("CO2 Emission Prediction")
    st.write("Enter vehicle details below for prediction")

    # ==================================
    # ROW 1
    # ==================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        make = st.selectbox(
            "Make",
            make_options
        )

    with col2:
        model_options = sorted(
            dataset[dataset["Make"] == make]["Model"].unique()
        )

        model = st.selectbox(
            "Model",
            model_options
        )

    with col3:
        vehicle_class = st.selectbox(
            "Vehicle Class",
            vehicle_class_options
        )

    with col4:
        fuel_type_display = st.selectbox(
        "Fuel Type",
        fuel_type_options)
        fuel_type = fuel_type_mapping[fuel_type_display]

    # ==================================
    # ROW 2
    # ==================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        engine_size = st.number_input(
            "Engine Size (L)",
            min_value=0.0,
            step=0.1
        )

    with col2:
        cylinders = st.number_input(
            "Cylinders",
            min_value=1,
            step=1
        )

    with col3:
        transmission_display = st.selectbox(
        "Transmission",
        list(transmission_mapping.keys())
    )

    transmission = transmission_mapping[transmission_display]

    with col4:
        fuel_consumption_mpg = st.number_input(
            "Fuel Consumption Comb (mpg)"
        )

    # ==================================
    # ROW 3
    # ==================================

    col1, col2, col3 = st.columns(3)

    with col1:
        fuel_consumption_city = st.number_input(
            "Fuel Consumption City (L/100 km)"
        )

    with col2:
        fuel_consumption_hwy = st.number_input(
            "Fuel Consumption Hwy (L/100 km)"
        )

    with col3:
        fuel_consumption_comb = st.number_input(
            "Fuel Consumption Comb (L/100 km)"
        )
    
    C02 = ''
    if st.button('C02 Emission result',
                 use_container_width=True):                                  
        C02 = co2([make, model, vehicle_class, engine_size, cylinders,
        transmission, fuel_type, fuel_consumption_city, fuel_consumption_hwy,
        fuel_consumption_comb, fuel_consumption_mpg])

    st.success(C02)
    

if __name__ == '__main__':

    main()
