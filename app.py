import streamlit as st

# Page config
st.set_page_config(
    page_title="Universal Unit Converter",
    page_icon="🔄",
    layout="centered"
)

st.title("🔄 Universal Unit Converter")
st.write("Convert between **Length, Weight, and Temperature** easily!")

# Sidebar for category selection
category = st.sidebar.selectbox("Select category", ["Length", "Weight", "Temperature"])

# --- Length Conversion ---
if category == "Length":
    st.header("Length Converter")
    option = st.selectbox("Conversion Type", ["Meters ➡ Kilometers", "Kilometers ➡ Meters", "Meters ➡ Centimeters", "Centimeters ➡ Meters"])
    value = st.number_input("Enter value", min_value=0.0, step=0.01)
    if option == "Meters ➡ Kilometers":
        st.success(f"{value} meters = {value / 1000} kilometers")
    elif option == "Kilometers ➡ Meters":
        st.success(f"{value} kilometers = {value * 1000} meters")
    elif option == "Meters ➡ Centimeters":
        st.success(f"{value} meters = {value * 100} centimeters")
    elif option == "Centimeters ➡ Meters":
        st.success(f"{value} centimeters = {value / 100} meters")

# --- Weight Conversion ---
elif category == "Weight":
    st.header("Weight Converter")
    option = st.selectbox("Conversion Type", ["Kilograms ➡ Grams", "Grams ➡ Kilograms", "Kilograms ➡ Pounds", "Pounds ➡ Kilograms"])
    value = st.number_input("Enter value", min_value=0.0, step=0.01)
    if option == "Kilograms ➡ Grams":
        st.success(f"{value} kg = {value * 1000} g")
    elif option == "Grams ➡ Kilograms":
        st.success(f"{value} g = {value / 1000} kg")
    elif option == "Kilograms ➡ Pounds":
        st.success(f"{value} kg = {value * 2.20462} lbs")
    elif option == "Pounds ➡ Kilograms":
        st.success(f"{value} lbs = {value / 2.20462} kg")

# --- Temperature Conversion ---
elif category == "Temperature":
    st.header("Temperature Converter")
    option = st.selectbox("Conversion Type", ["Celsius ➡ Fahrenheit", "Fahrenheit ➡ Celsius"])
    value = st.number_input("Enter value", step=0.1)
    if option == "Celsius ➡ Fahrenheit":
        st.success(f"{value}°C = {(value * 9/5) + 32}°F")
    elif option == "Fahrenheit ➡ Celsius":
        st.success(f"{value}°F = {(value - 32) * 5/9}°C")
