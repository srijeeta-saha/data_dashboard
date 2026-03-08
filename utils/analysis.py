# utils/analysis.py
# This file loads, cleans and analyses the superstore data

import pandas as pd
import numpy as np

# ══════════════════════════════════════════
# FUNCTION 1 — Load & Clean Data
# ══════════════════════════════════════════
def load_data():
    # Read the CSV file
    df = pd.read_csv('data/superstore.csv')

    # Convert date columns from text to real dates
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date']  = pd.to_datetime(df['Ship Date'])

    # Extract useful time columns
    df['Year']  = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.month
    df['Month Name'] = df['Order Date'].dt.strftime('%b')  # Jan, Feb...

    # Remove any rows where Sales is missing or zero
    df = df[df['Sales'] > 0]

    # Reset index after cleaning
    df = df.reset_index(drop=True)

    return df


# ══════════════════════════════════════════
# FUNCTION 2 — Calculate KPI Cards
# ══════════════════════════════════════════
def get_kpis(df):
    kpis = {
        'Total Sales'   : round(df['Sales'].sum(), 2),
        'Total Profit'  : round(df['Profit'].sum(), 2),
        'Total Orders'  : int(df['Order ID'].nunique()),
        'Total Quantity': int(df['Quantity'].sum()),
        'Avg Order Value': round(df['Sales'].mean(), 2),
        'Profit Margin' : round((df['Profit'].sum() / df['Sales'].sum()) * 100, 2)
    }
    return kpis


# ══════════════════════════════════════════
# FUNCTION 3 — Sales by Category
# ══════════════════════════════════════════
def sales_by_category(df):
    result = df.groupby('Category')['Sales'].sum().reset_index()
    result.columns = ['Category', 'Total Sales']
    result = result.sort_values('Total Sales', ascending=False)
    result['Total Sales'] = result['Total Sales'].round(2)
    return result


# ══════════════════════════════════════════
# FUNCTION 4 — Sales by Region
# ══════════════════════════════════════════
def sales_by_region(df):
    result = df.groupby('Region')['Sales'].sum().reset_index()
    result.columns = ['Region', 'Total Sales']
    result = result.sort_values('Total Sales', ascending=False)
    result['Total Sales'] = result['Total Sales'].round(2)
    return result


# ══════════════════════════════════════════
# FUNCTION 5 — Monthly Sales Trend
# ══════════════════════════════════════════
def monthly_sales_trend(df):
    result = df.groupby(['Year', 'Month', 'Month Name'])['Sales'].sum().reset_index()
    result.columns = ['Year', 'Month', 'Month Name', 'Total Sales']
    result = result.sort_values(['Year', 'Month'])
    result['Total Sales'] = result['Total Sales'].round(2)

    # Create a label like "Jan 2021" for x-axis
    result['Period'] = result['Month Name'] + ' ' + result['Year'].astype(str)
    return result


# ══════════════════════════════════════════
# FUNCTION 6 — Top 5 Cities by Sales
# ══════════════════════════════════════════
def top_cities(df):
    result = df.groupby('City')['Sales'].sum().reset_index()
    result.columns = ['City', 'Total Sales']
    result = result.sort_values('Total Sales', ascending=False).head(5)
    result['Total Sales'] = result['Total Sales'].round(2)
    return result


# ══════════════════════════════════════════
# FUNCTION 7 — Profit by Category
# ══════════════════════════════════════════
def profit_by_category(df):
    result = df.groupby('Category')['Profit'].sum().reset_index()
    result.columns = ['Category', 'Total Profit']
    result = result.sort_values('Total Profit', ascending=False)
    result['Total Profit'] = result['Total Profit'].round(2)
    return result


# ══════════════════════════════════════════
# FUNCTION 8 — Filter Data (for dashboard)
# ══════════════════════════════════════════
def filter_data(df, regions=None, categories=None, years=None):
    filtered = df.copy()

    if regions and len(regions) > 0:
        filtered = filtered[filtered['Region'].isin(regions)]

    if categories and len(categories) > 0:
        filtered = filtered[filtered['Category'].isin(categories)]

    if years and len(years) > 0:
        filtered = filtered[filtered['Year'].isin(years)]

    return filtered