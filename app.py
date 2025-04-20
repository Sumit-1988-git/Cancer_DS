import streamlit as st
import numpy as np
import pickle

# Load the model
with open('random_forest_classifier.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit UI
st.title("Cancer Prediction Web App")
st.write("🔍 This app uses a Random Forest Classifier to predict type of cancer.")

# Collect user input
age = st.number_input("Age", min_value=1, max_value=90, value=30)
gender = st.selectbox("Gender", options={"Female", "Male"})
tumor_size = st.number_input("Tumor Size (in cm)", min_value=0.0, value=2.5)
location = st.selectbox("Tumor Location", options={"Frontal", "Occipital", "Parietal", "Temporal"})  # Update as per your values
histology = st.selectbox("Histology Type", options={"Astrocytoma", "Glioblastoma", "Medulloblastoma", "Meningioma"})          # Update as per your values
stage = st.selectbox("Cancer Stage", options={"Stage 0", "Stage 1", "Stage 2", "Stage 3", "Stage 4"})

symptom_1 = st.selectbox("Symptom 1", options=[0, 1, 2, 3])
symptom_2 = st.selectbox("Symptom 2", options=[0, 1, 2, 3])
symptom_3 = st.selectbox("Symptom 3", options=[0, 1, 2, 3])
radiation = st.selectbox("Radiation Treatment Received", options=["No", "Yes"])
surgery = st.selectbox("Surgery Performed", options=["No", "Yes"])
chemo = st.selectbox("Chemotherapy Received", options=["No", "Yes"])

survival_rate = st.number_input("Survival Rate (%)", min_value=0.0, max_value=100.0, value=75.0)
tumor_growth_rate = st.number_input("Tumor Growth Rate", min_value=0.0, value=1.2)

family_history = st.selectbox("Family History of Cancer", options=["No", "Yes"])
mri_result = st.selectbox("MRI Result Abnormality", options=["No", "Yes"])
follow_up = st.selectbox("Follow-Up Required?", options=["No", "Yes"])

# Button to predict
if st.button("Predict Follow-up Requirement"):
    input_data = np.array([[
        age,
        0 if gender == "Female" else 1,
        tumor_size,
        location,
        histology,
        stage,
        symptom_1,
        symptom_2,
        symptom_3,
        radiation,
        surgery,
        chemo,
        survival_rate,
        tumor_growth_rate,
        family_history,
        mri_result, 
        follow_up
    ]])

    # Prediction
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("🔴 Malignant Cancer !!!")
    else:
        st.success("🟢 Benign Cancer !!!")

