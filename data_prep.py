# ============================================
# DATA PREPARATION
# Loads raw data, cleans it, and aggregates
# total monthly sales per salesperson.
# ============================================

import pandas as pd

def load_and_prepare(filepath="data/car_sales_data.csv"):

    # Step 1 — Load the raw CSV file
    df = pd.read_csv(filepath)
    print("✅ Data loaded:", df.shape[0], "rows")
    print("Columns found:", list(df.columns))

    # Step 2 — Clean column names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    # Step 3 — Convert date column to proper date format
    df['date'] = pd.to_datetime(df['date'])

    # Step 4 — Extract year and month
    df['year_month'] = df['date'].dt.to_period('M')

    # Step 5 — Aggregate total sales per salesperson per month
    monthly = df.groupby(['salesperson', 'year_month'])['sale_price'].sum().reset_index()
    monthly.columns = ['salesperson', 'year_month', 'total_sales']
    print("✅ Aggregation done:", monthly.shape[0], "rep-month combinations")

    return df, monthly


# Run this file directly to test it
if __name__ == "__main__":
    df_raw, df_monthly = load_and_prepare()
    print(df_monthly.head(10))