import streamlit as st

st.title("Largest Number")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")
num3 = st.number_input("Enter third number")

if num1 > num2 and num1 > num3:
    st.write("The largest number is", num1)
elif num2 > num1 and num2 > num3:
    st.write("The largest number is", num2)
else:
    st.write("The largest number is", num3)
