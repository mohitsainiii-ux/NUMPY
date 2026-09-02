# # Write a NumPy program using:Reshape the 1D array into a 3 × 4 matrix.
# Calculate the sum of each row.
# Calculate the sum of each column.
# Calculate the average of each row.
# Find the maximum value from each column.
# Find the minimum value from each row.
# Reshape the original data into a 4 × 3 matrix.
# Convert the 3 × 4 matrix back into a 1D array.

import numpy as np

data = np.array([
    10, 20, 30, 40,
    50, 60, 70, 80,
    90, 100, 110, 120
])

# Reshape the 1D array into a 3 × 4 matrix
matrix_3x4 = data.reshape(3, 4)
print("3 × 4 matrix:")
print(matrix_3x4)

# Calculate the sum of each row
row_sums = np.sum(matrix_3x4, axis=1)
print("Sum of each row:", row_sums)

# Calculate the sum of each column
column_sums = np.sum(matrix_3x4, axis=0)

print("Sum of each column:", column_sums)

# Calculate the average of each row
row_averages = np.mean(matrix_3x4, axis=1)
print("Average of each row:", row_averages)

# Find the maximum value from each column
column_max = np.max(matrix_3x4, axis=0)
print("Maximum value from each column:", column_max)

# Find the minimum value from each row
row_min = np.min(matrix_3x4, axis=1)
print("Minimum value from each row:", row_min)

# Reshape the original data into a 4 × 3 matrix
matrix_4x3 = data.reshape(4, 3)
print("4 × 3 matrix:")

print(matrix_4x3)
