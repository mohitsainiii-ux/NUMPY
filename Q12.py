# Write a NumPy program to perform the following operations on this array: Extract the values:

# 20, 60, 80

# Extract the entire second row:

# [40, 50, 60]

# Extract the first and third columns:

# [[10, 30],
#  [40, 60],
#  [70, 90]]

# Extract the diagonal values:

# [10, 50, 90]
# Replace the values 20 and 80 with 0.

import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Extract the values 20, 60, 80
extracted_values = arr[[0, 1, 2], [1, 2, 1]]
print("Extracted values:", extracted_values)

# Extract the entire second row
second_row = arr[1, :]
print("Second row:", second_row)

# Extract the first and third columns
first_and_third_columns = arr[:, [0, 2]]
print("First and third columns:", first_and_third_columns)

# Extract the diagonal values
diagonal_values = np.diag(arr)
print("Diagonal values:", diagonal_values)

# Replace the values 20 and 80 with 0
arr[arr == 20] = 0
arr[arr == 80] = 0
print("Array after replacement:", arr)