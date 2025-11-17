import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Step 1: Load the dataset
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "../data/student_scores.csv")
df = pd.read_csv(file_path)

# Step 2: Preview
print("Preview of Student Data:")
print(df.head(), "\n")

# Step 3: Create total score column
df["Total"] = df["CAT1"] + df["CAT2"] + df["Exam"]

# Step 4: Basic statistics
print("Descriptive Statistics:")
print(df[["CAT1", "CAT2", "Exam", "Total"]].describe(), "\n")

# Step 5: Average performance by gender
gender_avg = df.groupby("Gender")["Total"].mean()
print("Average Total by Gender:")
print(gender_avg, "\n")

# Step 6: Visualize grade distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Total"], bins=8, kde=True)
plt.title("Distribution of Total Scores")
plt.xlabel("Total Marks")
plt.ylabel("Number of Students")
plt.show()

# Step 7: Visualize gender comparison
plt.figure(figsize=(6,5))
sns.boxplot(x="Gender", y="Total", data=df)
plt.title("Gender vs Total Score")
plt.show()

# Step 8: Identify top and struggling students
top_students = df.nlargest(3, "Total")
low_students = df.nsmallest(3, "Total")

print("Top 3 Performers:")
print(top_students[["Name", "Total"]], "\n")

print("Bottom 3 Students:")
print(low_students[["Name", "Total"]], "\n")

# Step 9: Export insights
summary = df.groupby("Department")["Total"].agg(["mean", "max", "min"])
summary.to_csv("performance_summary.csv")
print("Performance summary exported successfully ")
