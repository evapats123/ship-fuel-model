import streamlit as st
import pandas as pd
import joblib

# Load trained model
## Option 2 (portable style with forward slashes)
model = joblib.load(r"C:\Users\evapa.EVAPATSBITCES\ship_fuel_model\model\ship_fuel_model_enhanced.pkl")


# Page setup
st.set_page_config(page_title="Ship Fuel Estimator", layout="centered")
st.title("🚢 Ship Fuel Consumption Estimator")

# Input fields
distance = st.number_input("Distance (km)", min_value=1.0)
fuel_type = st.selectbox("Fuel Type", ["HFO", "Diesel"])
engine_eff = st.slider("Engine Efficiency (%)", min_value=50.0, max_value=100.0, value=85.0)
avg_sog = st.number_input("Average Speed Over Ground (knots)", min_value=0.0)
speed_std = st.number_input("Speed Variability (std)", min_value=0.0)
idle_pct = st.slider("Idle Time Percentage", 0.0, 1.0, 0.1)
trip_duration = st.number_input("Trip Duration (minutes)", min_value=1.0)
est_distance = st.number_input("Estimated Distance Traveled (km)", min_value=1.0)
msg_count = st.number_input("Number of AIS Messages", min_value=1)

# Encode fuel type
fuel_type_encoded = 0 if fuel_type == "Diesel" else 1

# Predict button
if st.button("Predict Fuel Consumption"):
    input_data = pd.DataFrame([[
        distance, fuel_type_encoded, engine_eff,
        avg_sog, speed_std, idle_pct,
        trip_duration, est_distance, msg_count
    ]], columns=[
        "distance", "fuel_type", "engine_efficiency",
        "avg_sog", "speed_std", "idle_time_pct",
        "trip_duration_min", "estimated_distance_km", "num_position_reports"
    ])

    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Fuel Consumption: {prediction:,.2f} units")
