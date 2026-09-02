# How do you replace all values greater than a specific value?

import numpy as np

arr = np.array([10, 25, 50, 75, 100])

arr[arr > 50] = 50

print(arr)