
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt

# Load model

with open('shipment_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title

st.title("Shipment Delay Prediction Dashboard")

st.write("Predict whether shipment will arrive on time or be delayed.")

# User Inputs

warehouse_block = st.selectbox(
    "Warehouse Block",
    [0,1,2,3,4]
)

mode_of_shipment = st.selectbox(
    "Mode of Shipment",
    [0,1,2]
)

customer_care_calls = st.slider(
    "Customer Care Calls",
    0,
    10,
    3
)

customer_rating = st.slider(
    "Customer Rating",
    1,
    5,
    3
)

cost_of_product = st.number_input(
    "Cost of Product",
    0,
    1000,
    200
)

prior_purchases = st.slider(
    "Prior Purchases",
    0,
    20,
    5
)

product_importance = st.selectbox(
    "Product Importance",
    [0,1,2]
)

gender = st.selectbox(
    "Gender",
    [0,1]
)

discount_offered = st.slider(
    "Discount Offered",
    0,
    100,
    10
)

weight_in_gms = st.number_input(
    "Weight in Grams",
    100,
    10000,
    3000
)

# Prediction Button

if st.button("Predict Shipment Status"):

    input_data = np.array([[
        warehouse_block,
        mode_of_shipment,
        customer_care_calls,
        customer_rating,
        cost_of_product,
        prior_purchases,
        product_importance,
        gender,
        discount_offered,
        weight_in_gms
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Shipment will arrive on time.")
    else:
        st.error("Shipment may be delayed.")
