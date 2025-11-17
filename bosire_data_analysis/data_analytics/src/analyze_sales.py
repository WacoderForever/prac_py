import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os

# Step 1: Load the dataset
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "../data/sales_data.csv")
df = pd.read_csv(file_path)

# Step 2: Quick look at the data
print("First 5 rows:")
print(df.head())

# Step 3: Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Step 4: Total sales per branch
sales_per_branch = df.groupby("Branch")["Total"].sum()
print("\nTotal sales per branch:")
print(sales_per_branch)

# Step 5: Most sold products
top_products = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
print("\nTop selling products:")
print(top_products)

# Step 6: Visualize
plt.figure(figsize=(8,5))
sns.barplot(x=sales_per_branch.index, y=sales_per_branch.values)
plt.title("Total Sales per Branch")
plt.xlabel("Branch")
plt.ylabel("Total Sales (KES)")
plt.show()
