# Calculate the revenue for every product in every month using broadcasting.

# Then:

# Calculate total revenue for each product.
# Calculate total revenue for each month.
# Find the product with the highest total revenue.
# Find the month with the highest total revenue.
# Calculate the overall revenue.
# Calculate the average revenue per month.
# Do everything using NumPy without loops.

import numpy as np

sales = np.array([
    [100, 120, 140, 160],
    [200, 220, 240, 260],
    [300, 320, 340, 360]
])

price = np.array([10, 20, 30])


# Reshape price so broadcasting works across the months
price = price.reshape(3, 1)


# Calculate revenue
revenue = sales * price

print("Revenue:")
print(revenue)


# 1. Total revenue for each product
product_revenue = np.sum(revenue, axis=1)

print("Total revenue for each product:")
print(product_revenue)


# 2. Total revenue for each month
monthly_revenue = np.sum(revenue, axis=0)

print("Total revenue for each month:")
print(monthly_revenue)


# 3. Product with highest total revenue
highest_product = np.argmax(product_revenue)

print("Product with highest revenue:",
      highest_product + 1)


# 4. Month with highest total revenue
highest_month = np.argmax(monthly_revenue)

print("Month with highest revenue:",
      highest_month + 1)


# 5. Overall revenue
total_revenue = np.sum(revenue)

print("Overall revenue:", total_revenue)


# 6. Average revenue per month
average_monthly_revenue = np.mean(monthly_revenue)

print("Average revenue per month:",
      average_monthly_revenue)