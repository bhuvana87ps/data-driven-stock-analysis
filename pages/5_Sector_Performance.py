import os
import pandas as pd
import streamlit as st

from utils.data_loader import load_data
from utils.filters import apply_global_filters

# -------------------------------------------------
# PAGE SETUP
# -------------------------------------------------
st.set_page_config(page_title="Sector Performance", layout="wide")
st.title("🏭 Sector Performance")

# -------------------------------------------------
# LOAD DATA (SINGLE SOURCE OF TRUTH)
# -------------------------------------------------
df = load_data()
df = apply_global_filters(df)

# -------------------------------------------------
# LOAD SECTOR MAPPING
# -------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sector_path = os.path.join(BASE_DIR, "data", "sector_mapping.csv")

sector_map = pd.read_csv(sector_path)

# Normalize columns
sector_map.columns = sector_map.columns.str.lower()
sector_map["ticker"] = sector_map["ticker"].str.strip().str.upper()

# -------------------------------------------------
# PREPARE RETURNS
# -------------------------------------------------
df = df.sort_values(["Ticker", "date"])
df["daily_return"] = df.groupby("Ticker")["close"].pct_change()

monthly_returns = (
    df.groupby(["Ticker", pd.Grouper(key="date", freq="M")])["daily_return"]
    .mean()
    .reset_index()
)

# -------------------------------------------------
# MERGE WITH SECTOR
# -------------------------------------------------
merged = monthly_returns.merge(
    sector_map,
    left_on="Ticker",
    right_on="ticker",
    how="inner"
)

if merged.empty:
    st.error("No matching tickers between stock data and sector mapping.")
    st.stop()

# -------------------------------------------------
# SECTOR PERFORMANCE
# -------------------------------------------------
sector_perf = (
    merged.groupby("sector")["daily_return"]
    .mean()
    .sort_values(ascending=False)
)

st.subheader("Average Monthly Return by Sector")
st.bar_chart(sector_perf)
