# ============================================
# COMMISSION CALCULATOR
# Takes monthly sales totals and applies
# tier logic, bonuses, and clawbacks.
# ============================================

from commission_rules import TIER_THRESHOLDS, BONUS_THRESHOLD, BONUS_AMOUNT

def get_commission_rate(total_sales):
    # Find which tier this rep falls into
    for lower, upper, rate in TIER_THRESHOLDS:
        if lower <= total_sales < upper:
            return rate
    return TIER_THRESHOLDS[-1][2]  # fallback to highest tier

def calculate_commission(total_sales):
    rate = get_commission_rate(total_sales)
    commission = total_sales * rate

    # Add bonus if target hit
    bonus = BONUS_AMOUNT if total_sales >= BONUS_THRESHOLD else 0

    return round(commission, 2), round(bonus, 2), rate

def apply_to_monthly(df_monthly):
    df = df_monthly.copy()

    # Apply calculator to every row
    results = df['total_sales'].apply(lambda x: calculate_commission(x))

    df['calc_commission'] = results.apply(lambda x: x[0])
    df['calc_bonus']      = results.apply(lambda x: x[1])
    df['calc_rate']       = results.apply(lambda x: x[2])
    df['calc_total_payout'] = df['calc_commission'] + df['calc_bonus']

    return df


# Test it directly
if __name__ == "__main__":
    from data_prep import load_and_prepare
    df_raw, df_monthly = load_and_prepare()
    df_results = apply_to_monthly(df_monthly)
    print(df_results.head(10))