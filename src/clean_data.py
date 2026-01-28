import pandas as pd

def clean_data():
    print("🧹 Starting Data Cleaning Pipeline...")
    
    # 1. Load Raw Data
    df = pd.read_csv('data/raw_sales.csv')
    
    # --- FIX 1: Remove Duplicates ---
    initial_rows = len(df)
    df = df.drop_duplicates()
    print(f"   - Removed {initial_rows - len(df)} duplicate rows.")
    
    # --- FIX 2: Handle Missing Data ---
    # Rule: If there is no Customer ID, we can't bill them. Drop the row.
    df = df.dropna(subset=['customer_id'])
    # Rule: If product is missing, label it 'Unknown'
    df['product'] = df['product'].fillna('Unknown')
    print(f"   - Dropped rows with missing Customer IDs. Rows left: {len(df)}")
    
    # --- FIX 3: Fix Data Types (The '$' problem) ---
    # This regex removes anything that isn't a digit or a dot
    df['price'] = df['price'].astype(str).str.replace(r'[^\d.]', '', regex=True)
    df['price'] = pd.to_numeric(df['price'])
    print("   - Converted 'price' column to numbers.")
    
    # --- FIX 4: Fix Logic Errors (Negative Quantities) ---
    df = df[df['quantity'] > 0]
    print(f"   - Removed negative quantities. Final Count: {len(df)}")
    
    # --- TRANSFORMATION: Add Value ---
    # Create a new column for Total Sales Amount
    df['total_amount'] = df['price'] * df['quantity']
    
    # 7. Save the Clean Data
    df.to_csv('data/clean_sales.csv', index=False)
    print("✅ Success! Clean data saved to 'data/clean_sales.csv'")

if __name__ == "__main__":
    clean_data()