# This is an important interview-level NumPy concept.
# Create a slice containing:

# [20, 30, 40]
# Change the first value of the slice to 999.
# Print both the slice and original arr.
# Now create a copy containing [20, 30, 40].
# Change the first value of the copy to 888.
# Print both the copy and original arr.
# From your output, determine:
# Does a NumPy slice share memory with the original array?
# Does .copy() share memory with the original array?
# Rules
# NumPy only
# No loops
# Write complete code
# Don't search the answer first 😄

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Create a slice containing [20, 30, 40]
slice_arr = arr[1:4]

# Change the first value of the slice to 999
slice_arr[0] = 999

# Print both the slice and original array
print("Slice:", slice_arr)
print("Original array:", arr)

# Now create a copy containing [20, 30, 40]
copy_arr = arr[1:4].copy()

# Change the first value of the copy to 888
copy_arr[0] = 888

# Print both the copy and original array
print("Copy:", copy_arr)
print("Original array:", arr)

