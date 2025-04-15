import streamlit as st
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression

with open("logistic_regression_model_health.pkl", 'rb') as file:
    model = pickle.load(file)

st.title("Medical Test Results Classification")
st.write("This app classifies test results into Normal, Inconclusive, or Abnormal using Logistic Regression Model.")

st.subheader("Enter Patient Information")

age = st.number_input("Age", min_value=0, max_value=120)
gender = st.selectbox("Gender",['Male','Female'])
blood_type = st.selectbox("Blood Type", ['A+','A-','B+','B-','AB+','AB-','O+','O-'])
medical_condition = st.selectbox("Medical Condition",['Cancer','Obesity','Diabetes','Asthma','Hypertension','Arthritis'])
admission_type = st.selectbox("Admission Type",['Urgent','Emergency','Elective'])
medication = st.selectbox("Medication",['Paracetamol','Ibuprofen','Aspirin','Penicillin','Lipitor'])