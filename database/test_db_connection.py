from connect_db import load_data

try:
    df = load_data("SELECT ticker, close FROM stock_prices LIMIT 5;")
    print(df)
    print("✔ Database connection successful")
except Exception as e:
    print("❌ Database connection failed:", e)
