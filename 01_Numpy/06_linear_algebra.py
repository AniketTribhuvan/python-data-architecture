"""
Matrix Multiplication & Dot Products
Focus: Inner dimension compatibility, @ (np.matmul) vs * (elementwise), and 1D/2D dot products.
"""

import numpy as np

rng = np.random.default_rng()

# Matrix Multiplication

arr_1 = rng.integers(1, 10, size=(6, 3), dtype= np.int32)
# Shape: (6, 3)

arr_2 = rng.integers(1, 10, size=(3, 2), dtype= np.int32)
# Shape: (3, 2)

# @ is used for matrix multiplication.
# It calls np.matmul() internally.

matrix_mul = arr_1 @ arr_2

# Matrix multiplication:
# Each element is calculated using Row × Column multiplication.
#
# Matrix multiplication rule:
#
# (m, n) @ (n, p) = (m, p)
#
# The inner dimensions must be equal.
#
# (6, 3) @ (3, 2)
#   ↑       ↑
#   3 == 3 → Compatible
#
# Result shape:
# (6, 2)

assert matrix_mul.shape == (6, 2), "Array must be 3 x 4"

# Element-wise Multiplication

arr_1 = rng.integers(1, 10, size=(3, ), dtype= np.int32)
# Shape: (3,)

arr_2 = rng.integers(1, 10, size=(5, 3), dtype= np.int32)
# Shape: (5, 3)

el_matrix_mul = arr_1 * arr_2

# * performs element-wise multiplication, not matrix multiplication.
# Element-wise multiplication multiplies corresponding elements.
#
# Broadcasting rules are used when the shapes are different.
#
# (3,) can be broadcast to (5, 3).


# Dot Product

# For two 2D arrays, np.dot() performs matrix multiplication.

arr_1 = rng.integers(1, 10, size=(3, 4), dtype= np.int32)
# Shape: (3, 4)

arr_2 = rng.integers(1, 10, size=(4, 2), dtype= np.int32)
# Shape: (4, 2)

dot_matrix = np.dot(arr_1, arr_2)

matrix_mul = arr_1 @ arr_2

print(np.array_equal(dot_matrix, matrix_mul))
# True

# For 2D arrays:
#
# np.dot(arr_1, arr_2)
#
# gives the same result as:
#
# arr_1 @ arr_2
#
# However, np.dot() behaves differently for arrays with
# more than 2 dimensions.
#
# For 1D arrays, np.dot() calculates the dot product:
#
# [a, b, c] · [x, y, z]
# = a*x + b*y + c*z

# dot product of 1D arrays :
arr_1 = np.arange(1,6)
arr_2 = np.arange(11, 16)
print(np.dot(arr_1, arr_2))     # 205


# ValueError on intentional matrix multiplication mismatch

arr_1 = rng.integers(1, 10, size=(3, 4), dtype= np.int32)
# Shape: (3, 4)

arr_2 = rng.integers(1, 10, size=(3, 2), dtype= np.int32)
# Shape: (3, 2)


try:
    matrix_mul = arr_1 @ arr_2

except ValueError as e:
    print(e)

# Matrix multiplication requires the inner dimensions to match:
#
# (3, 4) @ (3, 2)
#    ↑       ↑
#    4 != 3
#
# Therefore, matrix multiplication is not possible.
#
# NumPy raises a ValueError.