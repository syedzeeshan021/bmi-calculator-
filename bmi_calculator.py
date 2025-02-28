# Project 8: Create a Python Streamlit BMI Calculator Web App - Enhanced Version

import streamlit as st
import pandas as pd

st.title("🏋️‍♀️ BMI (Body Mass Index) Calculator 🏋️‍♂️")
st.write("Calculate your BMI and get personalized health advice! 😊")

# Height input in feet and inches
st.subheader("📏 Your Height")
height_feet = st.slider("Enter your height (in feet):", min_value=4, max_value=8, value=4, step=1, format="%d ft")
height_inches = st.slider("Enter your height (in inches):", min_value=0, max_value=11, value=0, step=1, format="%d in")

# Convert height from feet and inches to meters
height_in_meters = (height_feet * 0.3048) + (height_inches * 0.0254)

st.subheader("⚖️ Your Weight")
weight = st.slider("Enter your weight (in kg):", min_value=0, max_value=300,value=0, step=1, format="%d kg")

# Calculate BMI
# Handling the ZeroDivisionError
if height_in_meters == 0:
    bmi = 0  # Or any other appropriate value like float('inf') to represent undefined
    st.warning("Height cannot be zero. Please enter a valid height.")
else:
    bmi = weight / (height_in_meters**2)

st.subheader("📊 Your BMI Result")
if height_in_meters == 0:
    st.write("Your BMI cannot be calculated, as height is zero")
else:
    st.write(f"Your BMI is: **{bmi:.2f}**")

st.write("---")  # Separator line

st.subheader("📈 BMI Categories & Advice")

# BMI Categories Data
bmi_data = {
    "Category": [
        "Underweight", 
        "Normal weight", 
        "Overweight", 
        "Obesity Class I", 
        "Obesity Class II", 
        "Obesity Class III"
    ],
    "BMI Range": [
        "Less than 18.5",
        "18.5 – 24.9",
        "25.0 – 29.9",
        "30.0 – 34.9",
        "35.0 – 39.9",
        "40.0 and above"
    ],
    "Advice": [
        "Consider gaining weight with a nutrient-rich diet. Consult a nutritionist.",
        "Maintain a balanced diet and regular exercise.",
        "Consider weight loss through physical activity and a healthy diet.",
        "Adopt a structured weight loss plan and consult a healthcare provider.",
        "Seek professional guidance for weight management.",
        "Serious health risks. Consult a doctor for personalized advice."
    ]
}

# Convert to DataFrame
bmi_df = pd.DataFrame(bmi_data)

# Find the matching category
if height_in_meters == 0:
    bmi_index = 0
    st.write("Category and Advice cannot be calculated as height is zero")
else:
  bmi_index = (
      0 if bmi < 18.5 else
      1 if bmi <= 24.9 else
      2 if bmi <= 29.9 else
      3 if bmi <= 34.9 else
      4 if bmi <= 39.9 else
      5
  )

  # Display the corresponding BMI category and advice
  st.markdown(f"### 📌 **Category:** {bmi_df.iloc[bmi_index, 0]}")
  st.markdown(f"#### 📉 **BMI Range:** {bmi_df.iloc[bmi_index, 1]}")
  st.info(f"💡 **Advice:** {bmi_df.iloc[bmi_index, 2]}")

# Display BMI Category Chart
st.write("### 📊 BMI Categories Overview")
st.dataframe(bmi_df, hide_index=True)
