import pandas as pd
import numpy as np
import random
import logging

logger = logging.getLogger(__name__)

def generate_data(num_rows=5000, output_path='data/raw_sales.csv'):
    logger.info(f"Generating {num_rows} rows of messy retail data...")
    
    ids = list(range(1000, 1000 + num_rows))
    products = ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Webcam', None]
    prices = {'Laptop': 1200, 'Mouse': 25, 'Monitor': 300, 'Keyboard': 50, 'Webcam': 80, None: 0}
    dates = pd.date_range(start='2024-01-01', periods=180).strftime('%Y-%m-%d').tolist()
    
    data = []
    for _ in range(num_rows):
        prod = random.choice(products)
        
        # 10% chance of a "Dirty" price
        if random.random() < 0.1:
            price = f"${prices[prod]}" if prod else "$0"
        else:
            price = prices[prod] if prod else 0
            
        # 5% chance of negative quantity
        qty = random.randint(-2, 5) 
        
        # 5% chance of missing Customer ID
        cust_id = random.choice([random.randint(1, 500), np.nan])
        
        row = {
            'order_id': random.choice(ids),
            'product': prod,
            'price': price,
            'quantity': qty,
            'order_date': random.choice(dates),
            'customer_id': cust_id
        }
        data.append(row)

    df = pd.DataFrame(data)
    
    # Add exact duplicates (Simulating system glitch)
    duplicate_rows = int(num_rows * 0.1)
    df = pd.concat([df, df.sample(duplicate_rows)])
    
    df.to_csv(output_path, index=False)
    logger.info(f"Created '{output_path}' with {len(df)} rows (includes {duplicate_rows} duplicates).")
    return output_path

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    generate_data()