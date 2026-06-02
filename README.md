# Retail Data ETL Pipeline

An end-to-end Python Extract, Transform, Load (ETL) pipeline for retail data, complete with an interactive Streamlit dashboard.

## Features
- **Data Generation (`generate_messy_data.py`)**: Simulates 10,000 rows of dirty retail data (duplicates, missing values, incorrect types).
- **Data Cleaning (`clean_data.py`)**: Sanitizes the data by removing duplicates, fixing string/numeric conversions, handling nulls, and filtering logic errors.
- **Database Loading (`load_to_db.py`)**: Ingests the cleaned data into a local **SQLite** database (`sales.db`), enforcing a strict SQL schema.
- **Orchestration (`main_pipeline.py`)**: A single master script to run the entire ETL flow unattended.
- **Dashboard (`dashboard.py`)**: A **Streamlit** web app to visualize revenue metrics, product breakdowns, and sales trends.

## Setup & Quickstart

We have provided a `Makefile` to simplify setup and execution.

### 1. Initialize the Environment
This command creates a Python virtual environment and installs all dependencies (`pandas`, `sqlite3`, `streamlit`, `plotly`).
```bash
make setup
```

### 2. Run the ETL Pipeline
This command generates the raw data, cleans it, and loads it into the `sales.db` SQLite database.
```bash
make run
```

### 3. Launch the Dashboard
Once the database is populated, launch the interactive dashboard to view the data!
```bash
make dashboard
```

## Clean Up
To remove the virtual environment and all generated databases/data files:
```bash
make clean
```
