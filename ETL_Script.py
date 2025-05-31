import pandas as pd
from sqlalchemy import create_engine
import numpy as np

# Step 1: Read the CSV file
df = pd.read_csv('sales_data.csv')
print("Original Data:\n", df)

# Step 2: Clean data (remove nulls, fix types if needed)
df = df.dropna()  # remove missing rows

# Step 3: Add 'Total' column
df['Total'] = df['Quantity'] * df['Price']

# Step 4: Show the transformed data
print("\nTransformed Data:\n", df)

# 3. Database connection details
username = "postgres"  # Change if your username is different
password = "elephant"  # 🔑 Replace with your actual password
host = "localhost"
port = "5432"
database = "salesdb"

# 4. Create SQLAlchemy engine
conn_str = f"postgresql://{username}:{password}@{host}:{port}/{database}"
engine = create_engine(conn_str)

# 5. Load data into PostgreSQL table named 'sales_table'
df.to_sql("sales_table", engine, if_exists="replace", index=False)

print("✅ Sales data loaded successfully into PostgreSQL!")