import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/sales.csv")

# Basic analysis
total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()
best_month = df.loc[df["Sales"].idxmax()]
worst_month = df.loc[df["Sales"].idxmin()]

print("Total Sales:", total_sales)
print("Average Monthly Sales:", round(average_sales, 2))
print("Best Month:", best_month["Month"], "-", best_month["Sales"])
print("Worst Month:", worst_month["Month"], "-", worst_month["Sales"])

# Plot
plt.figure()
plt.plot(df["Month"], df["Sales"])
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_trend.png")
plt.show()
