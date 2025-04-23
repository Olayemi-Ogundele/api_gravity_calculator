# API Gravity Calculator
import streamlit as st

st.title("API Gravity Calculator")

# take the user input
with st.form("Calculate_form"):
    value = st.text_input("Enter your Value Here:", "0")
    operations = st.selectbox(
        "Choose Operation", ["Specific Gravity to API", "API to Specific Gravity"])

    submitted = st.form_submit_button("Calculate")

    # handle the error
    if submitted:
        try:
            num_value = float(value)

            if operations == "Specific Gravity to API":
                if num_value <= 0:
                    st.error("Error: Specific Gravity Must be Greater than Zero")
                else:
                    api = (141.5/num_value) - 131.5
                    st.success(f"API Gravity = {api:2f}°")

                 # Interpreting the outcome
                if api > 40:
                    st.info("Light Crude Oil (High API gravity)")
                elif api > 30:
                    st.info("Medium Crude Oil")
                elif api > 22:
                    st.info("Heavy Crude Oil")
                else:
                    st.info("Extra Heavy Crude Oil (Low API gravity)")

            else:
                if num_value < 0:
                    st.error("Error: API Gravity cannot be Zero")
                else:
                    specific_g = 141.5/(num_value + 131.5)
                    st.success(f"Specific Gravity = {specific_g:2f}")

        except ValueError:
            st.error("Error: Enter  a Valid Number")
