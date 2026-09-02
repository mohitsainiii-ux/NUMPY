# How do you normalize an array between 0 and 1?

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

normalized = (arr - arr.min()) / (arr.max() - arr.min())

print(normalized)