# What is broadcasting in NumPy?

# Broadcasting allows NumPy to perform operations between arrays with compatible shapes without manually resizing them.

import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

value = np.array([1, 2, 3])

result = arr + value

print(result)