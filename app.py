import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load your trained model (ensure best_model.pkl is in your directory)
model = joblib.load("best_model.pkl")

st.set_page_config(page_title="Employee Salary Prediction", layout="centered")
st.title("💼 Employee Salary Prediction App")

st.markdown("Enter the employee details below to predict the estimated salary.")

# User input fields
experience = st.number_input("Years of Experience", min_value=0.0, max_value=50.0, step=0.1)
education_level = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "PhD"])
job_title = st.selectbox("Job Title", ["Software Engineer", "Data Scientist", "Project Manager", "HR Manager"])
location = st.selectbox("Location", ["New York", "San Francisco", "London", "Remote"])

# Encoding education level
education_map = {"High School": 0, "Bachelor's": 1, "Master's": 2, "PhD": 3}
education_encoded = education_map[education_level]

# Encoding job title
job_map = {
    "Software Engineer": 0,
    "Data Scientist": 1,
    "Project Manager": 2,
    "HR Manager": 3
}
job_encoded = job_map[job_title]

# Encoding location
location_map = {
    "New York": 0,
    "San Francisco": 1,
    "London": 2,
    "Remote": 3
}
location_encoded = location_map[location]

# Predict salary
if st.button("Predict Salary"):
    input_data = np.array([[experience, education_encoded, job_encoded, location_encoded]])
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated Salary: ${prediction:,.2f}")
