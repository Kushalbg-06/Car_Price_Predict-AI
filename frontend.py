import streamlit as st
import requests

st.title("🚗 Car Price Predictor")

year = st.number_input("Year")
km = st.number_input("KM Driven")

fuel = st.selectbox("Fuel", ["Petrol", "Diesel"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox("Owner", ["First", "Second"])
company = st.selectbox("Company", ["Maruti", "Hyundai", "Honda"])

if st.button("Predict"):
    res = requests.post(
        "http://127.0.0.1:8000/predict",
        json={
            "year": year,
            "km_driven": km,
            "fuel": fuel,
            "transmission": transmission,
            "owner": owner,
            "company": company
        }
    )
    st.write(res.json())