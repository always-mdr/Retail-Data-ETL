import pandas as pd
import numpy as np
import random

# Settings
NUM_ROWS = 500

# 1. Generate Fake Data
ids = list(range(1000, 1000 + NUM_ROWS))
products = ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Webcam', None] # Oops, missing products
prices = {'Laptop': 1200, 'Mouse': 25, 'Monitor': 300, 'Keyboard': 50, 'Webcam': 80, None: 0}
dates = pd.date_range(start='2024-01-01', periods=60).strftime('%Y-%m-%d').tolist()

data = []

for _ in range(NUM_ROWS):
    prod = random.choice(products)
    # 10% chance of a "Dirty" price (string with $)
    if random.random() < 0.1:
        price = f"${prices[prod]}"
    else:
        price = prices[prod]
        
    # 5% chance of negative quantity (data error)
    qty = random.randint(-2, 5) 
    
    # 5% chance of missing Customer ID
    cust_id = random.choice([random.randint(1, 50), np.nan])
    
    row = {
        'order_id': random.choice(ids), # Will create duplicates later
        'product': prod,
        'price': price,
        'quantity': qty,
        'order_date': random.choice(dates),
        'customer_id': cust_id
    }
    data.append(row)

# 2. Convert to DataFrame
df = pd.DataFrame(data)

# 3. Add exact duplicates (Simulating system glitch)
df = pd.concat([df, df.sample(50)])

# 4. Save to CSV
df.to_csv('data/raw_sales.csv', index=False)

print(f"✅ Created 'data/raw_sales.csv' with {len(df)} rows.")
print("⚠️  Warning: This data is messy! (Duplicates, Nulls, Bad Types)")