import streamlit as st
import pandas as pd
import numpy as np

from utils.data_loader import load_data
from utils.filters import apply_global_filters

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(page_title="Market Overview", layout="wide")

st.title("📊 Market Overview")
st.caption("Executive summary of Nifty 50 stock performance")

# --------------------------------------------------
# LOAD + FILTER DATA
# --------------------------------------------------
df = load_data()
df = apply_global_filters(df)

# --------------------------------------------------
# BASIC VALIDATION
# --------------------------------------------------
required_cols = {"Ticker", "date", "close", "volume"}
if not required_cols.issubset(df.columns):
    st.error("Required columns missing from dataset")
    st.stop()

# --------------------------------------------------
# YEARLY RETURNS CALCULATION
# --------------------------------------------------
df = df.sort_values(["Ticker", "date"])

yearly = (
    df.groupby("Ticker")
    .agg(
        start_price=("close", "first"),
        end_price=("close", "last"),
        avg_volume=("volume", "mean")
    )
    .reset_index()
)

yearly["yearly_return"] = (
    (yearly["end_price"] - yearly["start_price"]) /
    yearly["start_price"]
)

# --------------------------------------------------
# MARKET KPIs
# --------------------------------------------------
total_stocks = yearly.shape[0]
green_stocks = (yearly["yearly_return"] > 0).sum()
red_stocks = (yearly["yearly_return"] <= 0).sum()

green_pct = (green_stocks / total_stocks) * 100
red_pct = 100 - green_pct

avg_return = yearly["yearly_return"].mean()
avg_volume = yearly["avg_volume"].mean()

# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------
st.markdown("### 📌 Market Snapshot")

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("Total Stocks", total_stocks)
c2.metric("🟢 Green Stocks", f"{green_pct:.1f}%")
c3.metric("🔴 Red Stocks", f"{red_pct:.1f}%")
c4.metric("📈 Avg Return", f"{avg_return*100:.2f}%")
c5.metric("📊 Avg Volume", f"{avg_volume:,.0f}")

# --------------------------------------------------
# TOP GAINERS & LOSERS
# --------------------------------------------------
top_gainers = yearly.sort_values(
    "yearly_return", ascending=False
).head(10)

top_losers = yearly.sort_values(
    "yearly_return", ascending=True
).head(10)

st.markdown("### 🟢 Top 10 Gainers & 🔴 Top 10 Losers")

g1, g2 = st.columns(2)

with g1:
    st.subheader("🟢 Top Gainers")
    st.dataframe(
        top_gainers[["Ticker", "yearly_return"]]
        .assign(yearly_return=lambda x: x["yearly_return"] * 100)
        .rename(columns={"yearly_return": "Return (%)"}),
        use_container_width=True
    )

with g2:
    st.subheader("🔴 Top Losers")
    st.dataframe(
        top_losers[["Ticker", "yearly_return"]]
        .assign(yearly_return=lambda x: x["yearly_return"] * 100)
        .rename(columns={"yearly_return": "Return (%)"}),
        use_container_width=True
    )

# --------------------------------------------------
# MARKET SENTIMENT BAR
# --------------------------------------------------
st.markdown("### 📊 Market Sentiment")

sentiment_df = pd.DataFrame({
    "Category": ["Green Stocks", "Red Stocks"],
    "Percentage": [green_pct, red_pct]
})

st.bar_chart(sentiment_df.set_index("Category"))

# --------------------------------------------------
# INVESTMENT INSIGHTS (AUTO)
# --------------------------------------------------
st.markdown("### 🧠 Investment Insights")

insights = []

if green_pct > 60:
    insights.append("📈 Market shows strong bullish momentum.")
elif green_pct < 40:
    insights.append("⚠️ Market sentiment is weak; caution advised.")
else:
    insights.append("➖ Market is range-bound with mixed performance.")

if avg_return > 0:
    insights.append("✅ Overall average returns are positive.")
else:
    insights.append("❌ Average returns indicate market pressure.")

top_vol = top_gainers.iloc[0]
worst_vol = top_losers.iloc[0]

insights.append(
    f"🚀 Best performer: **{top_vol['Ticker']}** "
    f"({top_vol['yearly_return']*100:.2f}%)"
)

insights.append(
    f"📉 Worst performer: **{worst_vol['Ticker']}** "
    f"({worst_vol['yearly_return']*100:.2f}%)"
)

for i in insights:
    st.markdown(f"- {i}")

# --------------------------------------------------
# DECISION SUPPORT NOTE
# --------------------------------------------------
st.info(
    "💡 **Decision Support:**\n"
    "• High returns + high volume → Strong interest\n"
    "• High volatility → Higher risk\n"
    "• Sector rotation visible in detailed pages"
)
