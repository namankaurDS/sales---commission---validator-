# ============================================
# VALIDATOR
# Compares our calculated commission against
# the original Commission Earned in the data.
# Flags every discrepancy.
# ============================================

import pandas as pd
from data_prep import load_and_prepare
from calculator import apply_to_monthly

def validate(df_raw, df_monthly_calculated):

    # Get original commission earned per rep per month from raw data
    original = df_raw.copy()
    original.columns = original.columns.str.strip().str.lower().str.replace(' ', '_')
    original['date'] = pd.to_datetime(original['date'])
    original['year_month'] = original['date'].dt.to_period('M')

    # Sum original commission earned per rep per month
    original_agg = original.groupby(['salesperson', 'year_month'])['commission_earned'].sum().reset_index()
    original_agg.columns = ['salesperson', 'year_month', 'original_commission']

    # Merge with our calculated results
    df = df_monthly_calculated.merge(original_agg, on=['salesperson', 'year_month'], how='left')

    # Calculate discrepancy
    df['discrepancy'] = round(df['calc_commission'] - df['original_commission'], 2)
    df['error_flag'] = df['discrepancy'].abs() > 0.01

    # Summary
    total = len(df)
    errors = df['error_flag'].sum()
    print(f"✅ Total rep-month records: {total}")
    print(f"⚠️  Discrepancies found: {errors} ({round(errors/total*100, 1)}%)")

    return df


if __name__ == "__main__":
    df_raw, df_monthly = load_and_prepare()
    df_calculated = apply_to_monthly(df_monthly)
    df_validated = validate(df_raw, df_calculated)
    print(df_validated[df_validated['error_flag'] == True].head(10))