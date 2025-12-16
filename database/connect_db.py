from sqlalchemy import create_engine
import pandas as pd

# Create MySQL engine
engine = create_engine("mysql+pymysql://root:@localhost/stock_analysis")

def load_data(query="SELECT * FROM stock_prices"):
    """
    Returns a DataFrame from MySQL given a query.
    """
    return pd.read_sql(query, engine)
