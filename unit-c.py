import streamlit as st

# Set page configuration
st.set_page_config(page_title="Unit Converter 🌐", page_icon="🔄", layout="centered", initial_sidebar_state="expanded")

# Set the theme for the app (dark mode)
st.markdown(
    """
    <style>
        body {
            background-color: #1e1e1e;
            color: white;
        }
        .css-1d391kg {
            background-color: #444;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title of the app
st.title("Unit Converter 🌐")

# Description of the app
st.write("Welcome to the **Unit Converter**! Use the tool below to easily convert between different units. Choose your units, and let me do it! 🔄")

# Length Conversion:
def convert_length(value, from_unit, to_unit):
    conversion_dict = {
        ('meters', 'kilometers'): value / 1000,
        ('kilometers', 'meters'): value * 1000,
        ('centimeters', 'meters'): value / 100,
        ('meters', 'centimeters'): value * 100,
        # Add more conversions as needed
    }
    return conversion_dict.get((from_unit, to_unit), "Conversion not available")

# Temperature Conversion:
def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    elif from_unit == 'Celsius' and to_unit == 'Kelvin':
        return value + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        return value - 273.15
    else:
        return "Invalid conversion"

# Create a sidebar for user input
st.sidebar.header("Select Conversion Type")

conversion_type = st.sidebar.selectbox(
    "Choose the type of conversion", ["Length", "Temperature"]
)

if conversion_type == "Length":

    # Length conversion options
    st.sidebar.subheader("Length Conversion")
    
    value = st.sidebar.number_input("Enter value", value=1.0)
    from_unit = st.sidebar.selectbox("From unit", ["meters", "kilometers", "centimeters"])
    to_unit = st.sidebar.selectbox("To unit", ["meters", "kilometers", "centimeters"])
    
    if st.sidebar.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.write(f"Converted {value} {from_unit} to {result} {to_unit}")

elif conversion_type == "Temperature":

    # Temperature conversion options
    st.sidebar.subheader("Temperature Conversion")
    
    value = st.sidebar.number_input("Enter value", value=25.0)
    from_unit = st.sidebar.selectbox("From unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.sidebar.selectbox("To unit", ["Celsius", "Fahrenheit", "Kelvin"])
    
    if st.sidebar.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.write(f"Converted {value} {from_unit} to {result} {to_unit} 🔄")
