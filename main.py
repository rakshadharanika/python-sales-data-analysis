import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# ==================================
# 1. READ THE CSV FILE
# ==================================

data = pd.read_csv("dataset/sales.csv")

print("========== SALES DATA ANALYSIS ==========")

# ==================================
# 2. DISPLAY FIRST 5 ROWS
# ==================================

print("\n1. First 5 Rows:")
print(data.head())

# ==================================
# 3. CHECK DATASET SHAPE
# ==================================

print("\n2. Dataset Shape:")
print(data.shape)

# ==================================
# 4. DISPLAY COLUMN NAMES
# ==================================

print("\n3. Column Names:")
print(data.columns)

# ==================================
# 5. DATASET INFORMATION
# ==================================

print("\n4. Dataset Information:")
data.info()

# ==================================
# 6. CHECK MISSING VALUES
# ==================================

print("\n5. Missing Values:")
print(data.isnull().sum())

# ==================================
# 7. CHECK DUPLICATE RECORDS
# ==================================

print("\n6. Duplicate Records:")
print(data.duplicated().sum())

# ==================================
# 8. REMOVE DUPLICATE RECORDS
# ==================================

data = data.drop_duplicates()

print("\n7. Shape After Removing Duplicates:")
print(data.shape)

# ==================================
# 9. CHECK DATA TYPES
# ==================================

print("\n8. Data Types:")
print(data.dtypes)

# ==================================
# 10. CONVERT DATE COLUMN
# ==================================

data["Date"] = pd.to_datetime(data["Date"])

print("\n9. Updated Data Types:")
print(data.dtypes)

# ==================================
# 11. FINAL DATASET
# ==================================

print("\n10. Cleaned Dataset:")
print(data)

print("\n========== DATA CLEANING COMPLETED ==========")

# ==================================
# 12. CALCULATE REVENUE
# ==================================

data["Revenue"] = data["Quantity"] * data["Unit_Price"]

print("\n11. Revenue for Each Order:")
print(data[["Order_ID", "Product", "Quantity", "Unit_Price", "Revenue"]])

# ==================================
# 13. CALCULATE TOTAL REVENUE
# ==================================

total_revenue = data["Revenue"].sum()

print("\n12. Total Revenue:")
print("Rs.", total_revenue)

# ==================================
# 14. BEST-SELLING PRODUCT
# ==================================

product_sales = data.groupby("Product")["Quantity"].sum()

print("\n13. Quantity Sold by Product:")
print(product_sales)

best_product = product_sales.idxmax()

print("\nBest-Selling Product:")
print(best_product)

# ==================================
# 15. REVENUE BY REGION
# ==================================

region_sales = data.groupby("Region")["Revenue"].sum()

print("\n14. Revenue by Region:")
print(region_sales)

best_region = region_sales.idxmax()

print("\nHighest Revenue Region:")
print(best_region)

# ==================================
# 16. FILTER ELECTRONICS PRODUCTS
# ==================================

electronics = data[data["Category"] == "Electronics"]

print("\nElectronics Products:")
print(electronics)

# ==================================
# 17. FILTER HIGH-VALUE SALES
# ==================================

high_sales = data[data["Revenue"] > 10000]

print("\nSales Above Rs. 10,000:")
print(high_sales[["Order_ID", "Product", "Revenue"]])

# ==================================
# 18. REVENUE BY PRODUCT
# ==================================

product_revenue = data.groupby("Product")["Revenue"].sum()

print("\nRevenue by Product:")
print(product_revenue)

# ==================================
# 19. MONTHLY SALES ANALYSIS
# ==================================

data["Month"] = data["Date"].dt.month_name()

monthly_sales = data.groupby("Month")["Revenue"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# ==================================
# 20. NUMPY ANALYSIS
# ==================================

# Convert revenue column into NumPy array
revenue_array = np.array(data["Revenue"])

# Calculate average revenue
average_revenue = np.mean(revenue_array)

print("\nAverage Revenue:")
print("Rs.", average_revenue)

# ==================================
# 21. BAR CHART - REVENUE BY PRODUCT
# ==================================

product_revenue = data.groupby("Product")["Revenue"].sum()

plt.figure(figsize=(8, 5))

plt.bar(product_revenue.index, product_revenue.values)

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (Rs.)")

plt.tight_layout()

plt.savefig("images/revenue_by_product.png")

plt.show()

# ==================================
# 22. LINE CHART - MONTHLY SALES
# ==================================

monthly_sales = data.groupby(
    data["Date"].dt.month
)["Revenue"].sum()

month_names = ["January", "February", "March", "April"]

plt.figure(figsize=(8, 5))

plt.plot(month_names, monthly_sales.values, marker="o")

plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Revenue (Rs.)")

plt.tight_layout()

plt.savefig("images/monthly_sales.png")

plt.show()

# ==================================
# 23. PIE CHART - CATEGORY SALES
# ==================================

category_sales = data.groupby("Category")["Revenue"].sum()

plt.figure(figsize=(7, 7))

plt.pie(
    category_sales.values,
    labels=category_sales.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Revenue by Category")

plt.tight_layout()

plt.savefig("images/category_sales.png")

plt.show()
