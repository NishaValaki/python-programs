import streamlit as st

st.set_page_config(page_title="Electricity Bill Calculator", page_icon="⚡")

st.title("⚡ Electricity Bill Calculator")

# Inputs
units = st.number_input(
    "Units Consumed (kWh)",
    min_value=0.0,
    value=100.0,
    step=1.0
)

rate = st.number_input(
    "Rate per Unit (₹)",
    min_value=0.0,
    value=6.50,
    step=0.10
)

fixed_charge = st.number_input(
    "Fixed Charges (₹)",
    min_value=0.0,
    value=100.0,
    step=10.0
)

tax_percent = st.number_input(
    "Electricity Duty / Tax (%)",
    min_value=0.0,
    value=5.0,
    step=0.5
)

if st.button("Calculate Bill"):
    energy_charge = units * rate
    tax = (energy_charge * tax_percent) / 100
    total_bill = energy_charge + fixed_charge + tax

    st.success("Bill Calculated Successfully!")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Energy Charge", f"₹{energy_charge:.2f}")

    with col2:
        st.metric("Tax", f"₹{tax:.2f}")

    with col3:
        st.metric("Total Bill", f"₹{total_bill:.2f}")

    st.divider()

    st.subheader("Bill Summary")
    st.write(f"**Units Consumed:** {units:.0f} kWh")
    st.write(f"**Rate per Unit:** ₹{rate:.2f}")
    st.write(f"**Fixed Charges:** ₹{fixed_charge:.2f}")
    st.write(f"**Tax:** {tax_percent}%")