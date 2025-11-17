import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --------------------------------------------------------------
# 1. LOAD THE DATA 
# --------------------------------------------------------------
csv_path = 'Superstore.csv'         
try:
    df = pd.read_csv(csv_path, encoding='cp1252')  
except FileNotFoundError:
    print(f"File not found: {csv_path}")
    print("   • Download the CSV from Kaggle and place it in the same folder as this script.")
    raise
except Exception as e:
    print(f"Unexpected error: {e}")
    raise

print(f"Dataset loaded – {df.shape[0]:,} rows, {df.shape[1]} columns\n")
print(df.head(), "\n")

# --------------------------------------------------------------
# 2. CLEAN & FEATURE ENGINEERING
# --------------------------------------------------------------
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date']  = pd.to_datetime(df['Ship Date'],  errors='coerce')

# Drop duplicates
df = df.drop_duplicates()

# Standardise text columns
df['Category'] = df['Category'].str.strip().str.title()
df['Region']   = df['Region'].str.strip().str.title()

# New columns
df['Year']    = df['Order Date'].dt.year
df['Month']   = df['Order Date'].dt.month_name()
df['Quarter'] = df['Order Date'].dt.quarter
df['Profit Margin %'] = (df['Profit'] / df['Sales']) * 100

print("Cleaning complete – no missing key columns.\n")

# --------------------------------------------------------------
# 3. BASIC STATISTICS
# --------------------------------------------------------------
total_sales  = df['Sales'].sum()
total_profit = df['Profit'].sum()
avg_margin   = df['Profit Margin %'].mean()

print(f"Overall Stats")
print(f"   Total Sales : ${total_sales:,.2f}")
print(f"   Total Profit: ${total_profit:,.2f}")
print(f"   Avg Margin  : {avg_margin:.2f}%\n")

# --------------------------------------------------------------
# 4. CATEGORY PERFORMANCE
# --------------------------------------------------------------
cat_perf = df.groupby('Category').agg(
    Sales=('Sales', 'sum'),
    Profit=('Profit', 'sum'),
    Quantity=('Quantity', 'sum'),
    Margin=('Profit Margin %', 'mean')
).round(2)

print("Sales & Profit by Category")
print(cat_perf, "\n")

# --------------------------------------------------------------
# 5. REGIONAL PERFORMANCE
# --------------------------------------------------------------
region_perf = df.groupby('Region').agg(
    Sales=('Sales', 'sum'),
    Profit=('Profit', 'sum'),
    Quantity=('Quantity', 'sum'),
    Margin=('Profit Margin %', 'mean')
).round(2)

print("Performance by Region")
print(region_perf, "\n")

# --------------------------------------------------------------
# 6. SEASONAL TRENDS
# --------------------------------------------------------------
month_order = ['January','February','March','April','May','June',
               'July','August','September','October','November','December']

monthly_sales = df.groupby('Month')['Sales'].sum().reindex(month_order)

print("Monthly Sales")
print(monthly_sales.apply(lambda x: f"${x:,.0f}"), "\n")

# --------------------------------------------------------------
# 7. PLOTS – FULLY VISIBLE VERSION
# --------------------------------------------------------------
plt.style.use('seaborn-v0_8')
plt.rcParams['figure.figsize'] = (16, 12)      # <-- BIGGER CANVAS
plt.rcParams['figure.autolayout'] = True       # <-- AUTO SPACING

fig, axs = plt.subplots(2, 2, figsize=(16, 12))

# 7.1 Sales by Category
cat_perf['Sales'].plot(kind='bar', ax=axs[0,0],
                       color=['#4e79a7','#f28e2b','#e15759'])
axs[0,0].set_title('Total Sales by Category', fontsize=14, pad=15)
axs[0,0].set_ylabel('Sales ($)', fontsize=12)
axs[0,0].tick_params(axis='x', rotation=0)

# 7.2 Profit by Region
region_perf['Profit'].plot(kind='bar', ax=axs[0,1],
                           color=sns.color_palette('viridis',4))
axs[0,1].set_title('Total Profit by Region', fontsize=14, pad=15)
axs[0,1].set_ylabel('Profit ($)', fontsize=12)
axs[0,1].tick_params(axis='x', rotation=0)

# 7.3 Monthly Sales Trend 
monthly_sales.plot(kind='line', marker='o', ax=axs[1,0], color='green', linewidth=2)
axs[1,0].set_title('Monthly Sales Trend', fontsize=14, pad=15)
axs[1,0].set_ylabel('Sales ($)', fontsize=12)
axs[1,0].set_xlabel('Month', fontsize=12)

# Use only existing months
existing_months = monthly_sales.index.tolist()
axs[1,0].set_xticks(range(len(existing_months)))
axs[1,0].set_xticklabels(existing_months, rotation=45, ha='right', fontsize=10)

# 7.4 Quarterly Sales
quarterly_sales = df.groupby('Quarter')['Sales'].sum()
quarterly_sales.plot(kind='bar', ax=axs[1,1], color='orange')
axs[1,1].set_title('Sales by Quarter', fontsize=14, pad=15)
axs[1,1].set_xlabel('Quarter', fontsize=12)
axs[1,1].set_ylabel('Sales ($)', fontsize=12)
axs[1,1].set_xticks(range(len(quarterly_sales.index)))
axs[1,1].set_xticklabels([f'Q{q}' for q in quarterly_sales.index])

# FINAL TOUCH: Tight layout with extra padding
plt.tight_layout(pad=3.0)
plt.subplots_adjust(top=0.93, bottom=0.12, left=0.08, right=0.95, hspace=0.4, wspace=0.3)
plt.show()

# Save high-res image for your report
fig.savefig('superstore_analysis_full.png', dpi=300, bbox_inches='tight')
print("Graph saved as: superstore_analysis_full.png")

# --------------------------------------------------------------
# 8. CORRELATION & TOP PRODUCTS TO PROMOTE
# --------------------------------------------------------------
corr = df['Sales'].corr(df['Profit'])
print(f"Correlation Sales ↔ Profit: {corr:.3f}")

top5_profit = df.groupby('Product Name').agg(
    Sales=('Sales','sum'),
    Profit=('Profit','sum')
).nlargest(5, 'Profit')
print("\nTop 5 Products to Promote (by Profit)")
print(top5_profit.round(2))