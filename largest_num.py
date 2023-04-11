import streamlit as st

st.title("Largest Number by 21f2000930")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")
num3 = st.number_input("Enter third number")

st.write("The largest number is", max(num1, num2, num3))
