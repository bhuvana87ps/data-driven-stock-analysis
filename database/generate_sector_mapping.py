import sys
import os
import pandas as pd

# Add project root to Python path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

from database.connect_db import load_data

# -------------------------------------------
# Generate sector mapping from actual DB data
# -------------------------------------------

df = load_data("SELECT DISTINCT ticker FROM stock_prices")

sector_map = {
    "SBIN": "BANKING",
    "HDFCBANK": "BANKING",
    "ICICIBANK": "BANKING",
    "AXISBANK": "BANKING",

    "TCS": "IT",
    "INFY": "IT",
    "HCLTECH": "IT",
    "WIPRO": "IT",

    "RELIANCE": "ENERGY",
    "ONGC": "ENERGY",
    "BPCL": "ENERGY",

    "ITC": "FMCG",
    "HINDUNILVR": "FMCG",
    "NESTLEIND": "FMCG",

    "BAJFINANCE": "FINANCE",
    "BAJAJFINSV": "FINANCE",
    "BAJAJ-AUTO": "AUTOMOBILES",
}

df["sector"] = df["ticker"].map(sector_map)
df = df.dropna()

df.to_csv("data/sector_mapping.csv", index=False)

print("✅ sector_mapping.csv generated successfully")
