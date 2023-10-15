import streamlit as st
import pandas as pd
import joblib  # Import joblib to load your pre-trained model


html_temp = """
  <div style="background-color:#025246 ;padding:10px">
  <h2 style="color:white;text-align:center;">Volve oil production ML App </h2>
  </div>
  """
st.markdown(html_temp, unsafe_allow_html=True)

# Load the pre-trained model
# # @st.cache_resource
# @st.cache_data(experimental_allow_widgets=True)
@st.cache_data
def load_model():
  model = joblib.load(
      "logistic.pkl")  # Replace "your_model.pkl" with your model's file path
  return model


model = load_model()

# Create a sidebar for user input
st.sidebar.header("Input Parameters")

# User inputs for prediction
AVG_DOWNHOLE_PRESSURE = st.sidebar.number_input("Average Downhole Pressure",
                                                value=0.0)
AVG_DOWNHOLE_TEMPERATURE = st.sidebar.number_input(
    "Average Downhole Temperature", value=0.0)
AVG_DP_TUBING = st.sidebar.number_input("Average DP Tubing", value=0.0)

# Make predictions
predicted_oil_vol = model.predict(
    [[AVG_DOWNHOLE_PRESSURE, AVG_DOWNHOLE_TEMPERATURE, AVG_DP_TUBING]])

# Display the prediction
# safe_html = """  
#     <div style="background-color:#F4D03F;padding:10px >
#      <h2 style="color:white;text-align:center;"> Predicted BORE_OIL_VOL: {predicted_oil_vol[0]}</h2>
#      </div>
#   """
st.write(f"Predicted BORE_OIL_VOL: {predicted_oil_vol[0]}")
# st.markdown(safe_html, unsafe_allow_html=True)
# Optionally, you can add additional content or visualizations here
