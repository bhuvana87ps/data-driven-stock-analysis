# 📊 Data-Driven Stock Market Analysis  
### End-to-End Analytics using Python, MySQL, Streamlit & Power BI

---

# 📌 Project Overview

This project demonstrates a complete **data analytics pipeline** for stock market data — from **data ingestion and storage** to **interactive dashboards** and **business-ready BI reports**.

The project showcases:

- Real-world financial data modeling
- KPI calculation using DAX
- Dashboard storytelling
- Tool interoperability (Python → MySQL → Power BI)
- Business-oriented visualization design

---

# 🧱 Tech Stack

| Category | Tools |
|---|---|
| Programming | Python |
| Database | MySQL (XAMPP) |
| Libraries | Pandas, NumPy |
| App Dashboard | Streamlit |
| BI Tool | Power BI Desktop |
| Data Format | CSV (fallback for BI integration) |

---

# 🗂️ Data Schema

## Table: `stock_prices`

| Column | Description |
|---|---|
| id | Unique row identifier |
| ticker | Stock symbol |
| trade_date | Trading timestamp |
| month | Trading month |
| open | Opening price |
| high | Highest price |
| low | Lowest price |
| close | Closing price |
| volume | Trade volume |
| created_at | Data insertion timestamp |

---

# 🔄 Data Flow Architecture

```text
Python (ETL)
      ↓
MySQL Database
      ↓
CSV Export
      ↓
Power BI Dashboard
