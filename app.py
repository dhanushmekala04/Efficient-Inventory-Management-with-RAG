import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.regression.linear_model import OLSResults

# Load the trained model
model = OLSResults.load("model.pickle")

# Function to predict new data
def predict_new_data(new_data):
    new_data_pred = model.predict(start=new_data.index[0], end=new_data.index[-1])
    return new_data_pred

# Streamlit app
st.title('Medical Inventory Time Series Forecasting')

# Upload new data file
uploaded_file = st.file_uploader("Choose an Excel file with new data for prediction", type="xlsx")
if uploaded_file is not None:
    new_data = pd.read_excel(uploaded_file)
    
    st.write("New Data:")
    st.write(new_data.head())

    # Predict using the uploaded new data
    new_data_pred = predict_new_data(new_data)

    # Plot the results
    fig, ax = plt.subplots()
    ax.plot(new_data['LIGNOCAINE HYDROCHLORIDE 2% INJ'], '-b', label='Actual Value')
    ax.plot(new_data.index, new_data_pred, '-r', label='Predicted Value')
    ax.legend()
    st.pyplot(fig)
    
    # Display predictions
    st.write("Predictions:")
    st.write(new_data_pred)




