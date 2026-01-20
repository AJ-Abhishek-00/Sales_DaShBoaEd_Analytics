import pandas as pd
import numpy as np
import os

print("🔄 Preparing sales dataset from raw CSV...")

csv_path = "data/sales_data.csv"
if not os.path.exists(csv_path):
    print("❌ CSV not found")
    exit(1)

# Load raw data
df = pd.read_csv(csv_path)

# -----------------------------
# Standardize column names
# -----------------------------
df.rename(columns={
    'Order ID': 'Order_ID',
    'Order Date': 'Order_Date',
    'CustomerName': 'Customer_Name',
    'State': 'State',
    'City': 'City'
}, inplace=True)

# -----------------------------
# Date handling
# -----------------------------
df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')
df = df.dropna(subset=['Order_Date'])

df['Year'] = df['Order_Date'].dt.year
df['Quarter'] = 'Q' + df['Order_Date'].dt.quarter.astype(str)

# -----------------------------
# Region from State (India)
# -----------------------------
north = ['Delhi', 'Haryana', 'Punjab', 'Uttar Pradesh', 'Rajasthan']
south = ['Telangana', 'Karnataka', 'Tamil Nadu', 'Kerala', 'Andhra Pradesh']
west  = ['Maharashtra', 'Gujarat']
east  = ['West Bengal', 'Odisha', 'Bihar']

def map_region(state):
    if state in north: return 'North'
    if state in south: return 'South'
    if state in west:  return 'West'
    if state in east:  return 'East'
    return 'Other'

df['Region'] = df['State'].apply(map_region)

# -----------------------------
# Generate Business Fields
# -----------------------------
np.random.seed(42)

df['Category'] = np.random.choice(
    ['Electronics', 'Furniture', 'Office Supplies'], len(df)
)

df['Product'] = df['Category'] + ' Item ' + (df.index % 10 + 1).astype(str)

df['Quantity'] = np.random.randint(1, 6, len(df))

df['Revenue'] = np.random.randint(500, 5000, len(df)) * df['Quantity']

df['Profit'] = (df['Revenue'] * np.random.uniform(0.05, 0.30, len(df))).round(0)

df['Profit_Margin'] = (df['Profit'] / df['Revenue']).round(2)

df['Discount'] = np.random.choice([0.05, 0.1, 0.15, 0.25], len(df))

df['Sales_Rep'] = 'Rep-' + (df.index % 5 + 1).astype(str)

df['Customer_Segment'] = np.random.choice(
    ['Consumer', 'Corporate', 'Home Office'], len(df)
)

# -----------------------------
# Save cleaned dataset
# -----------------------------
df.to_csv(csv_path, index=False)

print("✅ Dataset is now analytics-ready")
print("📊 Final columns:")
print(df.columns.tolist())
