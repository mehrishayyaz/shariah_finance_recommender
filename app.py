import streamlit as st

from islamic_contracts import Murabaha, Ijara, Mudarabah

# Page Config
st.set_page_config(
    page_title="Shariah Financing Recommendation System",
    page_icon="💰",
    layout="centered"
)

# Title
st.title("💰 AI-Assisted Shariah Financing Recommendation System")

st.write("""
This application recommends and demonstrates
Shariah-compliant financing contracts using
rule-based decision support.
""")

# Sidebar
st.sidebar.title("Islamic Finance Products")

product = st.sidebar.selectbox(
    "Choose Financing Product",
    ["Murabaha", "Ijara", "Mudarabah"]
)

# ---------------- MURABAHA ----------------
if product == "Murabaha":

    st.header("Murabaha Contract")

    asset_name = st.text_input("Asset Name")

    cost_price = st.number_input(
        "Cost Price",
        min_value=0.0
    )

    profit_rate = st.number_input(
        "Profit Rate (%)",
        min_value=0.0
    )

    if st.button("Generate Murabaha Contract"):

        contract = Murabaha(
            asset_name,
            cost_price,
            profit_rate
        )

        st.success("Contract Generated Successfully")

        st.write(contract.summary())

        st.subheader("Contract Value")

        st.metric(
            "Selling Price",
            contract.contract_value()
        )

# ---------------- IJARA ----------------
elif product == "Ijara":

    st.header("Ijara Contract")

    asset_name = st.text_input("Asset Name")

    monthly_rent = st.number_input(
        "Monthly Rent",
        min_value=0.0
    )

    months = st.number_input(
        "Duration (Months)",
        min_value=1
    )

    if st.button("Generate Ijara Contract"):

        contract = Ijara(
            asset_name,
            monthly_rent,
            months
        )

        st.success("Contract Generated Successfully")

        st.write(contract.summary())

        st.subheader("Contract Value")

        st.metric(
            "Total Rent",
            contract.contract_value()
        )

# ---------------- MUDARABAH ----------------
elif product == "Mudarabah":

    st.header("Mudarabah Contract")

    capital = st.number_input(
        "Capital",
        min_value=0.0
    )

    total_profit = st.number_input(
        "Total Profit",
        min_value=0.0
    )

    investor_ratio = st.slider(
        "Investor Ratio",
        0.0,
        1.0,
        0.5
    )

    if st.button("Generate Mudarabah Contract"):

        contract = Mudarabah(
            capital,
            total_profit,
            investor_ratio
        )

        st.success("Contract Generated Successfully")

        st.write(contract.summary())

        st.subheader("Profit Distribution")

        st.metric(
            "Investor Share",
            contract.investor_share
        )

        st.metric(
            "Entrepreneur Share",
            contract.entrepreneur_share
        )

# Footer
st.markdown("---")

st.write("""
Developed using:
- Python
- Streamlit
- Object-Oriented Programming
- Rule-Based AI
- Islamic Finance Principles
""")