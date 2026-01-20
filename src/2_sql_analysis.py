import pandas as pd
import sqlite3
from sqlalchemy import create_engine
import os

print("🔍 Loading CSV...")

df = pd.read_csv('data/sales_data.csv')

# Recreate database
db_path = 'data/sales_database.db'
if os.path.exists(db_path):
    os.remove(db_path)

engine = create_engine(f'sqlite:///{db_path}')
df.to_sql('sales', engine, index=False, if_exists='replace')

print("✅ SQLite database created")

# Test query
conn = sqlite3.connect(db_path)
test = pd.read_sql("""
SELECT Region, COUNT(*) AS Orders, SUM(Revenue) AS Revenue
FROM sales
GROUP BY Region
""", conn)

print("\n🧪 Test Query Output:")
print(test)

conn.close()
