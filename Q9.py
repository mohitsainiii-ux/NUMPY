# What is the difference between * and @ in NumPy?

#* The * operator performs element-wise multiplication between two arrays. It multiplies corresponding elements of the arrays together.
#@ The @ operator performs matrix multiplication between two arrays. It follows the rules of linear algebra for multiplying matrices.

import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print(A * B)
print(A @ B)