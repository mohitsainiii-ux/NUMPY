# A company wants to calculate the final sales amount after applying a 10% discount to every sale above 3000.

# Perform the following:

# Create a boolean condition for sales greater than 3000.
# Apply a 10% discount only to values greater than 3000.
# Keep all other values unchanged.
# Store the result in a new NumPy array without modifying the original sales.
# Calculate the total original sales.
# Calculate the total sales after the discount.
# Calculate the total discount amount.
# Find the sale with the highest final value.
# Find the average final sales value.
# Solve the discount operation using NumPy vectorization — do not use for or while loops.

import numpy as np

sales = np.array([
    1200, 2500, 1800, 3200, 4500,
    2100, 3900, 5000, 2750, 1600
])

# 1. Create condition for sales greater than 3000
condition = sales > 3000

print("Condition:")
print(condition)


# 2 & 3. Apply 10% discount only to sales above 3000
final_sales = np.where(
    condition,
    sales * 0.90,
    sales
)

print("Final sales:")
print(final_sales)


# 4. Original sales remains unchanged
print("Original sales:")
print(sales)


# 5. Total original sales
total_original = np.sum(sales)

print("Total original sales:", total_original)


# 6. Total sales after discount
total_final = np.sum(final_sales)

print("Total final sales:", total_final)


# 7. Total discount
total_discount = total_original - total_final

print("Total discount:", total_discount)


# 8. Highest final sale
highest_sale = np.max(final_sales)

print("Highest final sale:", highest_sale)


# 9. Average final sales
average_sale = np.mean(final_sales)

print("Average final sale:", average_sale)