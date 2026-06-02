import pandas as pd
import logging

logger = logging.getLogger(__name__)

def clean_data(input_path='data/raw_sales.csv', output_path='data/clean_sales.csv'):
    logger.info("🧹 Starting Data Cleaning Pipeline...")
    
    df = pd.read_csv(input_path)
    initial_rows = len(df)
    
    # 1. Remove Duplicates
    df = df.drop_duplicates()
    logger.info(f"Removed {initial_rows - len(df)} duplicate rows.")
    
    # 2. Handle Missing Data
    df = df.dropna(subset=['customer_id'])
    df['product'] = df['product'].fillna('Unknown')
    logger.info(f"Dropped rows with missing Customer IDs. Rows left: {len(df)}")
    
    # 3. Fix Data Types
    df['price'] = df['price'].astype(str).str.replace(r'[^\d.]', '', regex=True)
    df['price'] = pd.to_numeric(df['price'])
    
    # 4. Fix Logic Errors
    df = df[df['quantity'] > 0]
    logger.info(f"Removed negative/zero quantities. Final Count: {len(df)}")
    
    # 5. Add Value
    df['total_amount'] = df['price'] * df['quantity']
    
    # 6. Save
    df.to_csv(output_path, index=False)
    logger.info(f"✅ Success! Clean data saved to '{output_path}'")
    return output_path

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    clean_data()