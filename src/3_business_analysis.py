import pandas as pd

df = pd.read_csv('data/sales_data.csv')
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

print("="*60)
print("📊 BUSINESS ANALYSIS")
print("="*60)

# KPIs
total_revenue = df['Revenue'].sum()
total_profit = df['Profit'].sum()
orders = len(df)
margin = (total_profit / total_revenue) * 100

print(f"Total Revenue: ₹{total_revenue:,.0f}")
print(f"Total Profit:  ₹{total_profit:,.0f}")
print(f"Orders:        {orders:,}")
print(f"Margin:        {margin:.2f}%")

# Region analysis
print("\n📍 Region Performance")
region = df.groupby('Region')[['Revenue','Profit']].sum()
print(region.sort_values('Profit', ascending=False))

# Category analysis
print("\n📦 Category Performance")
category = df.groupby('Category')[['Revenue','Profit']].sum()
print(category.sort_values('Profit', ascending=False))

# Loss-making products
loss = df.groupby('Product')['Profit'].sum()
loss = loss[loss < 0]

if not loss.empty:
    print("\n⚠️ Loss Making Products:")
    print(loss.sort_values())
else:
    print("\n✅ No loss-making products")

print("\n✅ Business analysis complete")
