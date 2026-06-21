And this:

st.title("Household Electric Power Consumption Prediction Web App")
    Global_reactive_power = 0.13 
    Voltage = st.number_input("Enter voltage value", min_value=0, max_value=300, value=220)
    Global_intensity = st.number_input("Enter Global Intensity (A)")  
        
    Sub_metering_1 = st.number_input("Energy used by kitchen appliances (kWh)", min_value=0, max_value=1000, value=0)
    Sub_metering_2 = st.number_input("Energy used by laundry room appliances (kWh)", min_value=0, max_value=1000, value=0)
    Sub_metering_3 = st.number_input("Energy used by water heater & AC (kWh)", min_value=0, max_value=1000, value=0)
    Time_sec = st.time_input("Select a time:", key='Timess')
    selected_date = st.date_input("Select a date")
    year = selected_date.year 
    dayofweek = selected_date.weekday()
    month = selected_date.month 
    day = selected_date.day
    recent_value = st.number_input("Most recent Global Active Power (kW):", value=1.5, key="number")
    