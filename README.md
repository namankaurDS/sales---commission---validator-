# Sales Commission Validator

> An auditable, Python-based commission calculator built to replace 
> an error-prone manual Excel process for a 200+ rep sales team.

---

## Business Problem

A sales team of 200+ reps operates on a tiered commission structure 
with monthly bonuses and clawback rules for returned sales. The 
existing Excel-based process produces miscalculations with no audit 
trail. This project builds a robust, transparent replacement.

---

## What This Project Does

- Calculates monthly commissions using a 3-tier rate structure
- Awards performance bonuses automatically when targets are hit
- Applies clawback deductions for returned sales
- Flags every discrepancy between the original payout and the 
  correct recalculated amount
- Cross-validates all totals using independent SQL queries
- Exports a formatted, multi-sheet Excel report for the finance team

---

## Commission Rules

| Monthly Sales Total | Commission Rate |
|---|---|
| Under $50,000 | 5% |
| $50,000 – $100,000 | 8% |
| Over $100,000 | 12% + $500 bonus |

---

## Tech Stack

- **Python** (pandas, openpyxl, sqlite3)
- **SQL** (SQLite — cross-validation layer)
- **Excel** (automated output via openpyxl)

---

## Project Structure
```
sales-commission-validator/
│
├── data/                    # Raw and synthetic datasets
├── outputs/                 # Final Excel report and audit log
├── notebooks/               # Exploratory analysis
│
├── commission_rules.py      # Tier thresholds, rates, bonus config
├── data_prep.py             # Data cleaning and monthly aggregation
├── calculator.py            # Core commission engine
├── validator.py             # Discrepancy detection
├── sql_crosscheck.py        # SQL cross-validation layer
├── excel_export.py          # Excel report builder
└── README.md
```

---

## Key Assumptions & Edge Cases

- Tier logic is **flat** (not progressive) — full monthly sales volume 
  earns the rate of the tier reached
- Cliff edge documented: a $1 difference at a tier boundary can 
  produce a large commission difference — flagged in audit log
- Returns are cross-period (a Feb return can claw back a Jan sale)
- Clawback does not retroactively change tier assignment

---

## Status

🔨 In progress
