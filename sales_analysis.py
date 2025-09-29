import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("sales_data.csv")


print("Dataset Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())


# Total sales per product
product_sales = df.groupby("Product")["Sales"].sum()

# Sales per region
region_sales = df.groupby("Region")["Sales"].sum()

# Monthly trend
monthly_sales = df.groupby("Month")["Sales"].sum()


plt.figure(figsize=(8, 5))
product_sales.plot(kind="bar", color="skyblue", title="Sales by Product")
plt.ylabel("Total Sales")
plt.show()

plt.figure(figsize=(6, 6))
region_sales.plot(kind="pie", autopct="%1.1f%%",
                  startangle=90, title="Sales by Region")
plt.ylabel("")
plt.show()

plt.figure(figsize=(8, 5))
monthly_sales.plot(kind="line", marker="o", color="green",
                   title="Monthly Sales Trend")
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()


print("\nBest-Selling Product(s):")
print(product_sales.sort_values(ascending=False).head(1))

print("\nTop-Performing Region(s):")
print(region_sales.sort_values(ascending=False).head(1))

print("\nMonthly Sales Trend:")
print(monthly_sales)
