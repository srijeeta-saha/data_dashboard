import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)
random.seed(42)

NUM_ROWS = 1000

regions    = ['East', 'West', 'North', 'South']
categories = ['Furniture', 'Technology', 'Office Supplies']
sub_cats   = {
    'Furniture'       : ['Chairs', 'Tables', 'Bookcases', 'Furnishings'],
    'Technology'      : ['Phones', 'Computers', 'Accessories', 'Copiers'],
    'Office Supplies' : ['Paper', 'Binders', 'Storage', 'Envelopes']
}
ship_modes = ['Standard Class', 'Second Class', 'First Class', 'Same Day']
segments   = ['Consumer', 'Corporate', 'Home Office']
cities     = {
    'East'  : ['New York', 'Boston', 'Philadelphia', 'Newark'],
    'West'  : ['Los Angeles', 'San Francisco', 'Seattle', 'Denver'],
    'North' : ['Chicago', 'Detroit', 'Minneapolis', 'Milwaukee'],
    'South' : ['Houston', 'Dallas', 'Miami', 'Atlanta']
}

rows = []
start_date = datetime(2021, 1, 1)

for i in range(NUM_ROWS):
    region   = random.choice(regions)
    category = random.choice(categories)
    sub_cat  = random.choice(sub_cats[category])
    city     = random.choice(cities[region])

    order_date = start_date + timedelta(days=random.randint(0, 1094))
    ship_date  = order_date + timedelta(days=random.randint(1, 7))

    sales    = round(random.uniform(20, 5000), 2)
    discount = round(random.choice([0, 0.1, 0.2, 0.3, 0.4]), 2)
    profit   = round(sales * random.uniform(0.05, 0.35) - (sales * discount), 2)
    quantity = random.randint(1, 10)

    rows.append({
        'Order ID'     : f'ORD-{1000 + i}',
        'Order Date'   : order_date.strftime('%Y-%m-%d'),
        'Ship Date'    : ship_date.strftime('%Y-%m-%d'),
        'Ship Mode'    : random.choice(ship_modes),
        'Segment'      : random.choice(segments),
        'City'         : city,
        'Region'       : region,
        'Category'     : category,
        'Sub-Category' : sub_cat,
        'Sales'        : sales,
        'Quantity'     : quantity,
        'Discount'     : discount,
        'Profit'       : profit,
    })

df = pd.DataFrame(rows)
df.to_csv('data/superstore.csv', index=False)

print(f"✅ Dataset created successfully!")
print(f"   Rows      : {df.shape[0]}")
print(f"   Columns   : {df.shape[1]}")
print(f"   Saved to  : data/superstore.csv")
print()
print(df.head())