# ============================================
# COMMISSION RULES CONFIGURATION
# All business rules live here in one place.
# If rules change, we only update this file.
# ============================================

# Tier thresholds (monthly sales total in USD)
TIER_THRESHOLDS = [
    (0, 50000, 0.05),        # Under $50k → 5%
    (50000, 100000, 0.08),   # $50k–$100k → 8%
    (100000, float('inf'), 0.12)  # Over $100k → 12%
]

# Bonus: flat cash bonus when monthly sales exceed this amount
BONUS_THRESHOLD = 100000
BONUS_AMOUNT = 500

# Clawback: percentage of sale price deducted when a sale is returned
# (same rate the rep earned on that original sale)
CLAWBACK_RATE = "original_rate"  # means: use whatever rate was applied

# Synthetic return rate (we inject this % of transactions as returns)
SYNTHETIC_RETURN_RATE = 0.05  # 5%