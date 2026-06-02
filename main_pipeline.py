import logging
import os
import sys

# Ensure src can be imported
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from src.generate_messy_data import generate_data
from src.clean_data import clean_data
from src.load_to_db import load_to_db

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

logger = logging.getLogger(__name__)

def run_pipeline():
    logger.info("🚀 Starting Retail ETL Pipeline...")
    
    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)
    
    # Step 1: Extract/Generate Data
    raw_path = generate_data(num_rows=10000, output_path='data/raw_sales.csv')
    
    # Step 2: Transform/Clean Data
    clean_path = clean_data(input_path=raw_path, output_path='data/clean_sales.csv')
    
    # Step 3: Load Data to Database
    db_path = load_to_db(input_path=clean_path, db_path='data/sales.db')
    
    logger.info(f"🎉 Pipeline Completed Successfully! Database ready at {db_path}")

if __name__ == "__main__":
    run_pipeline()
