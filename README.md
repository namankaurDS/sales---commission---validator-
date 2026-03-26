# Sales Commission Validator

> An auditable, Python-based commission calculator built to replace 
> an error-prone manual Excel process for a 200+ rep sales team.

---

## Business Problem

A sales team of 200+ reps operates on a tiered commission structure 
with monthly bonuses and clawback rules for returned sales. The 
existing process applied inconsistent per-transaction commission rates 
(ranging from 5–15%) with no standardised logic and no audit trail. 
This project builds a robust, transparent replacement.

---

## What This Project Does

- Calculates monthly commissions using a standardised 3-tier structure
- Awards $500 performance bonus automatically when monthly target is hit
- Flags every discrepancy between original payouts and correct amounts
- Cross-validates all totals independently using SQL queries
- Exports a formatted, multi-sheet Excel report for the finance team

---

## Commission Rules

| Monthly Sales Total | Commission Rate |
|---|---|
| Under $50,000 | 5% |
| $50,000 – $100,000 | 8% |
| Over $100,000 | 12% + $500 bonus |

---

## Key Findings

- The original dataset applied **random per-transaction rates** (0.05–0.15) 
  with no standardised logic across 1M+ records
- A tier-based system creates **fairness and predictability** — 
  rewarding total monthly performance rather than individual transactions
- SQL cross-validation **independently confirmed** Python calculations, 
  with top earner (Michael Smith) generating $1.9M in annual commission
- **Cliff edge documented:** a $1 difference at a tier boundary can 
  produce significant commission differences — flagged in audit log

---

## Tech Stack

- **Python** (pandas, openpyxl, sqlite3)
- **SQL** (SQLite — cross-validation layer)
- **Excel** (automated 3-sheet report via openpyxl)

> Dataset: Car Sales Data (2.5M rows) — available on Kaggle. 
> Not included in repo due to file size.

---

## Project Structure
```
sales-commission-validator/
│
├── data/                    # Raw dataset (not tracked - see .gitignore)
├── outputs/                 # Final Excel report and audit log
├── notebooks/               # Exploratory analysis
│
├── commission_rules.py      # Tier thresholds, rates, bonus config
├── data_prep.py             # Data cleaning and monthly aggregation
├── calculator.py            # Core commission engine
├── validator.py             # Discrepancy detection
├── sql_crosscheck.py        # SQL cross-validation layer
├── excel_export.py          # Excel report builder
├── requirements.txt         # Python dependencies
└── README.md
```

---

## How To Run
```bash
# 1. Clone the repo
git clone https://github.com/namankaurDS/sales---commission---validator-.git

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add dataset to data/ folder (download from Kaggle: Car Sales Data)

# 4. Run the full pipeline
python excel_export.py
```

---

## Key Assumptions & Edge Cases

- Tier logic is **flat** — full monthly sales volume earns the rate 
  of the tier reached
- Cliff edge: a $1 difference at a tier boundary creates a large 
  commission jump — documented in audit log
- Original data used inconsistent per-transaction rates — 
  discrepancies reflect method difference, not data entry errors

---

## Status

✅ Complete