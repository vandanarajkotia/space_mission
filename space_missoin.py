# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (make sure file is in same folder)
df = pd.read_csv("mission_launches.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month

# -------------------------------
# 1. Launches per Year
# -------------------------------
launches_per_year = df.groupby("Year").size()

plt.figure()
launches_per_year.plot()
plt.title("Launches per Year")
plt.xlabel("Year")
plt.ylabel("Number of Launches")
plt.show()

# -------------------------------
# 2. Success vs Failure
# -------------------------------
plt.figure()
df["Mission_Status"].value_counts().plot(kind="pie", autopct='%1.1f%%')
plt.title("Mission Success vs Failure")
plt.ylabel("")
plt.show()

# -------------------------------
# 3. Top Companies
# -------------------------------
plt.figure()
df["Company Name"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Companies by Launch Count")
plt.xlabel("Company")
plt.ylabel("Number of Launches")
plt.xticks(rotation=45)
plt.show()

# -------------------------------
# 4. Launches by Month
# -------------------------------
plt.figure()
df["Month"].value_counts().sort_index().plot()
plt.title("Launches by Month")
plt.xlabel("Month")
plt.ylabel("Number of Launches")
plt.show()

# -------------------------------
# 5. Cost Trend (if available)
# -------------------------------
if "Price" in df.columns:
    df["Price"] = pd.to_numeric(df["Price"], errors='coerce')
    cost_trend = df.groupby("Year")["Price"].mean()

    plt.figure()
    cost_trend.plot()
    plt.title("Average Mission Cost Over Time")
    plt.xlabel("Year")
    plt.ylabel("Cost")
    plt.show()

# -------------------------------
# PRINT SOME INSIGHTS
# -------------------------------
print("\n--- Key Insights ---")

print("Total Missions:", len(df))

print("Most Active Company:")
print(df["Company Name"].value_counts().idxmax())

print("Success Rate:")
print(df["Mission_Status"].value_counts(normalize=True) * 100)