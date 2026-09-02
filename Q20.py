# Write a NumPy program to:

# Add A and B.
# Subtract B from A.
# Perform element-wise multiplication.
# Perform matrix multiplication.
# Find the transpose of A.
# Find the determinant of A.
# Find the inverse of A.
# Verify that A × inverse(A) produces the identity matrix.
# Calculate the eigenvalues of A.

import numpy as np

A = np.array([
    [2, 1],
    [1, 3]
])

B = np.array([
    [4, 2],
    [5, 1]
])


# 1. Addition
addition = A + B

print("Addition:")
print(addition)


# 2. Subtraction
subtraction = A - B

print("\nSubtraction:")
print(subtraction)


# 3. Element-wise multiplication
element_multiplication = A * B

print("\nElement-wise multiplication:")
print(element_multiplication)


# 4. Matrix multiplication
matrix_multiplication = A @ B

print("\nMatrix multiplication:")
print(matrix_multiplication)


# 5. Transpose of A
transpose = A.T

print("\nTranspose of A:")
print(transpose)


# 6. Determinant of A
determinant = np.linalg.det(A)

print("\nDeterminant of A:")
print(determinant)


# 7. Inverse of A
inverse = np.linalg.inv(A)

print("\nInverse of A:")
print(inverse)


# 8. Verify A × inverse(A)
identity = A @ inverse

print("\nA × inverse(A):")
print(identity)


# 9. Eigenvalues of A
eigenvalues = np.linalg.eigvals(A)

print("\nEigenvalues of A:")
print(eigenvalues)