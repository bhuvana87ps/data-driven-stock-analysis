import streamlit as st
import pandas as pd

def apply_global_filters(df: pd.DataFrame) -> pd.DataFrame:
    st.sidebar.header("Global Filters")

    # Date filter
    min_date = df["date"].min()
    max_date = df["date"].max()

    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    if len(date_range) == 2:
        start_date, end_date = pd.to_datetime(date_range)
        df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

    # Ticker filter
    tickers = sorted(df["Ticker"].unique())
    selected_tickers = st.sidebar.multiselect(
        "Select Stocks",
        options=tickers,
        default=tickers
    )

    if selected_tickers:
        df = df[df["Ticker"].isin(selected_tickers)]

    return df
