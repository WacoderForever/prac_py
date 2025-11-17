import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Step 1: Load the dataset
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "../data/maize_production.csv")
df = pd.read_csv(file_path)

print("Preview of Maize Data:")
print(df.head(), "\n")

# Step 2: Check for missing values
print("Missing Values:")
print(df.isnull().sum(), "\n")

# Step 3: Summary by county
county_summary = df.groupby("County")["Production_Tons"].mean().sort_values(ascending=False)
print("Average Production per County (tons):")
print(county_summary, "\n")

# Step 4: Summary by year
year_summary = df.groupby("Year")["Production_Tons"].sum()
print("Total National Production per Year:")
print(year_summary, "\n")

# Step 5: Visualize county production
plt.figure(figsize=(8,5))
sns.barplot(x=county_summary.index, y=county_summary.values)
plt.title("Average Maize Production by County (tons)")
plt.xlabel("County")
plt.ylabel("Average Production (tons)")
plt.xticks(rotation=25)
plt.show()

# Step 6: Visualize trend over years
plt.figure(figsize=(8,5))
sns.lineplot(x=year_summary.index, y=year_summary.values, marker="o")
plt.title("Total National Maize Production Over Time")
plt.xlabel("Year")
plt.ylabel("Total Production (tons)")
plt.show()

# Step 7: Export summarized data
county_summary.to_csv("county_maize_summary.csv")
print("Summary exported successfully ")
