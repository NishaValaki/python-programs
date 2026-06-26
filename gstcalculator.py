import streamlit as st

st.set_page_config(page_title="GST Calculator", page_icon="🧾")

st.title("🧾 GST Calculator")

# Input mode
mode = st.radio(
    "Select Calculation Type",
    ["Add GST", "Remove GST"]
)

amount = st.number_input(
    "Enter Amount (₹)",
    min_value=0.0,
    value=1000.0,
    step=100.0
)

gst_rate = st.selectbox(
    "GST Rate (%)",
    [0, 3, 5, 12, 18, 28]
)

if st.button("Calculate"):
    if mode == "Add GST":
        gst_amount = amount * gst_rate / 100
        total = amount + gst_amount

        st.success("Calculation Complete")
        st.write(f"**Original Amount:** ₹{amount:,.2f}")
        st.write(f"**GST ({gst_rate}%):** ₹{gst_amount:,.2f}")
        st.write(f"**Total Amount:** ₹{total:,.2f}")

        st.divider()
        st.write("### GST Split")
        st.write(f"CGST ({gst_rate/2}%): ₹{gst_amount/2:,.2f}")
        st.write(f"SGST ({gst_rate/2}%): ₹{gst_amount/2:,.2f}")

    else:
        base_amount = amount / (1 + gst_rate / 100)
        gst_amount = amount - base_amount

        st.success("Calculation Complete")
        st.write(f"**Total Amount:** ₹{amount:,.2f}")
        st.write(f"**Taxable Amount:** ₹{base_amount:,.2f}")
        st.write(f"**GST ({gst_rate}%):** ₹{gst_amount:,.2f}")

        st.divider()
        st.write("### GST Split")
        st.write(f"CGST ({gst_rate/2}%): ₹{gst_amount/2:,.2f}")
        st.write(f"SGST ({gst_rate/2}%): ₹{gst_amount/2:,.2f}")