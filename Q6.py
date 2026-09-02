# How do you calculate row-wise and column-wise sums in a 2D array?

import numpy as np
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

row_sums = np.sum(arr, axis=1)
column_sums = np.sum(arr, axis=0)

print("Row-wise sums:", row_sums)
print("Column-wise sums:", column_sums)