import streamlit as st
import pandas as pd
import numpy as np

from utils.data_loader import load_data
from utils.filters import apply_global_filters

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(page_title="Top Gainers & Losers", layout="wide")

st.title("📈 Top Gainers & Losers")
st.caption("Yearly return ranking of Nifty 50 stocks")

# --------------------------------------------------
# LOAD + FILTER DATA
# --------------------------------------------------
df = load_data()
df = apply_global_filters(df)

# --------------------------------------------------
# VALIDATION
# --------------------------------------------------
required_cols = {"Ticker", "date", "close"}
if not required_cols.issubset(df.columns):
    st.error("Required columns missing from dataset")
    st.stop()

# --------------------------------------------------
# YEARLY RETURN CALCULATION
# --------------------------------------------------
df = df.sort_values(["Ticker", "date"])

returns = (
    df.groupby("Ticker")
    .agg(
        start_price=("close", "first"),
        end_price=("close", "last")
    )
    .reset_index()
)

returns["yearly_return"] = (
    (returns["end_price"] - returns["start_price"]) /
    returns["start_price"]
)

returns["Return (%)"] = returns["yearly_return"] * 100

# --------------------------------------------------
# TOP 10 GAINERS & LOSERS
# --------------------------------------------------
top_gainers = returns.sort_values(
    "yearly_return", ascending=False
).head(10)

top_losers = returns.sort_values(
    "yearly_return", ascending=True
).head(10)

# --------------------------------------------------
# KPI SUMMARY
# --------------------------------------------------
best = top_gainers.iloc[0]
worst = top_losers.iloc[0]

k1, k2, k3 = st.columns(3)

k1.metric(
    "🚀 Best Performer",
    best["Ticker"],
    f"{best['Return (%)']:.2f}%"
)

k2.metric(
    "📉 Worst Performer",
    worst["Ticker"],
    f"{worst['Return (%)']:.2f}%"
)

k3.metric(
    "📊 Avg Return (All Stocks)",
    f"{returns['Return (%)'].mean():.2f}%"
)

# --------------------------------------------------
# TABLES
# --------------------------------------------------
st.markdown("### 🟢 Top 10 Gainers vs 🔴 Top 10 Losers")

c1, c2 = st.columns(2)

with c1:
    st.subheader("🟢 Top Gainers")
    st.dataframe(
        top_gainers[["Ticker", "Return (%)"]]
        .style.format({"Return (%)": "{:.2f}%"})
        .background_gradient(cmap="Greens"),
        use_container_width=True
    )

with c2:
    st.subheader("🔴 Top Losers")
    st.dataframe(
        top_losers[["Ticker", "Return (%)"]]
        .style.format({"Return (%)": "{:.2f}%"})
        .background_gradient(cmap="Reds"),
        use_container_width=True
    )

# --------------------------------------------------
# BAR CHART (VISUAL COMPARISON)
# --------------------------------------------------
st.markdown("### 📊 Return Comparison")

chart_df = pd.concat([
    top_gainers.assign(Type="Gainer"),
    top_losers.assign(Type="Loser")
])

st.bar_chart(
    chart_df.set_index("Ticker")["Return (%)"]
)

# --------------------------------------------------
# INSIGHTS
# --------------------------------------------------
st.markdown("### 🧠 Insights")

st.markdown(
    f"""
- **{best['Ticker']}** delivered the highest yearly return, indicating strong momentum.
- **{worst['Ticker']}** showed the steepest decline, signaling underperformance.
- Wide dispersion between gainers and losers suggests **stock-specific opportunities**, not a uniform market trend.
- Ideal for **momentum strategies** and **risk screening**.
"""
)

# --------------------------------------------------
# DECISION SUPPORT
# --------------------------------------------------
st.info(
    "💡 **How to use this view:**\n"
    "• Long-term investors → focus on consistent gainers\n"
    "• Short-term traders → exploit momentum reversals\n"
    "• Risk-averse users → avoid high negative return stocks"
)
