import streamlit as st
import pandas as pd

from utils.data_loader import load_data
from utils.filters import apply_global_filters

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------
st.set_page_config(page_title="Volatility Analysis", layout="wide")

st.title("📈 Volatility Analysis")
st.caption("Risk assessment using standard deviation of daily returns")

# ----------------------------------------------------
# LOAD & FILTER DATA
# ----------------------------------------------------
df = load_data()
df = apply_global_filters(df)

df = df.sort_values(["Ticker", "date"])

# ----------------------------------------------------
# CALCULATE DAILY RETURNS
# ----------------------------------------------------
df["daily_return"] = df.groupby("Ticker")["close"].pct_change()

# ----------------------------------------------------
# VOLATILITY CALCULATION
# ----------------------------------------------------
volatility = (
    df.groupby("Ticker")["daily_return"]
    .std()
    .reset_index(name="volatility")
)

volatility["volatility_pct"] = volatility["volatility"] * 100

top_volatile = volatility.sort_values(
    "volatility_pct", ascending=False
).head(10)

# ----------------------------------------------------
# KPI METRICS
# ----------------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Highest Volatility",
        top_volatile.iloc[0]["Ticker"],
        f'{top_volatile.iloc[0]["volatility_pct"]:.2f}%'
    )

with col2:
    st.metric(
        "Average Volatility",
        f'{volatility["volatility_pct"].mean():.2f}%'
    )

with col3:
    st.metric(
        "Lowest Volatility",
        volatility.sort_values("volatility_pct").iloc[0]["Ticker"],
        f'{volatility.sort_values("volatility_pct").iloc[0]["volatility_pct"]:.2f}%'
    )

st.divider()

# ----------------------------------------------------
# TABLE VIEW
# ----------------------------------------------------
st.subheader("📋 Top 10 Most Volatile Stocks")

st.dataframe(
    top_volatile.style
    .format({"volatility_pct": "{:.2f}%"})
    .background_gradient(cmap="Oranges"),
    use_container_width=True
)

# ----------------------------------------------------
# BAR CHART
# ----------------------------------------------------
st.subheader("📊 Volatility Comparison")

st.bar_chart(
    top_volatile.set_index("Ticker")["volatility_pct"]
)

# ----------------------------------------------------
# BUSINESS INSIGHT
# ----------------------------------------------------
st.info(
    "📌 Stocks with higher volatility experience larger price fluctuations. "
    "They may offer higher returns but also carry greater risk. "
    "Lower volatility stocks are generally more stable and preferred for conservative portfolios."
)
