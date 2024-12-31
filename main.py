import streamlit as st
import numpy as np
import pandas as pd
import datetime
import xgboost as xgb
import os

# Check current directory
current_directory = os.getcwd()
print("Current Working Directory:", current_directory)

# Full path to the model file
model_path = r'C:\Users\Ayush\OneDrive\Desktop\Shriyanshi Project\MINI PROJECT\xgb_model.json'

# Load the model
model = xgb.XGBRegressor()
try:
    model.load_model(model_path)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    st.error(f"Error loading model: {e}")

# Function to define the Streamlit app
def main():
    # App header
    html_temp = """
     <div style="background-color:lightblue;padding:16px">
     <h2 style="color:black;text-align:center;">Car Price Prediction Using ML</h2>
     </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
   
    st.markdown("##### Are you planning to sell your car!?\n##### Let's try evaluating its price.")
    st.write('')
    st.write('')
    
    # Input fields
    p1 = st.number_input('What is the current ex-showroom price of the car? (In Lakhs)', 2.5, 100.0, step=1.0) 
    p2 = st.number_input('What is the distance completed by the car in Kilometers?', 100, 50000000, step=100)

    s1 = st.selectbox('What is the fuel type of the car?', ('Petrol', 'Diesel', 'CNG'))
    if s1 == "Petrol":
        p3 = 0
    elif s1 == "Diesel":
        p3 = 1
    elif s1 == "CNG":
        p3 = 2
        
    s2 = st.selectbox('Are you a dealer or an individual?', ('Dealer', 'Individual'))
    if s2 == "Dealer":
        p4 = 0
    elif s2 == "Individual":
        p4 = 1
        
    s3 = st.selectbox('What is the Transmission Type?', ('Manual', 'Automatic'))
    if s3 == "Manual":
        p5 = 0
    elif s3 == "Automatic":
        p5 = 1
        
    p6 = st.slider("Number of Owners the car previously had", 0, 3)
    
    # Age of the car
    years = st.number_input('In which year was the car purchased?', 1990, datetime.datetime.now().year, step=1)
    p7 = datetime.datetime.now().year - years
    
    # Create DataFrame for input
    data_new = pd.DataFrame({
        'Present_Price': p1,
        'Kms_Driven': p2,
        'Fuel_Type': p3,
        'Seller_Type': p4,
        'Transmission': p5,
        'Owner': p6,
        'Age': p7
    }, index=[0])
    
    # Prediction
    try: 
        if st.button('Predict'):
            prediction = model.predict(data_new)
            if prediction > 0:
                st.balloons()
                st.success(f'You can sell the car for ₹{prediction[0]:.2f} lakhs')
            else:
                st.warning("You will not be able to sell this car!")
    except Exception as e:
        st.error(f"Oops! Something went wrong: {e}")

# Run the app
if __name__ == '__main__':
    main()
