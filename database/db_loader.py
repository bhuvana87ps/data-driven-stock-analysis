import pandas as pd
from sqlalchemy import create_engine
import os

engine = create_engine("mysql+pymysql://root:@localhost/stock_analysis")

df = pd.read_csv("output_combined/all_data.csv")

# FIX: rename column to match MySQL schema
df = df.rename(columns={"date": "trade_date"})

df["month"] = df["trade_date"].str[:7]

df.to_sql("stock_prices", engine, if_exists="append", index=False, chunksize=5000)

print("Data loaded into MySQL successfully")
