import numpy as np

arr = np.array([10, 20, 30, 20, 40, 10, 50])

unique, counts = np.unique(arr, return_counts=True)

duplicates = unique[counts > 1]

print(duplicates)