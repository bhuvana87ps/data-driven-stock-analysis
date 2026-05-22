# 📊 Data-Driven Stock Market Analysis  
**End-to-End Analytics using Python, MySQL, Streamlit & Power BI**

---

## 📌 Project Overview
This project demonstrates a **complete data analytics pipeline** for stock market data — from **data ingestion and storage** to **interactive dashboards** and **business-ready BI reports**.

The project is designed to showcase:
- Real-world financial data modeling
- KPI calculation using DAX
- Dashboard storytelling
- Tool interoperability (Python → SQL → Power BI)

---

## 🧱 Tech Stack
- **Programming**: Python  
- **Database**: MySQL (XAMPP)
- **Libraries**: Pandas, NumPy  
- **App Dashboard**: Streamlit  
- **BI Tool**: Power BI Desktop  
- **Data Format**: CSV (used as fallback for BI)

---

## 🗂️ Data Schema

**Table: `stock_prices`**

| Column | Description |
|------|------------|
| id | Unique row identifier |
| ticker | Stock symbol |
| trade_date | Trading timestamp |
| month | Trading month |
| open | Opening price |
| high | Highest price |
| low | Lowest price |
| close | Closing price |
| volume | Trade volume |
| created_at | Data insertion time |

---

## 🔄 Data Flow Architecture
Python (ETL)
↓
MySQL Database
↓
CSV Export
↓
Power BI Dashboard


> ⚠️ CSV import was used in Power BI for stability during presentation time.

---

## 📈 Power BI Dashboard

### ✅ Page 1 – Market Overview (Completed)

This page provides a **high-level snapshot of the entire market** using KPI cards and a global date slicer.

---

## 🧩 Page 1 Components

### 🔹 Global Date Slicer
- Visual: **Slicer**
- Field: `Trade Date`
- Type: **Between**
- Scope: Filters all visuals on Page 1

---

## 📊 KPI Cards (Exact DAX Used)


---

### 🟦 Total Stocks
**Purpose**: Market breadth

```DAX
Total Stocks = COUNT(stock_prices[ticker])
🟦 Average Close Price

Purpose: Overall price level

```DAX
Avg Close Price = AVERAGE(stock_prices[close])
Formatting

Display Units: Thousands (K)

Decimal Places: 2
🟦 Daily Return (Calculated Column)

```DAX
Daily Return =
DIVIDE(
    stock_prices[close] - stock_prices[open],
    stock_prices[open]
)
🟦 Average Daily Return (%)

Purpose: Market performance indicator

```DAX
Avg Daily Return (%) = AVERAGE(stock_prices[Daily Return])
Formatting

Percentage

2 decimal places

🟦 Total Volume

Purpose: Market liquidity

```DAX
Total Volume = SUM(stock_prices[volume])


Formatting

Display Units: Billions (Bn)

🎨 Conditional Logic (Optional)
Market Direction Label

```DAX
Market Color =
IF(
    stock_prices[Daily Return] >= 0,
    "Green",
    "Red"
)


Used for conditional formatting or sentiment cards.

📐 Page Layout

```DAX
[ Trade Date Slicer ]

[ Total Stocks ] [ Avg Close Price ] [ Avg Daily Return (%) ] [ Total Volume ]


Design Principles:

Executive-friendly

One-glance insights

Clean & minimal UI

🎯 Business Use Cases

Market trend monitoring

Investor performance tracking

Educational financial analytics

Portfolio research dashboards

🚀 Future Enhancements
📌 Power BI

Top Gainers & Losers page

Volatility & risk analysis

Correlation heatmap

Monthly & yearly performance views

Drill-through stock detail pages

Conditional color-driven sentiment cards

📌 Data & Backend

Live MySQL connector with scheduled refresh

Incremental data loading

Indexing for performance optimization

📌 Advanced Analytics

Moving averages (SMA / EMA)

Volatility indicators

Sharpe ratio & risk metrics

ML-based trend prediction

📌 Deployment

Publish to Power BI Service

Role-based access (RLS)

Automated refresh pipelines

✅ Project Status

✔ Data ingestion completed
✔ KPI modeling completed
✔ Power BI Page 1 finalized
✔ Presentation-ready

👤 Author

Bhuvana PS
Data Analytics | Python | SQL | Power BI | Streamlit

⭐ If you like this project, feel free to fork, star, and explore further!


---

If you want next:
- **GitHub project description + tags**
- **Viva / interview Q&A**
- **Page 2 – Top Gainers & Losers (step-by-step)**
- **Power BI storytelling script**

Just tell me.
