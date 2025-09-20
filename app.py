import streamlit as st

# Conversion functions
def convert_length(value, from_unit, to_unit):
    to_meters = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'miles': 1609.34,
        'feet': 0.3048,
        'inches': 0.0254
    }
    value_in_meters = value * to_meters[from_unit]
    return value_in_meters / to_meters[to_unit]

def convert_weight(value, from_unit, to_unit):
    to_kilograms = {
        'kilograms': 1.0,
        'grams': 0.001,
        'pounds': 0.453592,
        'ounces': 0.0283495
    }
    value_in_kg = value * to_kilograms[from_unit]
    return value_in_kg / to_kilograms[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'celsius':
        celsius = value
    elif from_unit == 'fahrenheit':
        celsius = (value - 32) * 5 / 9
    elif from_unit == 'kelvin':
        celsius = value - 273.15
    if to_unit == 'celsius':
        return celsius
    elif to_unit == 'fahrenheit':
        return (celsius * 9 / 5) + 32
    elif to_unit == 'kelvin':
        return celsius + 273.15

# Streamlit UI
st.title("🌍 Unit Converter")

category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])

if category == "Length":
    value = st.number_input("Enter value:", value=0.0)
    from_unit = st.selectbox("From:", ["meters", "kilometers", "miles", "feet", "inches"])
    to_unit = st.selectbox("To:", ["meters", "kilometers", "miles", "feet", "inches"])
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {round(result, 4)} {to_unit}")

elif category == "Weight":
    value = st.number_input("Enter value:", value=0.0)
    from_unit = st.selectbox("From:", ["kilograms", "grams", "pounds", "ounces"])
    to_unit = st.selectbox("To:", ["kilograms", "grams", "pounds", "ounces"])
    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {round(result, 4)} {to_unit}")

elif category == "Temperature":
    value = st.number_input("Enter value:", value=0.0)
    from_unit = st.selectbox("From:", ["celsius", "fahrenheit", "kelvin"])
    to_unit = st.selectbox("To:", ["celsius", "fahrenheit", "kelvin"])
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {round(result, 2)} {to_unit}")
