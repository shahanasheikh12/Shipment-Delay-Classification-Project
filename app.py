import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model

with open('shipment_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title

st.title("Shipment Delay Prediction Dashboard")

st.write("Predict whether shipment will arrive on time or be delayed.")

# User Inputs

origin_warehouse = st.number_input(
    "Origin Warehouse",
    min_value=0,
    value=1
)

destination_store = st.number_input(
    "Destination Store",
    min_value=0,
    value=1
)

product = st.number_input(
    "Product",
    min_value=0,
    value=1
)

driver_identifier = st.number_input(
    "Driver Identifier",
    min_value=0,
    value=1
)

# Prediction

if st.button("Predict Shipment Status"):

    input_data = pd.DataFrame([{
        'origin_warehouse': origin_warehouse,
        'destination_store': destination_store,
        'product': product,
        'driver_identifier': driver_identifier
    }])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Shipment will arrive on time.")
    else:
        st.error("Shipment may be delayed.")
