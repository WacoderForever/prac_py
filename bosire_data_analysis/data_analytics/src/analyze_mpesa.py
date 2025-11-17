import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Step 1: Load the dataset
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "../data/mpesa_transactions.csv")
df = pd.read_csv(file_path)

# Step 2: Quick preview
print("Preview of data:")
print(df.head(), "\n")

# Step 3: Check data types and missing values
print("Info:")
print(df.info(), "\n")
print("Missing values per column:")
print(df.isnull().sum(), "\n")

# Step 4: Clean data
# Fill missing amounts with 0 (if any)
df["Amount"].fillna(0, inplace=True)

# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Step 5: Basic insights
total_amount = df["Amount"].sum()
avg_amount = df["Amount"].mean()
successful = len(df[df["Status"] == "Success"])
failed = len(df[df["Status"] == "Failed"])

print(f"Total Transaction Volume: KES {total_amount}")
print(f"Average Transaction Amount: KES {avg_amount:.2f}")
print(f"Successful Transactions: {successful}")
print(f"Failed Transactions: {failed}\n")

# Step 6: Group by transaction type
type_summary = df.groupby("Transaction_Type")["Amount"].sum().sort_values(ascending=False)
print("Total Amount by Transaction Type:")
print(type_summary, "\n")

# Step 7: Visualize
plt.figure(figsize=(8, 5))
sns.barplot(x=type_summary.index, y=type_summary.values)
plt.title("M-Pesa Transaction Totals by Type")
plt.xlabel("Transaction Type")
plt.ylabel("Total Amount (KES)")
plt.xticks(rotation=30)
plt.show()

# Step 8: Trend over time
daily_trend = df.groupby("Date")["Amount"].sum()
plt.figure(figsize=(8, 5))
sns.lineplot(x=daily_trend.index, y=daily_trend.values, marker="o")
plt.title("Daily M-Pesa Transaction Trends")
plt.xlabel("Date")
plt.ylabel("Total Amount (KES)")
plt.show()
