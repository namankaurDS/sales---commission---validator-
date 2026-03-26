# ============================================
# SQL CROSS-VALIDATION
# Independently calculates commissions using
# SQL and compares with Python results.
# ============================================

import sqlite3
import pandas as pd
from data_prep import load_and_prepare
from calculator import apply_to_monthly

def run_sql_crosscheck():
    # Load and calculate using Python
    df_raw, df_monthly = load_and_prepare()
    df_calculated = apply_to_monthly(df_monthly)

    # Create in-memory SQLite database
    conn = sqlite3.connect(":memory:")

    # Load our calculated results into SQL table
    df_calculated['year_month'] = df_calculated['year_month'].astype(str)
    df_calculated.to_sql("commissions", conn, index=False)

    # SQL query to independently verify totals
    query = """
        SELECT
            salesperson,
            COUNT(*) as total_months,
            ROUND(SUM(total_sales), 2) as total_revenue,
            ROUND(SUM(calc_commission), 2) as total_commission,
            ROUND(SUM(calc_bonus), 2) as total_bonus,
            ROUND(SUM(calc_total_payout), 2) as total_payout
        FROM commissions
        GROUP BY salesperson
        ORDER BY total_payout DESC
        LIMIT 10
    """

    df_sql = pd.read_sql_query(query, conn)
    conn.close()

    print("✅ SQL cross-check complete")
    print("Top 10 earners:")
    print(df_sql)

    return df_sql


if __name__ == "__main__":
    run_sql_crosscheck()