import pandas as pd
import re

from dateutil import parser

class Transformer:
    """
    Transformer class cleans and standardizes each YAML entry into
    a consistent, analysis-ready format.

    Responsibilities:
    - Normalize dates
    - Convert string numbers to float/int
    - Handle missing values safely
    - Validate rows before loading
    """

    # Fields that must be numeric
    NUMERIC_FIELDS = ["open", "high", "low", "close", "volume"]

    def __init__(self):
        pass

    # ---------------------------------------------------------
    # 1. DATE NORMALIZATION
    # ---------------------------------------------------------
    def normalize_date(self, date_value):
        """
        Converts any date format into 'YYYY-MM-DD HH:MM:SS'
        """

        if not date_value:
            return None

        try:
            # Example: "2023-10-30 05:30:00"
            dt = parser.parse(str(date_value))
            return dt.strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            return None

    # ---------------------------------------------------------
    # 2. NUMERIC CLEANING
    # ---------------------------------------------------------
    def clean_number(self, value):
        """
        Convert values like "1,45,000" or "602.95" or 15322196 into valid numbers.
        """
        if value is None:
            return None

        # Remove commas, spaces
        if isinstance(value, str):
            value = value.replace(",", "").strip()

        try:
            # Convert float / int automatically
            if "." in str(value):
                return float(value)
            else:
                return int(value)
        except Exception:
            return None

    # ---------------------------------------------------------
    # 3. MASTER NORMALIZE METHOD
    # ---------------------------------------------------------
    def normalize(self, entry):
        """
        Convert raw YAML entry dict into a clean row dict.
        """

        clean_row = {}

        # Extract ticker
        clean_row["Ticker"] = entry.get("Ticker")

        # Extract and normalize date
        clean_row["date"] = self.normalize_date(entry.get("date"))

        # Extract or auto-generate month
        month_value = entry.get("month")
        if not month_value and clean_row["date"]:
            month_value = clean_row["date"][:7]   # YYYY-MM
        clean_row["month"] = month_value

        # Clean numeric fields
        for field in self.NUMERIC_FIELDS:
            clean_row[field] = self.clean_number(entry.get(field))

        return clean_row

    # ---------------------------------------------------------
    # 4. VALIDATION METHOD
    # ---------------------------------------------------------
    def is_valid(self, row):
        """
        Basic validation before sending row to loader.
        Ensures:
        - Ticker exists
        - Date exists
        - Close price is not missing
        """

        if not row.get("Ticker"):
            return False
        if not row.get("date"):
            return False
        if row.get("close") is None:
            return False

        return True
        """
        return (
            row.get("Ticker") is not None and
            row.get("date") is not None and
            row.get("close") is not None
        )
        
        """
