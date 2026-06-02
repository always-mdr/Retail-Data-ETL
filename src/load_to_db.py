import pandas as pd
import sqlite3
import logging

logger = logging.getLogger(__name__)

def load_to_db(input_path='data/clean_sales.csv', db_path='data/sales.db'):
    logger.info("🚚 Loading data into SQL Database...")
    
    df = pd.read_csv(input_path)
    conn = sqlite3.connect(db_path)
    
    # Create table with a strict schema instead of relying purely on pandas
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER,
        product TEXT,
        price REAL,
        quantity INTEGER,
        order_date TEXT,
        customer_id INTEGER,
        total_amount REAL
    );
    """
    
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS orders;")
    cursor.execute(create_table_sql)
    conn.commit()
    
    df.to_sql('orders', conn, if_exists='append', index=False)
    
    conn.close()
    logger.info(f"✅ Data successfully loaded into '{db_path}'!")
    return db_path

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    load_to_db()