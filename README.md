# 📊 Data-Driven Stock Analysis  
### Organizing, Cleaning, and Visualizing Market Trends

---

## 📌 Project Overview

This project implements a **complete end-to-end data analytics pipeline** for analyzing stock market performance.  
It starts from **raw YAML stock data**, processes it through a **custom ETL pipeline**, stores clean data in **MySQL**, and delivers insights via **Streamlit** and **Power BI dashboards**.

The solution helps investors, analysts, and decision-makers understand:
- Overall market health
- Top gainers and losers
- Market sentiment (Bullish / Neutral / Bearish)
- Risk and volatility trends

---

## 🎯 Problem Statement

Stock market data is often available in raw, semi-structured formats that are difficult to analyze directly.  
Manual analysis makes it hard to identify:
- Market direction
- Consistent performers
- Risk exposure
- Sector-wise trends

This project solves that by building a **scalable analytics workflow** that converts raw data into **actionable insights**.

---

## 🛠️ Tech Stack

### Languages & Libraries
- Python
- Pandas, NumPy
- PyYAML
- SQLAlchemy
- Matplotlib / Seaborn
- Streamlit

### Database
- MySQL (XAMPP)

### Visualization
- Streamlit (interactive analytics)
- Power BI (executive dashboards)

---

## 📂 Data Source

- Raw data provided in **YAML format**
- Organized as:
  - Month-wise folders  
  - Date-wise YAML files  
- Each file contains:
  - Ticker
  - Date & time
  - Open, High, Low, Close
  - Volume

This structure closely resembles real-world market data feeds.

---

## ⚙️ ETL Pipeline Architecture

### 1️⃣ Extraction (`etl/extract.py`)
- Recursively scans data folders
- Reads YAML files
- Converts them into Python dictionaries

### 2️⃣ Transformation (`etl/transform.py`)
- Date normalization
- Numeric cleaning
- Missing value handling
- Data validation

### 3️⃣ Loading (`etl/load.py`)
- Generates:
  - Symbol-wise CSV files (one per stock)
  - Combined dataset
  - Monthly summary reports

### 4️⃣ Orchestration (`etl/run_etl.py`)
- Controls the full ETL flow
- Ensures correct execution order
- Handles logging and errors

---

## 🗄️ Database Layer (MySQL)

- Database: `stock_analysis`
- Table: `stock_prices`

**Columns**
- ticker
- date
- month
- open
- high
- low
- close
- volume

Clean data is loaded using a dedicated Python loader script, enabling SQL-based analytics and BI integration.

---

## 📊 Data Analysis Performed

- Yearly stock returns
- Green vs Red stock classification
- Market breadth (% green stocks)
- Average price and volume
- Volatility (standard deviation of returns)
- Cumulative returns
- Monthly top gainers and losers
- Sector-wise performance

---

## 🖥️ Streamlit Dashboard

**Purpose**
- Interactive, analyst-focused exploration

**Features**
- Market overview KPIs
- Stock-level filters
- Volatility analysis
- Correlation heatmap
- Sector performance

Streamlit enables rapid, Python-driven analytics and real-time interaction.

---

## 📈 Power BI Dashboard

**Purpose**
- Executive-level reporting and decision support

**Key Visuals**
- Market overview KPIs
- Green vs Red stocks
- Market sentiment card
- Market health gauge
- Conditional formatting using DAX

**Market Sentiment Logic**
- ≥ 60% green stocks → Bullish
- 40–59% → Neutral
- < 40% → Bearish

---

## 🎯 Business Use Cases

- Stock performance ranking
- Market health assessment
- Investment decision support
- Risk and volatility evaluation
- Sector-wise comparison

---

## 🚀 Project Outcomes

- Built a real-world ETL pipeline
- Created clean, analysis-ready financial data
- Integrated database and BI tools
- Delivered interactive dashboards
- Developed a portfolio-grade analytics project

---

## 🏁 Conclusion

This project demonstrates the **complete lifecycle of a data analytics solution**, from raw data ingestion to business-ready insights.  
It follows industry-aligned practices and is suitable for **Data Analyst / Business Analyst / Junior Data Engineer** roles.

---

## 📌 How to Run (High Level)

1. Run ETL pipeline  
   ```bash
   python etl/run_etl.py
2. Load data into MySQL
   ```bash
   python database/db_loader.py
3. Launch Streamlit app
  ```bash
   streamlit run app.py
4. Open Power BI file and refresh data source


Author
Bhuvaneswari G
Data Analytics Project

