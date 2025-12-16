import os
import pandas as pd
from pathlib import Path


class Loader:
    """
    Loader class is responsible for writing clean, validated rows into:
    - Per-symbol CSV files  (SBIN.csv, TCS.csv, etc.)
    - Combined master CSV   (all_data.csv)
    - Monthly summary reports (monthly_summary_YYYY-MM.csv)
    """

    def __init__(self, output_csv_dir, output_combined_dir, output_reports_dir):
        self.output_csv_dir = Path(output_csv_dir)
        self.output_combined_dir = Path(output_combined_dir)
        self.output_reports_dir = Path(output_reports_dir)

        # Ensure directories exist
        self.output_csv_dir.mkdir(parents=True, exist_ok=True)
        self.output_combined_dir.mkdir(parents=True, exist_ok=True)
        self.output_reports_dir.mkdir(parents=True, exist_ok=True)

        # Keep all rows in memory for combined CSV + monthly stats
        self.all_rows = []

    # ---------------------------------------------------------
    # 1. WRITE / APPEND SYMBOL-WISE CSV
    # ---------------------------------------------------------
    def write_symbol_csv(self, row):
        """
        Writes a clean row into its corresponding <Ticker>.csv file.
        If file doesn't exist → create with header.
        If file exists → append without header.
        """

        ticker = row.get("Ticker")
        if not ticker:
            return   # Safe check

        file_path = self.output_csv_dir / f"{ticker}.csv"
        df = pd.DataFrame([row])

        # Write new file OR append to existing file
        if not file_path.exists():
            df.to_csv(file_path, index=False)
        else:
            df.to_csv(file_path, mode="a", header=False, index=False)

        # Store for combined + monthly reports
        self.all_rows.append(row)

    # ---------------------------------------------------------
    # 2. WRITE COMBINED CSV FILE (ALL TICKERS)
    # ---------------------------------------------------------
    def write_combined_csv(self):
        """
        Writes all rows collected during ETL into a single dataset.
        Useful for Power BI, Streamlit, and analytics.
        """

        if not self.all_rows:
            return

        df = pd.DataFrame(self.all_rows)
        output_file = self.output_combined_dir / "all_data.csv"
        df.to_csv(output_file, index=False)

    # ---------------------------------------------------------
    # 3. GENERATE MONTHLY SUMMARY REPORTS
    # ---------------------------------------------------------
    def write_monthly_reports(self):
        """
        Monthly summary per (month, Ticker):
        - Average open, high, low, close
        - Total volume
        - Row count

        Creates file: monthly_summary_YYYY-MM.csv
        """

        if not self.all_rows:
            return

        df = pd.DataFrame(self.all_rows)

        # Ensure month column exists
        if "month" not in df.columns:
            df["month"] = df["date"].str.slice(0, 7)

        grouped = df.groupby(["month", "Ticker"]).agg(
            open_avg=("open", "mean"),
            high_avg=("high", "mean"),
            low_avg=("low", "mean"),
            close_avg=("close", "mean"),
            volume_sum=("volume", "sum"),
            rows=("date", "count"),
        ).reset_index()

        # Output each month into its own CSV
        for month, data in grouped.groupby("month"):
            output_file = self.output_reports_dir / f"monthly_summary_{month}.csv"
            data.to_csv(output_file, index=False)
