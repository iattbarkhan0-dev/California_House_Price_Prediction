import streamlit as st
import pandas as pd
import pickle
st.set_page_config(page_title="California House Price Prediction",layout="centered")
st.title("California House Price Prediction")
st.write("Please enter the details related to house for price prediction.")
with open("CALIFORNIA_HOUSE_PRICE1.pickle","rb") as f:
    rf=pickle.load(f)
with open("california_house_preprocessor.pkl","rb") as f:
    preprocessor=pickle.load(f)
longitude=st.number_input("longitude",min_value=-124.65,max_value=-114.13)
latitude=st.number_input("latitude",min_value=32.51,max_value=42.01)
housing_median_age=st.number_input("housing_median_age")
total_rooms=st.number_input("total_rooms")
total_bedrooms=st.number_input("total_bedrooms")
population=st.number_input("population")
households=st.number_input("households")
median_income=st.number_input("median_income")
ocean_proximity=st.selectbox("Ocean Proximity",["<1H OCEAN","INLAND","ISLAND","NEAR BAY","NEAR OCEAN"])
if st.button("Predict House Price"):
    input_data = pd.DataFrame({"longitude": [longitude],"latitude": [latitude],"housing_median_age": [housing_median_age], "total_rooms": [total_rooms],"total_bedrooms": [total_bedrooms],"population": [population],"households": [households],"median_income": [median_income],"ocean_proximity": [ocean_proximity]})
    input_prepared = preprocessor.transform(input_data)
    prediction = rf.predict(input_prepared)
    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")

    
