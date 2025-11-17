import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Step 1: Load the dataset
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "../data/matatu_fares.csv")
df = pd.read_csv(file_path)


# Step 2: Convert to datetime
df["DateTime"] = pd.to_datetime(df["Date"] + " " + df["Time"])

print("Preview:")
print(df.head(), "\n")

# Step 3: Basic stats
print("Average Fare:", df["Fare_KES"].mean())
print("Average Travel Time:", df["Avg_Travel_Time_Min"].mean(), "\n")

# Step 4: Trend over time
plt.figure(figsize=(8,5))
sns.lineplot(x="DateTime", y="Fare_KES", data=df, marker="o")
plt.title("Matatu Fare Changes Over Time (CBD–Rongai)")
plt.xlabel("Time")
plt.ylabel("Fare (KES)")
plt.xticks(rotation=30)
plt.show()

# Step 5: Compare Fare vs Travel Time
plt.figure(figsize=(8,5))
sns.scatterplot(x="Fare_KES", y="Avg_Travel_Time_Min", data=df)
plt.title("Fare vs Traffic Time")
plt.xlabel("Fare (KES)")
plt.ylabel("Average Travel Time (min)")
plt.show()

# Step 6: Correlation check
correlation = df["Fare_KES"].corr(df["Avg_Travel_Time_Min"])
print(f"Correlation between fare and traffic: {correlation:.2f}")
if correlation > 0.7:
    print("Strong positive correlation — fares rise with traffic delays.")
elif correlation > 0.4:
    print("Moderate correlation — possible influence of traffic on fares.")
else:
    print("Weak correlation — other factors may affect pricing.")
