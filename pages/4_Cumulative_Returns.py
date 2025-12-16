import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils.data_loader import load_data
from utils.filters import apply_global_filters

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------
st.set_page_config(page_title="Cumulative Returns", layout="wide")
st.title("📈 Cumulative Returns Over Time")
st.caption("Compounded performance of selected stocks")

# ----------------------------------------------------
# LOAD + FILTER DATA
# ----------------------------------------------------
df = load_data()
df = apply_global_filters(df)

if df.empty:
    st.warning("No data available for selected filters.")
    st.stop()

# ----------------------------------------------------
# SORT DATA (VERY IMPORTANT)
# ----------------------------------------------------
df = df.sort_values(["Ticker", "date"])

# ----------------------------------------------------
# DAILY RETURNS
# ----------------------------------------------------
df["daily_return"] = df.groupby("Ticker")["close"].pct_change()

# ----------------------------------------------------
# CUMULATIVE RETURNS (✅ FIXED)
# ----------------------------------------------------
df["cumulative_return"] = (
    df.groupby("Ticker")["daily_return"]
      .transform(lambda x: (1 + x).cumprod() - 1)
)

# ----------------------------------------------------
# SELECT TOP 5 PERFORMERS (FINAL VALUE)
# ----------------------------------------------------
final_returns = (
    df.groupby("Ticker")["cumulative_return"]
      .last()
      .sort_values(ascending=False)
      .head(5)
)

top_stocks = final_returns.index.tolist()
df_top = df[df["Ticker"].isin(top_stocks)]

# ----------------------------------------------------
# PLOT
# ----------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 6))

for ticker in top_stocks:
    temp = df_top[df_top["Ticker"] == ticker]
    ax.plot(
        temp["date"],
        temp["cumulative_return"],
        label=ticker,
        linewidth=2
    )

ax.set_title("Cumulative Returns – Top 5 Performing Stocks")
ax.set_xlabel("Date")
ax.set_ylabel("Cumulative Return")
ax.legend()
ax.grid(alpha=0.3)

st.pyplot(fig)

# ----------------------------------------------------
# INSIGHTS
# ----------------------------------------------------
st.subheader("📌 Insights")
best = final_returns.index[0]
best_val = final_returns.iloc[0] * 100

st.markdown(
    f"""
    - **{best}** delivered the highest cumulative return (**{best_val:.2f}%**)
    - The chart shows **compounded growth**, not simple price change
    - Diverging lines indicate relative outperformance over time
    """
)
