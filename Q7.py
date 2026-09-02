# How do you find the mean of each row and column?

import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Row mean:", np.mean(arr, axis=1))
print("Column mean:", np.mean(arr, axis=0))