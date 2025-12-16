import streamlit as st

# ----------------------------------------------------
# APP CONFIG
# ----------------------------------------------------
st.set_page_config(
    page_title="Data-Driven Stock Analysis",
    layout="wide"
)

# ----------------------------------------------------
# HERO SECTION
# ----------------------------------------------------
st.markdown(
    """
    <div style="padding:20px 10px;">
        <h1 style="text-align:center;">📈 Data-Driven Stock Analysis Dashboard</h1>
        <p style="text-align:center; font-size:18px; color:gray;">
            An end-to-end analytics solution to explore Nifty 50 stock performance
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ----------------------------------------------------
# PROJECT OVERVIEW
# ----------------------------------------------------
col1, col2 = st.columns([2, 3])

with col1:
    st.subheader("📌 Project Overview")
    st.markdown(
        """
        This dashboard analyzes **daily stock market data** to help investors
        and analysts understand:

        - Market trends  
        - Top performing & losing stocks  
        - Risk & volatility  
        - Sector-wise performance  
        - Stock correlations  

        The project follows a **complete ETL → Analytics → Visualization** pipeline.
        """
    )

with col2:
    st.subheader("🛠 Tech Stack")
    st.markdown(
        """
        - **Language:** Python  
        - **Data Processing:** Pandas, NumPy  
        - **ETL:** YAML → Clean CSV → MySQL  
        - **Visualization:** Streamlit, Matplotlib, Seaborn  
        - **Analytics:** Statistics, Time-series analysis  

        Designed for **real-world financial analytics**.
        """
    )

st.divider()

# ----------------------------------------------------
# DASHBOARD GUIDE
# ----------------------------------------------------
st.subheader("🧭 How to Use This Dashboard")

st.markdown(
    """
    👉 Use the **sidebar navigation** to explore different analytical views:

    - **Market Overview** – KPI snapshot of the market  
    - **Top Gainers & Losers** – Best & worst performing stocks  
    - **Volatility Analysis** – Risk assessment  
    - **Cumulative Returns** – Long-term growth trends  
    - **Sector Performance** – Industry-level insights  
    - **Correlation Heatmap** – Portfolio diversification analysis  
    """
)

st.info(
    "📊 Tip: Use the global filters in the sidebar to dynamically explore stocks, dates, and trends."
)

# ----------------------------------------------------
# FOOTER
# ----------------------------------------------------
st.markdown(
    """
    <hr>
    <p style="text-align:center; color:gray;">
        Built as a portfolio-grade data analytics project | Streamlit Dashboard
    </p>
    """,
    unsafe_allow_html=True
)
