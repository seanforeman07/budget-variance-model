# Finance SQL Reporting Project

Python project for entry-level financial analysis that compares budget vs. actual spend and highlights variance drivers.

## What It Does
- Loads budget and actual finance data
- Calculates variance amount and variance percent
- Summarizes results by department and month
- Prints top over-budget and under-budget lines

## Stack
- Python 3.11+
- pandas
- pytest

## Run
```bash
cd /Users/seanforeman/Documents/Playground/finance-budget-variance-analyzer
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/variance_analysis.py
python -m pytest -q
```

## Resume Bullet Ideas
- Built a Python budget-vs-actual variance workflow to surface top monthly over/under-spend drivers.
- Automated department-level variance reporting with repeatable CLI execution and tests.
