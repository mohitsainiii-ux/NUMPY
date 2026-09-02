# What will happen when we perform operations on arrays having different shapes?

import numpy as np

A = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

B = np.array([
    [1],
    [2]
])

result = A + B

print(result)