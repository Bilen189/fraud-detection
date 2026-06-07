## Project Structure

```text
fraud-detection/
├── data/
├── notebooks/
├── src/
├── reports/
├── tests/
├── requirements.txt
└── README.md
```

# Fraud Detection for E-commerce and Bank Transactions

## Project Overview
This project analyzes and preprocesses fraud detection datasets for e-commerce and bank transactions.

## Data
- Fraud_Data.csv: e-commerce transaction data
- IpAddress_to_Country.csv: IP range to country mapping
- creditcard.csv: anonymized bank transaction data

## Project Structure
- data/raw: original datasets
- data/processed: cleaned datasets
- notebooks: exploratory analysis and preprocessing notebooks
- src: reusable Python modules
- reports: interim and final reports
- tests: unit tests

## Setup
```bash
pip install -r requirements.txt