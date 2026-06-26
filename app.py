import streamlit as st

st.set_page_config(page_title="Profit & Loss Calculator", page_icon="📈")

st.title("📈 Profit & Loss Calculator")

cost_price = st.number_input(
    "Cost Price (₹)",
    min_value=0.0,
    value=1000.0,
    step=100.0
)

selling_price = st.number_input(
    "Selling Price (₹)",
    min_value=0.0,
    value=1200.0,
    step=100.0
)

if st.button("Calculate"):

    if selling_price > cost_price:
        profit = selling_price - cost_price
        profit_percent = (profit / cost_price) * 100 if cost_price != 0 else 0

        st.success("Profit Earned ✅")
        st.metric("Profit", f"₹{profit:,.2f}")
        st.metric("Profit %", f"{profit_percent:.2f}%")

    elif selling_price < cost_price:
        loss = cost_price - selling_price
        loss_percent = (loss / cost_price) * 100 if cost_price != 0 else 0

        st.error("Loss Incurred ❌")
        st.metric("Loss", f"₹{loss:,.2f}")
        st.metric("Loss %", f"{loss_percent:.2f}%")

    else:
        st.info("No Profit, No Loss")