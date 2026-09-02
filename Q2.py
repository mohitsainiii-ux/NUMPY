# How do you find the second-largest value without sorting the entire array?

import numpy as np

arr = np.array([10, 50, 30, 80, 20])

second_largest = np.partition(arr, -2)[-2]

print(second_largest)