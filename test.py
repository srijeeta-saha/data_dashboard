from utils.analysis import *

df = load_data()
print('Data loaded:', df.shape)
print()

kpis = get_kpis(df)
for k, v in kpis.items():
    print(f'{k}: {v}')
print()

print('Sales by Category:')
print(sales_by_category(df))
print()

print('Sales by Region:')
print(sales_by_region(df))