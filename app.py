import streamlit as st
from islamic_contracts import Murabaha, Ijara, Mudarabah

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Shariah Financing Recommender",
    page_icon="💰",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.stApp {
    background-color: #f5f7fa;
}

h1, h2, h3 {
    color: #111111;
}

div.stButton > button {
    background-color: #0E5A8A;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    border: none;
}

div.stButton > button:hover {
    background-color: #1177bb;
    color: white;
}

[data-testid="stMetricValue"] {
    color: green;
    font-size: 28px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("💰 AI-Assisted Shariah Financing Recommendation System")

st.markdown("""
<div style='text-align: center; font-size:18px;'>

This fintech application recommends and demonstrates
<b>Shariah-compliant financing products</b>
using rule-based intelligent decision support.

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- SIDEBAR ----------------
st.sidebar.title("📌 Navigation")

product = st.sidebar.radio(
    "Choose Financing Product",
    ["Murabaha", "Ijara", "Mudarabah"]
)

st.sidebar.markdown("---")

st.sidebar.info("""
### Technologies Used
- Python
- Streamlit
- OOP
- Rule-Based AI
- Islamic Finance
""")

# ================= MURABAHA =================
if product == "Murabaha":

    st.header("📦 Murabaha Contract")

    col1, col2 = st.columns(2)

    with col1:
        asset_name = st.text_input("Asset Name")

        cost_price = st.number_input(
            "Cost Price",
            min_value=0.0
        )

    with col2:
        profit_rate = st.number_input(
            "Profit Rate (%)",
            min_value=0.0
        )

    st.markdown("")

    if st.button("Generate Murabaha Contract"):

        contract = Murabaha(
            asset_name,
            cost_price,
            profit_rate
        )

        st.success("✅ Contract Generated Successfully")

        st.markdown("### 📄 Contract Summary")

        st.info(contract.summary())

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "💵 Profit Amount",
                f"{contract.profit_amount:,.2f}"
            )

        with col2:
            st.metric(
                "💰 Selling Price",
                f"{contract.contract_value():,.2f}"
            )

# ================= IJARA =================
elif product == "Ijara":

    st.header("🏢 Ijara Contract")

    col1, col2 = st.columns(2)

    with col1:
        asset_name = st.text_input("Asset Name")

        monthly_rent = st.number_input(
            "Monthly Rent",
            min_value=0.0
        )

    with col2:
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

        st.success("✅ Contract Generated Successfully")

        st.markdown("### 📄 Contract Summary")

        st.info(contract.summary())

        st.metric(
            "💰 Total Rent",
            f"{contract.contract_value():,.2f}"
        )

# ================= MUDARABAH =================
elif product == "Mudarabah":

    st.header("📈 Mudarabah Contract")

    col1, col2 = st.columns(2)

    with col1:
        capital = st.number_input(
            "Capital",
            min_value=0.0
        )

        total_profit = st.number_input(
            "Total Profit",
            min_value=0.0
        )

    with col2:
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

        st.success("✅ Contract Generated Successfully")

        st.markdown("### 📄 Contract Summary")

        st.info(contract.summary())

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "👤 Investor Share",
                f"{contract.investor_share:,.2f}"
            )

        with col2:
            st.metric(
                "🏢 Entrepreneur Share",
                f"{contract.entrepreneur_share:,.2f}"
            )

# ---------------- FOOTER ----------------
st.markdown("---")

st.markdown("""
<div style='text-align:center'>

Developed with ❤️ using Streamlit and Python

</div>
""", unsafe_allow_html=True)
