%%writefile app.py
import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Food Safety Analyzer")

st.title("🍽️ AI Food Safety Analyzer")
st.write("Predict health risk due to food adulteration")

product_name = st.number_input("Product Name", 0)
adulterant = st.number_input("Adulterant", 0)
detection_method = st.number_input("Detection Method", 0)
action_taken = st.number_input("Action Taken", 0)

if st.button("Analyze"):
    features = np.array([[product_name, adulterant, detection_method, action_taken]])
    
    prediction = model.predict(features)
    
    risk_labels = ["Low", "Medium", "High"]
    result = risk_labels[prediction[0]]
    
    st.success(f"Predicted Risk: {result}")