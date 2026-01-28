import pandas as pd

# 1. Load the raw data
df = pd.read_csv('data/raw_sales.csv')

print("--- 🔍 DATA AUDIT REPORT ---")

# Check 1: How does the data look?
print("\n[1] First 5 Rows (Notice the '$' signs):")
print(df.head())

# Check 2: What are the data types?
print("\n[2] Column Info (Notice 'price' is Object/Text, not Number):")
print(df.info()) 

# Check 3: Are there duplicates?
print("\n[3] Duplicate Rows Found:")
print(df.duplicated().sum())

# Check 4: Weird Math?
print("\n[4] Statistics (Check Min 'quantity'):")
print(df.describe())