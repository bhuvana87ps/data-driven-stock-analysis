import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv("output_combined/all_data.csv")

    # Canonical column cleanup
    df.columns = df.columns.str.strip()

    # Enforce correct column names
    if "Ticker" not in df.columns:
        raise ValueError("Ticker column missing from dataset")

    df["Ticker"] = df["Ticker"].str.strip().str.upper()
    df["date"] = pd.to_datetime(df["date"])

    return df
