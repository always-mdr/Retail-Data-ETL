import pandas as pd
import sqlite3

def load_to_db():
    print("🚚 Loading data into SQL Database...")
    
    # 1. Read the Clean Data
    df = pd.read_csv('data/clean_sales.csv')
    
    # 2. Connect to Database (Creates 'sales.db' if it doesn't exist)
    conn = sqlite3.connect('data/sales.db')
    
    # 3. Write Data to Table 'orders'
    # if_exists='replace' -> Overwrite the table if we run this again
    df.to_sql('orders', conn, if_exists='replace', index=False)
    
    conn.close()
    print("✅ Data successfully loaded into 'sales.db'!")

if __name__ == "__main__":
    load_to_db()