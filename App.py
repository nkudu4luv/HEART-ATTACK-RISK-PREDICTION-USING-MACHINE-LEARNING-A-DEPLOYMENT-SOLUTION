import streamlit as st
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the saved model and scaler
logreg = joblib.load('logreg_model.pkl')
scaler = joblib.load('scaler.pkl')

# Apply custom page style
st.markdown(
    """
    <style>
    body {
        background-color: #D3D3D3;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background-color: #D3D3D3;
    }
    .stButton > button {
        background-color: #FF4B4B;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px;
        width: 100%;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #E63946;
    }
    .title {
        color: #2C3E50;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit interface
st.markdown("<h1 class='title'>Heart Disease Prediction Web App</h1>", unsafe_allow_html=True)

# User input for prediction
st.header('📊 Enter User Data for Prediction')

# Create inputs for all 13 features in the dataset
age = st.number_input('Age', min_value=20, max_value=120, value=50)
sex = st.selectbox('Sex', ['Male', 'Female'])
cp = st.selectbox('Chest Pain Type', [0, 1, 2, 3])
trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=80, max_value=200, value=120)
chol = st.number_input('Serum Cholesterol (mg/dL)', min_value=100, max_value=600, value=200)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dL', [0, 1])  # 0 = No, 1 = Yes
restecg = st.selectbox('Resting Electrocardiographic Results', [0, 1, 2])
thalach = st.number_input('Max Heart Rate Achieved', min_value=50, max_value=220, value=150)
exang = st.selectbox('Exercise Induced Angina', [0, 1])  # 0 = No, 1 = Yes
oldpeak = st.number_input('ST Depression Induced by Exercise', value=1.0)
slope = st.selectbox('Slope of Peak Exercise ST Segment', [0, 1, 2])
ca = st.number_input('Number of Major Vessels Colored by Fluoroscopy', min_value=0, max_value=4, value=1)
thal = st.selectbox('Thalassemia', [0, 1, 2, 3])

# Convert categorical inputs to numeric values
sex = 1 if sex == 'Male' else 0

# Prepare the input data
user_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
user_data_scaled = scaler.transform(user_data)

# Prediction button
if st.button('🔍 Predict Heart Disease'):
    prediction = logreg.predict(user_data_scaled)
    
    st.subheader("Prediction Result")
    if prediction[0] == 1:
        st.markdown("<h3 style='color: red;'>🚨 The model predicts: Heart Disease 😞</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='color: green;'>✅ The model predicts: No Heart Disease 😊</h3>", unsafe_allow_html=True)
