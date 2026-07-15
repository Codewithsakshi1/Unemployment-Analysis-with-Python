# Unemployment Data Analysis Using Python
# Author: Sakshi Sharma

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")

# Display first 5 rows
print("========== First 5 Rows ==========")
print(data.head())

# Display dataset information
print("\n========== Dataset Information ==========")
data.info()

# Check missing values
print("\n========== Missing Values ==========")
print(data.isnull().sum())

# Display statistical summary
print("\n========== Statistical Summary ==========")
print(data.describe())

# Display column names
print("\n========== Column Names ==========")
print(data.columns)

# Convert Date column into datetime format
data[" Date"] = pd.to_datetime(data[" Date"], dayfirst=True)

# -------------------------------
# Graph 1: Unemployment Rate Over Time
# -------------------------------
plt.figure(figsize=(10,5))
plt.plot(data[" Date"], data[" Estimated Unemployment Rate (%)"])
plt.title("Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# -------------------------------
# Graph 2: Top 10 States by Average Unemployment Rate
# -------------------------------
average = data.groupby("Region")[" Estimated Unemployment Rate (%)"].mean()

average = average.sort_values(ascending=False)

plt.figure(figsize=(10,5))
average.head(10).plot(kind="bar")
plt.title("Top 10 States by Average Unemployment Rate")
plt.xlabel("State")
plt.ylabel("Average Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -------------------------------
# Highest Unemployment State
# -------------------------------
highest = average.idxmax()
rate = average.max()

print("\nState with Highest Average Unemployment Rate:")
print(highest)
print("Rate:", round(rate,2), "%")