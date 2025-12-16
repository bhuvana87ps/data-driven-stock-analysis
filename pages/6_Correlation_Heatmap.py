import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from utils.data_loader import load_data
from utils.filters import apply_global_filters

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------
st.set_page_config(page_title="Correlation Heatmap", layout="wide")

st.title("🧠 Stock Price Correlation")
st.caption("Relationship analysis using daily returns")

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

returns_df = df.pivot(
    index="date",
    columns="Ticker",
    values="daily_return"
)

# Drop stocks with too many missing values
returns_df = returns_df.dropna(axis=1, thresh=int(len(returns_df) * 0.7))

# ----------------------------------------------------
# USER CONTROL — NUMBER OF STOCKS
# ----------------------------------------------------
max_stocks = min(returns_df.shape[1], 15)

selected_n = st.slider(
    "Select number of stocks for correlation analysis",
    min_value=5,
    max_value=max_stocks,
    value=min(10, max_stocks)
)

returns_df = returns_df.iloc[:, :selected_n]

# ----------------------------------------------------
# CORRELATION MATRIX
# ----------------------------------------------------
corr_matrix = returns_df.corr()

# ----------------------------------------------------
# HEATMAP
# ----------------------------------------------------
st.subheader("📊 Correlation Heatmap")

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    center=0,
    linewidths=0.5,
    fmt=".2f",
    ax=ax
)

st.pyplot(fig)

st.divider()

# ----------------------------------------------------
# INSIGHTS SECTION
# ----------------------------------------------------
st.subheader("📌 Key Insights")

# Exclude self-correlation
mask = ~pd.DataFrame(
    pd.np.eye(corr_matrix.shape[0], dtype=bool),
    index=corr_matrix.index,
    columns=corr_matrix.columns
)

max_corr = corr_matrix.where(mask).max().max()
min_corr = corr_matrix.where(mask).min().min()

st.markdown(
    f"""
- **Highest Correlation:** `{max_corr:.2f}`
- **Lowest Correlation:** `{min_corr:.2f}`

**Interpretation:**
- Highly correlated stocks move together and can increase portfolio risk.
- Low or negative correlations help diversification.
- Investors can combine low-correlated stocks to reduce overall volatility.
"""
)

st.info(
    "📌 Correlation does not imply causation. "
    "This analysis helps in portfolio diversification, not price prediction."
)
