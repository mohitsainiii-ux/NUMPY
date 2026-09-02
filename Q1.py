#How do you find the indices of the maximum and minimum values in a NumPy array?

import numpy as np

arr = np.array([10, 45, 23, 89, 12, 67])

max_index = np.argmax(arr)
min_index = np.argmin(arr)

print("Maximum index:", max_index)
print("Minimum index:", min_index)