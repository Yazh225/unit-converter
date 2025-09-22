import streamlit as st

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="Universal Unit Converter",
    page_icon="🔄",
    layout="centered"
)

st.title("🔄 Universal Unit Converter")
st.write("Convert between **Length, Weight, Temperature, Speed, Area, and Volume** easily!")

# ---------------- Sidebar ----------------
category = st.sidebar.selectbox(
    "Select category",
    ["Length", "Weight", "Temperature", "Speed", "Area", "Volume"]
)

# ---------------- Length ----------------
if category == "Length":
    st.header("Length Converter")
    option = st.selectbox(
        "Conversion Type",
        ["Meters ➡ Kilometers", "Kilometers ➡ Meters",
         "Meters ➡ Centimeters", "Centimeters ➡ Meters"]
    )
    value = st.number_input("Enter value", min_value=0.0, step=0.01)
    if option == "Meters ➡ Kilometers":
        st.success(f"{value} meters = {value / 1000} kilometers")
    elif option == "Kilometers ➡ Meters":
        st.success(f"{value} kilometers = {value * 1000} meters")
    elif option == "Meters ➡ Centimeters":
        st.success(f"{value} meters = {value * 100} centimeters")
    elif option == "Centimeters ➡ Meters":
        st.success(f"{value} centimeters = {value / 100} meters")

# ---------------- Weight ----------------
elif category == "Weight":
    st.header("Weight Converter")
    option = st.selectbox(
        "Conversion Type",
        ["Kilograms ➡ Grams", "Grams ➡ Kilograms",
         "Kilograms ➡ Pounds", "Pounds ➡ Kilograms"]
    )
    value = st.number_input("Enter value", min_value=0.0, step=0.01)
    if option == "Kilograms ➡ Grams":
        st.success(f"{value} kg = {value * 1000} g")
    elif option == "Grams ➡ Kilograms":
        st.success(f"{value} g = {value / 1000} kg")
    elif option == "Kilograms ➡ Pounds":
        st.success(f"{value} kg = {value * 2.20462} lbs")
    elif option == "Pounds ➡ Kilograms":
        st.success(f"{value} lbs = {value / 2.20462} kg")

# ---------------- Temperature ----------------
elif category == "Temperature":
    st.header("Temperature Converter")
    option = st.selectbox(
        "Conversion Type",
        ["Celsius ➡ Fahrenheit", "Fahrenheit ➡ Celsius"]
    )
    value = st.number_input("Enter value", step=0.1)
    if option == "Celsius ➡ Fahrenheit":
        st.success(f"{value}°C = {(value * 9/5) + 32}°F")
    elif option == "Fahrenheit ➡ Celsius":
        st.success(f"{value}°F = {(value - 32) * 5/9}°C")

# ---------------- Speed ----------------
elif category == "Speed":
    st.header("Speed Converter")
    option = st.selectbox(
        "Conversion Type",
        ["Kilometers/hour ➡ Meters/second",
         "Meters/second ➡ Kilometers/hour",
         "Miles/hour ➡ Kilometers/hour",
         "Kilometers/hour ➡ Miles/hour"]
    )
    value = st.number_input("Enter value", min_value=0.0, step=0.01)
    if option == "Kilometers/hour ➡ Meters/second":
        st.success(f"{value} km/h = {value / 3.6} m/s")
    elif option == "Meters/second ➡ Kilometers/hour":
        st.success(f"{value} m/s = {value * 3.6} km/h")
    elif option == "Miles/hour ➡ Kilometers/hour":
        st.success(f"{value} mph = {value * 1.60934} km/h")
    elif option == "Kilometers/hour ➡ Miles/hour":
        st.success(f"{value} km/h = {value / 1.60934} mph")

# ---------------- Area ----------------
elif category == "Area":
    st.header("Area Converter")
    option = st.selectbox(
        "Conversion Type",
        ["Square meters ➡ Square kilometers",
         "Square kilometers ➡ Square meters",
         "Square meters ➡ Square feet",
         "Square feet ➡ Square meters"]
    )
    value = st.number_input("Enter value", min_value=0.0, step=0.01)
    if option == "Square meters ➡ Square kilometers":
        st.success(f"{value} m² = {value / 1_000_000} km²")
    elif option == "Square kilometers ➡ Square meters":
        st.success(f"{value} km² = {value * 1_000_000} m²")
    elif option == "Square meters ➡ Square feet":
        st.success(f"{value} m² = {value * 10.7639} ft²")
    elif option == "Square feet ➡ Square meters":
        st.success(f"{value} ft² = {value / 10.7639} m²")

# ---------------- Volume ----------------
elif category == "Volume":
    st.header("Volume Converter")
    option = st.selectbox(
        "Conversion Type",
        ["Liters ➡ Milliliters", "Milliliters ➡ Liters",
         "Liters ➡ Gallons", "Gallons ➡ Liters"]
    )
    value = st.number_input("Enter value", min_value=0.0, step=0.01)
    if option == "Liters ➡ Milliliters":
        st.success(f"{value} L = {value * 1000} mL")
    elif option == "Milliliters ➡ Liters":
        st.success(f"{value} mL = {value / 1000} L")
    elif option == "Liters ➡ Gallons":
        st.success(f"{value} L = {value / 3.78541} gallons")
    elif option == "Gallons ➡ Liters":
        st.success(f"{value} gallons = {value * 3.78541} L")
