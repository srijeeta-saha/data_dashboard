# test_charts.py
from utils.analysis import load_data, sales_by_category, sales_by_region
from utils.analysis import monthly_sales_trend, top_cities, profit_by_category
from charts import *

# Load data
df = load_data()

# Test each chart
print("Testing charts...")

fig1 = bar_chart_category(sales_by_category(df))
fig1.show()   # opens in browser!

print("Chart 1 - Sales by Category ✅")