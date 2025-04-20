#Project 9 : BMI CALCULATOR
import streamlit as st
import time

st.set_page_config(page_title="bmi calculator", page_icon="✅",layout="centered")

st.title("Project 9: BMI Calculator in python")
st.markdown("""
## apna BMI calculate karen or neeche apna **weight and height** enter kren""")

col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("weight (kg): " , min_value=1.0, format="%.2f")
with col2:
    height = st.number_input("height (m): " , min_value=1.0, format="%.2f")

if height > 0 and weight > 0:
    bmi =weight / (height ** 2) #bmi 
    st.subheader("apka BMI hai:")
    st.markdown(f"{bmi:.2f}",unsafe_allow_html=True)

    if bmi < 18.5:
        st.error("underweight")
    elif 18.5 <= bmi < 24.9:
        st.success("normal weight")
    elif 25 <= bmi < 29.9:
        st.warning("overweight")
    else:
        st.error("Obesity 🔥")
else:
    st.info("please enter a valid weight and height")